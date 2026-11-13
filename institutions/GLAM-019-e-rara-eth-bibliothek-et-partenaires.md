---
id: GLAM-019
institution: e-rara (ETH-Bibliothek et partenaires)
pays: Suisse
statut: NON TROUVÉ APRÈS RECHERCHE (wiki officiel des API non lisible)
classe: non trouvé après recherche
statut_quota: NON TROUVÉ APRÈS RECHERCHE (wiki officiel des API non lisible) ; Documentation officielle d'API non accessible dans cette session ; aucune preuve d'absence de limite
debit_iiif: 'Aucun débit, quota ni limite de requêtes trouvé. Le wiki officiel des API (www.e-rara.ch/wiki/apiinfo), cité par la fiche de la Zentralbibliothek Zürich, n''a pas pu être lu : URL refusée par l''outil (hors liste autorisée). La fiche de données de la ZB Zürich (extraits lus) décrit les endpoints IIIF v2.1 (Image) et v2.0 (Presentation) sans chiffre. Aucun seuil publié trouvé.'
iiif_image: 'Image API Version 2.1 (page ZB Data Map « e-rara IIIF », version #3, mise à jour 19 mars 2025)'
iiif_presentation: Presentation API Version 2.0 (URI /i3f/v20/{id}/manifest)
api_recherche: NON PRÉSENT dans les sources lues
acces: NON PRÉSENT dans les sources lues
moissonnage: 'OAI-PMH : le lien manifeste figure dans la réponse METS de l''interface OAI (ZB Data Map)'
robots_waf: NON PRÉSENT dans les sources lues
droits: NON PRÉSENT dans les sources lues
lacunes:
- 'https://www.e-rara.ch/wiki/apiinfo : à retrouver via recherche pour lecture directe'
- limites, licences, bots non lus
methode: 'WebSearch « e-rara ETH-Bibliothek IIIF API Nutzungsbedingungen Limite Anfragen » : fiches ZB Zürich et Université de Berne, sans limite ; WebFetch e-rara.ch/wiki/apiinfo : refusé (hors liste autorisée)'
verifie_le: '2026-11-13'
sources:
- url: https://www.e-rara.ch/wiki/apiinfo
  note: (cité ; refusé)
  surveiller: false
- url: https://data.zb.uzh.ch/map/books/data-map-der-zentralbibliothek-zurich/export/pdf
  note: '(fiche officielle ZB Zürich : endpoints, sans limite dans les extraits lus)'
  surveiller: true
- url: https://www.zb.uzh.ch/en/services/die-plattformen-e-rara-und-e-manuscripta
  note: (présentation, sans chiffre)
  surveiller: true
---

# e-rara (ETH-Bibliothek et partenaires)

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (wiki officiel des API non lisible)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « e-rara ETH-Bibliothek IIIF API Nutzungsbedingungen Limite Anfragen » : fiches ZB Zürich et Université de Berne, sans limite
- WebFetch e-rara.ch/wiki/apiinfo : refusé (hors liste autorisée)
