---
id: GLAM-025
institution: SUB Göttingen – GDZ
pays: Allemagne
statut: DOC LUE, AUCUN CHIFFRE (page IIIF de la bibliothèque lue ; aucun seuil publié)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni throttling sur la page IIIF ; clé non précisée'
debit_iiif: Aucun seuil de débit IIIF publié sur la page IIIF de la bibliothèque. La page nomme les API Image et Presentation, plus Authentication et Content Search, sans chiffre. Elle ne dit pas si une clé est requise, ne renvoie vers aucune documentation d’API et renvoie pour les limites d’usage vers la bibliothèque elle-même.
iiif_image: 'NON PRÉSENT SUR CETTE PAGE (guide IIIF ; seule mention : copier l''URL du manifeste)'
iiif_presentation: NON PRÉSENT SUR CETTE PAGE (guide IIIF)
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
droits: NON PRÉSENT SUR CETTE PAGE
lacunes:
- pas de lien vers une documentation IIIF propre à Göttingen
- limites d’usage renvoyées vers la bibliothèque, non publiées sur la page
methode: 'WebSearch « SUB Göttingen GDZ IIIF API documentation Nutzung Limit Anfragen » : pages SUB et guide communautaire ; WebFetch page IIIF officielle SUB Göttingen : aucune limite ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (page IIIF).'
verifie_le: '2026-11-13'
sources:
- url: https://www03.sub.uni-goettingen.de/en/digital-library/digital-tools/iiif-at-the-goettingen-state-and-university-library
  note: '(lue : aucun chiffre)'
  surveiller: true
- url: https://www.sub.uni-goettingen.de/en/research/research-tools
  note: '(outils de recherche SUB : TIFY, repositories IIIF, sans chiffre lu)'
  surveiller: true
- url: https://iiif.io/guides/guides/gdz.sub.uni-goettingen.de
  note: (guide communautaire, non officiel, sans chiffre lu)
  surveiller: true
---

# SUB Göttingen – GDZ

**Verdict** : DOC LUE, AUCUN CHIFFRE (page IIIF officielle lue)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « SUB Göttingen GDZ IIIF API documentation Nutzung Limit Anfragen » : pages SUB et guide communautaire
- WebFetch page IIIF officielle SUB Göttingen : aucune limite

## Passe 2 (2026-11-13)
- WebFetch page IIIF : aucun seuil ni throttling ; clé non précisée ; aucun lien de documentation.
- Les seuls chiffres de la page sont des dates de conférence, non des limites.
