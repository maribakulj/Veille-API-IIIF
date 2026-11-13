---
id: GLAM-015
institution: Leiden University Libraries
pays: Pays-Bas
statut: DOC LUE, AUCUN CHIFFRE (conditions d'utilisation en brouillon, renvoi vers une page non lue)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE (conditions d''utilisation en brouillon, renvoi vers une page non lue) ; '
debit_iiif: 'Aucun débit, quota, nombre de requêtes, throttling, code 429, clé d''API ni règle de moissonnage sur la page des services IIIF ni sur la page des conditions. La page des services indique : Image API v2.1 pour certaines collections seulement, Presentation API v2.1, Authentication API non prévue, Image API v3 non prévue. La page des conditions se dit « This page is a draft » et renvoie à une page « Terms and conditions » non lue, où des règles d''usage pourraient figurer.'
iiif_image: Image API v2.1 (page officielle de services)
iiif_presentation: Presentation API v2.1 ; v3 « non prévue, sur le radar »
api_recherche: 'Content Search API : « currently not supported for any IIIF content »'
change_discovery: Change Discovery v0.3 « not available » ; WebSub « not available »
acces: Authentication API « not yet planned » ; accès aux œuvres non libres restreint selon droits
moissonnage: Non relevé ; page terms « draft »
droits: Conditions d'usage publiées en brouillon ; « rights information linked from the info.json resource »
strategie: Founding member IIIF ; plateforme UBL IIIF avec ~200 000 objets (communiqué 2020)
lacunes:
- page terms en brouillon (non définitive)
methode: 'WebSearch « Leiden University Libraries IIIF image API rate limit terms of use » : pages lab.library, aucune limite ; WebFetch lab.library services : aucune limite, Image API v2.1 seulement ; WebFetch lab terms-of-use : brouillon, aucune limite ; page des conditions finales non lue'
verifie_le: '2026-11-13'
sources:
- url: https://lab.library.universiteitleiden.nl/iiif-docs/services/
  note: (aucun chiffre, relu)
  surveiller: true
- url: https://lab.library.universiteitleiden.nl/iiif-docs/terms-of-use/
  note: (brouillon ; droits et republication, sans limite technique)
  surveiller: true
- url: https://iiif.universiteitleiden.nl/
  note: (serveur IIIF public, sans chiffre lu)
  surveiller: true
---

# Leiden University Libraries

**Verdict** : DOC LUE, AUCUN CHIFFRE (conditions d'utilisation en brouillon, renvoi vers une page non lue)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Leiden University Libraries IIIF image API rate limit terms of use » : pages lab.library, aucune limite
- WebFetch lab.library services : aucune limite, Image API v2.1 seulement
- WebFetch lab terms-of-use : brouillon, aucune limite ; page des conditions finales non lue
