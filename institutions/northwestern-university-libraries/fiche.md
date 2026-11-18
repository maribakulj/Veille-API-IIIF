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

## Rattrapage documentaire — 15 novembre 2026

La spécification institutionnelle **OpenAPI 3.1** de l'API REST v2 a été récupérée et parcourue intégralement (19 463 caractères) ; elle décrit la représentation des œuvres par `?as=iiif` et des schémas d'authentification, **sans plafond chiffré dans le YAML**. Ne pas assimiler cette REST API à l'hôte d'images : le `info.json` exact de `iiif.dc.library.northwestern.edu` **n'a toujours pas été extrait**. Voir [`VERIFICATIONS-CHATGPT-2026-11-15-V-SOURCES-ET-TRIAGE.md`](../../VERIFICATIONS-CHATGPT-2026-11-15-V-SOURCES-ET-TRIAGE.md).

## Rattrapage documentaire — passe AC (18 novembre 2026)

La documentation **Clover** éditée par Northwestern University Libraries montre des manifestes **Presentation v3 statiques** documentés et récupérables. Trois exemples ont été lus : *tagging* (1 canevas), *paged* (31 canevas) et *navPlace* (1 canevas). Le document *tagging* a été **conservé en JSON** dans `sources/lectures-2026-11-18/clover-tagging-manifest-static.json` ; il pointe vers un vrai service d'image `iiif.dc.library.northwestern.edu` mais comporte des **annotations ajoutées à des fins de démonstration**. Deux essais ponctuels de `info.json` pour les images référencées ont encore rendu un **`fetch_error` code200 sans corps**. L'URL originale `/iiif/3/e814609e-.../info.json` demeure non extraite : **une démonstration n'est pas une mesure HTTP du service Image**.

Voir [`VERIFICATIONS-CHATGPT-2026-11-18-AC-DRI-NORTHWESTERN.md`](../../VERIFICATIONS-CHATGPT-2026-11-18-AC-DRI-NORTHWESTERN.md).
