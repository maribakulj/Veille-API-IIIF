# Smithsonian Institution (Open Access) — `smithsonian`

- **Statut** : vérifiée partiellement (doc et recherche faites ; point d'entrée api.si.edu non testé, clé requise ; un endpoint public testé sans clé)
- **Pays** : États-Unis
- **Point d'entrée testé** : `https://smithsonian-open-access.s3-us-west-2.amazonaws.com/metadata/edan/index.txt` (index public des métadonnées, S3). Point d'entrée API `https://api.si.edu/openaccess/api/v1.0/` : documenté, **non testé** (clé api.data.gov exigée, on ne la demande pas).
- **Vérifié le** : 2026-11-13 (sonde à 21:07:55 UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://edan.si.edu/openaccess/apidocs/ (doc de l'API, citée par des tiers) | 2026-11-13, WebFetch : page « Loading... » seulement | rien lu (page non rendue). Aucune mention de quota vérifiée. |
| https://edan.si.edu/openaccess/docs/ (schéma des métadonnées) | 2026-11-13, WebFetch | « The API is open and all that we require is that you get a key at » ; lien d'inscription https://edan.si.edu/openaccess/signup/form. **Aucune** limite de débit, quota ni « requests per hour » mentionné. Pas d'URL d'endpoint. |
| https://www.si.edu/openaccess/devtools (page développeurs) | 2026-11-13, WebFetch : **HTTP 403** (non lue) | rien lu. Un résumé de recherche indique que la page renvoie vers api.data.gov et le dépôt GitHub (non vérifié). |
| https://www.si.edu/openaccess (page programme) | 2026-11-13, WebFetch : **HTTP 403** (non lue) | rien lu. |
| https://github.com/Smithsonian/OpenAccess (dépôt) | 2026-11-13, WebFetch | pas de mention de clé, quota ou débit. Le dépôt est **archivé** (« archived by the owner on May 21, 2026. It is now read-only. »). Donne l'index S3 des métadonnées : `https://smithsonian-open-access.s3-us-west-2.amazonaws.com/metadata/edan/index.txt`. Données « refreshed at a weekly rate » (page devtools, via résumé). |
| https://registry.opendata.aws/smithsonian-open-access/ (registre AWS Open Data) | 2026-11-13, citée par le dépôt GitHub, non consultée directement | non lue. |
| https://api.data.gov/docs/developer-manual/ (plateforme d'hébergement de la clé) | 2026-11-13, WebFetch | « Hourly Limit: 1,000 requests per hour » (défaut de la plateforme, « Rate limits may vary by service, but the defaults are: »). Clé `DEMO_KEY` : 50 requêtes/IP/jour. Pas de date sur la page. **Ce n'est pas une doc Smithsonian** : il s'agit de la valeur par défaut d'api.data.gov. Rien n'indique que le Smithsonian l'applique. |

Pour la demande : la doc Smithsonian (edan.si.edu) dit seulement que l'API est ouverte moyennant une clé. Le chiffre « 1000 requêtes par heure » provient de la doc générale d'api.data.gov, non de la doc Smithsonian.

## 2. Recherche élargie

- Termes cherchés : « Smithsonian Open Access API documentation api.si.edu rate limit 1000 requests per hour » ; « Smithsonian Open Access GitHub repository API v1.0 search content endpoints api key api.data.gov ».
- Sources examinées : résultats de recherche (sites tiers : glama.ai MCP, apis.io, si-openaccess PyPI, notebook nbviewer) ; doc officielle via WebFetch (ci-dessus).
- Résultat : **aucune limite chiffrée Smithsonian trouvée**. Les wrappers tiers indiquent que « without an API key, rate limits will be lower » (commentaire de code, non officiel) et qu'un 429 est renvoyé en cas de dépassement (non vérifié, non observé). Endpoints tiers (non officiels, non vérifiés) : `https://api.si.edu/openaccess/api/v1.0/search` avec paramètre `api_key`, `category_search`, `stats`. Aucun n'a été testé.

## 3. Tests d'appel (voir `institutions/smithsonian/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 2026-11-13T21:07:55Z | https://smithsonian-open-access.s3-us-west-2.amazonaws.com/metadata/edan/index.txt | GET (probe.py) | 200 OK | aucun en-tête de limite | liste d'URL d'index S3 (`.../metadata/edan/aaa/index.txt`, ...) | - |

Non testés, volontairement :
- `https://api.si.edu/openaccess/api/v1.0/search` (et autres routes de l'API) : clé api.data.gov requise selon la doc Smithsonian. Aucune clé utilisée, aucune demandée. Sans clé, un refus serait une erreur d'authentification, pas un 403 anti-bot : elle ne serait pas interprétable comme la sonde le ferait.
- Pages `si.edu/openaccess*` : 403 reçu via WebFetch (outil de recherche documentaire, non compté dans le budget de la sonde). Non relues.

Budget : 1 requête sur 15 utilisée.

## 4. Conclusion sur les limites

- Limite **documentée par le Smithsonian** (citation et URL) : non. La doc EDAN dit « The API is open and all that we require is that you get a key » (https://edan.si.edu/openaccess/docs/), sans chiffre.
- Limite documentée par la plateforme de clé (api.data.gov, non Smithsonian) : oui, « Hourly Limit: 1,000 requests per hour » (https://api.data.gov/docs/developer-manual/). Application au Smithsonian : **non vérifiée**.
- Limite **observée** (429 ou en-tête de quota reçu) : non. Aucun appel à l'API elle-même.
- Accès refusé à ce client (403 anti-bot) : non, sur la sonde (requête n° 1 : 200). Les 403 de pages si.edu cités ci-dessus viennent de WebFetch et ne sont pas une mesure de notre client.
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucun appel à l'API).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : « 1,000 requests per hour » (api.data.gov, défaut générique) ; rien de spécifique au Smithsonian.
- Blocages rencontrés : 403 sur deux pages si.edu via WebFetch ; page apidocs non rendue.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la doc Smithsonian parle d'une clé sans chiffre. Le dépôt GitHub est archivé en lecture seule depuis le 21/05/2026. L'index S3 des métadonnées est accessible sans clé.
- Hypothèses (étiquetées comme telles) : hypothèse 1 : la limite réelle est celle d'api.data.gov (1 000 req/h) appliquée à chaque clé (non vérifié). Hypothèse 2 : la doc chiffrée est sur la page `apidocs` rendue par JavaScript, que nous n'avons pas pu lire (non vérifié).

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Méthode : termes en anglais, WebSearch (mode extended), WebFetch sur la doc EDAN, la doc api.data.gov et le dépôt GitHub. **Aucune requête vers api.si.edu** : l'API exige une clé, et on ne la demande pas.

- a) Endpoint de statut de quota : **non trouvé** côté Smithsonian — termes cherchés : « rate limit », « rate limit status », « usage », « quota » (edan.si.edu/openaccess/apidocs/ : page « Loading... », aucun texte lisible ; github.com/Smithsonian/OpenAccess : archivé le 21/05/2026, aucune mention de quota ; github.com/Smithsonian/smithsonian-openaccess : aucune mention de quota). Côté api.data.gov : pas d'endpoint de statut dans la doc (https://api.data.gov/docs/developer-manual/, lue le 2026-11-13).
- b) En-têtes de limite documentés : **oui, mais côté plateforme** — doc api.data.gov (https://api.data.gov/docs/developer-manual/, lue le 2026-11-13) : « inspecting the `X-RateLimit-Limit` and `X-RateLimit-Remaining` HTTP headers » ; « you will receive a response with an HTTP status code of 429 (Too Many Requests). ». La doc ne cite pas de Retry-After (« The page does not mention a `Retry-After` header » : constat de notre lecture). Le Smithsonian ne documente pas lui-même d'en-tête.
- c) Clé ou compte donnant un quota : **oui** — inscription https://api.data.gov/signup/ (citée par le dépôt smithsonian-openaccess, lu le 2026-11-13 : « The API requires you to provide your own 'api_key' value. » / « Please register with https://api.data.gov/signup/ to get a key. »). Quota de la plateforme (non propre au Smithsonian) : « Hourly Limit: 1,000 requests per hour » par clé ; DEMO_KEY : « Hourly Limit: 30 requests per IP address per hour » et « Daily Limit: 50 requests per IP address per day » (api.data.gov, 2026-11-13). Application au Smithsonian : **non vérifiée**. Clé non demandée, non utilisée.
- d) Contact officiel pour un quota : **partiel** — api.data.gov : « If you need higher rate limits, please contact the API owner at the agency that offers the service you're trying to query » (2026-11-13). Adresse Smithsonian non trouvée : termes cherchés « OpenAccess@si.edu », « Smithsonian Open Access contact » ; aucune adresse lue. Un contact « Smithsonian Open Access Team » est cité par un annuaire tiers, sans courriel.

Conclusion : moyen d'interroger le quota : **oui, sous conditions** — les en-têtes X-RateLimit-Limit / X-RateLimit-Remaining et le 429 sont documentés par api.data.gov pour une clé valide. Non testé : aucun appel avec clé. Sans clé, pas de moyen de lire le quota. Aucun fichier `scripts/config/smithsonian-quota.json` écrit, la sonde n'étant pas autorisée sans clé. Décision à prendre par Marcel avant tout test avec une clé du projet.

## 6. Confiance et pistes restantes

- Niveau de confiance : faible (aucune réponse de l'API elle-même ; doc Smithsonian sans chiffre).
- Ce qui reste à vérifier, et comment :
  1. Lire https://edan.si.edu/openaccess/apidocs/ dans un navigateur ordinaire et noter toute phrase sur les limites.
  2. Lire https://www.si.edu/openaccess/devtools et https://www.si.edu/openaccess depuis un navigateur (403 via WebFetch).
  3. Si le projet a une clé api.data.gov légitime (compte du projet, à décider par Marcel), tester une seule requête `search` et lire les en-têtes `X-RateLimit-*` ; ne rien faire sans cette décision.
  4. Demander par écrit au Smithsonian Open Access (contact sur si.edu/openaccess) la limite applicable aux clés.
