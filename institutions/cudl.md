# Cambridge University Library (CUDL) — `cudl`

- **Statut** : en cours (tests bloqués : 403 anti-bot sur l'hôte principal, cudl.link non résolu ; doc et recherche faites, détail dans `tests/cudl.log`)
- **Pays** : Royaume-Uni
- **Point d'entrée testé** : `https://cudl.lib.cam.ac.uk/iiif/` (supposé, non testé en direct : requête n°1 sur `/terms` reçue en 403). `https://cudl.link/v1/metadata/MS-ADD-03958` (route de services documentée dans le dépôt cudl-services) : échec DNS, aucune réponse HTTP.
- **Vérifié le** : 2026-11-13 (tests vers 21:05 UTC ; documentation consultée entre 21:0x et 21:1x UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://cudl.lib.cam.ac.uk/terms (conditions d'utilisation du site) | 2026-11-13 — **non lue** : 403 via WebFetch | rien lu. Aucune mention de quota vérifiée. À relire depuis un navigateur. |
| https://iiif.io/guides/guides/cudl.lib.cam.ac.uk/ (guide IIIF communautaire) | 2026-11-13 (WebFetch, résumé par un petit modèle, non vérifié brut) | Aucune phrase sur quota, limite, accès en masse ou restriction d'usage. Seule consigne : « When copying&pasting the Manifest URL, manually add the “.json” file extension before pasting into desired use location. » |
| https://raw.githubusercontent.com/cambridge-collection/cudl-services/master/README.md (doc officielle du service d'API du dépôt Cambridge Collection) | 2026-11-13 (WebFetch, non vérifié brut) | « The API is publicly accessible and (for the most part) requires no authentication, but is designed to be used primarily » ; aucune mention de rate limit, throttling, quota ou politique d'usage. Routes listées : /v1/darwin/, /v1/iiif/, /v1/images/, /v1/metadata/, /v1/xtf/similarity/, /v1/tags/, /v1/transcription/, /v1/translation/, /v1/images/download/. Route IIIF : « The 'iiif' route is not currently in use as the IIIF implementation is still in development. » Route images : « The 'images' route is currently disused. » |
| https://cambridge-collection.github.io/the-solr-stack.html (architecture de recherche CUDL) | 2026-11-13 (WebFetch, non vérifié brut) | « By default, only GET requests (i.e. queries) are publicly available. » Le moteur de recherche n'est pas public : « It can only be accessed from within the CDCP subnet by one component: the cudl-search API ». Aucune limite de requêtes mentionnée. |
| https://www.lib.cam.ac.uk (conditions de fourniture d'images, « Image Supply and Reproduction ») | 2026-11-13 (WebFetch-résultat de recherche, non lu en entier) | Concerne les commandes d'images, pas l'accès API. Aucun quota trouvé. |

Conclusion documentaire : aucune limite chiffrée (quota, fenêtre, débit) trouvée dans la documentation consultée. La doc dit que l'API de services est publique, sans authentification « for the most part ».

## 2. Recherche élargie

- Termes cherchés : « Cambridge Digital Library CUDL IIIF API documentation rate limit » ; « cudl.lib.cam.ac.uk iiif manifest terms of use fair use request limits » ; « CUDL IIIF image server host manifest json example » ; « Cambridge Digital Library CUDL developers API search JSON endpoint documentation ».
- Sources examinées : résultats de recherche (non lus en entier), guide iiif.io, dépôt cudl-services (README), page Solr stack, page de conditions CUDL (inaccessible). Exemples de manifestes repérés dans des fixtures tierces (Mirador, `cudl.lib.cam.ac.uk/iiif/MS-ADD-03965`, `cudl.lib.cam.ac.uk/iiif/PR-FB-00886-00005-00006`) : cela ne documente aucun quota.
- Résultat : rien sur un quota ou un rate limit CUDL. Les résultats génériques (429, limites d'autres API : Museum-digital, EBSCO, UCD) ne concernent pas CUDL et ne sont pas retenus. Hôte d'images non identifié dans la doc consultée : on ne le devine pas.

## 3. Tests d'appel (voir `tests/cudl.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:0x (avant 21:05:53Z, exacte non fournie) | https://cudl.lib.cam.ac.uk/terms | GET via WebFetch (UA non maîtrisé) | 403 | aucun lu | « HTTP 403 Forbidden », corps non récupéré | - |
| 2 | 2026-11-13T21:05:53Z | https://cudl.link/v1/metadata/{id} | GET curl, UA honnête | échec DNS (aucune réponse HTTP) | - | - | - |

Non réalisés (arrêt sur 403 pour l'hôte cudl.lib.cam.ac.uk) : `https://cudl.lib.cam.ac.uk/iiif/` (point d'entrée supposé), manifeste d'exemple `PR-FB-00886-00005-00006`, info.json d'image, requête de recherche (non publique selon la doc).

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non (aucune limite chiffrée trouvée ; conditions d'utilisation non lues).
- Limite **observée** (429 ou en-tête de quota reçu) : non.
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : oui, à la requête n° 1 (GET /terms, via WebFetch). Ce 403 n'est pas une limite de débit. Nous ne savons pas quel élément a déclenché le refus (UA de WebFetch, IP, ou règle sur l'hôte) : l'outil ne permet pas de le régler.
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucune réponse exploitable de l'hôte).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : 403 anti-bot sur cudl.lib.cam.ac.uk (requête n°1) ; DNS non résolu pour cudl.link (requête n°2).

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la doc de cudl-services dit que l'API est publique et sans authentification « for the most part » ; elle ne mentionne aucune limite. Le moteur de recherche est réservé au réseau interne (page Solr stack). Les routes IIIF et images sont « not currently in use » / « disused » (README cudl-services).
- Hypothèses (étiquetées comme telles) : hypothèse 1 : pas de politique de quota formalisée, l'équipe comptant sur un usage raisonnable (non vérifié). Hypothèse 2 : le 403 vient d'une protection anti-bot de l'hôte web, indépendante d'un quota (non vérifié, car nous n'avons pas pu tester avec notre UA).

## 6. Confiance et pistes restantes

- Niveau de confiance : faible (aucune réponse HTTP de l'institution exploitable ; conditions d'utilisation non lues).
- Ce qui reste à vérifier, et comment :
  1. Lire https://cudl.lib.cam.ac.uk/terms depuis un navigateur ordinaire (hors de cette veille, sans contournement) et noter les phrases sur l'usage automatisé.
  2. Demander par écrit à l'équipe CUDL (Cambridge University Library) s'il existe une limite de débit pour les manifestes et images IIIF, et l'hôte d'images.
  3. Refaire un test de 2 requêtes espacées de 6 s sur le manifeste, plus tard, si le 403 disparaît ; ne pas insister si le 403 revient.
  4. Vérifier si cudl.link ou un autre nom d'hôte de services est résolu depuis un autre réseau (à noter, sans supposer l'URL).
