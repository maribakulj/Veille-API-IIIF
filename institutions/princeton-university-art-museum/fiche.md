# Princeton University Art Museum (`princeton-university-art-museum`)

- **Classeur** : GLAM-042 · États-Unis · **Vérifié le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `data.artmuseum.princeton.edu` (API JSON + manifestes IIIF Presentation 3), `media.artmuseum.princeton.edu` (IIIF Image 3 et 2, CloudFront), `static.artmuseum.princeton.edu` (jeux zip, S3/CloudFront), `artmuseum.princeton.edu` (site, Cloudflare).

## Sources
- Doc officielle : dépôt GitHub `Princeton-University-Art-Museum/puam-api-docs` (README, objects, makers, packages, search), lue en entier (`sources/b`, `sources/c`). « No authentication is currently required to access the API, however this may change in future versions. » `size` : par défaut 10, maximum 500. Aucune limite de débit, aucun quota, aucun en-tête de limite documenté. Jeux statiques zip « refreshed on a weekly basis », proposés pour les usages sans connexion dynamique.
- Site `artmuseum.princeton.edu` : défi Cloudflare 403 dès la 1re requête. Conditions d'utilisation et robots.txt lus via Wayback (capture 2025-06-01, `sources/wayback/`) : usage non commercial/éducatif, citation exigée ; `Crawl-delay: 10`, `Disallow: /search/`. Aucune mention d'API ni de débit. Page à vérifier à la main (onglet dédié).
- robots.txt : data 404, static 404, media 500 puis 302 (indisponible).

## Tests (2 passes, 8 + 10 requêtes, pauses ≥ 6 s, configurations committées avant lancement)
Passe 1 (data) : `objects/9449`, `objects/9449/tombstone`, `makers/6353`, `packages/123`, `objects?maker=6353&size=2`, `search?q=blue&type=all&size=2`, manifeste IIIF `iiif/objects/24625` : **200** ×7. En-têtes : `cache-control: max-age=300`, `access-control-allow-origin: *`, nginx/Express ; aucun en-tête de limite.
Passe 2 (media/static) : info.json IIIF 3 et 2, miniature `!350,350`, HEAD de la collection IIIF, HEAD des trois zips (objects.zip 464 652 062 octets) : **200** ×7. CloudFront (`x-cache`, `via`) ; aucun en-tête de limite. Aucun 429.

## Web
Quatre recherches : politique/doc (GitHub officiel), utilisateurs (aucun résultat), tickets (aucun ticket tiers ; issues du dépôt vides), présentations (talk IIIF 2018 de Dan Brennan, session MCN, billet du CDH 2020). Aucune limite ni plainte trouvée.

## Pourquoi pas de quota publié ? (hypothèse)
API ouverte sans clé, conçue pour étudiants et chercheurs, avec un jeu zip hebdomadaire pour le volume : le musée ne chiffre rien. Hypothèse, non confirmée par une source.

## Conclusion
Limite chiffrée : aucune (seul `size` ≤ 500). Contact : issues GitHub du dépôt puam-api-docs. Confiance : moyenne. Crash test (g) : à faire à la fin ; aucun réseau protégé sur data, CloudFront sur media/static.
