#!/usr/bin/env python3
"""Intègre la branche lot/<ID> dans la branche principale (coordinateur seulement).

1. refuse si le diff du lot touche autre chose que institutions/<slug>/ des institutions DU LOT ;
2. fusion (commit local), puis validation GLOBALE sur le résultat (toutes les étapes cochées, ordre par lot, journaux) ;
3. si tout passe : régénération du classeur ; sinon : retour au commit précédent (rien n'est poussé).
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



def secrets():
    f = Path.home() / ".veille-state" / "secrets.txt"
    return [l.strip() for l in f.read_text().splitlines() if l.strip()] if f.exists() else []


def commits_avec_secret(rev_range):
    """Commits de la plage dont l'ARBRE contient une valeur sensible (IP de Marcel…) : le dépôt est PUBLIC."""
    mauvais = []
    for c in sh("git", "rev-list", rev_range).stdout.split():
        for v in secrets():
            if subprocess.run(["git", "grep", "-qF", v, c, "--", "."], cwd=REPO, capture_output=True).returncode == 0:
                mauvais.append(c)
                break
    return mauvais


def purger_lot(lot):
    """Réécrit la branche lot/<ID> (non poussée) en remplaçant les valeurs sensibles ; sauvegardes supprimées."""
    wt = REPO / ".lots" / f"lot-{lot}"
    for v in secrets():
        sed = "s/" + v.replace(".", "\\.") + "/[IP retirée]/g"
        subprocess.run(["git", "filter-branch", "-f", "--tree-filter",
                        f'grep -rlF "{v}" . 2>/dev/null | grep -v "^./.git/" | xargs -I{{}} sed -i "" "{sed}" {{}}',
                        f"{sh('git', 'rev-parse', '--abbrev-ref', 'HEAD').stdout.strip()}..lot/{lot}"], cwd=wt, capture_output=True)
    refs = sh("git", "for-each-ref", "--format=%(refname)", "refs/original").stdout.split()
    for r in refs:
        sh("git", "update-ref", "-d", r)


def main(lot, push):
    lots = json.loads((REPO / "data" / "lots.json").read_text())
    if lot not in lots:
        sys.exit(f"lot inconnu : {lot}")
    base = sh("git", "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if base.startswith("lot/") or sh("git", "status", "--porcelain").stdout.strip():
        sys.exit("intégration depuis la branche principale, arbre propre, seulement.")
    br = f"lot/{lot}"
    if commits_avec_secret(f"{base}..{br}"):
        print(f"lot {lot} : valeur sensible dans des commits non intégrés : purge de la branche avant fusion")
        purger_lot(lot)
        if commits_avec_secret(f"{base}..{br}"):
            sys.exit("REFUSÉ : la purge n'a pas suffi (valeur sensible dans l'arbre d'un commit du lot).")
        sh("git", "-C", str(REPO / ".lots" / f"lot-{lot}"), "merge", "-q", "--no-edit", base, check=False)
    ok = tuple(f"institutions/{s}/" for s in lots[lot])
    fichiers = sh("git", "diff", "--name-only", f"{base}...{br}").stdout.split()
    hors = [f for f in fichiers if not f.startswith(ok)]
    if hors:
        sys.exit(f"REFUSÉ : le lot {lot} touche des fichiers hors de son périmètre : {hors[:8]}")
    if not fichiers:
        print(f"lot {lot} : rien à intégrer")
        return 0
    avant = sh("git", "rev-parse", "HEAD").stdout.strip()
    r = sh("git", "merge", "--no-ff", "--no-verify", "-q", "-m",
           f"Intégration du lot {lot} ({len(fichiers)} fichiers)\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>", br, check=False)
    if r.returncode:
        sh("git", "merge", "--abort", check=False)
        sys.exit(f"REFUSÉ : conflit de fusion\n{r.stdout}{r.stderr}")
    # validation GLOBALE sur le résultat fusionné (l'historique git du lot est alors visible : contrôle « configuration
    # committée avant lancement ») ; en cas d'échec on revient au commit précédent (fusion locale, jamais poussée)
    v = subprocess.run([sys.executable, "scripts/suivi.py", "all"], cwd=REPO, capture_output=True, text=True)
    if v.returncode:
        sh("git", "reset", "-q", "--hard", avant)
        sys.exit("REFUSÉ : validation globale en échec, fusion annulée :\n" + "\n".join(v.stdout.splitlines()[-15:]))
    subprocess.run([PY, "scripts/build_benchmark.py"], cwd=REPO, capture_output=True)
    sh("git", "add", "BENCHMARK.xlsx", "institutions")
    sh("git", "commit", "-q", "-m", f"Régénération du classeur après intégration du lot {lot}\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>", check=False)
    mal = commits_avec_secret(f"origin/{base}..{base}")
    if mal:
        sys.exit(f"PUSH REFUSÉ : valeur sensible dans l'arbre de {len(mal)} commit(s) non poussé(s) : {mal[:5]}")
    if push:
        sh("git", "push", "-q", "origin", base)
    print(f"lot {lot} intégré ({len(fichiers)} fichiers)" + (" et poussé" if push else ""))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], "--push" in sys.argv))
