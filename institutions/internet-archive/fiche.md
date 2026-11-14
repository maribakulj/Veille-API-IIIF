# Internet Archive — `internet-archive` (audit v2, passe 2 du 14/11/2026)

## Sources
- Doc développeurs lue en entier : `sources/a1` (index, bots, md-read, md-write, terms, advancedsearch), `sources/a2` (ias3, tasks, iarest, items, metadata, views_api, changes, ocr, md-record, simplelists, bibliothèque Python/CLI, wayback_api, billets 2026 et 2023, iiif.archive.org/), `sources/a3` (README CDX, GitHub internetarchive/iiif, skills, FAQ), `sources/a4` (billet 2023-05-29). Empreintes : `SHA256SUMS` de chaque dossier.
- robots.txt : archive.org (`Disallow: /control/`, `/report/` seulement ; pas de Crawl-delay), blog.archive.org (`/wp-admin/`), web.archive.org et be-api.us.archive.org (404 : tout autorisé), iiif.archive.org (code 464 non standard, corps vide), iiif.archivelab.org (erreur TLS). Dossiers `sources/robots*`.
- Conditions d'utilisation : la page directe est vide (rendu client) ; lue par Wayback (`sources/wayback/terms.md`) : accès « for scholarship and research purposes only », « not to interfere with ... servers, or resources », aucun chiffre.
- Doc de débit : `bots.html` § Rate Limiting (« Add delays between requests for bulk operations », « Honor 429 Too Many Requests responses and Retry-After headers », exemple `-j4 --delay 1`) ; Tasks API (« Users are limited to the number of tasks they may submit », seuil lisible avec `rate_limits=1` mais clés S3 requises) ; ias3 (503 SlowDown, `check_limit`) ; iarest (429, 503) ; billet 2026-09-15 (protections anti-trafic Wayback, 429). Aucun chiffre pour la lecture (advancedsearch, metadata, IIIF).
- Billet 2023-05-29 (attaque de « tens of thousands of requests per second » depuis 64 hôtes AWS sur les fichiers OCR) : explique la fragilité mais ne publie pas de seuil.

## Tests (passe 2, 9 requêtes, `tests/journal.log`, `tests/raw/p2-*`)
8 réponses 200 (advancedsearch, metadata, manifeste IIIF 3, info.json Image 2, vignette 200 px, Views API be-api, Wayback availability, CDX Wayback) ; iiif.archivelab.org : erreur TLS (certificat non valide pour le nom d'hôte), non contournée. Aucun 429/503/403 ; aucun en-tête `X-RateLimit-*`, `RateLimit-*` ni `Retry-After`. Le CDX renvoie des en-têtes internes `x-rl: 0`, `x-na: 0` (non documentés ; sens non établi, pas interprétés comme quota).
La passe 1 (10 requêtes par curl le 13/11) est conservée dans le journal et confirme.

## Web (4 catégories)
- institution : aucune politique chiffrée ; pages officielles déjà lues ; Techdirt (Mark Graham, 02/2026, via moteur) dit que l'Archive utilise « rate limiting, filtering, monitoring » (résumé de moteur, original illisible : 403).
- utilisateurs : mainteneur du paquet Python `wayback` (GitHub edgi-govdata-archiving/wayback issue 153, 16/12/2023), qui relaie le personnel IA : « 60 requests/minute averaged over a 5-minute window » pour le CDX, par IP, et après un 429 « stop all new requests immediately and do not start again for at least 60s ». Étiquette : tiers, non officiel.
- tickets : GitHub internetarchive/iiif (issues : aucune sur les 429, résumé de moteur) ; aucun ticket d'outil IIIF citant des limites de iiif.archive.org.
- presentations : billets de blog 2023 (attaque) et 2026-09-15 (Wayback) ; aucune présentation chiffrée.

## Conclusion
Aucun quota chiffré publié pour advancedsearch, metadata, IIIF ; seules consignes qualitatives (délais, respecter 429 et Retry-After). Seule valeur chiffrée : 60 req/min sur 5 min pour le CDX Wayback, relayée par un tiers (non vérifiée ici). Aucun en-tête de limite observé. Pourquoi non publié : hypothèse (étiquetée) : limites adaptatives par IP face au trafic automatisé (billets 2023 et 2026). Contact : info@archive.org (billet 2026). L'adresse Aitratelimit@archive.org citée par des tiers n'est pas confirmée.

## Crash test (étape g)

Crash test fait le 2026-11-14 : crash-iiif-info sur iiif.archive.org : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/internet-archive.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
