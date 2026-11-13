---
id: GLAM-048
institution: J. Paul Getty Trust – Museum
pays: États-Unis
statut: DOC LUE, AUCUN CHIFFRE (docs API et IIIF lues ; pas de limite publiée)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur REST, ActivityStream, SPARQL ni IIIF ; clé non précisée'
debit_iiif: Aucun seuil de débit publié pour l’API de collection REST, le flux ActivityStream, le point SPARQL ni les images IIIF (Image et Presentation). Les chiffres lus sont des tailles de collection (plus de 250 000 objets) ou des numéros de page de pagination, non des limites. Les restrictions d’image des conditions concernent la licence, non le volume.
iiif_image: 'Image API 2.1.1 : https://media.getty.edu/iiif/image/{IMAGE_ID} (doc Getty liant iiif.io/api/image/2.1/)'
iiif_presentation: 'Presentation API 2.1.1 : https://media.getty.edu/iiif/manifest/{MANIFEST_ID} (doc Getty liant iiif.io/api/presentation/2.1/)'
acces: NON PRÉSENT dans la doc Getty lue
moissonnage: Flux d'activité (ActivityStream) et SPARQL mentionnés ; bulk IIIF non décrit
robots_waf: NON PRÉSENT dans la doc Getty lue
droits: NON PRÉSENT dans la doc Getty lue
strategie: 'Doc Getty : « This API Documentation is a work in progress. » ; page Getty 2017 : plus de 30 000 images publiées en IIIF'
lacunes:
- 'absence de téléchargement global : fonctionnalité manquante, non un plafond'
- clé et authentification non précisées
- contact MuseumCollections@getty.edu non contacté
methode: 'WebSearch « Getty Museum Open Content IIIF API rate limit terms » : documentation officielle data.getty.edu lue en extrait, pas de chiffre ; Passe 2 (2026-11-13) : 1 WebFetch (docs).'
verifie_le: '2026-11-13'
sources:
- url: https://data.getty.edu/museum/collection/docs/
  note: '(extrait lu : aucun chiffre)'
  surveiller: true
- url: https://www.getty.edu/publications/virtuallibrary/terms.html
  note: '(conditions : images Open Content sous CC0, pas de quota, extrait)'
  surveiller: true
---

# J. Paul Getty Trust – Museum

**Verdict** : DOC LUE, AUCUN CHIFFRE (documentation officielle data.getty.edu lue en extrait)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Getty Museum Open Content IIIF API rate limit terms » : documentation officielle data.getty.edu lue en extrait, pas de chiffre

## Passe 2 (2026-11-13)
- WebFetch data.getty.edu/museum/collection/docs : aucun seuil, quota, fair use ni limite pour REST, ActivityStream, SPARQL, IIIF ; clé non mentionnée.
- Pas de téléchargement global de l’ensemble des données : fonctionnalité absente, non un plafond.
