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
- [`BENCHMARK.xlsx`](BENCHMARK.xlsx) — **classeur de synthèse dérivé des dossiers d'institutions, régénéré automatiquement par la CI quand ses sources changent.**
- [`scripts/`](scripts/) — `probe.py` (sonde polie), `fetch_doc.sh` (téléchargement avec empreintes),
  `extract_text.py` (texte lisible), `suivi.py` (consigne, cases, validation), `build_benchmark.py` (classeur).

## Mise à jour automatique

Le crochet `.githooks/pre-commit` (activation : `git config core.hooksPath .githooks`) :
1. recopie la consigne intégrale dans chaque `CONSIGNE-ET-SUIVI.md` et recalcule les contrôles de prudence ;
2. **valide** le suivi : une case cochée sans justification ou sans preuve existante bloque le commit ;
3. régénère `BENCHMARK.xlsx` (nécessite `openpyxl`, voir `requirements.txt`).

Si `openpyxl` n'est pas dans le Python par défaut, définir `VEILLE_PYTHON`
(ex. `/Users/marcel/.venvs/veille/bin/python`).

## Chaîne de provenance et synchronisation GitHub Actions (novembre 2026)

Les sources de vérité sont les **dossiers institutionnels**, pas le tableur.

1. `institutions/<slug>/data.json` porte les **données structurées** (limites, domaines, sources, observations, blocages et URL à vérifier).
2. `institutions/<slug>/CONSIGNE-ET-SUIVI.md` porte les **étapes a à g**, avec justifications et chemins des preuves. `sources/`, `config/` et `tests/` conservent les éléments cités lorsque disponibles. `fiche.md` est la synthèse lisible.
3. [`.github/workflows/benchmark-sync-rattrapage.yml`](.github/workflows/benchmark-sync-rattrapage.yml) se déclenche quand les **sources du classeur** changent : `institutions/**` (y compris `CONSIGNE-ET-SUIVI.md` et les preuves), scripts de validation/génération, méthodologie, dépendances et configuration du workflow. La CI exécute `scripts/suivi.py validate` et `scripts/valider_preuves_rattrapage.py`, puis **régénère** `BENCHMARK.xlsx` avec `scripts/build_benchmark.py`. Elle vérifie le ZIP/XLSX et commite le résultat binaire **uniquement sur la branche de révision**.
4. Si un autre commit a fait avancer la branche pendant la génération, le workflow **repart des dernières sources et recalcule le classeur avant de pousser** ; il n'écrase jamais les fichiers distants. Il échoue plutôt que de publier un tableur potentiellement obsolète après quatre tentatives.
5. [`.github/workflows/rattrapage-documentaire.yml`](.github/workflows/rattrapage-documentaire.yml) tourne à chaque `push` de la branche, vérifie les observations et publie un **CSV de triage actif** distinct du tableau historique des URL. Les tests documentaires ne font **aucune requête vers les services IIIF**.

**Différences de garantie :** les contrôles automatiques attestent que les chemins de preuves déclarés existent, que les étapes ont des justifications, que les nouvelles entrées `web` renvoient à un rapport versionné contenant l'URL, et que le classeur peut être reconstruit. Ils **n'authentifient pas à eux seuls la vérité d'une page web**, une mesure de débit, la complétude des captures originales ou la possibilité de moissonner en production. Les textes récupérés dans une **copie indexée** restent distincts des réponses HTTP de la sonde. Une note de lecture ne se fait pas passer pour une capture brute avec empreinte SHA-256.

Le fichier `data/reverifications-chatgpt-2026-11-14.csv` est le **registre append-only des observations** (ancien blocage et nouvelle lecture peuvent coexister), non une source à recopier manuellement dans Excel. La file de travail `triage-interventions-humaines.csv` est calculée par CI et distribuée dans les artefacts GitHub Actions. L'onglet historique « À vérifier à la main » reste volontairement exhaustif pour la traçabilité.

**Prudence :** aucun nouveau test de charge ni franchissement de protection n'est déclenché par ces workflows. L'étape g requiert une décision explicite au cas par cas, conformément à `METHODOLOGY.md`.
