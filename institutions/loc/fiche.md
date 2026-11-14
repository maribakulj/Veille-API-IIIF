# Library of Congress (loc.gov) — fiche d'audit v2

## Sources
- Doc lue en entier (sources/doc, doc11-doc34, doc41, doc45) : page « Working Within Limits », Legal, chapitres JSON/YAML (requests, endpoints, parameters, responses, item-and-resource, search-results, examples), sitemaps, microservices (Text, Image, Streaming), contact, services additionnels (Congress.gov, NLS BARD, Chronicling America, PPOC, Linked Data, SRU), Technical Center de id.loc.gov. Cinq lectures ont expiré à mi-corps le 14/11 vers 01:47-01:49 UTC (timeouts curl à 30 s, 8 Ko reçus) ; elles ont été refaites une par une, 12-16 s d'écart.
- Limites **documentées** (https://www.loc.gov/apis/json-and-yaml/working-within-limits/) : JSON/YAML 20/min, Text Services 150/min, Image Services 150/min, Streaming 60/min, /storage-services/ 150/min, tous bloqués 1 h ; MARCXML lccn.loc.gov 30/min, bloqué 72 h, « The countdown will reset any time a request is made during the block period ». En période de forte charge les seuils peuvent baisser et des 429 ou des CAPTCHA surviennent sous ces seuils. Pagination : 100 000 résultats maximum, 1 000 par page recommandés.
- Page Legal : « no more than 10 requests per minute to our applications, regardless of the number of machines » ; blocage d'IP possible si robots.txt ignoré ; arrêt des programmes de plus de 24 h.
- robots.txt : www.loc.gov Crawl-Delay 5 (+ Disallow /search, /pictures/search, /cgi-bin/…), id.loc.gov Crawl-delay 3, tile.loc.gov 404 (tout autorisé), lccn.loc.gov et lx2.loc.gov : page « LCCN Permalink - No Connections Available » au lieu d'un robots.txt.

## Tests (5 passes, 15 requêtes d'appel ; le journal du 13/11 est archivé verbatim dans tests/archive car sa configuration a été committée après lancement)
- www.loc.gov JSON/YAML : 403 Cloudflare (`cf-mitigated: challenge`) dès la 1re requête ; la page de doc PPOC /pictures/api donne aussi « Just a moment... » (403). Hôte arrêté, rien contourné.
- tile.loc.gov : Text Services (ALTO), Image Services (info.json, dérivé), Streaming (dérivé), /storage-services/ : 200, aucun en-tête de limite.
- id.loc.gov (Linked Data) : concept .json 200 ; flux ActivityStreams 303 puis .json 200 ; aucun en-tête de limite.
- lx2.loc.gov SRU (doc) : 200 (Metaproxy/1.22.4), aucun en-tête de limite.
- lccn.loc.gov MARCXML : 200 (une seule requête ; le 13/11 deux timeouts).

## Web
Quatre catégories lues : page officielle de limites, billet The Signal 2023 (Wayback), ticket Wikimedia T435179 (Zotero : « Temporary IP blocks are made if we exceed 10 requests in one minute » sur le SRU ; LoC a ensuite relevé la limite), ticket cyanheads/libofcongress-mcp-server #54 (CAPTCHA sans pause).

## Conclusion
Limites chiffrées publiées par famille d'API, mais aucun en-tête de quota (X-RateLimit, Retry-After) émis ; pas d'endpoint de statut ; pas de clé. L'API JSON de www.loc.gov est protégée par un défi Cloudflare qui refuse notre client (refus d'accès, pas un quota). Les microservices de tile.loc.gov, id.loc.gov, SRU et MARCXML répondent sans en-tête. Dépassement non testé (accord de Marcel requis ; crash test à la fin).
