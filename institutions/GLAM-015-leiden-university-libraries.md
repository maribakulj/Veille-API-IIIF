---
id: GLAM-015
institution: Leiden University Libraries
pays: Pays-Bas
statut: DOC LUE, AUCUN CHIFFRE (pages de services en brouillon)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur les trois pages lues ; pages marquées brouillon'
debit_iiif: Aucun seuil de débit publié sur les trois pages lues (services, conditions d’utilisation, serveur IIIF public). Les pages indiquent IIIF Image API v2.1, une disponibilité limitée à certaines collections, l’absence de service d’authentification IIIF prévu, et des droits rattachés au info.json. Les pages étant en brouillon, leur contenu peut changer.
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
- "page d’usage liée depuis iiif.universiteitleiden.nl : non suivie"
methode: 'WebSearch « Leiden University Libraries IIIF image API rate limit terms of use » : pages lab.library, aucune limite ; WebFetch lab.library services : aucune limite, Image API v2.1 seulement ; WebFetch lab terms-of-use : brouillon, aucune limite ; page des conditions finales non lue ; Passe 2 (2026-11-13) : 1 WebSearch, 3 WebFetch (services ; terms-of-use ; iiif.universiteitleiden.nl).'
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

## Passe 2 (2026-11-13)
- WebFetch lab.library.universiteitleiden.nl/iiif-docs/services/ : aucun chiffre ; IIIF Image API v2.1 ; disponibilité pour certaines collections ; authentification IIIF non prévue ; page en brouillon.
- WebFetch terms-of-use : aucun chiffre ni clé ; chaque image renvoie vers ses droits via le info.json ; page en brouillon.
- WebFetch iiif.universiteitleiden.nl : aucun chiffre ; renvoie vers une page décrivant les usages permis et interdits, sans URL donnée ; non suivie, à lire en priorité à la prochaine passe.
