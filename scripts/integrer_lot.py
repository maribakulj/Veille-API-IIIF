#!/usr/bin/env python3
"""Intègre la branche lot/<ID> dans la branche principale (coordinateur seulement).

1. refuse si le diff du lot touche autre chose que institutions/<slug>/ des institutions DU LOT ;
2. fusion sans commit, puis validation GLOBALE (toutes les étapes cochées, ordre par lot, journaux) ;
3. si tout passe : commit de fusion + régénération du classeur ; sinon : annulation de la fusion.
Usage : python3 scripts/integrer_lot.py A [--push]
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PY = str(Path.home() / ".venvs/veille/bin/python") if (Path.home() / ".venvs/veille/bin/python").exists() else sys.executable


def sh(*a, check=True):
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"échec : {' '.join(a)}\n{r.stdout}{r.stderr}")
    return r


def main(lot, push):
    lots = json.loads((REPO / "data" / "lots.json").read_text())
    if lot not in lots:
        sys.exit(f"lot inconnu : {lot}")
    base = sh("git", "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if base.startswith("lot/") or sh("git", "status", "--porcelain").stdout.strip():
        sys.exit("intégration depuis la branche principale, arbre propre, seulement.")
    br = f"lot/{lot}"
    ok = tuple(f"institutions/{s}/" for s in lots[lot])
    fichiers = sh("git", "diff", "--name-only", f"{base}...{br}").stdout.split()
    hors = [f for f in fichiers if not f.startswith(ok)]
    if hors:
        sys.exit(f"REFUSÉ : le lot {lot} touche des fichiers hors de son périmètre : {hors[:8]}")
    if not fichiers:
        print(f"lot {lot} : rien à intégrer")
        return 0
    r = sh("git", "merge", "--no-commit", "--no-ff", br, check=False)
    if r.returncode:
        sh("git", "merge", "--abort", check=False)
        sys.exit(f"REFUSÉ : conflit de fusion\n{r.stdout}{r.stderr}")
    v = subprocess.run([sys.executable, "scripts/suivi.py", "all"], cwd=REPO, capture_output=True, text=True)
    if v.returncode:
        sh("git", "merge", "--abort", check=False)
        sys.exit("REFUSÉ : validation globale en échec, fusion annulée :\n" + "\n".join(v.stdout.splitlines()[-15:]))
    sh("git", "commit", "--no-verify", "-q", "-m", f"Intégration du lot {lot} ({len(fichiers)} fichiers, validation globale OK)\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>")
    subprocess.run([PY, "scripts/build_benchmark.py"], cwd=REPO, capture_output=True)
    sh("git", "add", "BENCHMARK.xlsx", "institutions")
    sh("git", "commit", "-q", "-m", f"Régénération du classeur après intégration du lot {lot}\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>", check=False)
    if push:
        sh("git", "push", "-q", "origin", base)
    print(f"lot {lot} intégré ({len(fichiers)} fichiers)" + (" et poussé" if push else ""))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], "--push" in sys.argv))
