# Europeana — `europeana`

- **Statut** : en cours (tests IIIF faits, 5 requêtes ; API de recherche et Record non testées faute de clé, volontairement ; recherche élargie partielle, sans Wayback)
- **Pays** : Union européenne (fondation Europeana, La Haye)
- **Point d'entrée testé** : `iiif.europeana.eu/presentation/{dataset}/{localId}/manifest` (200, v2.1 par défaut et v3 par en-tête Accept) ; `iiif.europeana.eu/image/.../info.json` (200). Hôte `api.europeana.eu` : non appelé (clé requise).
- **Vérifié le** : 2026-11-13 (tests de 21:05 à 21:06 UTC ; documentation consultée le 2026-11-13)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://europeana.eu/en/rights/terms-of-use (section « Europeana API », lue par résumé WebFetch, non brut) | 2026-11-13 | « Europeana may limit the number of requests the User may send and receive through the Europeana API. » ; « Such a limit shall be reasonable and may be set by Europeana at any time to ensure even performance of the Europeana API to all Users. » ; « API keys are confidential and are for use by the User only » ; « Europeana will log all uses of the Europeana API by the User » |
| https://europeana.atlassian.net/wiki/spaces/EF/pages/2462351393/Accessing+the+APIs (« Accessing the APIs », lu par WebFetch, page tronquée) | 2026-11-13 | « The rate limits for personal keys have been progressively reduced until April 2026 » (la phrase continue, sans chiffre visible) ; « These keys come with significantly higher usage limits, and we can only commit to a defined level of service » (clés projet) ; « Requests from accounts that do not hold, or have not used, a Personal API key will be automatically rejected. » ; « Each user account is limited to one active key » ; « If abuse of an API key is detected, Europeana Foundation may impose additional usage limits » |
| https://europeana.atlassian.net/wiki/spaces/EF/pages/2704146433 (« Fair use policy & guidelines », daté « Updated Sept 05, 2024 », lu par WebFetch, tronqué) | 2026-11-13 | « Europeana may specify a limit per type of request and/or accross all Europeana APIs » ; « Use of the API must be limited to a reasonable number of concurrent requests to an API » ; « In the event that you receive an error response resulting from reaching the limit considered as reasonable, you must reduce the number of concurrent requests to a reasonable limit » ; « The failture to comply with this policy may result in your access key be temporarily blocked or even revoked. » **Aucun chiffre** (requêtes/seconde, minute, jour, quota) dans la partie lue. |
| https://europeana.atlassian.net/wiki/spaces/EF/pages/2462351393 (rubriques « X-Api-Key header (preferred) » et « wskey parameter ») | 2026-11-13 | Corps non visible dans la lecture : rien trouvé sur le paramètre `wskey`, ni sur les 429. La recherche indique que le paramètre `wskey` est déprécié au profit de l'en-tête (source : résumé de recherche, non vérifié brut). |
| https://pro.europeana.eu/page/search (portail développeurs) | 2026-11-13 | **HTTP 403** à la lecture (WebFetch) : corps non récupéré. Non contourné. Ce n'est pas la doc de quotas, mais le portail développeurs n'a pas pu être lu. |

**Pas de chiffre officiel trouvé** pour les clés personnelles ni pour les clés projet.

## 2. Recherche élargie

- Termes cherchés : « Europeana API rate limit quota wskey terms of use » ; « Europeana "fair use policy" API personal key requests per minute » ; « Europeana IIIF presentation manifest iiif.europeana.eu presentation manifest URL example ».
- Sources examinées : pages Atlassian ci-dessus (documentation officielle) ; conditions d'utilisation (officielles) ; un fil du groupe Google « europeanaapi » (dnjJBzWaQQU), forum non officiel, rédigé par le personnel selon le résumé ; une page « how to register for and manage an api key » sur europeana.eu (non lue).
- Résultat : **un seul chiffre trouvé, dans un message de forum** : « the current set rate limit for external requests is set at a maximum of 120 requests per 10 seconds » (soit 720/min si cela s'applique). Date du message et portée (clés personnelles ou projet) **non établies** : non documenté, à ne pas citer comme limite officielle. Le mot « 429 » apparaît dans un résumé de recherche (« A 429 response means your application has hit its usage limit ») sans source primaire lue : non vérifié.
- Non examiné : Wayback (`ia_find_snapshots`), GitHub (dépôts Europeana), billet « api.europeana.eu » pour les en-têtes.

## 3. Tests d'appel (voir `institutions/europeana/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:05:45 | `iiif.europeana.eu/presentation/9200396/BibliographicResource_…/manifest` (v2.1) | GET | 200 | aucun | JSON Presentation 2 ; 136 587 o ; 80 canvases | — |
| 2 | 21:05:59 | `iiif.europeana.eu/image/…/00001/info.json` | GET | 200 | aucun | JSON Image 2 ; 998 o | ~14 s |
| 3 | 21:06:10 | même manifeste, Accept v3 | GET | 200 | aucun | JSON-LD Presentation 3 ; 187 872 o | ~11 s |
| 4 | 21:06:17 | même manifeste | HEAD | 200 | aucun | — | ~7 s |
| 5 | 21:06:25 | même manifeste (répétition) | GET | 200 | aucun | identique au n°1 | ~8 s |
| — | — | `api.europeana.eu` (recherche, Record) | — | non appelé | — | clé requise : pas de requête sans clé | — |

Aucun 429, aucun 403, aucun en-tête `Retry-After`, `X-RateLimit-*` ou `RateLimit-*` sur les 5 réponses. Pauses ≥ 7 s entre requêtes. Budget : 5 requêtes sur 15.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : **oui, en principe** : « Europeana may limit the number of requests… » (conditions d'utilisation) et « The rate limits for personal keys have been progressively reduced until April 2026 » (Accessing the APIs). **Chiffres : non** trouvés dans la doc officielle.
- Limite **observée** (429 ou en-tête de quota reçu) : **non** (sur iiif.europeana.eu, 5 requêtes, pas de rafale).
- Accès refusé à ce client (403 anti-bot) : **non** sur iiif.europeana.eu. **Oui** sur le portail `pro.europeana.eu` (403 à la lecture WebFetch, requête documentaire, non API).
- L'API annonce-t-elle ses limites dans la réponse ? **non** (aucun en-tête de limite sur les réponses IIIF). Les endpoints de recherche, non testés, pourraient différer.
- Mécanisme observé : rien (pas de limitation observée sur les endpoints IIIF).
- Valeurs trouvées (quota, fenêtre) : **aucune officielle**. Un chiffre de forum (120 req / 10 s, date et portée inconnues) : non documenté, non vérifié.
- Blocages rencontrés : 403 sur `pro.europeana.eu` (portail développeurs, lecture de doc). Clé non demandée (consigne). Rien d'autre.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : Europeana publie une politique (« fair and reasonable use », « reasonable number of concurrent requests », « may specify a limit per type of request ») et des clés obligatoires pour l'API de recherche et Record ; les clés personnelles ont des limites réduites « progressively … until April 2026 ». Les chiffres ne sont donnés nulle part dans les pages lues (sauf le message de forum non daté). La doc renvoie à api@europeana.eu pour les usages dépassant les limites.
- Hypothèses (étiquetées comme telles) :
  - Hypothèse : les limites sont volontairement non chiffrées publiquement pour pouvoir être ajustées « at any time », d'où la formule « reasonable ».
  - Hypothèse : les endpoints IIIF (iiif.europeana.eu) ne sont pas soumis à la clé ni aux mêmes quotas que l'API de recherche ; à confirmer.

## 6. Confiance et pistes restantes

- Niveau de confiance : **moyen** sur ce qui est dit (citations lues en partie, pages tronquées) ; **faible** sur l'absence de chiffres (la page « Fair use policy » et le détail de « Accessing the APIs » n'ont pas été lus en entier).
- Ce qui reste à vérifier, et comment :
  - Lire en entier la page « Fair use policy & guidelines » et « Accessing the APIs » (navigateur de l'utilisateur, car `pro.europeana.eu` a répondu 403 à notre client).
  - Demander à api@europeana.eu : quotas actuels des clés personnelles et projet, et si les endpoints IIIF sont inclus dans la politique.
  - Vérifier la date et la portée du chiffre « 120 req / 10 s » (fil Google Groups dnjJBzWaQQU).
  - Tester l'API de recherche avec une clé de l'utilisateur, si l'utilisateur la fournit lui-même (non fait ici) : en-têtes `X-Api-Key`, éventuels 429.
  - Refaire le test IIIF plus tard, à rythme lent, pour un historique.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

- a) **non trouvé** — termes cherchés : « Europeana API rate limit status endpoint » ; « Europeana API usage quota endpoint » ; pages Confluence « Accessing the APIs » (`https://europeana.atlassian.net/wiki/spaces/EF/pages/2462351393/Accessing+the+APIs`) et « Fair use policy & guidelines » (`.../pages/2704146433`), lues par WebFetch le 2026-11-13 : aucun endpoint d'usage ni de statut de clé cité (« Europeana API » seulement pour la recherche, clé requise, non appelée). `pro.europeana.eu` : 403 (non relu).
- b) **non trouvé** — termes cherchés : X-RateLimit-*, RateLimit-*, Retry-After, 429. Aucune de ces en-têtes dans les pages Europeana lues. Lecture WebFetch de la page « Fair use policy » : « Number-with-unit sentences: None found. Response header names: None found. 429 response descriptions: None found. » Les seules mentions 429 viennent de sites tiers (résultats de recherche, non vérifiés). Sur iiif.europeana.eu, aucun en-tête de limite (fiche § 3).
- c) **trouvé** — source : `https://europeana.atlassian.net/wiki/spaces/EF/pages/2462351393/Accessing+the+APIs` (WebFetch, 2026-11-13) : « Requests from accounts that do not hold, or have not used, a Personal API key will be automatically rejected. » ; « These keys come with significantly higher usage limits, and we can only commit to a defined level of service » (clés projet) ; « Each user account is limited to one active key ». Le même service précise « Its usage limits are generous enough to support most testing and discovery use cases. » sans chiffre. Clé en-tête : `X-Api-Key` (page `.../pages/2358673409`, lue : « this approach is being deprecated in favor of passing the API key through HTTP headers »). Clé non demandée (consigne).
- d) **trouvé** — source : page « Fair use policy & guidelines » (`https://europeana.atlassian.net/wiki/spaces/EF/pages/2704146433`, « Updated Sept 05, 2024 », WebFetch 2026-11-13) : « please get in contact with the Europeana API's customer support at api@europeana.eu ». Même adresse citée dans les conditions (fiche § 1).

Conclusion : moyen d'interroger le quota : **non**. Il existe un moyen de demander une clé personnelle (c) et un contact (d) ; aucun endpoint ni en-tête ne permet de lire le quota. Le chiffre « 120 requêtes / 10 s » (forum, fiche § 2) reste non vérifié. Aucun fichier `scripts/config/europeana-quota.json` écrit.
