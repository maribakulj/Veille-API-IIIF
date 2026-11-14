# EPFL – Plume (`epfl-plume`)

- **Classeur de référence** : GLAM-021 · **Pays** : Suisse
- **Hôte** : `plume.epfl.ch` (Omeka S ; serveur d'images Cantaloupe sur le même hôte)
- **Vérifié le** : 2026-11-14, par Sonnet 5.5
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Sources
- Pages « Aide », « À propos », « Mentions légales », accueil, liste des documents, expositions et item 100 de Plume (`sources/`, `sources/pages/`, `sources/item/`) : lues en entier.
  - Mentions légales : réutilisation libre et gratuite, y compris commerciale (Public Domain Mark), avec mention de la source ; métadonnées Dublin Core moissonnables par OAI-PMH, « usage libre ». Aucune limite de débit, aucune règle sur les robots.
  - « À propos » : interopérabilité par IIIF, OAI-PMH (`/oai?verb=ListIdentifiers&metadataPrefix=oai_dc`) et API REST d'Omeka S (`/api`).
  - Contact : `library@epfl.ch` (fichiers haute définition, réutilisation).
- `robots.txt` de `plume.epfl.ch` : `Disallow: /admin/`, `/login` ; pas de Crawl-delay. `www.epfl.ch` : 200 mais vide ; `actu.epfl.ch` : Disallow `/search/`, `/subscription/`.

## Tests (2 passes, configurations committées avant lancement)
| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | API REST `api/items/100` | **200** |
| 1 | OAI-PMH `ListIdentifiers` | **200** |
| 1 | manifeste IIIF 2 `iiif/2/100/manifest` | **200**, 508 ko |
| 2 | Cantaloupe `info.json`, vignette 200 px | **200** ×2 |
| 2 | IIIF Search `iiif-search/100/search?q=ratio` | **200** |

Aucun 429, aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`. Pauses de 6 s. PDF et ALTO non testés (fichiers lourds, interdits par nos règles).

## Web
Quatre recherches, une par catégorie. Institution : page « Rare books and PLUME » et billet de lancement lus, aucune règle de débit ni de bots. Utilisateurs et tickets : aucun résultat concernant `plume.epfl.ch`. Présentations : billet de lancement (2019) sans mention d'IIIF. Un guide IIIF de tiers répertorie Plume sans URL d'API.

## Conclusion
- **Limite documentée** : aucune. `robots.txt` sans Crawl-delay.
- **Limite observée** : non ; aucun en-tête de limite sur 6 requêtes.
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne (rien d'écrit ni d'observé ; le serveur est un Apache/PHP, Cantaloupe derrière Jetty, sans CDN détecté).
- **Crash test (g)** : plafond 200 req/min (aucune limite documentée) ; à décider par Marcel.

## Crash test (étape g)

Crash test fait le 2026-11-14 : cantaloupe-info-json sur plume.epfl.ch : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/epfl-plume.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
