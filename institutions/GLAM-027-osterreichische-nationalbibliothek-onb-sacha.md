---
id: GLAM-027
institution: Österreichische Nationalbibliothek – ÖNB (SACHA)
pays: Autriche
statut: DOC LUE, AUCUN CHIFFRE (API lue ; clé non précisée, contact pour accès)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni règle d’usage chiffrée sur la page API'
debit_iiif: 'Aucun seuil de débit IIIF publié sur la page de l’API ÖNB. Elle liste IIIF Presentation 3.0, Image 3.0 et Content Search 2.0, la version 1.0 de la recherche étant dépréciée. L’authentification n’est pas mentionnée, mais la page invite à contacter l’équipe pour un accès : une demande d’accès n’est pas un débit.'
iiif_image: 'Documentée – SACHA (ÖNB) : « IIIF Image API and IIIF Presentation API are implemented » (iiif.onb.ac.at/api, extrait). Version non précisée dans l''extrait'
iiif_presentation: 'Documentée – SACHA (ÖNB) : Presentation API implémentée (iiif.onb.ac.at/api, extrait). Version non précisée'
api_recherche: 'Non documentée – SACHA : Search API « planned to be implemented in the future » (iiif.onb.ac.at/api, extrait)'
acces: 'Non documentée – SACHA : Authentication API « planned » (iiif.onb.ac.at/api, extrait)'
moissonnage: Moissonnage NON PRÉSENT SUR CETTE PAGE ; fichiers METS objet par objet ; mesures contre le téléchargement massif des objets ABO
robots_waf: NON PRÉSENT SUR CETTE PAGE ; codes HTTP listés 200, 201, 303, 400, 404, 500 (pas de 429)
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: '« No Copyright - Non-Commercial Use Only » (rightsstatements NoC-NC) ; ANNO : objets de plus de 140 ans seulement'
lacunes:
- 'clé ou accès à demander : non précisé'
- « Getting started with IIIF » nommé sans lien
methode: 'WebSearch « ÖNB IIIF API Nutzung Limit Anfragen » : page officielle api.onb.ac.at trouvée ; WebFetch api.onb.ac.at : aucune limite, contact api@onb.ac.at ; Passe 2 (2026-11-13) : 1 WebFetch (api.onb.ac.at).'
verifie_le: '2026-11-13'
sources:
- url: https://api.onb.ac.at/
  note: '(lue : aucun chiffre ; contact api@onb.ac.at)'
  surveiller: true
- url: https://iiif.onb.ac.at/api/
  note: (documentation IIIF de l'ÖNB, non lue)
  surveiller: false
- url: https://onb.ac.at/en/digital-offers/faq-oenb-digital
  note: (FAQ, non lue sur ce point)
  surveiller: false
---

# Österreichische Nationalbibliothek – ÖNB (SACHA)

**Verdict** : DOC LUE, AUCUN CHIFFRE (renvoi vers un contact pour les conditions d'accès)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « ÖNB IIIF API Nutzung Limit Anfragen » : page officielle api.onb.ac.at trouvée
- WebFetch api.onb.ac.at : aucune limite, contact api@onb.ac.at

## Passe 2 (2026-11-13)
- WebFetch api.onb.ac.at : aucun seuil, quota ni règle de fair use ; authentification non mentionnée ; contact pour accès.
- Content Search 1.0 signalée comme dépréciée ; la version 2.0 est celle des chemins listés.
