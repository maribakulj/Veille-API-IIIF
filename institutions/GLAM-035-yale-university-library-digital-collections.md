---
id: GLAM-035
institution: Yale University Library – Digital Collections
pays: États-Unis
statut: DOC LUE, AUCUN CHIFFRE (aide lue ; visionneuse IIIF, pas d’API)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur la page d’aide ; téléchargements sans plafond chiffré'
debit_iiif: Aucun seuil publié sur la page d’aide. Les images se téléchargent en JPG (réduit ou plein format), en TIFF plein format ou en PDF ; la seule contrainte est non chiffrée (JPG redimensionné pour certains très grands objets). La visionneuse est décrite comme compatible IIIF, avec un manifeste par objet, sans limite. Les connexions (NetID Yale, compte pour accès restreint) sont des contrôles d’accès, non des clés d’API.
iiif_image: NON PRÉSENT dans l'aide lue ; services IIIF images.collections.yale.edu/iiif/2/ observés dans des manifestes officiels (non décrits dans l'aide)
iiif_presentation: « All Digital Collections objects have a corresponding IIIF manifest » (aide) ; version non précisée
acces: NON PRÉSENT dans l'aide lue
moissonnage: Téléchargement unitaire via le visualiseur (icône de téléchargement) ; bulk NON PRÉSENT
robots_waf: NON PRÉSENT dans l'aide lue
droits: NON PRÉSENT dans l'aide lue
lacunes:
- aucune documentation d’API sur la page d’aide
- documentation IIIF propre à Yale non lue
methode: 'WebSearch « Yale University Library digital collections IIIF API rate limit » : agrégateurs tiers écartés ; WebSearch « Yale University Library IIIF collections manifests guide rate limits crawling » (domaines iiif.io, library.yale.edu, yale.edu) : aide et atelier lus, pas de chiffre ; Passe 2 (2026-11-13) : 1 WebFetch (aide).'
verifie_le: '2026-11-13'
sources:
- url: https://digital.library.yale.edu/help_guide
  note: '(lue : aucun chiffre)'
  surveiller: true
- url: https://training.iiif.io/advanced_iiif/basics/finding_yale.html
  note: '(lue en extrait : version 3 par défaut, accès restreint au campus, pas de chiffre)'
  surveiller: true
---

# Yale University Library – Digital Collections

**Verdict** : DOC LUE, AUCUN CHIFFRE (aide Digital Collections et atelier IIIF lus ; guide IIIF Yale Library non lu)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Yale University Library digital collections IIIF API rate limit » : agrégateurs tiers écartés
- WebSearch « Yale University Library IIIF collections manifests guide rate limits crawling » (domaines iiif.io, library.yale.edu, yale.edu) : aide et atelier lus, pas de chiffre

## Passe 2 (2026-11-13)
- WebFetch help_guide : aucun seuil ni quota ; pas d’API mentionnée ; clé non mentionnée ; connexions = contrôles d’accès.
- Le chiffre 4516 x 2951 px et 300 dpi est un exemple, non une limite.
