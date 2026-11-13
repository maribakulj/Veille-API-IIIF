# Consignes pour maintenir ce dépôt

Ce dépôt est une veille des documentations API IIIF de bibliothèques, archives et musées (84 fiches au départ).

## Sources de vérité

- `institutions/*.md` : une fiche par institution. L'en-tête YAML contient les données ; le corps contient les notes.
- `data/` : empreintes des pages surveillées et historique des changements, écrits par `scripts/check_sources.py`.
- `docs/veille_iiif.xlsx` et `docs/veille_iiif.csv` : sorties générées. Ne jamais les modifier à la main.

## Règles de rédaction des fiches

- Ne rien inventer. Chaque valeur vient d'une page officielle listée dans `sources`. Sinon, écrire `NON PRÉSENT SUR CETTE PAGE` ou un verdict « non trouvé ».
- Distinguer le débit IIIF des limites d'API REST, de plateforme ou de pagination. Une limite voisine n'est pas un débit IIIF.
- Une absence de chiffre ne signifie pas « pas de limite ».
- Une URL refusée par l'outil de lecture ne doit pas être contournée : la noter dans `note` et mettre `surveiller: false`.
- Citations : moins de 15 mots, une seule par source, paraphrase par défaut. Ne pas reproduire de texte protégé.
- Mettre `verifie_le` à la date de la vérification, au format AAAA-MM-JJ.
- Le `statut` doit commencer par un préfixe reconnu ; la `classe` doit correspondre (voir `scripts/fiches.py`).
- Rédiger en français.

## Après toute modification

```
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
python3 scripts/build_xlsx.py
```

Ne pas committer directement sur `main` : ouvrir une branche.
