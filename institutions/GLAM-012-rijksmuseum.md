---
id: GLAM-012
institution: Rijksmuseum
pays: Pays-Bas
statut: DOC LUE, AUCUN CHIFFRE IIIF (limite de volume REST seulement)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE IIIF (limite de volume REST seulement) ; '
debit_iiif: 'Aucun débit ni quota sur la page IIIF (images servies via Micrio). Chiffre de volume, hors IIIF : les API REST récupèrent au maximum 10 000 objets. Clé d’API requise pour les API de métadonnées (compte Rijksstudio) ; moissonnage OAI-PMH et LDES sans chiffre.'
iiif_image: 'Image API implémentée (Micrio, Q42) ; version non confirmée par extrait officiel (classeur : v3)'
iiif_presentation: 'Presentation API implémentée ; version non confirmée (classeur : v3)'
api_recherche: 'Search API nouvelle (classeur : 100 résultats/page ; à relire)'
change_discovery: 'Change Discovery API : max 100 événements par page ; pagination, pas quota ; dataset CC0'
acces: Non relevé sur extraits officiels
moissonnage: Change Discovery, LDES, OAI-PMH ; datasets licence CC0 (dataset register)
droits: Licence CC0 sur datasets de métadonnées
strategie: Plateforme de données multi-représentations ; open data depuis 2012 (de facto) ; FAIR depuis 2021
conflits:
- Source acc.data = environnement d'acceptation, pas production
lacunes:
- docs officielles data.rijksmuseum.nl/docs/iiif non lues (seules versions acc.)
- confirmation des versions IIIF
methode: 'WebSearch « Rijksmuseum API rate limit requests per second Linked Art IIIF » : doc officielle et tiers (connecteur Microsoft 100/60 s exclu : tiers) ; WebSearch « Rijksmuseum data services API key limits IIIF » : clé requise, 10 000 objets ; WebFetch doc IIIF : aucun chiffre ; WebFetch user-generated-content : 10 000 objets, sans débit'
verifie_le: '2026-11-13'
sources:
- url: https://acc.data.rijksmuseum.nl/docs/iiif/image
  note: (aucun chiffre, relu)
  surveiller: true
- url: https://data.rijksmuseum.nl/user-generated-content
  note: (« maximum of 10,000 objects » pour les API REST)
  surveiller: true
- url: https://data.rijksmuseum.nl/docs/api
  note: (clé requise via compte Rijksstudio)
  surveiller: true
---

# Rijksmuseum

**Verdict** : DOC LUE, AUCUN CHIFFRE IIIF (limite de volume REST seulement)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Rijksmuseum API rate limit requests per second Linked Art IIIF » : doc officielle et tiers (connecteur Microsoft 100/60 s exclu : tiers)
- WebSearch « Rijksmuseum data services API key limits IIIF » : clé requise, 10 000 objets
- WebFetch doc IIIF : aucun chiffre
- WebFetch user-generated-content : 10 000 objets, sans débit
