# Cambridge University Library (CUDL) — `cudl`

- **Statut** : en cours (manifestes IIIF testés ; info.json, métadonnées et recherche non testés, voir section 3)
- **Pays** : Royaume-Uni
- **Point d'entrée testé** : `https://cudl.lib.cam.ac.uk/iiif/{id}` (manifestes Presentation, 200 OK). Le 403 reçu sur `https://cudl.lib.cam.ac.uk/terms` (page du site, pas un endpoint d'API) a été consigné ; il n'a pas bloqué les manifestes. `https://cudl.link/v1/metadata/{id}` (route documentée dans cudl-services) : échec DNS.
- **Vérifié le** : 2026-11-13 (tests de 21:05 à 21:07 UTC ; documentation consultée entre 21:0x et 21:1x UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://cudl.lib.cam.ac.uk/terms (conditions d'utilisation du site) | 2026-11-13 — **non lue** : 403 via WebFetch | rien lu. Aucune mention de quota vérifiée. À relire depuis un navigateur. |
| https://iiif.io/guides/guides/cudl.lib.cam.ac.uk/ (guide IIIF communautaire) | 2026-11-13 (WebFetch, résumé par un petit modèle, non vérifié brut) | Aucune phrase sur quota, limite, accès en masse ou restriction d'usage. Seule consigne : « When copying&pasting the Manifest URL, manually add the “.json” file extension before pasting into desired use location. » (Dans les faits, la forme `.json` redirige en 302 vers la forme sans extension : voir tests.) |
| https://raw.githubusercontent.com/cambridge-collection/cudl-services/master/README.md (doc du service d'API du dépôt Cambridge Collection) | 2026-11-13 (WebFetch, non vérifié brut) | « The API is publicly accessible and (for the most part) requires no authentication, but is designed to be used primarily » ; aucune mention de rate limit, throttling, quota ou politique d'usage. Routes listées : /v1/darwin/, /v1/iiif/, /v1/images/, /v1/metadata/, /v1/xtf/similarity/, /v1/tags/, /v1/transcription/, /v1/translation/, /v1/images/download/. Route IIIF : « The 'iiif' route is not currently in use as the IIIF implementation is still in development. » Route images : « The 'images' route is currently disused. » |
| https://cambridge-collection.github.io/the-solr-stack.html (architecture de recherche CUDL) | 2026-11-13 (WebFetch, non vérifié brut) | « By default, only GET requests (i.e. queries) are publicly available. » Mais le moteur de recherche n'est pas public : « It can only be accessed from within the CDCP subnet by one component: the cudl-search API ». Aucune limite de requêtes mentionnée. |
| https://www.lib.cam.ac.uk (conditions de fourniture d'images, « Image Supply and Reproduction ») | 2026-11-13 (résultat de recherche, non lu en entier) | Concerne les commandes d'images, pas l'accès API. Aucun quota trouvé. |

Conclusion documentaire : aucune limite chiffrée (quota, fenêtre, débit) trouvée dans la documentation consultée. La doc dit que l'API de services est publique, sans authentification « for the most part ».

## 2. Recherche élargie

- Termes cherchés : « Cambridge Digital Library CUDL IIIF API documentation rate limit » ; « cudl.lib.cam.ac.uk iiif manifest terms of use fair use request limits » ; « CUDL IIIF image server host manifest json example » ; « Cambridge Digital Library CUDL developers API search JSON endpoint documentation ».
- Sources examinées : résultats de recherche (non lus en entier), guide iiif.io, dépôt cudl-services (README), page Solr stack, page de conditions CUDL (inaccessible). Exemples de manifestes repérés dans des fixtures tierces (Mirador : `cudl.lib.cam.ac.uk/iiif/MS-ADD-03965`) et un exemple de manifeste `PR-FB-00886-00005-00006` : ce ne sont pas des pages de doc, et elles ne documentent aucun quota.
- Résultat : rien sur un quota ou un rate limit CUDL. Les résultats génériques (429, limites d'autres API : Museum-digital, EBSCO, UCD) ne concernent pas CUDL et ne sont pas retenus. Hôte d'images non identifié dans la doc consultée : on ne le devine pas.

## 3. Tests d'appel (voir `institutions/cudl/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:0x (avant 21:05:53Z, exacte non fournie) | https://cudl.lib.cam.ac.uk/terms | GET via WebFetch (UA non maîtrisé) | 403 | aucun lu | « HTTP 403 Forbidden », corps non récupéré. Page du site, pas un endpoint d'API. | - |
| 2 | 2026-11-13T21:05:53Z | https://cudl.link/v1/metadata/{id} | GET curl, UA honnête | échec DNS (aucune réponse HTTP) | - | - | - |
| 3 | 21:06:47Z | https://cudl.lib.cam.ac.uk/iiif/{id}.json (PR-FB-00886-00005-00006) | GET (sonde probe.py) | 302 | aucun | redirige vers la forme sans `.json` | - (premier appel à l'hôte après le 403 de la requête 1) |
| 4 | 21:06:53Z | https://cudl.lib.cam.ac.uk/iiif/{id}.json (MS-ADD-03965) | GET (sonde) | 302 | aucun | idem | 6 s |
| 5 | 21:07:06Z | https://cudl.lib.cam.ac.uk/iiif/PR-FB-00886-00005-00006 (Location du 302) | HEAD (fonction fetch de probe.py) | 302 | aucun | Location relative : `PR-FB-00886-00005-00006` | 13 s |
| 6 | 21:07:18Z | https://cudl.lib.cam.ac.uk/iiif/PR-FB-00886-00005-00006 | GET (sonde) | 200 | aucun | JSON IIIF (`viewingDirection`, `metadata`…) | 12 s |
| 7 | 21:07:30Z | https://cudl.lib.cam.ac.uk/iiif/MS-ADD-03965 | GET (sonde) | 200 | aucun | JSON IIIF | 12 s |

Non réalisés :
- info.json d'image : aucune URL d'image documentée ; l'identifiant d'image est dans le corps du manifeste, que la sonde ne lit que sur 200 octets. À faire avec une lecture plus large du manifeste, ou en suivant une URL d'image citée dans la doc.
- Métadonnées (route `/v1/metadata/`) : la doc ne donne que `cudl.link`, qui ne se résout pas depuis ce poste ; aucune autre URL documentée, donc non testée.
- Recherche : la doc dit que le moteur de recherche n'est accessible que depuis le sous-réseau interne (cudl-search). Non testé, par conception.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non (aucune limite chiffrée trouvée ; conditions d'utilisation non lues).
- Limite **observée** (429 ou en-tête de quota reçu) : non. Aucune réponse 429 ni en-tête `Retry-After`, `X-RateLimit-*` ou `RateLimit-*` sur les 7 requêtes, dont 5 requêtes sur les manifestes espacées de 6 s ou plus.
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : oui, à la requête n° 1 (GET /terms, via WebFetch). Ce 403 n'est pas une limite de débit. Il ne touche pas les manifestes (200 OK ensuite). Nous ne savons pas quel élément l'a déclenché (UA de WebFetch, règle sur la page). Le 403 n'a pas été reproduit avec notre UA.
- L'API annonce-t-elle ses limites dans la réponse ? non (aucun en-tête de limite sur les réponses 200 ou 302).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : 403 sur la page /terms (requête 1, hors API) ; DNS non résolu pour cudl.link (requête 2).

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la doc de cudl-services dit que l'API est publique et sans authentification « for the most part » ; elle ne mentionne aucune limite. Le moteur de recherche est réservé au réseau interne (page Solr stack). Les routes IIIF et images sont « not currently in use » / « disused » (README cudl-services), alors que les manifestes IIIF répondent en 200.
- Hypothèses (étiquetées comme telles) : hypothèse 1 : pas de politique de quota formalisée, l'équipe comptant sur un usage raisonnable (non vérifié). Hypothèse 2 : le 403 de /terms vient d'une protection de la page web, sans rapport avec un quota (non vérifié).

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen sur l'absence d'en-tête de limite (sur 7 requêtes seulement) ; faible sur la politique réelle (conditions d'utilisation non lues, pas de documentation de quota).
- Ce qui reste à vérifier, et comment :
  1. Lire https://cudl.lib.cam.ac.uk/terms depuis un navigateur ordinaire (hors de cette veille, sans contournement) et noter les phrases sur l'usage automatisé.
  2. Tester l'info.json d'une image (identifiant lu dans le manifeste) et l'hôte d'images, si la doc ou le manifeste les donne.
  3. Demander par écrit à l'équipe CUDL s'il existe une limite de débit pour les manifestes et images IIIF, et si `/v1/metadata/` est accessible hors du réseau de l'université (cudl.link non résolu ici).
  4. Refaire quelques requêtes espacées de 6 s plus tard, pour voir si un en-tête de limite apparaît.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

- a) **non trouvé** — termes cherchés : « Cambridge University Library CUDL API rate limit quota contact » ; « cudl.lib.cam.ac.uk iiif rate limit throttling usage policy » ; dépôt `cambridge-collection/cudl-services` (README lu par WebFetch, 2026-11-13) : aucune route de statut. Pages `https://cudl.lib.cam.ac.uk/terms` et `https://cudl.lib.cam.ac.uk/help` : **403** à la lecture WebFetch (2026-11-13), non relues, non contournées.
- b) **non trouvé** — termes cherchés : RateLimit-Limit, X-RateLimit-*, Retry-After. Le README `cudl-services` ne mentionne aucun en-tête. Sur 7 requêtes (fiche § 3), aucun en-tête de limite reçu.
- c) **non trouvé** pour un accès à quota — cudl-services : « The API is publicly accessible and (for the most part) requires no authentication, but is designed to be used primarily by the CUDL viewer. » ; une route est protégée : « NB: This route is secured by an authentication token so that only the DCP Drupal instance can use it. » (route interne, non utilisable).
- d) **non trouvé** — aucun contact pour quota dans cudl-services ni dans les résultats de recherche. Contact général de la bibliothèque non retenu (non vérifié).

Conclusion : moyen d'interroger le quota : **non**. Aucun endpoint de statut, aucun en-tête, aucune clé, aucun contact documenté. Aucun fichier `scripts/config/cudl-quota.json` écrit.

## Passe méthode v2 complétée (2026-11-13)
- a) /terms et /help : 403 (défi CloudFront), non lues. README cudl-services lu en entier. robots.txt : 403 (non lisible).
- e) Passe v2 : 2 requêtes (manifestes `PR-FB-00886-00005-00006` et `MS-ADD-03965`), 200, aucun en-tête de limite. Les deux sont sans `.json`, comme la passe précédente.
- f) Recherche web : aucune politique de moissonnage trouvée. Un profil d'API tiers mentionne des limites sans chiffre (non vérifié).
- g) Crash test : non lancé, car l'hôte renvoie déjà des 403 anti-bot sur les pages de règles.
