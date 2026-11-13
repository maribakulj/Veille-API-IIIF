---
id: GLAM-020
institution: e-manuscripta (bibliothèques partenaires suisses)
pays: Suisse
statut: DOC LUE, AUCUN CHIFFRE (page de la ZB lue ; wiki API refusé en passe 1)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur la page ZB ; clé non précisée'
debit_iiif: Aucun seuil de débit publié sur la page de la ZB Zürich. La page indique que chaque titre e-manuscripta a un manifeste IIIF, sans expliquer comment y accéder ; les documents sont consultables en ligne ou téléchargeables en PDF gratuitement. Pas de documentation API.
iiif_image: 'Image API Version 2.1 (page ZB Data Map « e-manuscripta IIIF », version #5, mise à jour 19 mars 2025)'
iiif_presentation: Presentation API Version 2.0 (URI /i3f/v20/{VLID}/manifest) ; « Every title on e-manuscripta comes with the associated IIIF manifest » (page ZB plateforme)
api_recherche: NON PRÉSENT dans les sources lues
acces: NON PRÉSENT dans les sources lues
moissonnage: 'OAI-PMH : le lien manifeste figure dans la réponse METS (ZB Data Map)'
robots_waf: NON PRÉSENT dans les sources lues
droits: NON PRÉSENT dans les sources lues
lacunes:
- wiki apiinfo refusé en passe 1
- documentation API e-manuscripta absente de la page lue
methode: 'WebSearch « e-manuscripta IIIF API Zentralbibliothek Zürich Nutzungsbedingungen Rate limit » : fiches ZB, sans limite ; Les wikis apiinfo n''ont pas été lus : URL hors liste autorisée (même cas que GLAM-019) ; Passe 2 (2026-11-13) : 1 WebFetch (page ZB, commune à e-rara).'
verifie_le: '2026-11-13'
sources:
- url: https://www.e-manuscripta.ch/wiki/apiinfo
  note: (cité ; non lu)
  surveiller: false
- url: https://www.zb.uzh.ch/en/services/die-plattformen-e-rara-und-e-manuscripta
  note: '(présentation officielle : manifeste IIIF pour chaque titre, sans chiffre)'
  surveiller: true
- url: https://data.zb.uzh.ch/map/books/data-map-der-zentralbibliothek-zurich/page/e-manuscripta-iiif/export/pdf
  note: '(fiche ZB : IIIF v2.1, sans limite dans les extraits lus)'
  surveiller: true
---

# e-manuscripta (bibliothèques partenaires suisses)

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (wiki officiel des API non lisible)

## Notes

Plateforme exploitée conjointement par BGE, ETH-Bibliothèque, UB Bâle, UB Berne et ZB Zurich (page ZB) ; Visual Library Server, hébergée par l'ETH Zurich

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « e-manuscripta IIIF API Zentralbibliothek Zürich Nutzungsbedingungen Rate limit » : fiches ZB, sans limite
- Les wikis apiinfo n'ont pas été lus : URL hors liste autorisée (même cas que GLAM-019)

## Passe 2 (2026-11-13)
- WebFetch page ZB (commune à e-rara) : chaque titre e-manuscripta a un manifeste IIIF, sans procédure d’accès décrite ; aucun chiffre.
- Le wiki apiinfo e-manuscripta a été refusé par l’outil en passe 1 : non réessayé.
