---
id: GLAM-062
institution: Norman B. Leventhal Map & Education Center – Boston Public Library
pays: États-Unis
statut: DOC LUE, AUCUN CHIFFRE (page des collections numériques lue ; manifestes et Search API décrits)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur la page ; clé pour la Search API non traitée'
debit_iiif: Aucun chiffre de limite sur la page des collections numériques. Les manifestes IIIF s’obtiennent en ajoutant un suffixe à l’URL d’un objet, et une API de recherche (search.json) accepte les mêmes paramètres que le portail. La page indique que les deux dépôts principaux sont accessibles sans inscription, sans dire si la Search API ou les endpoints IIIF requièrent une clé.
iiif_image: API IIIF mentionnée (github bplmaps/collections-api) ; version non précisée
iiif_presentation: 'Manifeste : suffixe /manifest.json ajouté à l''URL collections.leventhalmap.org (leventhalmap.org/collections/digital-collections)'
api_recherche: 'JSON : collections.leventhalmap.org/search.json, mêmes paramètres que le portail'
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: Tous les items interrogeables par API JSON et API IIIF (github bplmaps) ; export en masse non documenté
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: Collections soumises aux spécifications de Digital Commonwealth (github bplmaps) ; conditions NON PRÉSENT SUR CETTE PAGE
strategie: Double accès JSON et IIIF, relayé par le portail Digital Commonwealth ; quota non publié
lacunes:
- clé pour la Search API et les endpoints IIIF non précisée
- aucune documentation d’API liée
methode: 'WebSearch « Leventhal Map Center Boston Public Library IIIF API rate limit terms » : page officielle des collections en extrait, pas de chiffre ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (collections numériques).'
verifie_le: '2026-11-13'
sources:
- url: https://www.leventhalmap.org/collections/digital-collections
  note: '(extrait lu : aucun chiffre)'
  surveiller: true
- url: https://github.com/bplmaps/collections-api
  note: '(dépôt BPL, extrait : API JSON et IIIF, pas de chiffre)'
  surveiller: true
---

# Norman B. Leventhal Map & Education Center – Boston Public Library

**Verdict** : DOC LUE, AUCUN CHIFFRE (page officielle des collections numériques lue en extrait)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Leventhal Map Center Boston Public Library IIIF API rate limit terms » : page officielle des collections en extrait, pas de chiffre

## Passe 2 (2026-11-13)
- WebFetch collections numériques : aucun seuil ni throttling ; accès sans inscription pour les deux dépôts ; clé non traitée pour l’API.
