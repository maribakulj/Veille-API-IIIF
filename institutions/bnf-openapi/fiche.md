# BnF — API publiques (openapi.bnf.fr / openapiproext.bnf.fr) — `bnf-openapi`

- **Statut** : **abandonnée** à la demande de Marcel (2026-11-13). Aucune requête supplémentaire ; pas de POST vers le point de jeton OAuth. Résultats partiels conservés ci-dessous.
- **Pays** : France
- **Point d'entrée testé** : https://openapi.bnf.fr/ (racine) ; chemins IIIF testés sous https://openapi.bnf.fr/iiif/presentation/v3/ (non documentés, voir § 3) ; https://openapiproext.bnf.fr/ (connexion non établie)
- **Vérifié le** : 2026-11-13 (UTC)
- **Vérifié par** : agent de veille (Haiku 5.5), session du 2026-11-13

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://apimpubext.bnf.fr (portail développeurs cité dans les notes) | 2026-11-13 | Non résolu (DNS impossible, curl 6). Rien trouvé. |
| https://api.bnf.fr/fr/api-iiif-de-recuperation-des-images-de-gallica | 2026-11-13 | Rien sur quota, débit, authentification. Seule mention : licence « Conditions d'utilisation des contenus de Gallica ». Concerne Gallica, pas openapi.bnf.fr. |
| https://www.bnf.fr/fr/portail-bnf-api-et-jeux-de-donnees | 2026-11-13 | Rien sur quota ni authentification. Renvoie vers api.bnf.fr ; « gratuitement, pour tout type de réutilisation » (licence, pas une limite technique). Chaque fiche technique « précise la licence ». |
| https://openapi.bnf.fr (racine) | 2026-11-13 | Page vide : « Welcome to APIM » + lien /service masqué. Aucune doc. |
| https://www.bnf.fr/sites/default/files/2026-01/JDIFF2025-03-du-nouveau-sur-api-bnf-fr.pdf | 2026-11-13 | PDF non lisible en texte par l'outil (flux compressés, 18 pages). Non vérifié. |

## 2. Recherche élargie

- Termes cherchés : « BnF API openapi.bnf.fr IIIF quota rate limit nextAccessTime » ; « apimpubext.bnf.fr portail développeurs BnF API IIIF OAuth client_credentials » ; « "openapiproext" bnf » ; « openapi.bnf.fr iiif manifest exemple URL API BnF ».
- Sources examinées : résultats de recherche web (pas de lien ouvert hors listes ci-dessous) ; README du paquet R bnfimage (tiers) ; page api.bnf.fr ; portail BnF.
- Résultat : **aucune mention** de `nextAccessTime`, de `retry-after`, de quota ou de débit pour openapi.bnf.fr ou openapiproext.bnf.fr. Le seul élément de limite trouvé est une phrase d'un paquet R tiers (bnfimage, documentation non officielle) : la BnF « considère les requêtes comme malveillantes » au-delà d'un seuil, sans chiffre ni source. Aucune mention d'OAuth BnF trouvée (les résultats OAuth concernent d'autres fournisseurs). Aucun billet ni issue GitHub sur openapi.bnf.fr trouvé. Wayback non consulté.

## 3. Tests d'appel (voir `institutions/bnf-openapi/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| S1 | ~20:32:50 | https://apimpubext.bnf.fr | HEAD | ERR DNS | - | - | - |
| S2 | ~20:33:00 | https://openapi.bnf.fr | HEAD | 200 | aucun relevé | - | 10 s |
| S3 | ~20:33:10 | https://apimauthpubext.bnf.fr | HEAD | 403 | - | - | 10 s |
| 1 | 20:33:50 | https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/bpt6k9761234x/manifest.json | GET | 404 | aucun | JSON `{"reason":"Not Found","code":404,"status":"error"}` | - |
| 2 | 20:34:00 | https://openapiproext.bnf.fr/iiif/presentation/v3/ark:/12148/bpt6k9761234x/manifest.json | GET | ERR (délai de connexion, 30 s) | aucun | vide | 10 s |
| 3 | 20:34:35 | https://openapi.bnf.fr/ | GET | 200 | aucun | HTML « Welcome to APIM » (142 o) | - |
| 4 | 20:34:45 | https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/btv1b8453475v/manifest | GET | 404 | aucun | JSON « No matching resource found for given API Request » | 10 s |

Non faits, et pourquoi :
- **Jeton OAuth** : l'obtention d'un jeton client_credentials passe normalement par un POST sur apimauthpubext.bnf.fr. METHODOLOGY.md interdit tout POST (GET seulement). Non effectué ; décision à prendre par Marcel (voir § 6). Le trousseau contient bien l'entrée `bnf-openapi-basic` (vérifiée sans affichage).
- **info.json, OCR/ALTO** : aucun chemin openapi.bnf.fr documenté trouvé ; les chemins devinés renvoient 404 (« No matching resource »). Pas de devinette supplémentaire, conformément à la méthode.
- **openapiproext.bnf.fr** : connexion non établie (délai dépassé) ; arrêt immédiat, pas de réessai.

## 4. Conclusion sur les limites

- L'API annonce-t-elle ses limites dans la réponse ? **non observé** (aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*` ni `nextAccessTime` sur les réponses reçues : 200, 404).
- Mécanisme observé : **aucun**. Le 429 avec `nextAccessTime` et `retry-after` signalé dans les notes n'a pas pu être reproduit : aucune réponse 429 reçue, et openapiproext.bnf.fr n'a pas répondu depuis cette session.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés :
  - apimpubext.bnf.fr : nom non résolu (DNS).
  - apimauthpubext.bnf.fr : 403 à la sonde HEAD (non répétée).
  - openapiproext.bnf.fr : délai de connexion dépassé (30 s), arrêt. Cohérent avec un filtrage IP depuis l'extérieur, mais c'est une hypothèse non vérifiée.
  - Le jeton n'a pas été demandé (POST interdit par la méthode).

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : rien de précis. La doc publique BnF accessible (api.bnf.fr, bnf.fr) ne mentionne ni openapi.bnf.fr ni de quota. Le seul texte sur la limitation est un paquet R tiers : la BnF bloque les requêtes jugées « malveillantes » au-delà d'un seuil non chiffré (source non officielle : https://rdrr.io/github/Rekyt/bnfimage/f/README.md).
- Hypothèses (étiquetées) :
  - Hypothèse : l'API est une passerelle APIM réservée à des comptes ou à des partenaires (OAuth client_credentials), sans documentation publique des quotas.
  - Hypothèse : le quota de openapiproext est appliqué par la passerelle et n'est visible que depuis les IP autorisées, ce qui explique le délai de connexion depuis l'extérieur.
  - Hypothèse : la publication des quotas est simplement absente du portail accessible ; le portail apimpubext est peut-être la seule source.

## 6. Confiance et pistes restantes

- Niveau de confiance : faible (peu de chemins valides testés, aucun jeton, portail injoignable).
- Ce qui reste à vérifier :
  1. Décision de Marcel : autoriser une seule requête POST vers le point de jeton OAuth (hors méthode GET-only), ou la faire à la main avec ses identifiants depuis le trousseau. Sans cela, on ne sait pas si openapi.bnf.fr renvoie des 429 avec `nextAccessTime`.
  2. Retrouver le chemin documenté d'une ressource IIIF sur openapi.bnf.fr (portail apimpubext, à réouvrir depuis un réseau où il résout ; ou demande à la BnF).
  3. Rejouer openapiproext.bnf.fr plus tard, depuis un réseau autorisé, pour retrouver le 429 + `nextAccessTime` signalé.
  4. Contacter la BnF (support API) pour la politique de quota : rien de public trouvé.
