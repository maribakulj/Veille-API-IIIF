# Rijksmuseum (Amsterdam) — `rijksmuseum`

- **Statut** : vérifiée (sonde IIIF faite ; API de recherche avec clé non testée, voir § 4)
- **Pays** : Pays-Bas
- **Point d'entrée testé** : `https://iiif.micr.io/` (racine IIIF de production indiquée dans la doc officielle). Le point d'entrée `https://www.rijksmuseum.nl/api/` ne liste aucun endpoint.
- **Vérifié le** : 2026-11-13 (sonde à 21:07:55 à 21:08:19 UTC ; documentation consultée le 2026-11-13)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://www.rijksmuseum.nl/api/ (page API du musée) | 2026-11-13 (WebFetch, résumé par un petit modèle) | Aucun endpoint, aucune mention de clé, quota ou limite. Renvoie vers data.rijksmuseum.nl. |
| https://data.rijksmuseum.nl/ (accueil « Rijksmuseum Data ») | 2026-11-13 (WebFetch, résumé) | Aucun quota. Citations : « The Rijksmuseum offers multiple access points for this dataset: via APIs and also as a download. » ; « the Rijksmuseum operates an Open Data policy ». Liens vers `/docs/`, `/policy/`, `/docs/data-dumps`. |
| https://acc.data.rijksmuseum.nl/tutorials/iiif/ (tutoriel IIIF, page acc.) | 2026-11-13 (WebFetch, résumé) | Aucun quota ni limite de débit, aucune clé. Limite **par requête** seulement : `maxArea` = « the maximum number of pixels that can be requested in a single image request ». |
| https://acc.data.rijksmuseum.nl/docs/iiif/presentation (doc IIIF Presentation, acc.) | 2026-11-13 (WebFetch, résumé) | « There is one production endpoint available. » Racine `https://iiif.micr.io`. Aucune clé, aucune limite de débit ou quota. |
| https://data.rijksmuseum.nl/docs/api | 2026-11-13 — **404** via WebFetch | Page non lue (404 au moment de la consultation). |
| https://acc.data.rijksmuseum.nl/object-metadata/api/ | 2026-11-13 — **404** via WebFetch | Page non lue. |
| https://data.rijksmuseum.nl/policy/introductie (politique d'information et de données) | Non lue en détail (lien trouvé depuis l'accueil) | Rien lu sur les quotas. À relire depuis un navigateur. |

Conclusion documentaire : **aucune limite chiffrée** (quota, fenêtre, débit) trouvée dans les pages officielles lues. Les pages IIIF ne demandent pas de clé.

## 2. Recherche élargie

- Termes cherchés : « Rijksmuseum API documentation IIIF manifest rate limit key » ; « Rijksmuseum Collection API key Rijksstudio "api key" quota requests per day 10000 ».
- Sources examinées (résumés, non lues en brut) : apis.io (fiche Rijksmuseum Images API) ; spécification OpenAPI de l'ancienne API (citée par apis.io) ; page « Legacy API (DEPRECATED) » du site développeurs (signalée dans les résultats, non ouverte) ; article navigatingart « Almost frictionless: open access museum collections in practice in 2026 » (résumé) ; scraper Apify `crawlerbros/rijksmuseum-collection-scraper` (résumé) ; Hugging Face `Riksarkivet/iiif_mcp_docs` (non ouvert).
- Résultat :
  - Ancienne API (secondaire, non vérifiée sur la doc officielle) : la spécification OpenAPI citée par apis.io dit que « every request must carry a key » (paramètre `key`), clé obtenue dans les paramètres avancés d'un compte Rijksstudio ; elle décrit une réponse de type 429 en cas de quota journalier ou de fenêtre courte dépassée, **sans chiffre**. La page Legacy API serait marquée DEPRECATED (signalé, non ouvert).
  - Article navigatingart 2026 (secondaire) : affirme que l'API de collection est ouverte, sans clé ni inscription. Non vérifié.
  - Un chiffre « 10 000 requêtes par jour » apparaît dans une requête de recherche mais n'a été retrouvé dans **aucune** source : **non vérifié, à écarter**.
  - Aucune source de recherche ne donne un quota officiel.

## 3. Tests d'appel (voir `tests/rijksmuseum.log`)

Configuration : `scripts/config/rijksmuseum.json` (4 endpoints, sur 15 autorisés). Pause de 6 s entre requêtes.

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:07:59 | https://iiif.micr.io/RFwqO/manifest | GET | 200 OK | aucun | Manifeste Presentation 3.0 (label « AK-NM-7009-Original-Cropped.jpg ») | - |
| 2 | 21:08:06 | https://iiif.micr.io/PJEZO/manifest | GET | 200 OK | aucun | Manifeste Presentation 3.0 | 7 s |
| 3 | 21:08:12 | https://iiif.micr.io/PJEZO/info.json | GET | 200 OK | aucun | Image API 3.0, profil level2 | 6 s |
| 4 | 21:08:19 | https://iiif.micr.io/PJEZO/full/800,/0/default.jpg | GET | 200 OK | aucun | Image JPEG (JFIF) | 7 s |

Non réalisé : l'API de recherche de collection (ancienne API avec clé, et endpoint de métadonnées non retrouvé en clair dans la doc lue). Aucun identifiant n'a été utilisé ni demandé. Total : 4 requêtes.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : **non** pour les endpoints IIIF (pages lues ci-dessus). Pour l'ancienne API avec clé : une mention de 429 (secondaire, sans chiffre) ; pas de quota publié trouvé dans la doc officielle lue.
- Limite **observée** (429 ou en-tête de quota reçu) : **non** (4 requêtes, aucun en-tête `Retry-After`, `X-RateLimit-*` ou `RateLimit-*`).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : **non** (aucune requête n° 1 à 4 refusée).
- L'API annonce-t-elle ses limites dans la réponse ? **non observé** (aucun en-tête de limite).
- Mécanisme observé : **aucun**.
- Valeurs trouvées (quota, fenêtre) : **aucune** dans une source officielle. Limite par requête d'image : `maxArea` (doc tutoriel IIIF, valeur non lue).
- Clé : les endpoints IIIF testés répondent **sans clé**. L'ancienne API de recherche indique une clé (secondaire, non testée, non demandée ici).
- Blocages rencontrés : aucun. Pages `data.rijksmuseum.nl/docs/api` et `acc.data.rijksmuseum.nl/object-metadata/api/` en 404 à la consultation.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

Sans objet pour les endpoints IIIF (publiés et sans clé d'après la doc). Pour l'API de recherche, la divergence entre sources (ancienne API avec clé, nouvelle affirmée ouverte) n'est pas tranchée.

- Trouvé (avec source) : pages IIIF officielles citées au § 1 ; ancienne API avec clé et 429 sans chiffre (spécification OpenAPI, secondaire).
- Hypothèses (étiquetées comme telles) : hypothèse 1 : l'API de recherche actuelle est ouverte sans clé (article 2026, non vérifié). Hypothèse 2 : l'ancienne API reste en service avec clé et quota non publié (non vérifié).

## 6. Confiance et pistes restantes

- Niveau de confiance : **moyen** pour les endpoints IIIF (4 réponses 200 sans en-tête de limite) ; **faible** pour l'API de recherche (pages 404, sources secondaires contradictoires).
- Ce qui reste à vérifier, et comment :
  1. Ouvrir depuis un navigateur `https://data.rijksmuseum.nl/docs/` (rubrique API) et la page « Legacy API » pour trancher : clé requise ou non, quota publié ou non.
  2. Lire `https://data.rijksmuseum.nl/policy/introductie` (conditions d'usage des données) depuis un navigateur.
  3. Identifier l'URL exacte de l'endpoint de recherche de la nouvelle API (non trouvée en clair dans les pages lues), puis le tester sans clé, si la doc confirme qu'il est public (une requête, pas de POST).
  4. Si une clé est exigée : ne pas en créer ni en utiliser dans cette veille ; consigner « clé requise, non testée ».
