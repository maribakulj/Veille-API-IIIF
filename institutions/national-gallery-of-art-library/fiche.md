# National Gallery of Art Library (`national-gallery-of-art-library`)

- **Classeur** : GLAM-049 · États-Unis · **Audit v2 le** 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `www.nga.gov` (site, en défi Cloudflare), `api.nga.gov` (images IIIF), `libraryimage.nga.gov` (manifestes et visionneuse de la Library), `library.nga.gov` (catalogue Primo).

## Sources
Les pages de doc de `www.nga.gov` répondent 403 (défi Cloudflare « Just a moment ») : hôte arrêté, URLs listées à vérifier à la main, une capture Wayback lue (open access, 2025). Lus : `robots.txt` de api, library, libraryimage (404), www ; README GitHub `opendata` et `accademia-research` ; guide IIIF « National Gallery of Art Library » (iiif.io, tiers).
`api.nga.gov/robots.txt` : « if you would like to crawl any nga.gov site you can contact us … to apply for white listing », `Crawl-delay: 10`. `library.nga.gov` : Crawl-delay 10, robots d'IA interdits.

## Tests (3 passes, 12 requêtes dont 4 robots.txt, pauses 10 s ou 6 s)
Passe 1 : `api.nga.gov/` → 301 vers www.nga.gov (non suivi, défi) ; `library.nga.gov/` → 302 → 302 (Primo) ; plan de site : **200**. Passe 2 : manifeste Library (Presentation v2, 250 ko, 186 canevas) : **200**. Passe 3 : `api.nga.gov/iiif/<uuid>/info.json`, dérivée 200 px, visionneuse UV : **200** ×3. Aucun en-tête de limite ni 429. Procédure : trois pages www.nga.gov demandées après le premier 403 (voir notes).

## Web (4 catégories)
Institution : robots.txt (liste blanche). Tickets : mnemosyne#22 (tiers, 403 par WAF). Présentations : article IIIF 2018. Utilisateurs : aucun résultat.

## Conclusion
Limite chiffrée : aucune. Règles écrites : crawl-delay 10 s, liste blanche demandée pour crawler. Accès : www.nga.gov refusé à ce client (Cloudflare), le IIIF de la Library est ouvert. Confiance : faible (doc officielle illisible). Crash test (g) : config `crash-api-nga.json` prête, à décider (liste blanche demandée).
