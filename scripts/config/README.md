# Configurations des sondes

Les configurations réelles vivent **dans le dossier de chaque institution** :
`institutions/<slug>/config/<nom>.json`. Elles se lancent avec :

    python3 scripts/probe.py institutions/<slug>/config/<nom>.json [--dry-run]

La sonde écrit le journal dans `institutions/<slug>/tests/journal.log` et les en-têtes complets
dans `institutions/<slug>/tests/raw/`. Une configuration est **committée avant d'être lancée**.

Format :
```json
{
  "slug": "<slug>",
  "min_delay_s": 6,
  "max_requests": 15,
  "follow_redirects": 1,
  "note": "pourquoi cette passe",
  "endpoints": [
    {"id": "manifeste", "method": "GET", "url": "https://..."}
  ]
}
```

Chaque endpoint vient de la doc officielle (URL citée dans la fiche) ou, quand la doc n'en décrit
pas et ne l'interdit pas, d'un script poli : identifiants issus de pages publiques ou d'exemples
de la doc, jamais énumérés ni devinés. `_exemple.json` est un modèle factice, à ne jamais lancer.

Options de la sonde :
- `"robots_files": {"hote": "chemin/vers/copie.txt"}` : lire le robots.txt d'un hôte depuis une copie locale (utile quand le serveur le bloque en 403 ; aucune requête n'est envoyée pour lui).
- Par endpoint : `"save_body": 2000000` enregistre le corps de la réponse dans `tests/raw/<id>.body` (pour en extraire des identifiants publics, par exemple depuis un manifeste, au lieu de les deviner).
- `"respect_robots": false` à n'utiliser que si le robots.txt est illisible et qu'une copie locale a été lue à la main.
