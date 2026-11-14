# Università di Bologna – AMS Historica (`universita-di-bologna-ams-historica`)

- **Classeur** : GLAM-030 · Italie · audit v2 du 2026-11-14 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `historica.unibo.it` (DSpace-GLAM 8.2 : interface, REST `/server/api`, OAI `/server/oai/request`, IIIF `/server/iiif/{uuid}/manifest`, images `/iiif-server/{id}`), `amshistorica.unibo.it` (ancien nom, redirige vers historica), `sba.unibo.it` (doc du système des bibliothèques).

## Sources
- **Carte de service** (PDF `carta_servizio_historica_EN.pdf`, sources/h15/charter.txt) : « Metadata are published and made openly and freely available through the platform's public APIs, in particular via the OAI-PMH protocol, accessible at: https://historica.unibo.it/oai » ; « The Service undertakes to make IIIF manifests [...] easily accessible » ; « web services for interoperability (APIs) ». Aucun quota, aucune limite de débit, aucune règle de robots.
- **Terms and conditions** (`/info/end-user-agreement`, sources/h3) : licences par œuvre ; métadonnées en CC0 ; « The University of Bologna makes reasonable efforts to ensure the availability of the repository » ; haute définition sur demande à historica@unibo.it ; rien sur le débit.
- **robots.txt** de `historica.unibo.it` (sources/h1) : Disallow `/search`, `/browse/*`, `/server/opensearch`, `/feedback`, etc. ; `Sitemap` annoncé ; groupes de mauvais robots (dont « fast » : « Misbehaving: requests much too fast ») ; aucun Crawl-delay. `amshistorica.unibo.it/robots.txt` renvoie la page d'accueil de l'interface après redirection (pas de robots.txt propre) ; `sba.unibo.it/robots.txt` : Disallow de chemins internes seulement.
- Pages « General information », « Privacy », « Feedback », page SBA sur la préservation (sources/h2, h5, h6, h12), diapositives 2023 de l'institution (sources/h13). Les premières tentatives sur `amshistorica.unibo.it` ont été marquées « sautées » par `fetch_doc.sh` à tort (faux positif : la chaîne « recaptcha » dans le JavaScript de l'interface) ; les pages ont été relues une par une sous `historica.unibo.it`.

## Tests (4 passes, configurations committées avant lancement, pauses 6 s ; 15 requêtes d'API (+ 1 redirection suivie) plus 4 robots.txt)
- Passe 1 : REST (racine, item, recherche), OAI `Identify` : `/oai?verb=Identify` (adresse de la carte de service) = **302** vers `/server/oai?verb=Identify` = **302** (redirections non suivies hors budget), `/server/oai/request?verb=Identify` = **200** ; OpenSearch (Disallow robots, testé selon C12) **200** ; `sitemap_index.xml` **200** ; manifeste IIIF d'un item sans IIIF : **404**.
- Passe 2 : recherche REST 10 résultats **200** ; page d'accueil de l'interface **200**.
- Passe 3 : manifeste IIIF 2.1 d'un item IIIF (2388a439…) **200** ; recherche « manoscritto » **200**.
- Passe 4 : `info.json` (IIIF Image 2), dérivé 200 px, manifeste d'un item d'images : **200** ×3.
- **En-têtes observés** : `x-ratelimit-limit: 500`, `x-ratelimit-remaining: 499`, `x-ratelimit-reset: <epoch>` sur les réponses du serveur Express de l'interface (`sitemap_index.xml`, `/home`), pas sur REST, OAI, IIIF ni images (CloudFront devant). Les deux valeurs de `reset` relevées (1794621039 et 1794620859) sont antérieures de 35 s et d'environ 3 min à l'heure de réponse pour la seconde : valeur non interprétable seule. 500 coïncide avec le défaut de DSpace Angular (500 requêtes par minute et par IP, config.example.yml, source tierce).
- Aucun 429.

## Web (4 catégories)
- Institution : carte de service et conditions d'utilisation (ci-dessus).
- Utilisateurs : aucune plainte 429 trouvée.
- Tickets : aucun ticket tiers sur `historica.unibo.it` ; source tierce utile : la configuration de DSpace Angular (limiteur par IP).
- Présentations : diapositives 2023 de l'institution (sources/h13) et communication Open Repositories 2026 « Historica: Exploring Cultural Heritage Through Space and Time with DSpace-GLAM » (Zenodo) : IIIF et REST/OAI cités, rien sur les limites.

## Pourquoi pas publié ?
Hypothèse : plateforme DSpace-GLAM standard dont le limiteur par IP de l'interface est un réglage par défaut de DSpace Angular, jamais repris dans la doc de l'institution.

## Conclusion
Limite documentée par l'institution : aucune. Limite observée : 500 requêtes par fenêtre (en-têtes `x-ratelimit-*` sur l'interface), cohérente avec le défaut du logiciel. Contact : historica@unibo.it. Confiance : moyenne. Crash test (g) : configuration `config/crash-sitemap-ratelimit.json` prête.
