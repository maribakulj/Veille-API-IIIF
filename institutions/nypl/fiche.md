# New York Public Library — `nypl` (audit v2, 2026-11-14)

- **Statut** : étapes a à f faites ; g non lancée (configuration prête : `config/crash-nypl-manifeste.json`).
- **Hôtes** : `api.repo.nypl.org` (API Repo v2, jeton), `api-collections.nypl.org` (manifestes IIIF Présentation 3), `iiif.nypl.org` (Cantaloupe, Image API v2), `www.nypl.org` et `digitalcollections.nypl.org` (défi JavaScript Incapsula, arrêtés).

## Sources
- `https://api.repo.nypl.org/` (sources/passe1/raw/06.html, texte 06.txt) : « The Repo API is being deprecated and will no longer be available starting August 1st, 2026. No public API replacement is planned at this time. » ; « The limit per authentication token while connecting from an application or curl request is 10,000 requests per day. » ; authentification obligatoire (jeton ou identifiant). Exemples `/api/v2/items/...`.
- `https://api.repo.nypl.org/terms_conditions` (passe2/raw/01.html) : « NYPL has established quota limits for the NYPL Repository API. Attempts to subvert or abuse quotas are a violation ... and could result in your access ... being disabled. » ; `/sign_up` : « API Request Limit (Default): 10000 ».
- `https://api.repo.nypl.org/api_documentation_v1` : v1 déprécié, retiré (410 observé le 2026-11-13, journal ancien).
- GitHub `NYPL/digital-collections` (passe3) : « We have a local instance of IIIF served via Cantaloupe ... We currently support v2.0 ». Aucune limite.
- robots.txt : api.repo.nypl.org (commentaires seulement, tout autorisé) ; iiif.nypl.org 404 Cantaloupe ; api-collections.nypl.org 404 ; www.nypl.org et digitalcollections.nypl.org : défi Incapsula ; Wayback du robots de digitalcollections : seulement Disallow pour Bytedance, Bytespider, GPTBot (`sources/wayback/nypl-incapsula.md`). Pas de Crawl-delay.
- Contacts : repoapi@nypl.org, digitaldam@nypl.org.

## Tests (tests/journal.log, passe v2-1 : 5 requêtes ; anciennes passes du 2026-11-13 conservées)
API Repo v2 sans jeton : 401 « HTTP Token: Access denied. » avec `www-authenticate: Token realm="Application"` (items/total et items/search) : accès refusé par authentification, pas un quota. Manifestes api-collections (2) : 200, sans en-tête de limite, sans canvas ni service d'image. iiif.nypl.org racine : 200 (Cantaloupe). Aucun 403 anti-bot ni 429 sur ces hôtes. info.json d'image : non testé, aucun identifiant d'image `iiif.nypl.org` dans la doc ni dans les manifestes lus.

## Web (4 recherches)
- institution : doc NYPL IIIF propre introuvable ; seule la limite 10 000/jour du Repo API.
- utilisateurs : aucune plainte sur NYPL ; FromThePage (tiers, lu) : « Nearly every digital library system we interact with has blocked FromThePage from accessing their materials » (ne cite pas NYPL).
- tickets : aucun ticket NYPL trouvé.
- présentations : billets NYPL de 2013 (API annoncée) vus en résumé de moteur seulement (www.nypl.org interdit à la lecture directe) ; rien sur 2026.

## Conclusion
Limite documentée : 10 000 requêtes/jour/jeton pour l'API Repo v2 (arrêt annoncé au 1er août 2026, date passée : l'hôte répond encore 401) ; aucune limite publiée ni observée pour les manifestes et le serveur d'images. Hôtes publics du site en défi Incapsula : accès refusé à ce client, ce n'est pas un quota. Confiance moyenne.
