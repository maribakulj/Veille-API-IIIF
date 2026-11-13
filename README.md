# Veille API IIIF

Veille des documentations d'API IIIF et de leurs conditions d'accès (débits, clés, moissonnage, bots) pour des bibliothèques, archives et musées.

## Structure

- `institutions/` : une fiche Markdown par institution (`GLAM-NNN-nom.md`). L'en-tête YAML contient les données ; le corps contient les notes et les traces de vérification. Le modèle est `institutions/_modele.md`.
- `scripts/fiches.py` : lecture des fiches et correspondance statut → classe.
- `scripts/validate.py` : contrôle des fiches (champs requis, identifiants, classes, dates, URL).
- `scripts/check_sources.py` : veille des pages marquées `surveiller: true`. Calcule une empreinte du texte, compare à la précédente, et enregistre les changements.
- `scripts/build_xlsx.py` : génère `docs/veille_iiif.xlsx` (onglets Synthèse, Institutions, Sources, Changements) et `docs/veille_iiif.csv`.
- `data/` : empreintes (`state.json`), historique des changements (`historique.jsonl`), dernier passage (`changements.json`).
- `.github/workflows/veille.yml` : à chaque modification des fiches ou des scripts, tests, validation, génération du classeur, puis commit des sorties. Chaque lundi, la veille des sources s'ajoute.

## Utilisation

```
pip install -r requirements.txt
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/check_sources.py     # réseau requis
python3 scripts/build_xlsx.py
```

Pour ajouter ou corriger une institution, modifier sa fiche, lancer `validate.py`, puis `build_xlsx.py`. Sur GitHub, le workflow fait ces étapes et met à jour le classeur.

## Vocabulaire des statuts

Le statut commence par un préfixe, qui détermine la classe :

- `CHIFFRE TROUVÉ` : chiffre de débit lu sur une page officielle (classe « chiffre publié »).
- `PAS DE DÉBIT IIIF CHIFFRÉ` : limite voisine (REST, plateforme, pagination) ou recommandation, sans chiffre IIIF.
- `PARTIEL` : règle annoncée sans valeur chiffrée.
- `CHIFFRE À CONFIRMER` : chiffre trouvé mais non confirmé par une page officielle.
- `DOC LUE` : documentation officielle lue, sans quota publié.
- `NON TROUVÉ APRÈS RECHERCHE` : aucune documentation officielle de quota trouvée. Ce n'est pas une preuve d'absence de limite.

## Ce qui est automatique et ce qui ne l'est pas

Automatique : validation, génération du classeur à chaque modification, détection des pages qui changent (empreinte du texte, une fois par semaine).

Non automatique : interpréter un changement. Une alerte signale qu'une page a bougé, pas quelle valeur a changé ; il faut ouvrir la page et mettre la fiche à jour. Les pages très dynamiques (horodatages, jetons) peuvent produire de fausses alertes.

Le classeur Excel n'est pas un fichier lié en direct à GitHub : il est régénéré et committé à chaque passage du workflow. Une modification de fiche se voit donc dans le classeur après l'exécution du workflow.
