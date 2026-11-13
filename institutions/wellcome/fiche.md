# Wellcome Collection — `wellcome`

- **Statut** : vérifiée
- **Pays** : Royaume-Uni
- **Point d'entrée testé** : `https://api.wellcomecollection.org/catalogue/v2/works?pageSize=1`, `https://iiif.wellcomecollection.org/presentation/v3/b18035723`, `https://iiif.wellcomecollection.org/thumbs/b18035723_0004.JP2/info.json`
- **Vérifié le** : 2026-11-13 (UTC, à partir de 20:33)
- **Vérifié par** : agent de veille (Haiku 5.5), session orchestrée

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://developers.wellcomecollection.org/ | 2026-11-13 | Rien trouvé : aucune phrase sur rate limit, fair use, clé d'API, quota ou usage policy. Sections listées : Catalogue API, IIIF APIs, Content. |
| https://developers.wellcomecollection.org/docs/catalogue | 2026-11-13 | Rien sur les limites. Citation : « There's no sign up or authentication required » (accès). Citation : « if you require a full harvest of the catalogue, you should use the daily snapshot instead of the API » (recommandation de moissonnage complet). |
| https://developers.wellcomecollection.org/docs/iiif | 2026-11-13 | Rien sur les limites. Citation : « There's no sign up or authentication required, but you might want to browse the documentation » ; « We license our images as openly as possible and ask you to please respect the licences on individual images. » |
| https://developers.wellcomecollection.org/docs/terms | 2026-11-13 | Page absente (HTTP 404). |
| https://docs.wellcomecollection.org/catalogue-api/ et `.../catalogue-api/llms.txt` | 2026-11-13 | Page de navigation, rien sur les limites ; pas d'exemple de requête works ni de manifeste. |
| https://docs.wellcomecollection.org/request-for-comments-rfcs/012-api_architecture (RFC 012, architecture API) | 2026-11-13 | Citation : « Some API endpoints require authentication, while others are public and would benefit from rate limiting. » ; « The `storage` API requires authentication, the catalogue API does not. » Aucun chiffre. |
| https://github.com/wellcomecollection/catalogue-api (README) | 2026-11-13 | Rien sur les limites. Citation : « Both are freely accessible over HTTP, with no authentication or sign-up required. » |

## 2. Recherche élargie

- Termes cherchés : « Wellcome Collection API developers rate limit fair use API key » ; « wellcome collection catalogue API "rate limit" OR "fair use" github wellcomecollection » ; « iiif.wellcomecollection.org presentation v3 manifest b example ».
- Sources examinées : résultats de recherche web ; RFC 012 ; note de version Wellcome de février 2025 (docs.wellcomecollection.org/fortnotes/20250205) ; pages de développeurs ci-dessus ; dépôt GitHub `catalogue-api`.
- Résultat : aucune limite chiffrée ni politique d'usage API trouvée. Une note de version (février 2025) mentionne un projet de rate limiting des requêtes de bots, mais elle concerne le site wellcomecollection.org, pas l'API (lecture par résumé du résultat de recherche, non vérifiée en intégralité). Les deux pages « fair use » trouvées par la recherche (nationalarchives.gov.uk) concernent un autre organisme (The National Archives) et ne s'appliquent pas à Wellcome.
- Wayback (`ia_find_snapshots`) : non consulté (non nécessaire, rien d'annoncé à historiser).

## 3. Tests d'appel (voir `institutions/wellcome/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 20:33:34 | `api.wellcomecollection.org/catalogue/v2/works?pageSize=1` | GET | 200 | aucun (`content-type: application/json`, CloudFront, `access-control-allow-origin: *`) | JSON `ResultList`, `pageSize: 1`, `totalResults: 1141704` | - |
| 2 | 20:33:42 | `iiif.wellcomecollection.org/presentation/v3/b18035723` | GET | 200 | aucun (`application/ld+json`, serveur Kestrel) | manifeste IIIF v3, environ 107 Ko | 6 s |
| 3 | 20:34:04 | `iiif.wellcomecollection.org/image/v2/b18035723_0004.JP2/info.json` | GET | 400 | aucun | corps vide (chemin « image/v2 » deviné, hors doc : erreur, non reproduit) | 6 s |
| 4 | 20:34:19 | `iiif.wellcomecollection.org/thumbs/b18035723_0004.JP2/info.json` | GET | 200 | aucun (`cache-control: public, max-age=60`) | info.json IIIF Image 2.0 (`@id` = `.../image/b18035723_0004.JP2`) | 6 s |

- Identifiant `b18035723` : trouvé hors de la doc officielle (exemple dans des fixtures Mirador / gist tiers, puis confirmé par l'API : statut 200). La doc Wellcome elle-même ne donne pas d'exemple de b-number.
- URL de l'info.json : déduite du `service` du manifeste (`@id` = `.../thumbs/b18035723_0004.JP2`), pas d'une doc publique.
- Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*` sur les 4 réponses. Aucune erreur 429/503/403. Total : 4 requêtes GET sur un budget de 15 (dont une au chemin deviné de la ligne 3, réponse 400).
- Pauses : 6 s entre deux requêtes vers les hôtes Wellcome (≥ 5 s respecté).

## 4. Conclusion sur les limites

- L'API annonce-t-elle ses limites dans la réponse ? **non** (aucun en-tête de quota sur 4 réponses).
- Mécanisme observé (429 + Retry-After, en-têtes X-RateLimit, rien) : rien observé ; aucun blocage.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : aucun blocage. Un 400 sur un chemin IIIF deviné (test 3) ; un script a échoué une fois sur une variable vide (requête inutile, retirée du log puis consignée en note).

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : RFC 012 : les endpoints publics « would benefit from rate limiting » (intention, sans chiffre) ; doc catalogue : pas d'inscription ni d'authentification ; pour un moissonnage complet, « use the daily snapshot instead of the API ».
- Hypothèses (étiquetées comme telles) :
  - Hypothèse : Wellcome ne publie pas de quota car la doc de l'API est en réalité peu formalisée (API publique sans clé, usage « raisonnable » implicite). Non vérifiable depuis les sources.
  - Hypothèse : le rate limiting évoqué dans la RFC (et la note de février 2025 sur les bots) est mis en place au niveau de la passerelle/CDN (CloudFront observé) sans être documenté. Non vérifiable.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

- a) Endpoint de statut de quota : non trouvé. Termes : « Wellcome Collection API rate limit », « Wellcome catalogue API rate limit status ». Les pages https://developers.wellcomecollection.org/ et https://docs.wellcomecollection.org/catalogue-api/ ne décrivent aucun endpoint de statut (§ 1).
- b) En-têtes de limite : non trouvé. Termes : « wellcomecollection 429 github issues rate limiting ». Aucune issue GitHub trouvée. Aucun en-tête de limite documenté ni observé (§ 4).
- c) Clé d'API ou compte donnant un quota : non trouvé, et absence de clé confirmée. Citation : « There's no sign up or authentication required » (https://developers.wellcomecollection.org/docs/catalogue et /docs/iiif, consultées le 2026-11-13). La RFC 012 (https://docs.wellcomecollection.org/request-for-comments-rfcs/012-api_architecture, 2019) dit que les endpoints publics « would benefit from rate limiting », sans chiffre ni clé.
- d) Contact officiel pour un quota : non trouvé. Termes : « Wellcome Collection API rate limit quota contact developers request higher limit ». Aucun contact ou formulaire de quota. La page https://developers.wellcomecollection.org/docs/terms répond 404 (§ 1).

Conclusion : moyen d'interroger le quota : non. Aucune sonde lancée : aucun endpoint de statut ni en-tête documenté trouvé.

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen (doc lue en entier pour les pages principales ; limites non documentées ; quatre réponses sans en-tête de quota).
- Ce qui reste à vérifier, et comment : demander à l'équipe Wellcome (GitHub `wellcomecollection`, issues) s'il existe une politique de débit pour l'API Catalogue ; relire `docs/requesting_flow.md` et `docs/developers.md` du dépôt `catalogue-api` (listés mais non lus) ; refaire un test de rafale espacé plus tard si le projet le décide.
