#!/usr/bin/env python3
"""Crash test progressif (étape g de METHODOLOGY.md), depuis l'IP de Marcel.

Usage : python3 scripts/crash.py institutions/<slug>/config/crash-<nom>.json

Configuration (committée AVANT le lancement) :
{
  "slug": "...", "endpoint": {"id": "...", "url": "https://...", "method": "GET"},
  "limite_documentee_req_min": null | nombre,   # null = illimité ou non documenté
  "source_limite": "URL + phrase qui fonde le chiffre, ou « aucune limite documentée »",
  "duree_palier_s": 180,                        # au moins 180 (méthode)
  "note": "..."
}
Paliers (méthode) :
  limite documentée L : L/3, 2L/3, L, 1,5 L, 2 L (plafond 2 L, jamais dépassé)
  sans limite documentée : 6, 10, 50, 200 req/min (plafond 200)
Arrêt immédiat au premier 429, 403, CAPTCHA/défi, 5xx, ou 3 erreurs réseau consécutives.
GET/HEAD uniquement. User-Agent honnête. Requêtes régulièrement espacées.
"""
import json
import statistics
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
UA = "VeilleAPIIIF/0.1 (veille documentaire; github.com/maribakulj/Veille-API-IIIF)"
MARQUEURS_DEFI = ("captcha", "verifying your browser", "human verification", "access denied", "request blocked")


# Réseaux de diffusion / pare-feu à réputation d'IP partagée (décision de Marcel, 14/11/2026) :
# plafond réduit, un seul test à la fois, 30 min entre deux, requête témoin avant.
VENDORS = {
    "Cloudflare": r"^(server: cloudflare|cf-ray)",
    "AWS CloudFront": r"^(x-amz-cf-id|x-amz-cf-pop|via:.*cloudfront|server: cloudfront)",
    "Akamai": r"^(x-akamai|akamai-grn|server: akamai|x-edgeconnect)",
    "Fastly": r"^(x-served-by:.*cache-|fastly-|via:.*fastly)",
    "Azure Front Door": r"^(x-azure-ref|x-msedge-ref)",
    "Imperva": r"^(x-iinfo|x-cdn: imperva|set-cookie:.*incap_ses)",
    "Sucuri": r"^(x-sucuri|server: sucuri)",
    "DataDome": r"^(x-datadome|set-cookie:.*datadome)",
    "HUMAN/PerimeterX": r"^(x-px|set-cookie:.*_px)",
    "Kasada": r"^(x-kpsdk)",
}
TEMOINS = {"Cloudflare": "https://www.cloudflare.com/cdn-cgi/trace", "AWS CloudFront": "https://aws.amazon.com/robots.txt"}
PLAFOND_RESEAU_PROTEGE = 60   # req/min
DELAI_ENTRE_TESTS_PROTEGES_S = 1800
ETAT_PROTEGES = REPO / "data" / "crash_reseaux_proteges.json"


def detecter_reseau(headers):
    import re
    txt = "\n".join(f"{k}: {v}" for k, v in headers.items())
    return [n for n, rx in VENDORS.items() if re.search(rx, txt, re.I | re.M)]


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def paliers(limite, protege=False):
    cap = PLAFOND_RESEAU_PROTEGE if protege else 200
    if limite:
        base = [round(limite * k, 2) for k in (1 / 3, 2 / 3, 1, 1.5, 2)]
    else:
        base = [6, 10, 30, 60] if protege else [6, 10, 50, 200]
    out = []
    for p in base:
        p = min(p, cap)
        if p not in out:
            out.append(p)
    return out


class Arret(Exception):
    pass


def requete(url, method):
    t0 = time.monotonic()
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            corps = r.read(2048) if method == "GET" else b""
            return r.status, dict(r.headers), corps, time.monotonic() - t0, None
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read(2048), time.monotonic() - t0, None
    except Exception as e:  # réseau, délai, TLS
        return None, {}, b"", time.monotonic() - t0, type(e).__name__


def main(cfg_path):
    cfg_file = (REPO / cfg_path) if not Path(cfg_path).is_absolute() else Path(cfg_path)
    cfg = json.loads(cfg_file.read_text(encoding="utf-8"))
    slug, ep = cfg["slug"], cfg["endpoint"]
    import subprocess
    r = subprocess.run([sys.executable, str(REPO / "scripts" / "suivi.py"), "autorise", slug], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(r.stdout.strip() or "REFUSÉ par le verrou d'ordre")
    method = ep.get("method", "GET")
    if method not in ("GET", "HEAD"):
        sys.exit("méthode interdite : GET/HEAD seulement")
    duree = max(int(cfg.get("duree_palier_s", 180)), 180)
    limite = cfg.get("limite_documentee_req_min")
    from urllib.parse import urlsplit
    hote = urlsplit(ep["url"]).netloc
    outdir = REPO / "institutions" / slug / "tests" / "crash"
    outdir.mkdir(parents=True, exist_ok=True)
    # 1) hôte déjà testé par une autre institution : on reprend son résultat, on n'envoie rien
    for v in sorted((REPO / "institutions").glob("*/tests/crash/*.json")):
        try:
            vv = json.loads(v.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if vv.get("hote") == hote and vv.get("slug") != slug and vv.get("conclusion") and not vv.get("interrompu"):
            log = (outdir / f"{slug}.log").open("a", encoding="utf-8")
            log.write(f"# Crash test {now()} — configuration {cfg_file.name} — endpoint {ep['id']} {method} {ep['url']}\n")
            log.write(f"# Fin {now()} — hôte {hote} déjà testé par {vv['slug']} ({v.name}) : résultat repris, aucune requête envoyée : {vv['conclusion']}\n\n")
            log.close()
            (outdir / f"{slug}-{ep['id']}.json").write_text(json.dumps({**vv, "slug": slug, "repris_de": vv["slug"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"{slug} : hôte {hote} déjà testé par {vv['slug']} : résultat repris ({vv['conclusion']})")
            return 0
    # 2) requête de détection du réseau (en-têtes de l'endpoint lui-même)
    code0, h0, corps0, dt0, err0 = requete(ep["url"], method)
    reseaux = detecter_reseau(h0)
    protege = bool(reseaux)
    if code0 in (403, 429) or err0 or any(m in corps0.decode("utf-8", "replace").lower() for m in MARQUEURS_DEFI):
        sys.exit(f"ABANDON : la requête de détection renvoie {code0 or err0} : hôte inaccessible ou déjà défié, pas de crash test (étape g « impossible » à documenter)")
    if protege:
        # 3) un seul test protégé à la fois, 30 min entre deux ; requête témoin avant
        etat = json.loads(ETAT_PROTEGES.read_text(encoding="utf-8")) if ETAT_PROTEGES.exists() else {}
        if etat.get("dernier"):
            ecoule = (datetime.now(timezone.utc) - datetime.fromisoformat(etat["dernier"].replace("Z", "+00:00"))).total_seconds()
            if ecoule < DELAI_ENTRE_TESTS_PROTEGES_S:
                sys.exit(f"ATTENTE : dernier test sur réseau protégé ({etat.get('hote')}) il y a {int(ecoule)} s ; attendre encore {int(DELAI_ENTRE_TESTS_PROTEGES_S - ecoule)} s")
        for r in reseaux:
            if r in TEMOINS:
                ct, ht, bt, _, et = requete(TEMOINS[r], "GET")
                if ct != 200 or any(m in bt.decode("utf-8", "replace").lower() for m in MARQUEURS_DEFI):
                    sys.exit(f"ABANDON : site témoin {r} ({TEMOINS[r]}) répond {ct or et} : l'IP est peut-être déjà défiée, on n'ajoute pas de charge")
    pal = paliers(limite, protege)
    plafond = max(pal)
    log = (outdir / f"{slug}.log").open("a", encoding="utf-8")
    log.write(f"# Crash test {now()} — configuration {cfg_file.name} — endpoint {ep['id']} {method} {ep['url']}\n")
    log.write(f"# réseau détecté : {', '.join(reseaux) if reseaux else 'aucun réseau à réputation partagée connu'} ; plafond {'réduit à ' + str(PLAFOND_RESEAU_PROTEGE) if protege else 'standard 200'} req/min (décision de Marcel 14/11/2026) ; requête de détection : {code0} en {dt0:.2f} s\n")
    log.write(f"# limite documentée : {limite if limite else 'aucune'} req/min ({cfg.get('source_limite','?')}) ; paliers {pal} ; plafond {plafond} req/min ; {duree} s par palier\n")
    log.flush()
    if protege:
        ETAT_PROTEGES.write_text(json.dumps({"dernier": now(), "hote": hote, "slug": slug}) + "\n", encoding="utf-8")
    arret = threading.Event()
    verdict = {"slug": slug, "hote": hote, "reseaux": reseaux, "plafond_req_min": plafond, "endpoint": ep["id"], "limite_documentee_req_min": limite, "paliers": [], "arret": None}
    erreurs_consecutives = 0
    for rpm in pal:
        if arret.is_set():
            break
        assert rpm <= plafond + 1e-9
        intervalle = 60.0 / rpm
        n_prevu = int(duree / intervalle)
        res, lock = [], threading.Lock()

        def une(i):
            nonlocal erreurs_consecutives
            if arret.is_set():
                return
            code, h, corps, dt, err = requete(ep["url"], method)
            texte = corps.decode("utf-8", "replace").lower()
            defi = any(m in texte for m in MARQUEURS_DEFI)
            with lock:
                res.append((code, dt))
                erreurs_consecutives = erreurs_consecutives + 1 if err else 0
                cause = None
                if code == 429:
                    cause = "429"
                elif code == 403 or defi:
                    cause = "403/défi anti-bot"
                elif code and code >= 500:
                    cause = f"{code}"
                elif erreurs_consecutives >= 3:
                    cause = f"3 erreurs réseau consécutives ({err})"
                if cause and not arret.is_set():
                    arret.set()
                    rl = {k: v for k, v in h.items() if any(s in k.lower() for s in ("retry", "ratelimit", "rate-limit", "x-rate", "limit"))}
                    verdict["arret"] = {"palier_req_min": rpm, "requete_n": i + 1, "heure": now(), "cause": cause, "code": code,
                                        "en_tetes_limite": rl, "en_tetes": h, "corps_tronque": corps[:300].decode("utf-8", "replace")}
                    log.write(f"{now()} | ARRÊT | palier {rpm} req/min | requête {i + 1}/{n_prevu} | {cause} | en-têtes de limite : {rl}\n")
                    log.write(f"{now()} | en-têtes complets : {json.dumps(h, ensure_ascii=False)}\n")
                    log.write(f"{now()} | corps tronqué : {corps[:300].decode('utf-8','replace')!r}\n")
                    log.flush()

        debut = time.monotonic()
        with ThreadPoolExecutor(max_workers=8) as ex:
            for i in range(n_prevu):
                cible = debut + i * intervalle
                while time.monotonic() < cible:
                    time.sleep(min(0.05, cible - time.monotonic()))
                if arret.is_set():
                    break
                ex.submit(une, i)
        codes = {}
        for c, _ in res:
            codes[str(c)] = codes.get(str(c), 0) + 1
        lat = [d for _, d in res]
        reel = round(len(res) / max((time.monotonic() - debut) / 60, 1e-9), 1)
        ligne = {"palier_req_min": rpm, "requetes": len(res), "debit_reel_req_min": reel, "codes": codes,
                 "latence_p50_s": round(statistics.median(lat), 3) if lat else None,
                 "latence_max_s": round(max(lat), 3) if lat else None}
        verdict["paliers"].append(ligne)
        log.write(f"{now()} | palier {rpm} req/min | {json.dumps(ligne, ensure_ascii=False)}\n")
        log.flush()
    verdict["conclusion"] = (f"blocage au palier {verdict['arret']['palier_req_min']} req/min ({verdict['arret']['cause']})"
                             if verdict["arret"] else f"aucun blocage jusqu'à {plafond} req/min")
    if protege:
        ETAT_PROTEGES.write_text(json.dumps({"dernier": now(), "hote": hote, "slug": slug}) + "\n", encoding="utf-8")
    log.write(f"# Fin {now()} — {verdict['conclusion']}\n\n")
    log.close()
    (outdir / f"{slug}-{ep['id']}.json").write_text(json.dumps(verdict, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{slug} : {verdict['conclusion']}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
