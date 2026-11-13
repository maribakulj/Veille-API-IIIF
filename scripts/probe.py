#!/usr/bin/env python3
"""Sonde prudente des endpoints IIIF / API d'une institution.

Usage :  python3 scripts/probe.py scripts/config/<slug>.json [--dry-run]

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
200 octets) est ajouté à tests/<slug>.log.

Aucune requête n'est répétée en rafale : le script ne fait jamais deux requêtes
à moins de `min_delay_s` d'intervalle, même pour un même endpoint.
"""
import http.client
import json
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


def fetch(url, method, timeout=20):
    """Une seule requête HTTP(S) sans authentification. Retourne un dict."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        raise ValueError(f"URL refusée : {url}")
    path = (parts.path or "/") + (("?" + parts.query) if parts.query else "")
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
        body = b"" if method == "HEAD" else resp.read(200)
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


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cfg_path = Path(sys.argv[1])
    dry = "--dry-run" in sys.argv
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    slug = cfg["slug"]
    delay = max(DEFAULT_DELAY, float(cfg.get("min_delay_s", DEFAULT_DELAY)))
    max_req = min(DEFAULT_MAX, int(cfg.get("max_requests", DEFAULT_MAX)))
    log_path = REPO / "tests" / f"{slug}.log"
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

    raw_dir = REPO / "tests" / "raw" / slug
    raw_dir.mkdir(parents=True, exist_ok=True)
    commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True).stdout.strip() or "inconnu"
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"# Session {now_utc()} — configuration {cfg_path.name} — "
                  f"sonde {Path(__file__).name} au commit {commit}\n")
        max_hops = int(cfg.get("follow_redirects", 1))  # redirections du MÊME hôte, comptées dans le budget
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
            wait = delay - (time.monotonic() - last_call[host]) if host in last_call else 0
            if wait > 0:
                time.sleep(wait)
            if method not in ("GET", "HEAD"):
                raise SystemExit(f"Méthode interdite : {method}")
            try:
                r = fetch(url, method)
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
