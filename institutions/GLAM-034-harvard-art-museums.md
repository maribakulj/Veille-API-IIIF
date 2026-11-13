---
id: GLAM-034
institution: Harvard Art Museums
pays: États-Unis
statut: PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement)
classe: pas de débit IIIF chiffré
statut_quota: 'PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement) ; README GitHub officiel lu via extrait de recherche (non rechargé en entier) ; page collections/api lue : pas de chiffre'
debit_iiif: 'Le README officiel du dépôt harvardartmuseums/api-docs (conditions d''utilisation, lu via extrait) fixe à 2 500 appels par jour la limite de l''API REST, clé obligatoire (401 si absente ou invalide). Les services IIIF, sans clé, n''ont aucun chiffre sur la même page : le chiffre ne vaut donc pas pour IIIF. Aucun code 429 ni limite par minute n''est décrit.'
iiif_image: 'Image API 2.1 (doc GitHub api-docs, section IIIF : service « adheres to version 2.1 »), base https://ids.lib.harvard.edu/ids/iiif (extrait de recherche)'
iiif_presentation: 'Presentation API 2.1 : service « accessed through a separate service » (readme api-docs, extrait de recherche)'
api_recherche: NON PRÉSENT dans les sources lues
acces: 'API de données : « Every request must be accompanied by the apikey parameter and an API key. » ; clé IIIF : NON PRÉSENT SUR CETTE PAGE'
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: Domaine public pour la grande majorité des URL d'images (discussion GitHub n° 16, extrait) ; lien « Terms of Use » en pied de page, texte non lu
lacunes:
- 'sections limites et conditions de la doc GitHub api-docs non lisibles : le WebFetch a été refusé (hors liste autorisée) après redirection depuis hvrd.art'
- texte des Terms of Use non lu
- 'le classeur indique « services IIIF sans clé » : non confirmé par les pages lues'
methode: 'WebSearch « Harvard Art Museums API rate limit requests per day key documentation » : résultats tiers (jentic, matrix-db) écartés car non officiels ; WebFetch github.com/harvardartmuseums/api-docs : refusé par l''outil (hors liste autorisée) ; WebSearch « harvardartmuseums api-docs github README apikey rate limit » (domaines github.com, harvardartmuseums.org) : chiffre 2500/jour trouvé dans le README officiel'
verifie_le: '2026-11-13'
sources:
- url: https://github.com/harvardartmuseums/api-docs
  note: '(README : « Terms of use » 2500 appels/jour)'
  surveiller: true
- url: https://harvardartmuseums.org/collections/api
  note: '(page officielle : clé requise, pas de chiffre)'
  surveiller: true
- url: https://github.com/harvardartmuseums/api-docs/blob/master/sections/object.md
  note: (documentation des objets, pas de limite)
  surveiller: true
---

# Harvard Art Museums

**Verdict** : PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Harvard Art Museums API rate limit requests per day key documentation » : résultats tiers (jentic, matrix-db) écartés car non officiels
- WebFetch github.com/harvardartmuseums/api-docs : refusé par l'outil (hors liste autorisée)
- WebSearch « harvardartmuseums api-docs github README apikey rate limit » (domaines github.com, harvardartmuseums.org) : chiffre 2500/jour trouvé dans le README officiel
