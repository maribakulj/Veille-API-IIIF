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


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "attendre":
        attendre(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 6.0)
    elif len(sys.argv) == 4 and sys.argv[1] == "noter":
        noter_delai(sys.argv[2], float(sys.argv[3]))
    else:
        sys.exit(__doc__)
