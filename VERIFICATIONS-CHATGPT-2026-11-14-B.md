# Deuxième lot de vérifications — 14 novembre 2026

Continuation de `VERIFICATIONS-CHATGPT-2026-11-14.md`. Même convention : **lecture web ≠ réponse HTTP de la sonde**. Les résultats documentaires déjà présents dans `data.json` sont expressément signalés pour éviter les doublons.

## Art Institute of Chicago

- `https://www.artic.edu/open-access/public-api`, `https://www.artic.edu/terms`, `https://www.artic.edu/articles/902/public-access-to-our-public-presence-sharing-our-api` et `https://www.artic.edu/iiif/2/b3974542-b9b4-7568-fc4b-966738f61d78/info.json` : l'outil de consultation web a échoué avec une erreur 403 ; ce sont **toujours des contrôles manuels/HTTP ouverts**.
- `https://www.artic.edu/robots.txt` : non consultable par l'outil ; contrôle HTTP ouvert.
- **Source officielle accessible en parallèle** : `https://api.artic.edu/docs/`. Elle confirme l'API de métadonnées **anonyme limitée à 60 requêtes/minute**, ainsi qu'une recommandation d'une requête/seconde, d'un seul fil lors du scraping, et des précautions analogues pour les images IIIF. **Déjà consigné** dans le `data.json` de l'institution : ne pas ajouter un quota nouveau ni appliquer automatiquement les 60/min à l'hôte d'images `www.artic.edu`.

## Biblioteca Nacional de España

- `https://bnedigital.bne.es/bd/es/simple` et `https://datos.bne.es/inicio.html` : la lecture web a encore échoué en 403.
- `https://www.bne.es/en/catalogs/hispanic-digital-library` : non consultable par l'outil.
- Le PDF `https://www.bne.es/sites/default/files/repositorio-archivos/procedimiento_normas_reproduccion.pdf` reste à inspecter séparément, avec rendu visuel si besoin. **Aucune ligne ne doit être fermée** par ce passage.

## Cornell / Brown

- Cornell `https://digital.library.cornell.edu/about` et `https://digital.library.cornell.edu/catalog/ss:549539` : toujours en 403 depuis la lecture web. Pas de manifeste IIIF ni d'en-têtes confirmés.
- Brown `https://repository.library.brown.edu/studio/api-docs/` : page de vérification humaine renvoyée ; statut **non résolu**.
- Pour Brown, la politique anti-bot Cloudflare instaurée au printemps 2025 est explicitement décrite sur le wiki institutionnel `https://github.com/Brown-University-Library/bdr_api_documentation/wiki`, **déjà citée dans le dossier**. Elle explique une catégorie de blocage, mais n'en donne pas un seuil chiffré et ne démontre pas une réponse 429.

## Library of Congress

- `https://www.loc.gov/pictures/api` : toujours en 403 par l'outil web. L'API JSON d'un item reste techniquement non testée par cette reprise.
- `https://www.loc.gov/apis/` : **page officielle lue**, liste les familles API JSON/YAML, sitemaps et microservices dont Image Services (IIIF).
- `https://www.loc.gov/apis/json-and-yaml/working-within-limits/` : **officielle et lisible**, confirme : JSON/YAML 20/min ; Text Services 150/min ; Image Services IIIF 150/min ; Streaming Services 60/min ; /storage-services/ 150/min ; MARCXML `lccn.loc.gov/{item-id}/marcxml` 30/min. Blocage annoncé de 1 h sur les premières catégories, 72 h pour MARCXML, avec possible abaissement des limites sous charge. **Tous ces chiffres figurent déjà dans `institutions/loc/data.json`**. Ce passage renouvelle seulement la lecture.
- `https://www.loc.gov/apis/micro-services/image-services/` : confirme explicitement que les *Image Services* implémentent IIIF Image et renvoie à la page de plafonds. Les **150/min** concernent cette famille, pas toutes les API de la bibliothèque.
- Action restante sur `https://www.loc.gov/apis/` : contact institutionnel seulement si la demande porte sur un dépassement ou un quota contractuel ; ce n'est pas une page « illisible ».

## Huntington

- `https://www.huntington.org/terms-and-conditions-use-photographs` : **texte lu**. Couvre les conditions de **photographies fournies par la bibliothèque pour la promotion/publication** ; le champ doit conserver ce périmètre et ne pas être généralisé à toutes les images IIIF ou à l'API.
- `https://researchguides.huntington.org/imagingservices` : **page lue**, mise à jour affichée le 5 novembre 2026. Indique l'accès/téléchargement via la Huntington Digital Library, et les commandes de reproduction haute qualité via Aeon. La limite d'environ 100 pages mentionnée sur la page concerne les **commandes d'imagerie**, **pas un quota API**.
- `https://www.huntington.org/digital-library` : pas de contenu récupéré lors de la lecture web. `https://huntington.emuseum.com/` et `https://www.huntington.org/robots.txt` restent ouverts.

## Kyoto University — Rare Materials Digital Archive

- `https://rmda.kulib.kyoto-u.ac.jp/en/reuse` : **page officielle lue**. Elle indique les conditions de réutilisation selon les bibliothèques, les liens à fournir lors d'une réutilisation sur le Web, et le téléchargement JPEG jusqu'à **2 000 pixels** de côté pour certains fonds. Cette valeur est une restriction de taille de fichier/images, **pas une limite de débit**. Pour les images sous droits différents, voir la notice et obtenir l'autorisation applicable.
- Elle était déjà classée comme « lue au deuxième essai » dans `data.json` ; sa présence dans la liste manuelle semble donc inutile pour le seul critère de lecture documentaire.

## National Library of Wales

- `https://www.library.wales/copyright` : **page officielle lisible** par l'outil web, plutôt qu'une simple archive Wayback. C'est une page sur les droits, pas une documentation de rate limit IIIF. Maintenir la vérification HTTP séparée.
- Les URL `robots.txt`, le PDF de politique d'accès et le communiqué IIIF restent non vérifiés par cette passe.

## National Library of Finland / Finna

- `https://www.kiwi.fi/spaces/Finna/pages/440828359/Finna+API+Documentation+In+English` : **page de navigation officielle lue**, mise à jour affichée le 24 août 2026. Elle renvoie vers les docs API publique, Auth, OAI-PMH, OIDC.
- `https://www.kiwi.fi/display/Finna/Finna+API+Terms+of+Use` : **texte officiel lu** via la nouvelle URL `https://www.kiwi.fi/spaces/Finna/pages/53839699/Finna+API+Terms+of+Use`. Ne requiert pas d'inscription pour l'API publique, mais la bibliothèque nationale se réserve la possibilité d'en introduire en cas de surcharge. **Déjà signalé dans `data.json`**.
- `https://www.kiwi.fi/spaces/Finna/pages/78382572/Finna+Authentication+API+In+English` : **lu**. API d'authentification **uniquement sur convention**, distincte de l'API publique des métadonnées ; nécessite parfois POST/identifiants, donc ne pas l'utiliser comme test.
- La page détaillée de la *Finna API (in English)* et le Swagger des endpoints publics restent bloqués, de même que `api.finna.fi/robots.txt`. Le renvoi vers un wiki accessible **ne clôt pas** ces contrôles.

## University College Dublin

- `https://www.ucd.ie/library/` : page officielle **lue**, lien vers UCD Digital Library et guides. Pas de règle chiffrée d'API dans cette page d'accueil.
- Le problème TLS de `https://digital.ucd.ie/` demeure une vérification technique distincte ; robots.txt n'a pas été établi.

## National Library of Scotland

- `https://data.nls.uk/about/ai-statement/` : **page institutionnelle lue** ; annonce un document Word de politique IA, sans le reproduire dans la page. Le document lié n'a **pas** encore été examiné. Ne pas prétendre avoir contrôlé ses restrictions concernant l'exploitation des données.

## Consignes pour intégration

- Ne retirer de la liste manuelle que les **demandes de lecture documentaire** résolues ; garder l'historique 403/429 et les vérifications HTTP/quotas ouvertes en tant que catégories distinctes.
- Les plafonds LoC et Art Institute of Chicago ne sont **pas des découvertes nouvelles** : ils sont déjà dans `data.json`.
- La distinction licences/tailles d'image/limitations de commandes de reproduction versus **rate limits** est essentielle.
- Pas de modification de `BENCHMARK.xlsx` ou des étapes du suivi depuis le connecteur GitHub sans régénération locale contrôlée.
