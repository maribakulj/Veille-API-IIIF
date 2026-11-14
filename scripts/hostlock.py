#!/usr/bin/env python3
"""Politesse PARTAGÉE entre processus et agents (même IP) : registre hors dépôt (~/.veille-state, ou $VEILLE_STATE).

attendre(host, delai) : réserve un créneau d'envoi et dort jusqu'à lui :
  - au moins max(delai, délai appris du robots.txt) secondes entre deux requêtes vers un même hôte, TOUS agents confondus ;
  - au plus GLOBAL_MAX requêtes par minute vers l'ensemble des hôtes (protège l'IP de Marcel) ;
  - pendant un crash test (verrou exclusif crash.lock) rien d'autre ne part.
CLI : hostlock.py attendre <hôte> [délai_s] | noter <hôte> <délai_s>
"""
import fcntl
import json
import os
import sys
import time
from pathlib import Path

STATE = Path(os.environ.get("VEILLE_STATE") or Path.home() / ".veille-state")
GLOBAL_MAX = 30          # requêtes / minute, tous hôtes et tous agents
FENETRE_S = 60.0


def _etat():
    STATE.mkdir(parents=True, exist_ok=True)
    f = open(STATE / "etat.json.lock", "a+")
    fcntl.flock(f, fcntl.LOCK_EX)
    p = STATE / "etat.json"
    try:
        e = json.loads(p.read_text())
    except (OSError, ValueError):
        e = {}
    e.setdefault("hotes", {})
    e.setdefault("global", [])
    return e, f, p


def _ecrire(e, f, p):
    p.write_text(json.dumps(e))
    fcntl.flock(f, fcntl.LOCK_UN)
    f.close()


def attendre(host, delai=6.0):
    STATE.mkdir(parents=True, exist_ok=True)
    c = open(STATE / "crash.lock", "a+")
    fcntl.flock(c, fcntl.LOCK_SH)      # bloque tant qu'un crash test (LOCK_EX) tourne
    fcntl.flock(c, fcntl.LOCK_UN)
    c.close()
    e, f, p = _etat()
    now = time.time()
    h = e["hotes"].setdefault(host, {"dernier": 0.0, "delai": 0.0})
    slot = max(now, h["dernier"] + max(float(delai), h.get("delai", 0.0)))
    g = sorted(t for t in e["global"] if t > now - FENETRE_S - 120)
    while len([t for t in g if t > slot - FENETRE_S]) >= GLOBAL_MAX:
        slot = min(t for t in g if t > slot - FENETRE_S) + FENETRE_S
    h["dernier"] = slot
    g.append(slot)
    e["global"] = g
    _ecrire(e, f, p)
    if slot > time.time():
        time.sleep(slot - time.time())


def noter_delai(host, delai):
    e, f, p = _etat()
    h = e["hotes"].setdefault(host, {"dernier": 0.0, "delai": 0.0})
    h["delai"] = max(h.get("delai", 0.0), float(delai))
    _ecrire(e, f, p)


def verrou_crash():
    """Verrou exclusif pour crash.py (bloque jusqu'à ce que les autres aient fini leur créneau)."""
    STATE.mkdir(parents=True, exist_ok=True)
    c = open(STATE / "crash.lock", "a+")
    fcntl.flock(c, fcntl.LOCK_EX)
    return c


def secrets():
    """Valeurs à ne jamais écrire dans le dépôt (IP de Marcel…), lues dans ~/.veille-state/secrets.txt (hors dépôt)."""
    try:
        return [l.strip() for l in (STATE / "secrets.txt").read_text().splitlines() if l.strip()]
    except OSError:
        return []


MOTIFS_JETONS = [
    r"\b[ps]k\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",      # Mapbox
    r"\bAKIA[0-9A-Z]{16}\b",                                       # clé d'accès AWS
    r"\bgh[pousr]_[A-Za-z0-9]{30,}\b",                             # jetons GitHub
    r"\bxox[abprs]-[A-Za-z0-9-]{10,}",                              # jetons Slack
    r"\bAIza[0-9A-Za-z_-]{35}\b",                                  # clé API Google
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",                           # clé privée
]


def redact(texte):
    import re
    for v in secrets():
        texte = texte.replace(v, "[IP retirée]")
    for m in MOTIFS_JETONS:
        texte = re.sub(m, "[jeton retiré]", texte)
    return texte


def redact_fichier(chemin):
    try:
        b = open(chemin, "rb").read()
    except OSError:
        return
    t = b.decode("utf-8", "replace")
    r = redact(t)
    if r != t:
        open(chemin, "wb").write(r.encode("utf-8"))


BLOCAGE_DUREE_S = 24 * 3600


def bloquer(host, raison=""):
    """Hôte arrêté (403 anti-bot, défi, CAPTCHA) pour TOUS les appels et TOUS les agents pendant 24 h."""
    e, f, p = _etat()
    e.setdefault("bloques", {})[host] = {"depuis": time.time(), "raison": raison}
    _ecrire(e, f, p)


def debloquer(host):
    e, f, p = _etat()
    e.get("bloques", {}).pop(host, None)
    _ecrire(e, f, p)


def bloque(host):
    """Retourne la raison si l'hôte est arrêté (registre partagé), sinon None."""
    e, f, p = _etat()
    b = e.get("bloques", {}).get(host)
    _ecrire(e, f, p)
    if b and time.time() - b["depuis"] < BLOCAGE_DUREE_S:
        return b.get("raison") or "bloqué"
    return None


def noter_robots(host, chemin):
    """Lit un robots.txt téléchargé : Crawl-delay du groupe « * » (ou du fichier sans groupe) appris pour TOUS les appels."""
    import re
    try:
        t = open(chemin, encoding="utf-8", errors="replace").read()
    except OSError:
        return
    groupe_etoile, vu_ua, delai = True, False, 0.0
    for l in t.splitlines():
        l = l.split("#")[0].strip()
        m = re.match(r"(?i)user-agent\s*:\s*(.*)", l)
        if m:
            vu_ua = True
            groupe_etoile = m.group(1).strip() == "*"
            continue
        m = re.match(r"(?i)crawl-delay\s*:\s*([0-9.]+)", l)
        if m and (groupe_etoile or not vu_ua):
            delai = max(delai, float(m.group(1)))
    if delai:
        noter_delai(host, delai)


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "attendre":
        attendre(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 6.0)
    elif len(sys.argv) >= 3 and sys.argv[1] == "bloquer":
        bloquer(sys.argv[2], " ".join(sys.argv[3:]))
    elif len(sys.argv) == 4 and sys.argv[1] == "noter_robots":
        noter_robots(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3 and sys.argv[1] == "debloquer":
        debloquer(sys.argv[2])
    elif len(sys.argv) == 3 and sys.argv[1] == "bloque":
        r = bloque(sys.argv[2])
        if r:
            print(r)
        sys.exit(0 if r else 1)
    elif len(sys.argv) == 3 and sys.argv[1] == "redact":
        redact_fichier(sys.argv[2])
    elif len(sys.argv) == 4 and sys.argv[1] == "noter":
        noter_delai(sys.argv[2], float(sys.argv[3]))
    else:
        sys.exit(__doc__)
