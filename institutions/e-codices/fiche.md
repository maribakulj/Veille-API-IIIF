# e-codices (Bibliothèque virtuelle des manuscrits en Suisse) — `e-codices`

- **Statut** : vérifiée (sonde de 7 requêtes, aucun 403 ni 429)
- **Pays** : Suisse
- **Point d'entrée testé** : https://www.e-codices.unifr.ch/en (page d'accueil ; versions de/fr/it existent)
- **Vérifié le** : 2026-11-13 (UTC, 21:07 à 21:08)
- **Vérifié par** : agent de veille (session Claude, branche claude/veille-iiif-quotas)

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://www.e-codices.unifr.ch/en/about/terms | 2026-11-13 | Pas de quota ni de limite de débit. Images : « the use of our digitally reproduced images for non-commercial purposes is free » ; usage commercial ou republication : citation de source requise et « the prior written permission of the manuscript owner library ». Métadonnées : « generally protected by a Creative Commons License », usage « as long as proper source citation is used ». OAI : « released for free use ». Aucune règle sur le téléchargement en masse ni sur l'usage automatisé (résumé de la page par WebFetch, pas de citation verbatim complète). |
| https://www.e-codices.unifr.ch/en/about/webapplication | 2026-11-13 | Indique que l'application utilise l'IIIF Image API (images) et l'IIIF Presentation API (métadonnées), **sans aucune URL d'endpoint**. Rien sur les quotas. |
| https://www.e-codices.unifr.ch/en/about/imaging | 2026-11-13 | Pas d'URL d'image ni de manifeste ; « For the web application viewer and for the image server, TIFF files are converted into JPEG 2000 files ». Aucune mention de quota, IIIF ou usage automatisé. |
| https://www.e-codices.unifr.ch/en/about/metadata | non consultée | — |

Constat : **aucune limite de débit, quota ou politique d'usage automatisé n'est annoncée** dans les pages officielles consultées. Les conditions d'usage renvoient à des autorisations par bibliothèque propriétaire pour l'usage commercial et les TIFF, pas à des quotas techniques.

Endpoints IIIF : la documentation officielle **ne donne aucune URL de manifeste ni d'info.json**. Les URL de manifeste ci-dessous viennent de sources tierces (recherche élargie), puis ont été **vérifiées par la sonde** (observé 200).

## 2. Recherche élargie

- Termes cherchés : « e-codices IIIF manifest API documentation » ; « e-codices manifest.json "e-codices.unifr.ch" iiif metadata » ; « e-codices OAI-PMH endpoint URL oai.php ».
- Sources examinées : résultats de recherche (aucun document e-codices officiel dans les résultats) ; documentation Europeana (IIIF, générique) ; un outil tiers de mise à plat de manifestes IIIF dont le README cite `e-codices.unifr.ch/metadata/iiif/fmb-cb-0100/manifest.json` (URL de README non retrouvée par l'outil) ; page de données ouvertes suisse (opendata.swiss) citant la collection `ubb.json` ; wiki de fixtures Mirador citant `gau-Fragment/manifest.json`.
- Résultat : URL de manifeste et de collection **trouvées dans des sources tierces** et confirmées par la sonde. Aucun quota trouvé nulle part. Aucune documentation d'API OAI-PMH e-codices trouvée (la recherche sur « oai.php » n'a donné que des résultats d'autres dépôts).

## 3. Tests d'appel (voir `institutions/e-codices/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:07:51 | https://www.e-codices.unifr.ch/en | GET | 200 | aucun | HTML, titre « e-codices – Virtual Manuscript Library of Switzerland » | — |
| 2 | 21:07:58 | https://www.e-codices.unifr.ch/en/about/terms | GET | 200 | aucun | HTML « Terms of Use » | 7 s |
| 3 | 21:08:04 | https://www.e-codices.unifr.ch/metadata/iiif/fmb-cb-0100/manifest.json | GET | 200 | aucun | JSON, @context Presentation API 2, label « Cologny, Fondation Martin Bodmer, Cod. … » | 6 s |
| 4 | 21:08:10 | https://www.e-codices.unifr.ch/metadata/iiif/gau-Fragment/manifest.json | GET | 200 | aucun | JSON Presentation API 2, label « Urnäsch, Gemeindearchiv Urnäsch, Fragment » | 6 s |
| 5 | 21:08:16 | https://www.e-codices.unifr.ch/metadata/iiif/collection/ubb.json | GET | 200 | aucun | JSON Collection Presentation API 2, « Basel, Universitätsbibliothek » | 6 s |
| 6 | 21:08:23 | https://www.e-codices.unifr.ch/en/search?…sSearchField=fullText… | GET | 200 | aucun | HTML « Search Results » | 7 s |
| 7 | 21:08:32 | https://www.e-codices.unifr.ch/rss/all/latest | GET | 200 | aucun | RSS 2.0 | 9 s |

Pauses : au moins 6 s entre deux requêtes (réglage du script). Budget : 7 requêtes sur 15.

Non testé : URL d'image (info.json) — aucune URL d'image IIIF n'est documentée ni citée avec certitude ; le service d'images est sur `media.e-codices.ch/iip/` d'après la page d'accueil, mais l'URL n'a pas été devinée. OAI-PMH — URL non trouvée, non testée.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non. Les conditions d'usage (https://www.e-codices.unifr.ch/en/about/terms) n'annoncent ni quota ni débit.
- Limite **observée** (429 ou en-tête de quota reçu) : non (7 requêtes, aucun en-tête de limite, aucun 429).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : non.
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucun en-tête `X-RateLimit`/`Retry-After`).
- Mécanisme observé : rien.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : aucun. Un seul point de vigilance : les conditions prévoient une autorisation écrite de la bibliothèque propriétaire pour l'usage commercial ou la republication.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

Sans objet : aucune limite annoncée à expliquer.
- Trouvé (avec source) : les images servent à usage non commercial libre ; la métadonnée est sous licence Creative Commons ; les manifestes IIIF Presentation 2 existent et répondent en 200.
- Hypothèses (étiquetées comme telles) : aucune limite technique n'est imposée à ce jour, mais ce n'est pas garanti pour des rafales (non testé, hors budget).

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen. Les manifestes et la collection sont confirmés par la sonde ; l'absence de quota repose sur les pages officielles lues, et la page des conditions a été lue par résumé (WebFetch), pas en texte intégral.
- À vérifier :
  1. Relire https://www.e-codices.unifr.ch/en/about/terms en texte intégral dans un navigateur, pour confirmer l'absence de clause sur l'usage automatisé.
  2. Trouver l'URL exacte du service image (info.json) et de l'OAI-PMH, idéalement dans la page https://www.e-codices.unifr.ch/en/about/metadata (non consultée) ou par contact de l'équipe e-codices.
  3. Refaire une sonde espacée plus tard (et en rafale contrôlée) pour voir si un en-tête de quota apparaît.
  4. Les URL de manifestes ne figurent pas dans la doc officielle : les considérer comme « observées, non documentées » tant que l'institution ne les publie pas.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

a) **Endpoint de statut de quota** : non trouvé — termes cherchés : « e-codices rate limit quota », « e-codices IIIF manifest API documentation », « e-codices Nutzung automatisiert Kontakt ». Guide IIIF e-codices lu le 2026-11-13 (https://guides.iiif.io/guides/e-codices.ch/) : ne mentionne aucun endpoint de statut, ni `/status`, `/limits` ou `/me`. Doc officielle (https://www.e-codices.unifr.ch/en/about/terms, lue le 2026-11-13) : aucune mention d'API.

b) **En-têtes de limite documentés** : non trouvé — aucun en-tête `RateLimit-*`, `X-RateLimit-*` ni `Retry-After` cité dans la doc ni dans les résultats. Nos 7 requêtes n'en renvoient aucun (institutions/e-codices/tests/journal.log).

c) **Clé d'API ou compte donnant un quota** : non trouvé — aucune clé ni compte mentionné pour l'accès IIIF ; les conditions ne parlent que d'autorisation écrite de la bibliothèque propriétaire pour l'usage commercial.

d) **Contact officiel pour demander un quota** : non trouvé — aucune adresse officielle confirmée. L'adresse e-codices@unifr.ch n'apparaît dans aucun résultat. Les seules adresses trouvées (ramona.fritschi@unifr.ch, actualité unifr.ch de 2015 ; christophe.flueler@unifr.ch, même source) sont anciennes et personnelles : non utilisées, à vérifier sur la page contact actuelle du site, non relue. Source : résultats de recherche « e-codices Verein Universität Freiburg contact », 2026-11-13.

Conclusion : moyen d'interroger le quota : **non**. Aucun endpoint, en-tête ni compte documenté ; aucune sonde ciblée lancée (pas de `scripts/config/e-codices-quota.json`).
