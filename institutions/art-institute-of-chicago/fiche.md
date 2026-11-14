# Art Institute of Chicago (`art-institute-of-chicago`)

- **Classeur** : GLAM-047 · États-Unis · **Vérifié le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `api.artic.edu` (API REST, manifestes IIIF Presentation, derrière Cloudflare/CloudFront mais répond à notre client), `www.artic.edu` (site et IIIF Image 2.0 `/iiif/2`, défi Cloudflare 403), `artic-api-data.s3.amazonaws.com` (dump), `iiif.artic.edu` (DNS introuvable, non cité par la doc).

## Sources
- `api.artic.edu/docs` lue en entier (`sources/a`, `sources/b` : openapi.json de 103 chemins, GitHub api-data et data-aggregator). Section Authentication : « Anonymous users are throttled to 60 requests per minute. If you are working on an application that needs to exceed this restriction, please get in touch with us ». Scraping : « please throttle your requests to no more than one per second and avoid running multiple scrapers in parallel » ; images : un fil, délai de 1 s, taille 843. Pagination : `limit` ≤ 100, 1 000 enregistrements max par recherche. En-tête `AIC-User-Agent` demandé par courtoisie. Dumps hebdomadaires proposés à la place du grattage. Conditions du site (Wayback) : usage non commercial ; données et images CC0 quand l'étiquette l'indique.
- `www.artic.edu` (robots.txt, terms, page API) : défi Cloudflare ; lus via Wayback (`sources/wayback/`). robots.txt de www : pas de Crawl-delay.

## Tests (1 passe, 9 requêtes dont 2 robots.txt, pauses 6 s)
`artworks/27992?fields=…`, `artworks?limit=2`, `artworks/search?q=monet`, manifeste `artworks/24645/manifest.json`, recherche `limit=0` domaine public, `artists?page=2&limit=10` : **200** ×6, avec **`x-ratelimit-limit: 60`** et **`x-ratelimit-remaining`** (57 à 59, décompte par minute) : l'API annonce bien sa limite. HEAD du dump S3 : 200, 130 504 161 octets. Aucun 429. IIIF Image (www.artic.edu) non testé (Cloudflare 403) ; POST (`/msearch`) non testé.

## Web
Quatre catégories couvertes : doc officielle ; article tiers navigating.art (2026) qui signale un 403 du serveur d'images sans Referer (non reproduit, ce serait un contournement) ; outil tiers artic-mcp qui implémente 60 req/min d'après la doc ; talk Chi Hack Night 2020 de l'ingénierie du musée. Aucune plainte 429 trouvée.

## Pourquoi cette politique ?
Trouvé : le grattage « puts undue stress on our systems » et un bot a déjà « taxed our site » (page API, Wayback) : d'où le dump hebdomadaire et la limite par IP.

## Conclusion
Limite chiffrée : 60 req/min anonymes, annoncée par `x-ratelimit-*`. Confiance : haute. Crash test (g) : à faire à la fin ; plafond 2 × 60 = 120 req/min, réseau protégé détecté (Cloudflare/CloudFront), donc 30 min d'écart avec les autres tests protégés.
