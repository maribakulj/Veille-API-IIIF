# Configurations des sondes

Une configuration par institution : `scripts/config/<slug>.json`, lancée avec
`python3 scripts/probe.py scripts/config/<slug>.json` (ou `--dry-run` pour
vérifier la liste sans rien envoyer).

Format :
```json
{
  "slug": "<slug>",
  "min_delay_s": 6,
  "max_requests": 15,
  "endpoints": [
    {"id": "manifeste", "method": "GET", "url": "https://..."},
    {"id": "info-json", "method": "GET", "url": "https://..."}
  ]
}
```

Chaque endpoint vient de la doc officielle de l'institution (URL citée dans la fiche).
`_exemple.json` est un modèle factice, à ne jamais lancer.
