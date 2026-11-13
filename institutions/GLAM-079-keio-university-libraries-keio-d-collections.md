---
id: GLAM-079
institution: Keio University Libraries – Keio D Collections
pays: Japon
statut: DOC LUE, AUCUN CHIFFRE (page À propos lue ; pas d’API documentée)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni throttling ; téléchargements PDF sans plafond annoncé'
debit_iiif: Aucun chiffre de limite sur la page À propos de D-Collections, pour le site, le serveur d’images IIIF ou une API. Le site est déclaré librement accessible, sans seuil. Les téléchargements en PDF ne sont proposés que pour des collections listées, sans plafond de taille ni de nombre. Les conditions de réutilisation ne contiennent pas de plafond numérique ; les questions sur les images renvoient vers la page de contact. Aucune API n’est mentionnée, donc aucune clé.
iiif_image: Serveur d'images IIIF pour la visionneuse (dcollections.lib.keio.ac.jp/en/about) ; version non précisée
iiif_presentation: Lien « IIIF Manifest » sur les fiches et ouverture dans une visionneuse IIIF (pages de collections)
api_recherche: NON PRÉSENT SUR CETTE PAGE
acces: Accès libre sans inscription (newsjunkie, tiers) ; PDF téléchargeables pour certaines collections
moissonnage: Téléchargement PDF pour les collections listées (page About) ; pas de moissonnage documenté
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: NON PRÉSENT SUR CETTE PAGE
strategie: Visionneuse IIIF et PDF pour les fonds rares ; projet commun Digital Fujikawa avec Kyoto (2018)
lacunes:
- aucune documentation API ou IIIF liée
- conditions d’usage des images à confirmer auprès du contact
methode: 'WebSearch « Keio University Libraries digital collections IIIF rate limit » : page officielle sans chiffre ; entrée tierce écartée ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (page À propos).'
verifie_le: '2026-11-13'
sources:
- url: https://dcollections.lib.keio.ac.jp/en/about
  note: '(extrait : serveur IIIF, PDF ; pas de chiffre)'
  surveiller: true
- url: https://apis.io/providers/keio/
  note: '(catalogue tiers, entrée « Rate Limits » sans valeur : non retenue)'
  surveiller: true
---

# Keio University Libraries – Keio D Collections

**Verdict** : DOC LUE, AUCUN CHIFFRE (page officielle « About » lue en extrait)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Keio University Libraries digital collections IIIF rate limit » : page officielle sans chiffre ; entrée tierce écartée

## Passe 2 (2026-11-13)
- WebFetch page À propos : accès libre sans seuil ; serveur IIIF sans limite chiffrée ; téléchargements PDF sans plafond annoncé.
