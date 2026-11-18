# Rattrapage documentaire I — 14 novembre 2026

Périmètre de cette passe : **University of British Columbia Open Collections (GLAM-051)**, puis revue complémentaire de Toronto, UNT, Washington, Villanova, Brown, NCSU et Folger (GLAM-050 à GLAM-057).

## UBC : **10 / 200 requêtes/minute retrouvées dans une source officielle primaire**

**Source officielle historique du producteur** :
https://github.com/ubc-library/docs-open-collections-api/blob/master/data/api.twig.html  
Fichier `data/api.twig.html` dans le dépôt `ubc-library/docs-open-collections-api`, organisation GitHub de la bibliothèque. Le dépôt est archivé dans son historique public, avec **dernier push le 9 septembre 2021** selon la métadonnée GitHub consultée (attention à l'ancienneté).

Le bloc HTML `<div id="api-keys">` contient explicitement :
- `Public API Key` : **10 req/min** ;
- `Your API Key` : **200 req/min** ;
- inscription par adresse e-mail et confirmation avant levée des restrictions à la clé personnelle ;
- plafond global annoncé : **pas plus de 200 requêtes/minute**.
La documentation présente des endpoints `/collections`, `/collections/{name}`, `/collections/{name}/items`, `/collections/{name}/items/{itemId}`.

**Nuance :** la doc officielle parle d'une **« Public API Key »** à 10/min, pas de l'absence de toute clé. La page tierce https://apis.io/security/ubc/ubc-authentication/ indique un accès anonyme avec plafond **10/min/IP** et un accès personnel **200/min** ; elle revendique un test sur `oc-index.library.ubc.ca` le **19 août 2026**, mais ses en-têtes et journaux bruts ne sont **pas disponibles ici**. Ce tiers constitue une **corroboration secondaire** de la valeur historique, pas une observation reproduite par cet audit.

**Portée** : ces quotas concernent **l'API de recherche/métadonnées Open Collections**, pas une preuve des quotas du service **IIIF Image**, ni de **l'OAI-PMH**. Les trois familles doivent rester distinctes. En particulier, `data.json` dit que le service OAI demande une clé enregistrée via en-tête : cette modalité n'est pas contredite par le tableau public des clés.

**Révision à entreprendre** dans `institutions/university-british-columbia-open-collections/data.json` :
- `limites_documentees` contient actuellement « Requêtes sans clé API limitées (nombre non chiffré) ». Préciser **la source ancienne officielle** et **10/min avec clé publique, 200/min avec clé personnelle**, puis distinguer `verification = officielle historique (2021), corroboration tierce 2026, pas de re-test HTTP`.
- L'URL `https://open.library.ubc.ca/docs` reste **bloquée par WAF au niveau du client original**, mais le **code source correspondant est lisible sans authentification**. Classer l'ancienne URL comme « contenu officiel retrouvé dans GitHub », sans effacer le fait HTTP 200 + page de blocage.
- Les `https://open.library.ubc.ca/robots.txt` et `https://oce-index.library.ubc.ca/oai?verb=Identify` restent **non vérifiés techniquement**.
- Le site tiers `https://apis.io/rate-limits/ubc/ubc-rate-limits/` ne doit **plus** être la source principale du chiffre dès lors qu'un original institutionnel existe.

## University of Toronto Libraries (GLAM-050)
- `https://collections.library.utoronto.ca/explore/help` est déjà **lu (200)** dans le dossier. Son absence de plafond n'est pas une opération « lecture manuelle » à refaire ; l'action résiduelle est une éventuelle demande de **politique d'usage non publiée**, sans mélanger avec un site illisible.

## UNT (GLAM-053)
- `https://texashistory.unt.edu/about/portal/policies/` a **déjà été lue** et n'indique pas de limite de débit.
- Le `Request-rate: 1/3` du `robots.txt` de `digital.library.unt.edu` est une **consigne de politesse crawler**, pas un serveur HTTP annonçant `429` et un quota contractualisé. Distinguer aussi le `Crawl-delay 3` de `texashistory.unt.edu`.
- `https://texashistory.unt.edu/feed/` a retourné 404 lors du HEAD mais la doc peut utiliser une URL relative à une collection ; vérifier le chemin exact plutôt que déduire qu'aucun feed n'existe.

## University of Washington (GLAM-054)
- `digitalcollections.lib.washington.edu` : plusieurs pages bloquées ou rendues uniquement en JavaScript. Pas de preuve nouvelle de débit. La règle `Crawl-Delay: 1` du robots.txt ne suffit pas pour décrire un quota IIIF. Les manifestes hébergés via OCLC ne doivent pas être confondus avec le quota de l'hôte UW.

## Villanova (GLAM-055)
- `digital.library.villanova.edu` reste bloqué par Azure Application Gateway (403 lors des tests d'origine), y compris le manifeste cité par un tiers. L'absence de chiffre dans une **archive 2025 de la page d'accueil** ne prouve pas une absence de quota : la valeur de `limites_documentees` « Aucune limite chiffrée = aucune » devrait être reclassée comme **« quota non documenté dans les sources examinées ; comportement non vérifié »**.

## Brown (GLAM-056)
- Le wiki du service décrit lui-même les mesures Cloudflare déployées au printemps 2025 ; voir rapport B. Cela étaye le **motif du blocage documentaire**, pas un chiffre de limite.

## North Carolina State (GLAM-052) et Folger (GLAM-057)
- Les systèmes de Bot Detection / Cloudflare Turnstile / AWS WAF recensés dans les `data.json` ne sont **pas contournés**. Ils ne doivent pas être décrits comme des quotas de requêtes.
- Pour le Folger, la même institution donne **Crawl-delay 5 s** sur `catalog.folger.edu` et **120 s** sur `digitalcollections.folger.edu`. Toute table comparative doit conserver **les hôtes et services distincts**, sans choisir arbitrairement une seule valeur « par institution ».

## Synthèse de ce lot
La découverte nouvelle et exploitable est **le code source officiel UBC** qui documente exactement le régime de clés et les deux plafonds. Les autres contrôles visent à reclasser des items mal définis « manuel » (page déjà lue ou contact à demander) et à conserver les vrais blocages techniques non résolus.
