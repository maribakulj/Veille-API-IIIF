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
