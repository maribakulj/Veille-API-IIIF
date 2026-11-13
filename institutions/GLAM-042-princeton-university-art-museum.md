---
id: GLAM-042
institution: Princeton University Art Museum
pays: États-Unis
statut: DOC LUE, AUCUN CHIFFRE (docs API du dépôt GitHub lues ; aucune clé requise à ce jour)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni throttling sur la documentation ; aucune authentification requise à ce jour'
debit_iiif: 'Aucun chiffre de limite de requêtes dans la documentation de l’API du musée. Elle indique qu’aucune authentification n’est requise actuellement, avec la réserve d’un changement futur. Des exports JSON en masse, rafraîchis chaque semaine, sont proposés : ce sont des fichiers statiques, non un débit. Les médias IIIF apparaissent sous un chemin de média, sans documentation IIIF liée.'
iiif_image: 'NON PRÉSENT SUR CETTE PAGE (doc Mirador : viewer Mirador 3.0.0 ; version de l''Image API non précisée)'
iiif_presentation: 'Packages IIIF : data.artmuseum.princeton.edu/iiif/packages/{id} (exemple cité dans la doc Mirador) ; version non précisée'
api_recherche: NON PRÉSENT dans les sources lues
acces: 'API ouverte à tous selon l''article CDH de Princeton (2020) ; clé : NON PRÉSENT dans les sources lues'
moissonnage: NON PRÉSENT dans les sources lues ; l'article CDH renvoie la documentation de l'API vers GitHub
robots_waf: NON PRÉSENT dans les sources lues
bots_ia: NON PRÉSENT dans les sources lues
droits: NON PRÉSENT dans les sources lues
strategie: API lancée en 2017 pour rendre accessibles plus de 113 000 œuvres aux étudiants, enseignants et développeurs (page du musée)
lacunes:
- aucune documentation IIIF liée (chemin de média seulement)
- réserve sur une future authentification
- limites non publiées
methode: 'WebSearch « Princeton University Art Museum IIIF API images rate limit terms » : dépôt officiel repéré ; WebSearch « Princeton University Art Museum open API documentation rate limit » (domaines artmuseum, github, guides.iiif.io) : dépôt puam-api-docs en extrait, pas de chiffre ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (dépôt GitHub de la documentation API).'
verifie_le: '2026-11-13'
sources:
- url: https://github.com/Princeton-University-Art-Museum/puam-api-docs
  note: '(extrait lu : aucun chiffre)'
  surveiller: true
- url: https://artmuseum.princeton.edu/art/collections/objects/44709
  note: '(page objet : API ouverte et manifeste IIIF, pas de chiffre)'
  surveiller: true
---

# Princeton University Art Museum

**Verdict** : DOC LUE, AUCUN CHIFFRE (dépôt officiel de documentation de l'API lu en extrait)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Princeton University Art Museum IIIF API images rate limit terms » : dépôt officiel repéré
- WebSearch « Princeton University Art Museum open API documentation rate limit » (domaines artmuseum, github, guides.iiif.io) : dépôt puam-api-docs en extrait, pas de chiffre

## Passe 2 (2026-11-13)
- WebFetch dépôt puam-api-docs : aucun seuil ; pas d’authentification actuelle ; exports JSON hebdomadaires sur site statique.
