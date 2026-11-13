---
id: GLAM-012
institution: Rijksmuseum
pays: Pays-Bas
statut: DOC LUE, AUCUN CHIFFRE (clé d’API obligatoire)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota publié sur la page API lue ; clé d’API obligatoire'
debit_iiif: 'Aucun seuil de débit publié sur la page API lue. La page ne nomme pas IIIF : elle évoque des images en mosaïque (tiled images) pour le zoom. Une clé d’API est requise, obtenue par un compte Rijksstudio : c’est un contrôle d’accès, non un débit. La page object-metadata/api n’a pas pu être lue (URL hors liste autorisée) ; elle n’a pas été contournée.'
iiif_image: 'Image API implémentée (Micrio, Q42) ; version non confirmée par extrait officiel (classeur : v3)'
iiif_presentation: 'Presentation API implémentée ; version non confirmée (classeur : v3)'
api_recherche: 'Search API nouvelle (classeur : 100 résultats/page ; à relire)'
change_discovery: 'Change Discovery API : max 100 événements par page ; pagination, pas quota ; dataset CC0'
acces: Clé d’API obligatoire (compte Rijksstudio), selon la page docs/api
moissonnage: Change Discovery, LDES, OAI-PMH ; datasets licence CC0 (dataset register)
droits: Licence CC0 sur datasets de métadonnées
strategie: Plateforme de données multi-représentations ; open data depuis 2012 (de facto) ; FAIR depuis 2021
conflits:
- Source acc.data = environnement d'acceptation, pas production
lacunes:
- docs officielles data.rijksmuseum.nl/docs/iiif non lues (seules versions acc.)
- confirmation des versions IIIF
methode: 'WebSearch « Rijksmuseum API rate limit requests per second Linked Art IIIF » : doc officielle et tiers (connecteur Microsoft 100/60 s exclu : tiers) ; WebSearch « Rijksmuseum data services API key limits IIIF » : clé requise, 10 000 objets ; WebFetch doc IIIF : aucun chiffre ; WebFetch user-generated-content : 10 000 objets, sans débit ; Passe 2 (2026-11-13) : 1 WebSearch (aucun résultat officiel exploitable), 1 WebFetch lu, 1 WebFetch refusé par l’outil (hors liste autorisée, non contourné).'
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
- url: https://data.rijksmuseum.nl/object-metadata/api/
  note: Refusée par l’outil de lecture (URL hors liste autorisée) ; non lue, non contournée
  surveiller: false
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

## Passe 2 (2026-11-13)
- WebFetch data.rijksmuseum.nl/docs/api : aucun seuil ; clé d’API ajoutée à chaque requête ; compte Rijksstudio requis ; aucun lien de documentation.
- WebFetch data.rijksmuseum.nl/object-metadata/api/ : refusé (hors liste autorisée). Non réessayé, non contourné. À reprendre si la page devient accessible.
- WebSearch « Rijksmuseum API rate limit requests per minute » : seuls des agrégateurs tiers (apis.io) sont apparus ; non retenus.
