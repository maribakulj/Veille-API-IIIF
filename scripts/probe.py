#!/usr/bin/env python3
"""Sonde prudente des endpoints IIIF / API d'une institution.

Usage :  python3 scripts/probe.py institutions/<slug>/config/<nom>.json [--dry-run]

Le fichier de configuration (un par institution) liste les endpoints à tester,
un par un. Le script applique les règles de METHODOLOGY.md, quelle que soit la
configuration :
  - GET (ou HEAD) seulement ; aucun POST ; aucun identifiant ; pas d'en-tête d'auth.
  - User-Agent honnête, fixé ci-dessous.
  - pause minimale entre deux requêtes vers un même hôte (défaut 6 s, ou le
    `min_delay_s` de la configuration si plus grand) ;
  - plafond de requêtes par institution (défaut 15) ;
  - un 403 ou une page de défi arrête UN hôte (étiqueté « 403 anti-bot ») ;
  - un 429 ou un CAPTCHA arrête TOUTE l'institution ;
  - un échec réseau est consigné et n'arrête que cet endpoint ;
  - une redirection vers le MÊME hôte est suivie (1 saut par défaut, `follow_redirects` dans la
    configuration), comptée dans le budget et soumise à la même pause ; vers un autre hôte : non suivie.
Le journal (une ligne par requête, en-têtes de limite seulement, corps tronqué à
200 octets) est ajouté à institutions/<slug>/tests/journal.log ; les en-têtes complets sont
dans institutions/<slug>/tests/raw/.

Aucune requête n'est répétée en rafale : le script ne fait jamais deux requêtes
à moins de `min_delay_s` d'intervalle, même pour un même endpoint.
"""
import http.client
import json
import re
import ssl
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

UA = "VeilleAPIIIF/0.1 (veille documentaire; github.com/maribakulj/Veille-API-IIIF)"
DEFAULT_DELAY = 6.0
DEFAULT_MAX = 15
LIMIT_HEADER_PREFIXES = ("retry-after", "x-ratelimit", "ratelimit", "cf-mitigated", "x-rate")
REPO = Path(__file__).resolve().parent.parent


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch(url, method, timeout=20, lire=200):
    """Une seule requête HTTP(S) sans authentification. Retourne un dict."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        raise ValueError(f"URL refusée : {url}")
    path = (parts.path or "/") + (("?" + parts.query) if parts.query else "")
    # http.client exige une ligne de requête ASCII : on encode les caractères non ASCII
    # (UTF-8) en conservant les %XX existants et les séparateurs d'URL.
    path = urllib.parse.quote(path, safe="/%:@!$&'()*+,;=~-._?")
    if parts.scheme == "https":
        conn = http.client.HTTPSConnection(
            parts.hostname, parts.port, timeout=timeout, context=ssl.create_default_context()
        )
    else:
        conn = http.client.HTTPConnection(parts.hostname, parts.port, timeout=timeout)
    try:
        conn.request(method, path, headers={"User-Agent": UA, "Accept": "*/*"})
        resp = conn.getresponse()
        headers = [(k.lower(), v) for k, v in resp.getheaders()]
        body = b"" if method == "HEAD" else resp.read(lire)
        return {"status": resp.status, "headers": headers, "body": body}
    finally:
        conn.close()


def limit_headers(headers):
    return [f"{k}: {v}" for k, v in headers if k.startswith(LIMIT_HEADER_PREFIXES)]


def classify(status, headers, body):
    """Classe la réponse selon METHODOLOGY.md."""
    text = body.decode("utf-8", "replace").lower()
    challenge = any(k == "cf-mitigated" for k, _ in headers) or "just a moment" in text
    if status == 429 or "captcha" in text and status >= 400:
        return "STOP_INSTITUTION_429"
    if status == 403 or challenge:
        return "403_ANTI_BOT"
    if status >= 500:
        return "ERREUR_SERVEUR"
    if 300 <= status < 400:
        return "REDIRECTION_NON_SUIVIE"  # la sonde ne suit pas les redirections
    return "OK" if status < 300 else f"HTTP_{status}"


# ---------------------------------------------------------------- robots.txt (RFC 9309)
UA_TOKEN = "veilleapiiiif"


def _motif(chemin):
    """Convertit un chemin robots.txt (jokers * et $) en expression régulière ancrée au début."""
    rx = re.escape(chemin).replace(r"\*", ".*")
    if rx.endswith(r"\$"):
        rx = rx[:-2] + "$"
    return re.compile("^" + rx)


def lire_robots(texte):
    """Retourne (règles, crawl_delay) pour notre User-Agent, sinon pour « * ».
    règles : liste de (autorise, longueur_du_motif, motif_source, regex)."""
    groupes, courant, agents_en_cours = [], None, False
    texte = texte.lstrip("\ufeff")  # BOM éventuel en tête de fichier (vu sur iiif.wellcomecollection.org)
    for brut in texte.splitlines():
        ligne = brut.split("#", 1)[0].strip()
        if ":" not in ligne:
            continue
        cle, val = [x.strip() for x in ligne.split(":", 1)]
        cle = cle.lower()
        if cle == "user-agent":
            if not agents_en_cours:
                courant = {"agents": [], "regles": [], "delai": None}
                groupes.append(courant)
            courant["agents"].append(val.lower())
            agents_en_cours = True
        elif courant is not None and cle in ("allow", "disallow"):
            agents_en_cours = False
            if val:  # « Disallow: » vide = tout autorisé
                courant["regles"].append((cle == "allow", len(val), val, _motif(val)))
        elif courant is not None and cle == "crawl-delay":
            agents_en_cours = False
            try:
                courant["delai"] = max(courant["delai"] or 0.0, float(val))
            except ValueError:
                pass
        elif courant is not None and cle == "request-rate":
            agents_en_cours = False
            m = re.match(r"(\d+)\s*/\s*(\d+)\s*([smhd]?)", val.lower())
            if m and int(m.group(1)) > 0:
                unite = {"": 1, "s": 1, "m": 60, "h": 3600, "d": 86400}[m.group(3)]
                courant["delai"] = max(courant["delai"] or 0.0, int(m.group(2)) * unite / int(m.group(1)))
        else:
            agents_en_cours = False
    precis = [g for g in groupes if any(UA_TOKEN in a for a in g["agents"])]
    generiques = [g for g in groupes if "*" in g["agents"]]
    choisis = precis or generiques
    regles = [r for g in choisis for r in g["regles"]]
    delais = [g["delai"] for g in choisis if g["delai"] is not None]
    return regles, (max(delais) if delais else None), ("notre User-Agent" if precis else "« * »")


def autorise(regles, url):
    """Plus long motif gagnant ; à égalité, Allow l'emporte (RFC 9309)."""
    parts = urllib.parse.urlsplit(url)
    cible = (parts.path or "/") + (("?" + parts.query) if parts.query else "")
    meilleur = None
    for aut, longueur, source, rx in regles:
        if rx.search(cible):
            if meilleur is None or longueur > meilleur[1] or (longueur == meilleur[1] and aut):
                meilleur = (aut, longueur, source)
    return (True, None) if meilleur is None or meilleur[0] else (False, meilleur[2])


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cfg_path = Path(sys.argv[1])
    dry = "--dry-run" in sys.argv
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    slug = cfg["slug"]
    delay = max(DEFAULT_DELAY, float(cfg.get("min_delay_s", DEFAULT_DELAY)))
    max_req = min(DEFAULT_MAX, int(cfg.get("max_requests", DEFAULT_MAX)))
    base = REPO / "institutions" / slug
    if not base.is_dir():
        sys.exit(f"dossier d'institution introuvable : {base} (créer le dossier avant de lancer la sonde)")
    log_path = base / "tests" / "journal.log"
    blocked_hosts = set()
    stop_all = False
    last_call = {}  # hôte -> horodatage monotonic de la dernière requête
    count = 0

    endpoints = cfg["endpoints"]
    if dry:
        for e in endpoints:
            print(f"[dry] {e['id']} {e.get('method','GET')} {e['url']}")
        print(f"[dry] pause {delay}s, plafond {max_req} requêtes")
        return

    raw_dir = base / "tests" / "raw"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)
    commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True).stdout.strip() or "inconnu"
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"# Session {now_utc()} — configuration {cfg_path.name} — "
                  f"sonde {Path(__file__).name} au commit {commit}\n")
        respect_robots = bool(cfg.get("respect_robots", True))
        robots = {}  # hôte -> (règles, crawl_delay)
        max_hops = int(cfg.get("follow_redirects", 1))  # redirections du MÊME hôte, comptées dans le budget
        opts = {e["id"]: e for e in endpoints}
        file = [(e["id"], e["url"], e.get("method", "GET"), 0) for e in endpoints]
        while file:
            eid, url, method, hops = file.pop(0)
            if stop_all:
                log.write(f"{now_utc()} | {eid} | NON LANCÉ : arrêt de l'institution (429)\n")
                continue
            host = urllib.parse.urlsplit(url).hostname
            if host in blocked_hosts:
                log.write(f"{now_utc()} | {eid} | NON LANCÉ : hôte {host} arrêté (403 anti-bot)\n")
                continue
            if count >= max_req:
                log.write(f"{now_utc()} | {eid} | NON LANCÉ : plafond de {max_req} requêtes atteint\n")
                continue
            if respect_robots and host not in robots and host in cfg.get("robots_files", {}):
                rf = REPO / cfg["robots_files"][host]
                txt = rf.read_text(encoding="utf-8", errors="replace")
                regles, cd, qui = lire_robots("\n".join(l for l in txt.splitlines() if not l.startswith("#")))
                robots[host] = (regles, cd)
                log.write(f"{now_utc()} | robots.txt:{host} | copie locale {cfg['robots_files'][host]} | {len(regles)} règle(s) pour {qui} (aucune requête envoyée)\n")
            if respect_robots and host not in robots:
                # robots.txt de l'hôte : lu une fois par passe, compté dans le budget, même pause
                scheme = urllib.parse.urlsplit(url).scheme
                rurl = f"{scheme}://{host}/robots.txt"
                wait = delay - (time.monotonic() - last_call[host]) if host in last_call else 0
                if wait > 0:
                    time.sleep(wait)
                try:
                    rr = fetch(rurl, "GET", lire=200000)
                    code = rr["status"]
                    if code == 200:
                        regles, cd, qui = lire_robots(rr["body"].decode("utf-8", "replace"))
                        robots[host] = (regles, cd)
                        log.write(f"{now_utc()} | robots.txt:{host} | {rurl} | GET | 200 | "
                                  f"{len(regles)} règle(s) pour {qui}" + (f" ; Crawl-delay {cd} s" if cd else "") + "\n")
                    elif 500 <= code < 600:
                        robots[host] = ([(False, 1, "/", _motif("/"))], None)
                        log.write(f"{now_utc()} | robots.txt:{host} | {rurl} | GET | {code} | erreur serveur : par prudence (RFC 9309) tout est traité comme interdit\n")
                    else:
                        robots[host] = ([], None)
                        log.write(f"{now_utc()} | robots.txt:{host} | {rurl} | GET | {code} | robots.txt indisponible : tout est autorisé (RFC 9309)\n")
                except Exception as exc:  # noqa: BLE001
                    robots[host] = ([(False, 1, "/", _motif("/"))], None)
                    log.write(f"{now_utc()} | robots.txt:{host} | {rurl} | GET | ERREUR_RÉSEAU | {type(exc).__name__} : tout est traité comme interdit\n")
                last_call[host] = time.monotonic()
                count += 1
            if respect_robots and host in robots:
                ok, motif = autorise(robots[host][0], url)
                if not ok and cfg.get("robots_disallow_autorise_par_marcel"):
                    # Décision de Marcel (C12, 14/11/2026) : un Disallow n'arrête plus l'audit ;
                    # le Crawl-delay, la pause, le budget et l'interdiction de contourner restent.
                    log.write(f"{now_utc()} | {eid} | robots.txt interdit {url} (Disallow: {motif}) ; lancé car autorisé par Marcel (C12)\n")
                elif not ok:
                    log.write(f"{now_utc()} | {eid} | {url} | NON LANCÉ : interdit par robots.txt (Disallow: {motif})\n")
                    print(f"NON LANCÉ (robots.txt) : {url}")
                    continue
            wait = max(delay, robots.get(host, (None, None))[1] or 0) - (time.monotonic() - last_call[host]) if host in last_call else 0
            if wait > 0:
                time.sleep(wait)
            if method not in ("GET", "HEAD"):
                raise SystemExit(f"Méthode interdite : {method}")
            try:
                gros = int(opts.get(eid.split("+redir")[0], {}).get("save_body", 0))
                r = fetch(url, method, lire=max(200, gros))
                err = ""
            except Exception as exc:  # noqa: BLE001 - on consigne toute erreur réseau
                r, err = None, f"{type(exc).__name__}: {exc}"
            last_call[host] = time.monotonic()
            count += 1
            if r is None:
                verdict = "ERREUR_RÉSEAU"
                line = f"{now_utc()} | {eid} | {url} | {method} | {verdict} | {err}\n"
            else:
                verdict = classify(r["status"], r["headers"], r["body"])
                # En-têtes complets, pour pouvoir vérifier chaque conclusion.
                hdr = "\n".join(f"{k}: {v}" for k, v in r["headers"])
                (raw_dir / f"{eid}.headers.txt").write_text(
                    f"{now_utc()} {method} {url}\nHTTP {r['status']}\n{hdr}\n", encoding="utf-8")
                lh = "; ".join(limit_headers(r["headers"])) or "aucun en-tête de limite"
                snippet = r["body"][:200].decode("utf-8", "replace").replace("\n", " ")
                line = (f"{now_utc()} | {eid} | {url} | {method} | {r['status']} {verdict} | "
                        f"{lh} | taille≥{len(r['body'])} | corps: {snippet}\n")
                if verdict == "403_ANTI_BOT":
                    blocked_hosts.add(host)
                    line += f"# ARRÊT de l'hôte {host} (403 anti-bot). Les autres hôtes continuent.\n"
                if verdict == "STOP_INSTITUTION_429":
                    stop_all = True
                    line += "# ARRÊT de l'institution (429 / CAPTCHA). Aucun nouvel appel.\n"
                if gros and r["status"] < 300 and method == "GET":
                    (raw_dir / f"{eid}.body").write_bytes(r["body"])
                    line += f"# corps enregistré : tests/raw/{eid}.body ({len(r['body'])} octets lus)\n"
                loc = dict(r["headers"]).get("location")
                if verdict == "REDIRECTION_NON_SUIVIE" and loc and hops < max_hops:
                    cible = urllib.parse.urljoin(url, loc)
                    if urllib.parse.urlsplit(cible).hostname == host:
                        file.insert(0, (eid + "+redir", cible, method, hops + 1))
                        line += f"# redirection vers {cible} : suivie (même hôte, comptée dans le budget)\n"
                    else:
                        line += f"# redirection vers {cible} : NON suivie (autre hôte)\n"
            log.write(line)
            print(line.strip()[:220])
        log.write(f"# Fin {now_utc()} — {count} requête(s) envoyée(s)\n")


if __name__ == "__main__":
    main()
