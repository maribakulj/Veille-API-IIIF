# Cultural Japan (GLAM-084)

## Sources
cultural.jp /about, /policy, /contact ; ld.cultural.jp about-rdf et about-sources ; OpenAPI https://api.cultural.jp/openapi.json (dossiers sources/doc, doc2, api, robots, robots2). Politique : renvoi aux conditions de chaque base source ; aucun quota.

## Tests
8 requêtes GET le 2026-11-14 (api.cultural.jp : count, search, item, manifeste, liste d'expositions, collection d'exposition, collection ; ld.cultural.jp : SPARQL ASK) : toutes 200, sans en-tête de limite. app.cultural.jp : robots.txt en 403, hôte arrêté.

## Web
4 recherches web faites le 2026-11-14 (sources/web/recherches-2026-11-14.md) : aucune plainte, aucun ticket ; présentation IIIF Week 2020 de Kanzaki (original lu).

## Conclusion
Aucun quota publié. robots.txt de cultural.jp : robots d'entraînement interdits (justifié par la charge), moteurs bienvenus, API recommandée ; api.cultural.jp/robots.txt dit Disallow / (contradiction). Tests de l'API faits avec l'accord de Marcel sur les Disallow. Confiance moyenne.
