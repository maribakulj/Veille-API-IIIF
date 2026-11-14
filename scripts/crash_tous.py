#!/usr/bin/env python3
"""Enchaîne les crash tests (étape g) UN PAR UN, en fin de boucle (décision de Marcel, C15). Coordinateur seulement.

Pour chaque institution dont l'audit a–f est terminé et dont l'étape g reste à faire :
  1. ordre : hôtes sans réseau à réputation partagée d'abord, réseaux protégés (Cloudflare, CloudFront…) en dernier ;
  2. lance scripts/crash.py pour chaque configuration config/crash-*.json (la politique adaptative de crash.py s'applique :
     plafond 200 ou 60 req/min, requête témoin, 30 min entre réseaux protégés, hôte partagé testé une fois, hôte arrêté refusé) ;
  3. coche g avec justification et preuves (journal + verdicts), ajoute une section « Crash test » à la fiche, valide, commite ;
  4. s'arrête net si l'IP semble défiée (3 abandons consécutifs sur requête de détection ou témoin).
Reprise possible à tout moment : une institution dont g est cochée est sautée.
Usage : python3 scripts/crash_tous.py [--max N] [--seulement slug,slug] [--push]
"""
import glob
import json
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import crash  # noqa: E402
import suivi  # noqa: E402

PY = sys.executable
OUT = REPO / "data" / "crash_tous.log"


def log(m):
    ligne = f"{crash.now()} | {m}"
    print(ligne, flush=True)
    with OUT.open("a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def hote_de(cfg_path):
    from urllib.parse import urlsplit
    return urlsplit(json.loads(Path(cfg_path).read_text(encoding="utf-8"))["endpoint"]["url"]).netloc


def reseau_connu(slug, hote):
    """Réseau déjà observé pour cet hôte dans les en-têtes bruts enregistrés (sert à ordonner, crash.py redétecte)."""
    for f in glob.glob(str(REPO / "institutions" / slug / "tests" / "raw" / "*.headers.txt")):
        t = Path(f).read_text(encoding="utf-8", errors="replace")
        lignes = t.splitlines()
        if lignes and hote in lignes[0]:
            r = crash.detecter_reseau(dict(l.split(": ", 1) for l in lignes[2:] if ": " in l))
            if r:
                return r
    return []


def a_faire():
    out = []
    for slug in suivi.slugs():
        r = suivi.lire_suivi(slug)
        if not r or r[0] != "active" or not suivi.termine(slug):
            continue
        if r[1].get("g", (" ",))[0] in ("x", "~"):
            continue
        excl = json.loads((REPO / "data" / "crash_exclusions.json").read_text(encoding="utf-8")) if (REPO / "data" / "crash_exclusions.json").exists() else {}
        if slug in excl:
            continue
        cfgs = sorted(glob.glob(str(REPO / "institutions" / slug / "config" / "crash-*.json")))
        if not cfgs:
            continue
        protege = any(reseau_connu(slug, hote_de(c)) for c in cfgs)
        out.append((1 if protege else 0, slug, cfgs))
    out.sort()
    return out


def justification(slug, verdicts):
    morceaux = []
    for v in verdicts:
        base = "repris d'une autre institution (hôte partagé)" if v.get("repris_de") else v.get("conclusion", "?")
        morceaux.append(f"{v['endpoint']} sur {v['hote']} : {base}" + (f" (réseau {', '.join(v['reseaux'])}, plafond {v['plafond_req_min']} req/min)" if v.get("reseaux") else f" (plafond {v.get('plafond_req_min', '?')} req/min)"))
    return "Crash test fait le " + crash.now()[:10] + " : " + " ; ".join(morceaux)


def cloturer(slug, push):
    vs = [json.loads(Path(f).read_text(encoding="utf-8")) for f in sorted(glob.glob(str(REPO / "institutions" / slug / "tests" / "crash" / f"{slug}-*.json")))]
    if not vs:
        return False
    j = justification(slug, vs)
    preuves = [f"institutions/{slug}/tests/crash/{slug}.log"] + [f"institutions/{slug}/tests/crash/{Path(f).name}" for f in sorted(glob.glob(str(REPO / "institutions" / slug / "tests" / "crash" / f"{slug}-*.json")))]
    fiche = REPO / "institutions" / slug / "fiche.md"
    with fiche.open("a", encoding="utf-8") as f:
        f.write("\n## Crash test (étape g)\n\n" + j + ".\nJournal : `tests/crash/" + slug + ".log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.\n")
    r = subprocess.run([PY, "scripts/suivi.py", "set", slug, "g", "x", j[:900]] + preuves, cwd=REPO, capture_output=True, text=True)
    if r.returncode:
        log(f"{slug} : suivi set g a échoué : {r.stderr[-200:]}")
        return False
    c = subprocess.run(["git", "add", "-A"], cwd=REPO, capture_output=True, text=True)
    c = subprocess.run(["git", "commit", "-q", "-m", f"Veille : crash test (étape g) — {slug}\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"], cwd=REPO, capture_output=True, text=True)
    if c.returncode:
        log(f"{slug} : commit refusé : {(c.stdout + c.stderr)[-300:]}")
        return False
    return True


def pousser():
    import integrer_lot
    mal = integrer_lot.commits_avec_secret("origin/claude/veille-iiif-quotas..claude/veille-iiif-quotas")
    if mal:
        log(f"PUSH REFUSÉ : valeur sensible dans {mal[:3]}")
        return
    for _ in range(3):
        r = subprocess.run(["git", "-c", "http.postBuffer=524288000", "push", "-q", "origin", "claude/veille-iiif-quotas"], cwd=REPO, capture_output=True, text=True)
        if r.returncode == 0:
            log("push OK")
            return
        time.sleep(10)
    log("push échoué (réessayé au prochain cycle)")


def main():
    args = sys.argv[1:]
    maxi = int(args[args.index("--max") + 1]) if "--max" in args else 10**6
    seul = set(args[args.index("--seulement") + 1].split(",")) if "--seulement" in args else None
    push = "--push" in args
    faits, abandons_consecutifs = 0, 0
    todo = a_faire()
    log(f"{len(todo)} institution(s) à crash-tester ({sum(1 for t in todo if t[0] == 0)} sans réseau protégé connu)")
    for _, slug, cfgs in todo:
        if seul and slug not in seul:
            continue
        if faits >= maxi:
            break
        log(f"=== {slug} ({len(cfgs)} configuration(s))")
        ok_une = False
        for cfg in cfgs:
            while True:
                r = subprocess.run([PY, "scripts/crash.py", str(Path(cfg).relative_to(REPO))], cwd=REPO, capture_output=True, text=True)
                sortie = (r.stdout + r.stderr).strip()
                if r.returncode == 0:
                    log(f"{slug} / {Path(cfg).name} : {sortie.splitlines()[-1] if sortie else 'ok'}")
                    ok_une = True
                    abandons_consecutifs = 0
                    break
                if sortie.startswith("ATTENTE"):
                    m = re.search(r"attendre encore (\d+) s", sortie)
                    att = int(m.group(1)) + 5 if m else 600
                    log(f"{slug} : {sortie[:120]} → attente {att} s")
                    time.sleep(att)
                    continue
                log(f"{slug} / {Path(cfg).name} : {sortie[:240]}")
                if "détection" in sortie or "témoin" in sortie:
                    abandons_consecutifs += 1
                break
        if abandons_consecutifs >= 3:
            log("ARRÊT GÉNÉRAL : 3 abandons consécutifs sur détection/témoin : l'IP est peut-être défiée.")
            break
        if ok_une and cloturer(slug, push):
            faits += 1
            log(f"{slug} : g cochée, commit fait ({faits})")
            if push and faits % 5 == 0:
                pousser()
    if push:
        pousser()
    log(f"terminé : {faits} institution(s) clôturée(s)")


if __name__ == "__main__":
    main()
