# Princeton University Library et Art Museum — `princeton`

- **Classeur** : GLAM-041 · États-Unis · Audit v2 le 2026-11-14 (Sonnet 5.5) ; l'ancien audit (sessions lancées avant le commit des configurations) est archivé dans `tests/archive/`.
- **Hôtes** : `iiif.princeton.edu` (Cantaloupe, derrière CloudFront), `libimages1.princeton.edu` (ancien, redirige), `figgy.princeton.edu` (manifestes, OAI), `data.artmuseum.princeton.edu` (API du musée), `media.artmuseum.princeton.edu` (IIIF Image du musée).

## Sources
- DPUL (`sources/bibliotheque/`) : « Contact us to learn more about harvesting Princeton's iiif data. » (contact digital-library@princeton.libanswers.com) ; aucun quota.
- Wiki Confluence DPUL (1 Mo lu) : mêmes contacts, aucune limite.
- GitHub du musée `puam-api-docs` (`sources/musee/`, `musee2/`) : API REST sans authentification (« No authentication is currently required to access the API ») ; `size` maximum 500 ; jeux statiques mis à jour chaque semaine ; aucune limite de débit.
- `robots.txt` : figgy `Disallow: /` ; catalog `Crawl-delay: 10` ; iiif/libimages1/media.artmuseum : HTTP 500 ; data.artmuseum : 404 ; library : lu ; artmuseum : 403 Cloudflare (Wayback 2026-01-01 lu, `sources/wayback/`).
- Blocages : `library.princeton.edu/about/*` et `artmuseum.princeton.edu` en défi Cloudflare (non contournés, listés « à vérifier à la main ») ; `visresiiif.princeton.edu` introuvable (DNS).

## Tests (2 passes, configurations committées avant lancement, pauses 6 s)
Passe 1 (8 requêtes) : racine Cantaloupe, info.json v2 (GET et HEAD), v3, ancien /loris/, libimages1 (301 vers iiif.princeton.edu, non suivie car autre hôte), manifeste figgy, OAI Identify figgy : tous 200 sauf la redirection. Passe 2 (9 requêtes) : API musée (objects, tombstone, makers, packages, search, liste filtrée), manifeste IIIF 3, info.json et HEAD : tous 200. Aucun en-tête de limite, aucun 429, aucun 403 (`tests/journal.log`, `tests/raw/`).

## Web (4 catégories)
- Institution/tiers : un serveur MCP tiers note que Princeton DPUL refuse les clients automatisés et que le robots.txt de figgy est `Disallow: /` (lu dans l'original).
- Utilisateurs : aucune plainte 429/503 trouvée (résumé de moteur, non vérifié).
- Tickets : pulibrary/figgy#1236 (URL de manifestes pour les instruments de recherche), aucune limite.
- Présentations : article IIIF 2018 de Princeton (figgy fournit les manifestes) ; rien sur le débit.

## Conclusion
Limite chiffrée : aucune. Règle écrite : contacter la bibliothèque numérique pour moissonner IIIF ; figgy interdit les robots par robots.txt. Confiance : moyenne. Crash test (étape g) : à faire à la fin, config `config/crash-media-artmuseum-info.json` prête.
