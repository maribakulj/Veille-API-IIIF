# Veille-API-IIIF

Veille sur les API IIIF des institutions patrimoniales : quotas, limites de débit (rate limits) et
leur annonce dans la documentation et dans les réponses.

## Où est quoi

- [`CONSIGNE.md`](CONSIGNE.md) — les consignes de Marcel, mot pour mot ; recopiées dans chaque dossier.
- [`METHODOLOGY.md`](METHODOLOGY.md) — la méthode v2 (étapes a à g), les règles de prudence.
- [`AUDIT-HAIKU.md`](AUDIT-HAIKU.md) — l'audit du premier travail et les décisions qui en découlent.
- [`institutions/`](institutions/) — **un dossier par institution** (93 : les 84 du classeur de référence
  + 9 hors liste). Dans chaque dossier :
  - `CONSIGNE-ET-SUIVI.md` — la consigne intégrale et chaque étape **cochée avec justification et preuves** ;
  - `fiche.md` — la fiche rédigée ; `data.json` — les données structurées ;
  - `sources/` — pages de doc téléchargées (HTML brut, texte extrait, empreintes SHA-256) ;
  - `config/` — configurations de sonde ; `tests/journal.log` et `tests/raw/` — journaux et en-têtes complets.
- [`data/perimetre.csv`](data/perimetre.csv) — les 84 institutions du classeur de référence et leur dossier.
- [`BENCHMARK.xlsx`](BENCHMARK.xlsx) — **classeur de synthèse, régénéré automatiquement à chaque commit.**
- [`scripts/`](scripts/) — `probe.py` (sonde polie), `fetch_doc.sh` (téléchargement avec empreintes),
  `extract_text.py` (texte lisible), `suivi.py` (consigne, cases, validation), `build_benchmark.py` (classeur).

## Mise à jour automatique

Le crochet `.githooks/pre-commit` (activation : `git config core.hooksPath .githooks`) :
1. recopie la consigne intégrale dans chaque `CONSIGNE-ET-SUIVI.md` et recalcule les contrôles de prudence ;
2. **valide** le suivi : une case cochée sans justification ou sans preuve existante bloque le commit ;
3. régénère `BENCHMARK.xlsx` (nécessite `openpyxl`, voir `requirements.txt`).

Si `openpyxl` n'est pas dans le Python par défaut, définir `VEILLE_PYTHON`
(ex. `/Users/marcel/.venvs/veille/bin/python`).
