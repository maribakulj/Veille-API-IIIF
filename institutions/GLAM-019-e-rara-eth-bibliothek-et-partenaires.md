---
id: GLAM-019
institution: e-rara (ETH-Bibliothek et partenaires)
pays: Suisse
statut: DOC LUE, AUCUN CHIFFRE (page de la ZB lue ; wiki API refusé en passe 1)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur la page ZB ; « 100 résultats par page » est un affichage'
debit_iiif: Aucun seuil de débit publié sur la page de la ZB Zürich. Le seul chiffre (jusqu’à 100 résultats par page) est une option d’affichage. Aucune documentation d’API e-rara n’est liée ; le seul lien IIIF renvoie à la norme générale. Les PDF e-rara sont accessibles gratuitement, sans condition chiffrée.
iiif_image: 'Image API Version 2.1 (page ZB Data Map « e-rara IIIF », version #3, mise à jour 19 mars 2025)'
iiif_presentation: Presentation API Version 2.0 (URI /i3f/v20/{id}/manifest)
api_recherche: NON PRÉSENT dans les sources lues
acces: NON PRÉSENT dans les sources lues
moissonnage: 'OAI-PMH : le lien manifeste figure dans la réponse METS de l''interface OAI (ZB Data Map)'
robots_waf: NON PRÉSENT dans les sources lues
droits: NON PRÉSENT dans les sources lues
lacunes:
- wiki apiinfo refusé en passe 1
- documentation API e-rara absente de la page lue
methode: 'WebSearch « e-rara ETH-Bibliothek IIIF API Nutzungsbedingungen Limite Anfragen » : fiches ZB Zürich et Université de Berne, sans limite ; WebFetch e-rara.ch/wiki/apiinfo : refusé (hors liste autorisée) ; Passe 2 (2026-11-13) : 1 WebFetch (page ZB, lue pour e-rara et e-manuscripta).'
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

## Passe 2 (2026-11-13)
- WebFetch zb.uzh.ch (plateformes) : aucun chiffre de requêtes ni de téléchargement ; 100 résultats par page (affichage) ; PDF gratuits ; clé non précisée.
- Le wiki apiinfo (e-rara.ch) a été refusé par l’outil en passe 1 : non réessayé, non contourné.
