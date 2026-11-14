# Rattrapage documentaire G — 14 novembre 2026

Périmètre : **University of Michigan Library Digital Collections (GLAM-040)** et **Yale LUX (YCBA, YUAG, Peabody, GLAM-036 à 038)**. Ce complément répond à des lacunes de gouvernance et de documentation, pas à des essais de débit en direct.

## GLAM-040 — University of Michigan : 2 infrastructures distinctes

### 1. API Directory institutionnel (ITS / Apigee)

La FAQ officielle **API Glossary & FAQ** https://documentation.its.umich.edu/node/3784 indique explicitement (mise à jour affichée **5 décembre 2022**) :
- « In general, API within the API Directory have a quota of **200 calls per minute for each app**. Any additional restrictions or policies will be individually documented within the Directory. »
- Tous les appels à des API du Directory sont authentifiés par **OAuth à deux acteurs**, liés à une application et à son équipe/propriétaire.
- Les quotas sont **par application**, éventuellement complétés par d'autres contrôles de sécurité contre les rafales.
- L'API Directory est hébergé par Google (VPC), avec des API products et politiques **Apigee**. Pour obtenir les identifiants, le guide https://its.umich.edu/data/data-database/api-directory/getting-started exige une affiliation U-M, un compte SSO et l'accès réseau U-M/VPN ; l'usage par les affiliés invités requiert un sponsor.
- **Important : cette FAQ date de 2022**. On peut qualifier la valeur 200/min comme « officiellement documentée pour le Directory », mais il faut demander confirmation de sa validité actuelle et de sa portée par produit. Elle ne se rattache **pas automatiquement** aux serveurs `quod.lib.umich.edu` ni à un service IIIF de la bibliothèque.

### 2. Digital Collections Library (DLXS) et migration Project DOR

Deux publications de la bibliothèque fournissent les jalons officiels :
- https://blogs.lib.umich.edu/library-tech-talk/delivering-exciting-upgrades-digital-collections-through-project-dor (**20 août 2026**).
- https://blogs.lib.umich.edu/digital-collections-files/improvements-digital-collections-upcoming-new-platform (**28 septembre 2026**).

Le système **DLXS** continue de servir les collections numérisées (plus de 200 collections). La bibliothèque développe une nouvelle infrastructure **Project DOR**, avec OCFL, PREMIS, OCR, stockage et découverte via OpenSearch. Objectif : **premières collections dans Project DOR d'ici juin 2027**, puis migration progressive du reste. L'interface publique conserve en partie ses visionneuses.

La page du 28 septembre mentionne que le téléchargement de documents textuels depuis certaines interfaces est limité à **10 pages par document** dans l'ancien système. Cette limite doit être conservée comme **limitation de téléchargement de l'interface utilisateur**, pas interprétée en « 10 appels/minute » ou en quota Image API.

### 3. Points manuels encore ouverts

Les trois items de `institutions/university-michigan-digital-collections/data.json` :
- `https://quod.lib.umich.edu/` (403 défi selon la sonde),
- `https://quod.lib.umich.edu/b/bhl/x-bl004079/bl004079` (403),
- `https://quod.lib.umich.edu/cgi/i/image/api/image/bhl:BL004079:BL004079/info.json` (pas testé après blocage),
restent techniquement non résolus. Aucun en-tête `RateLimit` ni statut Live du service IIIF ne découle des documents sur Apigee.

### 4. Source tierce à ne surtout pas attribuer à la bibliothèque

La page https://parse.bot/marketplace/07cdc5ea-9f99-43e6-a2c0-b7ca0ce61f62/quod-lib-umich-edu-api décrit une **API tierce hébergée par Parse** qui revendique des 429 et des clés `X-API-Key`. **Ce n'est pas la documentation d'une API de la bibliothèque.** Toute limite « Parse » doit rester hors du champ des limites officielles `quod.lib.umich.edu`. Le `web` du dossier la classe déjà comme tierce : conserver ce marquage.

**Résultat :** un quota **200/min** est documenté pour le **Directory universitaire**, pas pour **IIIF/DLXS**. Ajouter l'information institutionnelle dans une rubrique « API Directory (hors IIIF, non démontré pour DLXS) », **pas** comme quota IIIF dans le benchmark.

## Yale LUX : documentation technique retrouvée malgré la SPA et les pages Atlassian

- Index officiel désormais accessible : https://project-lux.github.io/documentation/ ; site maintenu par l'équipe Project LUX, avec schémas Linked Art et liens vers les quatre dépôts (pipeline, front-end, back-end, middle tier). Il n'annonce pas de quota chiffré.
- **Documentation d'endpoints du middle tier**, directement accessible par GitHub :
  https://github.com/project-lux/lux-middletier/blob/main/docs/api-endpoints.md .
  Familles **GET** documentées :
  - `/api/advanced-search-config`
  - `/api/auto-complete` (expérimental, non utilisé en production dans le document)
  - `/api/facets/:scope`
  - `/api/related-list/:scope`
  - `/api/search/:scope` (requête `q` JSON encodée)
  - `/api/search-estimate/:scope`, `/api/search-info`, `/api/search-will-match`
  - `/api/stats`, `/api/translate/:scope`, `/api/_info`
  - données Linked Art `GET /data/{id}` ; exemple **officiel** https://lux.collections.yale.edu/data/object/fbe069b3-4d30-4406-a4a0-47303d4fae22 .
  Les exemples `https://lux.collections.yale.edu/api/advanced-search-config` ou `/api/stats` sont **documentés, pas testés ici en direct**.
- **Documentation interne du backend MarkLogic** :
  https://github.com/project-lux/lux-marklogic/blob/main/docs/lux-backend-api-usage.md .
  Elle exige une **authentification** pour **tous les endpoints backend**, avec comptes de service et rôles consommateurs. Cela **ne signifie pas que les routes publiques du middle tier exigent toutes ces mêmes identifiants** : le README officiel https://github.com/project-lux/lux-middletier/blob/main/README.md explique que le middle tier prend en charge l'authentification du backend et la masque au front-end.
- Il faut distinguer trois couches :
  1. **Backend MarkLogic** (services internes authentifiés) ;
  2. **Middle tier LUX** exposant les routes HTTP publiques ci-dessus, modalités de quota non chiffrées ici ;
  3. **IIIF Image et Presentation** de chaque partenaire Yale, qui peuvent dépendre d'autres hôtes et contrôles.

**Conséquences pour les dossiers YCBA/YUAG/Peabody** :
- Les items `https://lux.collections.yale.edu/content/technology` et `https://lux.collections.yale.edu/`, identifiés comme SPA sans texte lisible, peuvent être **complétés documentairement** grâce à cet ensemble officiel de GitHub et MkDocs. Cela **ne clôture pas** la vérification technique de la SPA, des en-têtes, ni des quotas LUX.
- Le dossier YCBA garde sa règle officielle de **courtoisie et transparence sur le User-Agent** (https://britishart.yale.edu/open-data-and-data-services-terms-use) et un droit de limiter les usages excessifs non chiffré. **Ne pas appliquer cela automatiquement à toute la plateforme LUX**.
- Le wiki Yale `https://yaleits.atlassian.net/wiki/x/NQA0jQ` ne se confond pas avec ces documents : seule la documentation des endpoints du middle tier est récupérée, **pas** les détails de chaque manifeste IIIF de chaque institution.

## Contrôles en attente
- La nouvelle documentation du Directory U-M doit être datée et ses conditions de sponsoring/SSO respectées ; pas de tentative d'identifiants d'un tiers ni de connexion.
- Pour Michigan, conserver tous les 403 `quod.lib.umich.edu` et les tests IIIF comme **non exécutés** ; aucun chiffre de quota spécifique confirmé.
- Pour LUX, les URL sont étayées par des fichiers sources mais **pas par des en-têtes HTTP** ; l'absence de `429` dans le guide ne prouve aucune absence de quota.
- Définir explicitement la portée LUX, à cheval sur plusieurs unités Yale, plutôt que compter ses quotas supposés trois fois.
