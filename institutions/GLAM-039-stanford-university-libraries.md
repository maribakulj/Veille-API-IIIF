---
id: GLAM-039
institution: Stanford University Libraries
pays: États-Unis
statut: DOC LUE, AUCUN CHIFFRE (docs API lues ; Presentation v3 en alpha)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur la page API lue ; clé non précisée'
debit_iiif: Aucun seuil de débit publié sur la page API. Presentation v3 est marquée alpha, et la page elle-même déconseille de développer de nouveaux projets dessus. Presentation v2 et Image v2 ne sont pas marquées alpha, sans statut stable explicitement annoncé. La page Image v2 ne donne que l’URL de base, sans précision sur les limites.
iiif_image: IIIF Image v2 API (base stacks.stanford.edu)
iiif_presentation: 'Presentation v2 : GET purl.stanford.edu/{id}/iiif/manifest. Presentation v3 « ALPHA » : « API consumers should not develop new projects with this API » (api.library.stanford.edu, extrait)'
api_recherche: NON PRÉSENT SUR CETTE PAGE
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: NON PRÉSENT pour l'API ; seul le lien général « Terms of Use » du pied de page
lacunes:
- limites de Digital Stacks non décrites sur la page API
- limites de l’Image v2 non précisées
- clé non précisée
methode: 'WebSearch « Stanford Libraries IIIF API rate limit digital collections terms » : pages officielles api.library.stanford.edu lues en extrait, pas de chiffre ; Passe 2 (2026-11-13) : 1 WebFetch (docs/iiif/api).'
verifie_le: '2026-11-13'
sources:
- url: https://api.library.stanford.edu/docs/iiif/api
  note: '(extrait lu : aucun chiffre ; avertissement d''usage interne)'
  surveiller: true
- url: https://api.library.stanford.edu/docs/digital-stacks/api
  note: '(extrait : services de téléchargement et IIIF, pas de chiffre)'
  surveiller: true
- url: https://apis.io/providers/stanford/
  note: '(agrégateur tiers, mention « Stanford Rate Limits » sans valeur : écarté)'
  surveiller: true
---

# Stanford University Libraries

**Verdict** : DOC LUE, AUCUN CHIFFRE (page officielle IIIF de l'API Stanford lue en extrait)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Stanford Libraries IIIF API rate limit digital collections terms » : pages officielles api.library.stanford.edu lues en extrait, pas de chiffre

## Passe 2 (2026-11-13)
- WebFetch docs/iiif/api : aucune limite numérique, quota ni règle de fair use ; clé non précisée.
- Presentation v3 : mention alpha, avec avertissement de la page contre les nouveaux projets ; Presentation v2 et Image v2 non marquées alpha.
