# Veille-API-IIIF

Veille sur les API IIIF des institutions patrimoniales : quotas, limites de
débit (rate limits) et leur annonce dans la documentation et dans les réponses.

- [`METHODOLOGY.md`](METHODOLOGY.md) — méthode, règles de prudence, statuts.
- [`TEMPLATE.md`](TEMPLATE.md) — gabarit d'une fiche institution.
- [`institutions.csv`](institutions.csv) — liste des institutions suivies.
- [`institutions/`](institutions/) — une fiche par institution.
- [`tests/`](tests/) — journaux bruts des requêtes.
- [`REPORT.md`](REPORT.md) — synthèse, mise à jour à la fin de chaque lot.

## Classeur de synthèse (BENCHMARK.xlsx)

- Source unique : `data/institutions.json` (une entrée par institution).
- Régénéré par `scripts/build_benchmark.py` (nécessite `openpyxl`, voir `requirements.txt`).
- Régénération automatique à chaque commit : `git config core.hooksPath .githooks` (une fois).
  Si `openpyxl` n'est pas disponible pour le Python par défaut, définir `VEILLE_PYTHON`
  vers un Python qui l'a (ex. `/Users/marcel/.venvs/veille/bin/python`).
