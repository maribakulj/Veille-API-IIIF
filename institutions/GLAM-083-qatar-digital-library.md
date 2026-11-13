---
id: GLAM-083
institution: Qatar Digital Library
pays: Qatar
statut: DOC LUE, AUCUN CHIFFRE DE DÉBIT (page des options d’image lue ; plafond de taille, non un débit)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE DE DÉBIT : aucun quota, débit ni throttling ; plafond de taille de 1 200 px, non une limite de requêtes'
debit_iiif: 'Aucun débit IIIF publié sur la page des options d’image. Le seul chiffre est un plafond de résolution : la plus grande image récupérable est fixée à 1 200 px, et une version plus grande s’obtient en contactant QDL. C’est une limite de taille de sortie, non une limite de requêtes ni de débit. Les options de taille, de région et de rotation contrôlent la sortie, non l’usage. Ni clé ni authentification ne sont mentionnées.'
iiif_image: IIIF Image API 2.0 via IIPImage (qdl.qa/en/image-options)
iiif_presentation: 'Presentation API : remplacer « archive » par « iiif » dans l''URL de l''archive et ajouter « /manifest » (qdl.qa/en/image-options)'
api_recherche: NON PRÉSENT SUR CETTE PAGE
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: NON PRÉSENT SUR CETTE PAGE
strategie: Image API 2.0 et Presentation API servies pour l'intégration dans des visionneuses ; quota non publié
lacunes:
- aucun débit ni quota publié sur la page
- clé ou authentification non mentionnées
- API IIIF Presentation non décrite sur cette page
methode: 'WebSearch « Qatar Digital Library IIIF API rate limit » : page officielle sans chiffre ; prestataire écarté comme source de limite ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (options d’image).'
verifie_le: '2026-11-13'
sources:
- url: https://www.qdl.qa/en/image-options
  note: '(extrait : API IIIF Presentation, pas de chiffre)'
  surveiller: true
- url: https://cogapp.com/r-d/iiif
  note: '(prestataire, extrait : implémentation de l''API, pas de chiffre ; non retenu)'
  surveiller: true
---

# Qatar Digital Library

**Verdict** : DOC LUE, AUCUN CHIFFRE (page officielle d'options d'intégration lue en extrait)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Qatar Digital Library IIIF API rate limit » : page officielle sans chiffre ; prestataire écarté comme source de limite

## Passe 2 (2026-11-13)
- WebFetch options d’image : plafond de taille de 1 200 px ; aucun quota, débit ni throttling ; clé non mentionnée.
