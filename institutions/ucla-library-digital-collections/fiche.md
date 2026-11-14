# UCLA Library Digital Collections — `ucla-library-digital-collections`

- **Classeur** : GLAM-046 · États-Unis · Audit v2 le 2026-11-14 (Sonnet 5.5).
- **Hôtes** : `iiif.library.ucla.edu` (Cantaloupe 6, manifestes), `digital.library.ucla.edu` (Ursus, Blacklight), `guides.library.ucla.edu` (doc).

## Sources
- Guide IIIF UCLA (`sources/doc/`) : manifestes `iiif.library.ucla.edu/ark%3A%2F21198%2F{id}/manifest`, Mirador hébergé ; aucun quota. Racine Cantaloupe : endpoints IIIF Image 1.x, 2.x, 3.x.
- Code4Lib Journal 15217 (Bucketeer, Fester, Cantaloupe), dépôts GitHub UCLALibrary : pas de limite.
- `robots.txt` : iiif 404 ; digital : liste de robots d'IA en `Disallow: /`, pas de groupe `*` ; guides : `Crawl-delay: 10` ; library et www.library : 404.

## Tests (2 passes, configurations committées avant lancement, 6 s ; 1re session archivée dans `tests/archive/`)
Passe 1 (6 requêtes) : racine, 2 manifestes (200), HEAD manifeste (405), opensearch.xml et page d'item (200). Passe 2 (4 requêtes + 1 non lancée) : info.json v2 (GET et HEAD) et v3 : 200 ; v1 : **403 text/plain de Cantaloupe** (endpoint refusé, pas un défi) ; l'hôte est arrêté, le dérivé 200 px n'est pas lancé. Aucun en-tête de limite, aucun 429.

## Web
- Institution : billet d'une employée de UCLA Library : défi Anubis « proof of work » sur les collections numériques.
- Utilisateurs : rapport Duke sur Anubis citant UCLA (résumé de moteur, non vérifié). Tickets : aucun résultat. Présentations : iiif-discuss 2019 (Samvera, Cantaloupe), Code4Lib 15217.

## Conclusion
Limite chiffrée : aucune. Protection anti-robots : Anubis (non rencontré sur nos requêtes) et liste de robots d'IA interdits. Confiance : moyenne. Crash test (g) à la fin : `config/crash-image-v2-info.json`.
