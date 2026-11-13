# Nasjonalbiblioteket (Bibliothèque nationale de Norvège) — `nb-no`

- **Statut** : en cours (tests faits sur les manifestes et la page Swagger ; spécification OpenAPI et conditions d'utilisation non trouvées)
- **Pays** : Norvège
- **Point d'entrée testé** : `https://api.nb.no/catalog/v1/iiif/<id>/manifest` (manifestes IIIF Presentation 2) ; racine `https://api.nb.no/` (page Swagger UI) ; `https://api.nb.no/catalog/v1/oembed` (oEmbed, voir section 3)
- **Vérifié le** : 2026-11-13 (UTC, tests 21:07:58Z à 21:08:41Z)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://api.nb.no/ (Swagger UI, « static distribution bundle ») | 2026-11-13 (GET par la sonde, 200 ; lu par WebFetch : page sans texte utile, pas de spec récupérée) | Aucune limite annoncée dans la page. La spécification OpenAPI n'a pas pu être lue (lien non extrait). |
| https://www.nb.no/dh-lab/ et https://www.nb.no/dh-lab/digital-tekstanalyse/ (page DH-lab, redirigée depuis dh.nb.no) | 2026-11-13 (WebFetch, résumé par un petit modèle) | « aucune mention » de quota, limite de requêtes, rate limit ni conditions d'usage. Renvoie vers des applications web (ngram, korpus, bildesøk) et vers un « dhlab pythonpakke og vårt API » sans lister les URL. Aucune date visible. |
| https://oembed.org/providers/nasjonalbiblioteket | 2026-11-13 (WebFetch) | Déclare l'endpoint `https://api.nb.no/catalog/v1/oembed`, format « json » uniquement. Aucune limite. |
| Manifeste IIIF d'exemple, `https://api.nb.no/catalog/v1/iiif/c71eaa93d415c69059ec145899794b4e/manifest` | 2026-11-13 (WebFetch, résumé) | Champ de licence `https://www.nb.no/lisens/#beskyttet-av-opphavsrett` (« Dette materialet er beskyttet av opphavsrett »). Aucune limite. |
| https://www.nb.no/content/uploads/2024/10/Reglement.pdf | 2026-11-13 (WebFetch) | PDF illisible par l'outil (texte compressé). Le titre (« Reglement », prêt) ne concerne pas l'API. Non lu : pas de conclusion. |

Rien trouvé dans la doc officielle sur un quota, une fenêtre de débit ou des conditions d'usage automatisé pour `api.nb.no`.

## 2. Recherche élargie

- Termes cherchés : « Nasjonalbiblioteket API IIIF manifest api.nb.no catalog v1 iiif documentation » ; « api.nb.no rate limit quota terms of use National Library of Norway API » ; « github NationalLibraryOfNorway api.nb.no iiif manifest documentation » ; « nb.no API dokumentasjon utviklere katalog IIIF "api.nb.no" bruksvilkår begrensning ».
- Sources examinées : page `dhlab` (PyPI, documentation de la bibliothèque Python `dhlab` et son `nb_search_api`, tierce) ; dépôt tiers `NB_API_Python` ; plugins tiers (Sanity `nbiiif`) ; cours universitaire (manifestes d'exemple) ; page de service Digitalt bevaringsarkiv (`digitalpreservation.no`, authentification OAuth pour dépôt, autre usage) ; `data.norge.no` (AI Search API : limite de 10 requêtes/min, mais c'est un autre service, non retenu).
- Résultat : aucune limite publiée pour `api.nb.no`. Les sources tierces (dhlab) décrivent des endpoints (manifestes, recherche) sans limite. Aucune source GitHub officielle de la bibliothèque trouvée. Le lien GitHub `NationalLibraryOfNorway` n'a pas été confirmé.

## 3. Tests d'appel (voir `institutions/nb-no/tests/journal.log`, en-têtes complets dans `institutions/nb-no/tests/raw/`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:07:58 | https://api.nb.no/ | GET | 200 | aucun | page HTML Swagger UI | - |
| 2 | 21:08:09 | https://api.nb.no/catalog/v1/iiif/c71eaa93…/manifest | GET | 200 | aucun | JSON IIIF, contexte Presentation 2 | 11 s |
| 3 | 21:08:19 | https://api.nb.no/catalog/v1/iiif/ea3d85be…/manifest | GET | 200 | aucun | JSON IIIF, contexte Presentation 2 | 10 s |
| 4 | 21:08:31 | https://api.nb.no/catalog/v1/iiif/3ac5be14…/manifest | GET | 200 | aucun | JSON IIIF, contexte Presentation 2 | 12 s |
| 5 | 21:08:41 | https://api.nb.no/catalog/v1/oembed?url=https://www.nb.no/items/c71eaa93… | GET | 404 | aucun | `{"detail":"No static resource catalog/v1/oembed.", ... "title":"Not Found"}` (problem+json) | 10 s |

Aucun 403, aucun 429, aucun CAPTCHA, aucune connexion coupée. 5 requêtes sur un budget de 15. Pas de test répété en rafale.

Non réalisés : URL d'image (info.json) : aucun service d'image identifié (voir section 6). Recherche par texte : aucun endpoint de recherche documenté dans les sources lues ; les endpoints `dhlab` (`api.nb.no/dhlab`, `api.nb.no/ngram/collocation`) sont tiers et non testés.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non (aucune limite trouvée dans les sources lues).
- Limite **observée** (429 ou en-tête de quota reçu) : non (aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*` sur les 5 réponses).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : non.
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucun en-tête de limite).
- Mécanisme observé (429 + Retry-After, en-têtes X-RateLimit, rien) : rien.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : aucun. Le 404 sur oEmbed est une réponse « ressource absente », pas un blocage.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : l'API est publique sans authentification pour les manifestes (200 sans en-tête d'auth, sans cookie demandé hors `_nblb` de session posé par le serveur). Les manifestes déclarent une licence « protégé par le droit d'auteur » : un usage de réutilisation doit tenir compte de cette licence (sources : manifestes d'exemple, section 1).
- Hypothèses (étiquetées comme telles) : hypothèse 1 : pas de quota publié pour les manifestes ; le service est servi par nginx sans limiteur visible (non vérifié, car nous n'avons pas testé de rafale). Hypothèse 2 : la rareté de l'information tient au fait que la bibliothèque renvoie l'usage des données vers les applications web et vers le package `dhlab` (hypothèse, non vérifiée).

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Recherche menée après la sonde, sans nouvelle requête vers l'API. Aucun endpoint de statut ni en-tête de quota trouvé, donc aucune configuration `scripts/config/nb-no-quota.json` n'a été écrite. La lecture de la spécification OpenAPI ci-dessous est une lecture de documentation (WebFetch), pas une sonde.

a) **Endpoint de statut de quota** : non trouvé — termes cherchés : « Nasjonalbiblioteket api.nb.no rate limit kvote API dokumentasjon IIIF » ; « api.nb.no rate limit quota terms of use National Library of Norway API » ; « api.nb.no catalog v1 openapi api-docs swagger rate limit » ; « Nasjonalbiblioteket kontakt API utviklere bruksvilkår maskinell tilgang ». Documentation lue : OpenAPI `https://api.nb.no/catalog/v1/items/api-docs` (cité par une issue GitHub tierce, lu 2026-11-13) : aucun champ de quota, de statut ni de limite ; la page Swagger racine https://api.nb.no/ (2026-11-13) ne donne aucun lien vers une spécification.
b) **En-têtes de limite documentés** : non trouvé — ni `RateLimit-*`, ni `X-RateLimit-*`, ni `Retry-After` dans la spécification. Observé (5 requêtes, fiche) : aucun en-tête de limite. Source tierce (issue GitHub bindery #2979, non officielle) : « NB publishes no rate limits, so this keeps the load to people who asked for it. ».
c) **Clé ou compte donnant un quota** : non trouvé. La spécification ne mentionne aucune clé d'API. Les services d'archivage (`digitalpreservation.no`) utilisent OAuth 2.0 mais relèvent d'un autre usage (dépôt), non de la consultation.
d) **Contact officiel pour un quota** : trouvé — nasa@nb.no, dans le champ `info.contact` de l'OpenAPI `https://api.nb.no/catalog/v1/items/api-docs` (lu 2026-11-13). Pour l'API de recherche, search@nb.no est indiqué dans le document OpenSearch (extrait de recherche, non lu à la source).

Standard : le brouillon IETF `draft-ietf-httpapi-ratelimit-headers` (RateLimit-*) n'est pas une norme ; la spécification IIIF n'a pas été relue sur ce point.

Conclusion : moyen d'interroger le quota : **non**. Piste : écrire à nasa@nb.no (ou search@nb.no) pour demander une politique de débit pour les manifestes et les images, comme le recommande déjà la fiche.

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen (3 manifestes et la page racine testés en 200 ; pas de limite observée ; doc officielle non trouvée).
- Ce qui reste à vérifier, et comment :
  1. Retrouver la spécification OpenAPI liée depuis https://api.nb.no/ (la sonde n'a pas suivi de lien ; à lire depuis un navigateur ordinaire, en GET).
  2. Lire les conditions d'utilisation de la bibliothèque (nb.no, « vilkår » / « bruksvilkår ») et la clause sur l'accès automatisé ; ce n'est pas trouvé dans les sources examinées.
  3. Identifier un service d'image : les manifestes testés ont été lus par WebFetch (résumé), qui a signalé « aucun service d'image » dans l'un et des canvases avec services dans un autre : contradiction, non tranchée. À refaire avec une lecture complète du JSON (lecture hors sonde, par un humain ou un outil dédié), puis test de l'info.json si une URL de service est trouvée.
  4. Le paramètre `{?fields,profile}` est annoncé par le manifeste lui-même (modèle d'URI) : valeurs acceptées non documentées ; non testé.
  5. oEmbed : endpoint déclaré sur oembed.org, mais 404 pour l'URL d'item testée. Refaire avec une URL d'item documentée, ou demander à la bibliothèque.
  6. Demander par écrit à la bibliothèque une politique de débit pour les manifestes et images si le projet dépasse quelques requêtes par minute.
