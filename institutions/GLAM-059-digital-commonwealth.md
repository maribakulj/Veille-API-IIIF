---
id: GLAM-059
institution: Digital Commonwealth
pays: États-Unis
statut: DOC LUE, AUCUN CHIFFRE (page API lue ; IIIF 2.0 listé sans limite)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni throttling ; clé non mentionnée sur la page'
debit_iiif: Aucun chiffre de limite de requêtes, de débit ni de quota sur la page API de Digital Commonwealth. La page liste IIIF Image 2.0 et Presentation 2.0, sans limite, et ne mentionne pas de clé. Aucune règle d’usage ni de moissonnage n’est chiffrée.
iiif_image: 'Image 2.0 : https://iiif.digitalcommonwealth.org/iiif/2/ (page /api, lecture WebFetch)'
iiif_presentation: 'Presentation 2.0 : manifeste obtenu en ajoutant /manifest à l''URL de la page item ; 404 si aucun manifeste'
api_recherche: 'JSON : www.digitalcommonwealth.org/search.json?q=… (page /api)'
acces: NON PRÉSENT SUR CETTE PAGE (seul « Sign Up / Log In » de navigation)
moissonnage: 'OAI-PMH : métadonnées de toutes les collections accessibles ; base https://oai.digitalcommonwealth.org/catalog/oai'
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: 'Lien « Copyright & Terms of Use » sans contenu lu : conditions NON PRÉSENT SUR CETTE PAGE'
strategie: 'Agrégateur du Massachusetts : Image 2.0 et Presentation 2.0 ouverts, moissonnage par OAI-PMH ; quota non publié'
lacunes:
- conditions de réutilisation non lues
- clé non mentionnée sur la page
methode: 'WebSearch « Digital Commonwealth Massachusetts API IIIF rate limit terms » : page API officielle lue en extrait, pas de chiffre ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (page API).'
verifie_le: '2026-11-13'
sources:
- url: https://digitalcommonwealth.org/api
  note: '(extrait lu : aucun chiffre)'
  surveiller: true
- url: https://github.com/bplmaps/collections-api
  note: '(dépôt de la Boston Public Library, extrait : API JSON et IIIF, pas de chiffre)'
  surveiller: true
---

# Digital Commonwealth

**Verdict** : DOC LUE, AUCUN CHIFFRE (page API officielle lue en extrait)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Digital Commonwealth Massachusetts API IIIF rate limit terms » : page API officielle lue en extrait, pas de chiffre

## Passe 2 (2026-11-13)
- WebFetch page API : aucun seuil ni throttling ; IIIF Image 2.0 et Presentation 2.0 listés ; clé non mentionnée.
