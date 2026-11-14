# University of Leicester Library (`university-of-leicester-library`)

- **Classeur** : GLAM-067 · Royaume-Uni · audit v2 du 2026-11-14 · suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `specialcollections.le.ac.uk` (Special Collections Online : 307 vers `leicester.contentdm.oclc.org`, plateforme CONTENTdm hébergée par OCLC, serveur d'images Cantaloupe), `staffblogs.le.ac.uk` (billets), `libraryhelp.le.ac.uk` (FAQ), `le.ac.uk` (site principal, 403 Cloudflare).

## Sources (étape a)
- Billet « How to use IIIF with Special Collections Online » (2023) : manifestes `manifest.json` au bas de la description d'objet, viseur Mirador 3, « we use ContentDM for our platform, which supports the IIIF APIs » ; aucune limite.
- FAQ droit d'auteur : usage non commercial libre pour les contenus sous Creative Commons, demande par e-mail sinon ; rien sur le moissonnage.
- Documentation OCLC CONTENTdm (`sources/a4`) : manifeste `iiif/info/{alias}/{id}/manifest.json`, API `bl/dmwebservices`, aucune règle de débit.
- `robots.txt` : `leicester.contentdm.oclc.org` (et `cdm16445.`) **Crawl-delay 1**, Disallow `/oai/`, `/utils/`, `/config/`, recherches ; `libraryhelp.le.ac.uk` **Crawl-delay 10** ; `staffblogs` : `Disallow: /wp-admin/` ; `le.ac.uk` : 403 Cloudflare à la sonde (Wayback 2025 : `Sitemap:` seulement).

## Tests (étape e, 6 passes, 22 requêtes robots.txt compris, configurations committées avant lancement)
`specialcollections.le.ac.uk` : 307 à chaque requête (3) ; la redirection (autre hôte) est lue puis rejouée sur `leicester.contentdm.oclc.org` : manifeste global (chaîne 301, 302, puis `iiif/2/manifest.json` : 200), `dmwebservices` (200), OAI `Identify` (200, Disallow `/oai/` testé sous C12), manifeste de collection (200), manifeste d'objet (200), `info.json` et vignette (200). Aucun 429, aucun en-tête de limite.

## Web (4 recherches)
Aucune plainte, aucun ticket ; une présentation OCLC (2019) indique « Harvest rate limited to prevent potential abuse » (OCLC, sans chiffre, pour son API expérimentale d'Activity Streams).

## Conclusion
Limite chiffrée : aucune. Crawl-delay 1 s (plateforme OCLC) et 10 s (FAQ) ; une limitation de moissonnage est mentionnée par OCLC sans valeur. Confiance : moyenne.
