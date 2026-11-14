# Northwestern University Libraries (`northwestern-university-libraries`)

- **Classeur** : GLAM-045 · États-Unis · audit v2 le 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `api.dc.library.northwestern.edu` (API v2 : works, collections, file-sets, search, OAI-PMH, manifestes IIIF), `iiif.dc.library.northwestern.edu` (images IIIF), `dc.library.northwestern.edu` et `digitalcollections.library.northwestern.edu` (site), `www.library.northwestern.edu`.

## Sources
- **Doc officielle** : https://api.dc.library.northwestern.edu/ (et /docs/v2/, même page : OpenAPI + guide ; `sources/a/`). Elle décrit works, collections, file-sets, annotations, search, OAI-PMH, thumbnails, formats `as=iiif|premis|c2pa`, `mcp/server-card`, authentification (« for now this feature is internal »). **Aucune mention de quota, limite de débit, clé ou politique de robots** ; seule limite écrite : `size` de thumbnail ≤ 300 px.
- `robots.txt` : `api.dc` = 404 (tout autorisé) ; `dc.library` = 403 CloudFront « Request blocked » pour nous, lu via Wayback (`sources/wayback/dc-robots.md` : `Disallow: /search`, pas de Crawl-delay) ; `iiif.dc`, `digitalcollections` = 403 ; `www.library` = 404.
- README GitHub nulib/dc-api-v2 : renvoie vers la doc de production ; aucune limite.

## Tests (2 passes, configurations committées avant lancement, pauses 6 s ; 17 requêtes dont 2 lectures de robots.txt)
Passe 1 : works (+ as=iiif, premis, c2pa), search/works, oai Identify et ListMetadataFormats, thumbnail, mcp/server-card, works/{id}/similar : **200** ×10. Passe 2 : collections (liste), collections/{id} (+ thumbnail), file-sets/{id}, annotations : **200** ×5. Aucun 429, aucun en-tête `RateLimit-*`, `Retry-After`, `X-RateLimit-*` ; en-têtes : `apigw-requestid` (API Gateway AWS), cookie JWT `dcapi…` (scope `read:Public`, non connecté).
Non testé : images IIIF sur `iiif.dc` (hôte en 403 pour son robots.txt, arrêté ; URL de service lue dans le manifeste) ; POST /search et POST /oai (POST interdit) ; `/auth/*` (compte requis).

## Web (4 recherches)
- Institution/utilisateurs/présentations : aucun résultat sur une politique de bots ou de débit, ni plainte 429/403, ni billet de lancement.
- Tickets : dépôts nulib/dc-api-v2 et dc-nextjs (le site appelle l'API) : aucune limite citée.

## Pourquoi pas publié
Aucune limite n'est publiée ; l'API sert aussi le site public de la bibliothèque. Les hôtes du site et des images répondent 403 CloudFront à notre client (protection WAF) alors que l'API répond sans défi. Hypothèse (non vérifiée) : limitation par WAF sur les hôtes de site/images, pas annoncée.

## Conclusion
Limite chiffrée : aucune. API v2 ouverte (200 partout, sans en-tête de limite) ; site et serveur d'images derrière un 403 CloudFront. Confiance : moyenne. Contact : page de contact du site Digital Collections (à vérifier à la main). Étape g : `config/crash-oai-identify.json` prête.
