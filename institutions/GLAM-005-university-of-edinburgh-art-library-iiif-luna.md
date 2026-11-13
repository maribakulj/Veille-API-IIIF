---
id: GLAM-005
institution: University of Edinburgh – Art / Library (IIIF, LUNA)
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE (pages IIIF lues, aucune documentation API propre au site)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni clé d’API sur les deux pages IIIF lues'
debit_iiif: Aucun seuil de débit IIIF publié sur les deux pages lues (art/iiif et mimed/iiif). Les pages décrivent IIIF comme standard adopté, des manifestes obtenus depuis les logos IIIF ou LUNA, et renvoient vers la plateforme d’images LUNA et vers des viewers tiers, sans documentation d’API propre au site.
iiif_image: « IIIF-compliant » sans version précisée
iiif_presentation: Manifestes ; version non précisée
api_recherche: ND
change_discovery: ND
acces: NON PRÉSENT SUR CETTE PAGE (aucune restriction décrite)
moissonnage: NON PRÉSENT SUR CETTE PAGE; partage et import de manifestes par URL seulement
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: Copyright Université « sauf mention contraire » ; page Licensing & Copyright sans contenu lu
strategie: IIIF adopté comme standard d'interopérabilité et de workflow ; images LUNA IIIF-compliant ; réutilisation par URL sans stockage local
lacunes:
- licence détaillée (page Licensing & Copyright) non lue
- plateforme LUNA (images.is.ed.ac.uk) non lue
methode: 'WebSearch « University of Edinburgh Art Collections IIIF API rate limit » : que des pages tierces ou génériques ; WebFetch collections.ed.ac.uk/art/iiif : aucun chiffre ; Passe 2 (2026-11-13) : 2 WebSearch (dont une restreinte à ed.ac.uk), 2 WebFetch (art/iiif ; mimed/iiif). La plateforme LUNA (images.is.ed.ac.uk) n’a pas été lue.'
verifie_le: '2026-11-13'
sources:
- url: https://collections.ed.ac.uk/art/iiif
  note: ''
  surveiller: true
- url: https://collections.ed.ac.uk/mimed/iiif
  note: Aucun chiffre ni clé mentionnée ; manifestes via logos IIIF ou LUNA ; pas de documentation API propre au site
  surveiller: true
---

# University of Edinburgh – Art / Library (IIIF, LUNA)

**Verdict** : DOC LUE, AUCUN CHIFFRE

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « University of Edinburgh Art Collections IIIF API rate limit » : que des pages tierces ou génériques
- WebFetch collections.ed.ac.uk/art/iiif : aucun chiffre

## Passe 2 (2026-11-13)
- WebFetch collections.ed.ac.uk/art/iiif : aucun chiffre ; liens vers iiif.io et les viewers tiers seulement ; pas de documentation API.
- WebFetch collections.ed.ac.uk/mimed/iiif : aucun chiffre ; lien vers images.is.ed.ac.uk (LUNA), présentée comme compatible IIIF mais non lue.
- WebSearch restreinte à ed.ac.uk : seules des conditions de services sans rapport avec les images sont apparues (EIDF, politique informatique) ; non retenues.
- Les deux pages lues sont sous collections.ed.ac.uk ; aucune page de services de bibliothèque n’a été lue.
