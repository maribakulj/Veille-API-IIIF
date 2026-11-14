# UNT Libraries — Portal to Texas History et UNT Digital Library (`university-of-north-texas-libraries`)

- **Classeur** : GLAM-053 · États-Unis · audit v2 du 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `texashistory.unt.edu` (Portal to Texas History), `digital.library.unt.edu` (UNT Digital Library), même logiciel (Django).

## Sources
- **Pages API** `texashistory.unt.edu/api/`, API de collection (TDNP) et `digital.library.unt.edu/api/` (lues en entier, `sources/a`, `sources/a2`) : OAI-PMH (`oai_dc`, `untl`), IIIF Presentation (manifeste d'objet `…/ark:/67531/metapth12412/manifest/`, manifeste de collection), flux Atom, OpenSearch, vignettes. « You do not need to apply for a special key to use these APIs. » Contact : Mark Phillips. Aucun quota ni limite de débit dans le texte.
- **robots.txt** des deux hôtes (lu en direct) : groupe `*` avec **`Crawl-delay: 3`** et **`Request-rate: 1/3`** ; `Disallow: /stats/`, `/feedback/`, `*/zoom/` ; ClaudeBot, Bytespider, meta-externalagent, meta-webindexer et GoogleOther interdits.
- Pages « Policies », « Technology », « Contact » du Portal (lues) : citation, accords des partenaires, architecture ; rien sur le débit.
- Dépôt GitHub `unt-libraries/django-altcha-middleware` : défi ALTCHA (preuve de travail) contre les robots.

## Tests (2 passes, configurations committées avant lancement, pause 6 s)
`texashistory.unt.edu` (10 requêtes) : OAI Identify / ListMetadataFormats / ListSets, manifeste, vignette, OpenSearch en **200** ; `feed/` en **404** (HEAD) ; manifeste de collection TDNP : 301 puis 200. **En-tête observé : `retry-after: 3` sur des réponses 200** (Identify, OpenSearch, vignette de `digital.library`), en accord avec le Crawl-delay. `digital.library.unt.edu` (5) : mêmes familles en 200. Aucun 429, aucun défi ALTCHA rencontré. Non testés : `ListRecords` et `identifiers/` (volume).

## Web (4 catégories)
- institution : dépôt `django-altcha-middleware` lu.
- utilisateurs : aucun résultat (articles généraux sur les bots d'IA seulement).
- tickets : aucun résultat.
- présentations : diapositives TCDL 2026 « The Road to Joy is DAMmed! » lues : « No longer effective methods : IP blocking, Rate-limiting, Filtering by user agents » ; solution : défis de preuve de travail. La notice d'une affiche UNT sur « Robots.txt and Crawler Politeness in the Age of Generative AI » existe (lue en direct, métadonnées seulement).

## Conclusion
Limite chiffrée écrite : Crawl-delay 3 s / Request-rate 1/3 (20 req/min) dans robots.txt ; `Retry-After: 3` annoncé par le serveur. Pas de clé. Mesure anti-bot déclarée : défi ALTCHA. Aucun 429 en 15 requêtes. Confiance : moyenne. Crash test (g) : configuration `config/crash-oai-identify.json` prête (limite documentée 20 req/min), non lancé.
