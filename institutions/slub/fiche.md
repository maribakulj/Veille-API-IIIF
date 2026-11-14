# SLUB Dresden — `slub` (audit v2, a à f)

- **Statut** : audit v2 complet a à f ; g (crash test) préparé, non lancé (`config/crash-iiif-info-json.json`).
- **Pays** : Allemagne · **Audit** : 2026-11-14 · **Verdict** : une limite documentée (API LOD : 10 000 résultats maximum) ; robots.txt annonce Crawl-delay 6 s et Request-rate 10/1m ; aucun en-tête de limite ni 429 observés.

## Sources (étapes a et d)
Copies et SHA-256 dans `sources/*/SHA256SUMS`, texte dans `sources/*/text/`.
- `sources/robots/`, `sources/doc3/` : robots.txt de 9 hôtes. sachsen.digital et digital.slub-dresden.de : groupe `*` avec `Crawl-delay: 6` et `Request-rate: 10/1m`, plus de 20 robots nommés interdits (ClaudeBot, GPTBot, Bytespider…) : notre User-Agent n'est pas visé. www.qucosa.de : `Crawl-delay: 30`. kartenforum.slub-dresden.de : `Disallow: /`. iiif.slub-dresden.de, images.iiif.slub-dresden.de, data.slub-dresden.de : 404.
- `sources/doc1/` : sachsen.digital, Nutzungsbestimmungen für die Digitalen Sammlungen (licences : Public Domain Mark 1.0, CC BY-SA 4.0 ; contact digital@slub-dresden.de ; aucune règle de débit ni d'automatisation), racine iiif.slub-dresden.de (200, vide).
- `sources/doc2/` : aide à la recherche, page Open Source / Open Data de la SLUB (« Digitale Sammlungen via OAI-PMH2 über http://digital.slub-dresden.de/oai/ » ; « Katalogdaten via API über https://data.slub-dresden.de/ » ; WMS Kartenforum ; Qucosa OAI), Benutzungsordnung.
- `sources/doc4/`, `doc5/`, `doc6/` : doc de l'API LOD data.slub-dresden.de : « Our API is not suited for bulk-download of data. It will not return more than 10’000 results. » ; swagger.json (« limit » = paramètre, pas un quota) ; page de contact (mail).
- d) Aucun endpoint de statut de quota, aucun en-tête de limite documenté, aucune clé donnant un quota.

## Tests (étape e ; `tests/journal.log`, `tests/raw/`)
La session du 2026-11-13 (4 requêtes, ancienne méthode, sans en-tête de session) reste en tête du journal. Deux passes v2, configurations committées avant lancement.

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | iiif.slub-dresden.de manifeste (Presentation 2, 583 ko) | 200 |
| 1 | sachsen.digital/oai Identify, ListMetadataFormats | 200 |
| 1 | qucosa.de/oai Identify (espacée de 31 s par le Crawl-delay) | 200 |
| 2 | images.iiif.slub-dresden.de info.json et vignette 200 px | 200 |
| 2 | data.slub-dresden.de /search, /source, /gnd/persons, /persons/search | 200 ×4 |

Aucun en-tête `Retry-After`/`RateLimit-*`, aucun 429. Le motif de manifeste vient du README de l'extension tierce InstantIIIF, non officiel. Non testés : /reconcile (POST par OpenRefine), WMS Kartenforum (pas d'URL, robots Disallow /).

## Web (étape f, 2026-11-14)
- institution : seule la page Open Source / Open Data (lue dans l'original) décrit les accès ; aucune politique de bots trouvée.
- utilisateurs, tickets, presentations : aucun résultat (requêtes dans `data.json`) ; résultats concernant d'autres institutions (résumé de moteur, non vérifié).

## Conclusion
Documenté : plafond de 10 000 résultats sur l'API LOD, et Crawl-delay 6 s / Request-rate 10/1m dans robots.txt (convention, effet non décrit). Observé : rien. Hypothèse : l'API IIIF (Cantaloupe) n'a pas de limite déclarée ; non vérifié. À demander à digital@slub-dresden.de : URL officielle et limites IIIF, WMS.
