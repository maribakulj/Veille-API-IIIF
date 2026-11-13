---
id: GLAM-050
institution: University of Toronto Libraries (Collections U of T)
pays: Canada
statut: DOC LUE, AUCUN CHIFFRE (page de démarrage lue ; aucun seuil publié)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni throttling ; clé non précisée'
debit_iiif: 'Aucun seuil de débit publié sur la page de démarrage de Collections U of T. La page décrit les manifestes comme des documents accessibles au public, sans dire si une clé est requise. Elle liste l’Image API en version 2 mais renvoie vers la spécification Image 3.0 : incohérence signalée. Les liens pointent vers les spécifications générales IIIF, qui ne décrivent pas les limites de l’université.'
iiif_image: 'Image API v2 (FAQ getting_started). La FAQ download indique « Image API version 2.1 » : conflit mineur, la v2 de la FAQ d''accueil est retenue et le conflit est signalé'
iiif_presentation: 'Presentation API v2 et v3 ; manifestes v2 par défaut ; URL : iiif.library.utoronto.ca/presentation/{PID}/manifest'
api_recherche: NON PRÉSENT SUR CETTE PAGE
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: 'Change Discovery non activé (page ingest) ; manifestes de collections : iiif.library.utoronto.ca/presentation/v2/collections'
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: Section « Copyright, Reuse and Credit Information » présente (contenu non lu en détail) ; aucune restriction d'accès IIIF mentionnée sur le site staff
strategie: Accès IIIF ouvert ; manifestes par PID ; pas de quota publié
lacunes:
- incohérence Image v2 (texte) et Image 3.0 (lien)
- limites propres à Toronto renvoyées vers le formulaire de contact
- clé non précisée
methode: 'WebSearch « University of Toronto Libraries Collections U of T IIIF rate limit terms » : FAQ IIIF officielle lue en extrait, pas de chiffre ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (page de démarrage).'
verifie_le: '2026-11-13'
sources:
- url: https://collections.library.utoronto.ca/explore/getting_started
  note: '(extrait lu : aucun chiffre)'
  surveiller: true
- url: https://collections.library.utoronto.ca/explore/faq/download_images
  note: '(extrait : modèle d''URL IIIF Image v2.1, pas de chiffre)'
  surveiller: true
---

# University of Toronto Libraries (Collections U of T)

**Verdict** : DOC LUE, AUCUN CHIFFRE (FAQ officielle Collections U of T lue en extrait)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « University of Toronto Libraries Collections U of T IIIF rate limit terms » : FAQ IIIF officielle lue en extrait, pas de chiffre

## Passe 2 (2026-11-13)
- WebFetch page de démarrage : aucun seuil ni throttling ; clé non précisée ; liens vers spécifications IIIF générales.
