# Parliamentary Archives – UK (GLAM-069)

## Sources
- Hôtes du catalogue (archives.parliament.uk, www.parliament.uk, developer.parliament.uk) : défi Cloudflare « Just a moment... » (403) dès la première requête ; arrêtés, non contournés (`sources/doc/FETCH.log`). Pages lues via Wayback (`sources/wayback/*.md`, extraits verbatim avec URL de réplique).
- robots.txt de archives.parliament.uk (Wayback 2025-04-13) : `Crawl-delay: 10` pour tous les robots ; bingbot exclu de /collections/search, PetalBot de /collections/. Aucun quota chiffré.
- Les collections sont en cours de transfert aux National Archives (Kew) : « Our collections are being moved to The National Archives. »
- Le Developer hub liste douze API de données parlementaires sous Open Parliament Licence, sans quota annoncé ; ce ne sont pas des API du catalogue des Archives.
- Aucune API ni IIIF des Archives documentés.

## Tests
- Passe 1 (2 requêtes) et passe 2 (5 requêtes) sur members-api, bills-api, committees-api.parliament.uk : 200 partout, aucun en-tête de limite (`RateLimit-*`, `Retry-After`), réseau Cloudflare (`server: cloudflare`). robots.txt de ces trois hôtes : 404.
- Catalogue des Archives : non testé (403/défi).
- Crash test préparé : `config/crash-members-constituency.json` (non lancé).

## Web
- institution : bilan annuel 2021-2022 (résumé de moteur, non vérifié) ; ingestion interne d'API, rien de public.
- utilisateurs, tickets : aucun résultat. presentations : article IJDC (Fryer) sur la préservation numérique, sans IIIF ni quota (résumé de moteur ; original en 403 pour WebFetch).
- WebFetch sur nationalarchives.gov.uk refusé par le système de permissions : noté, non contourné.

## Conclusion
Aucun quota ni limite de débit publiés pour les Archives du Parlement ; seul le Crawl-delay de 10 s du robots.txt (via Wayback). Pas de IIIF ni d'API pour le catalogue ; les API de données du Parlement répondent sans en-tête de limite. Confiance faible (hôtes principaux inaccessibles à la sonde). À vérifier à la main : voir `a_verifier_manuellement`.
