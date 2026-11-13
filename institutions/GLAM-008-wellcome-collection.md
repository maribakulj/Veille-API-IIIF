---
id: GLAM-008
institution: Wellcome Collection
pays: Royaume-Uni
statut: PARTIEL (règle annoncée, chiffre absent)
classe: règle sans chiffre
statut_quota: 'PARTIEL (règle annoncée, chiffre absent) ; '
debit_iiif: Aucun débit, quota ni clé d’API sur la page IIIF ; accès sans inscription ni authentification. Une note de version officielle (févr. 2025) annonce une limitation de débit pour les nouvelles requêtes de robots, sans seuil publié.
iiif_image: Image API v3 (documentation IIIF API v3 sur developers.wellcomecollection.org)
iiif_presentation: 'NON DÉPLOYÉE : « We are working to add the IIIF Presentation, Search and Authentication APIs across all of our digitised collections » ; seules les collections open image sont servies'
api_recherche: Non déployée (même source)
acces: « There's no sign up or authentication required » pour démarrer
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: Licences ouvertes « as openly as possible » ; respecter licences par image
lacunes:
- page officielle complète non lue avec WebFetch
- politique WAF/robots
methode: 'WebFetch developers.wellcomecollection.org/docs/iiif : pas de chiffre ; WebSearch « Wellcome Collection API rate limit » : trouve la note officielle 2025 et la RFC 012, sans chiffre'
verifie_le: '2026-11-13'
sources:
- url: https://developers.wellcomecollection.org/docs/iiif
  note: ''
  surveiller: true
- url: https://docs.wellcomecollection.org/fortnotes/20250205
  note: '(note officielle : « Rate limit new bot requests »)'
  surveiller: true
- url: https://docs.wellcomecollection.org/request-for-comments-rfcs/012-api_architecture
  note: '(RFC : les API publiques « would benefit from rate limiting », sans chiffre)'
  surveiller: true
---

# Wellcome Collection

**Verdict** : PARTIEL (règle annoncée, chiffre absent)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebFetch developers.wellcomecollection.org/docs/iiif : pas de chiffre
- WebSearch « Wellcome Collection API rate limit » : trouve la note officielle 2025 et la RFC 012, sans chiffre
