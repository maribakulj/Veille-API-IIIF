# Bayerische Staatsbibliothek / MDZ (Digitale Sammlungen) — `mdz`

- **Statut** : vérifiée
- **Pays** : Allemagne
- **Point d'entrée testé** : https://api.digitale-sammlungen.de/iiif/ (saisi dans institutions.csv) → 404 ; endpoints documentés testés : manifeste Presentation v2, collection top, info.json Image v2, OCR hOCR, image JPEG réduite
- **Vérifié le** : 2026-11-13 (UTC, 21:04–21:07)
- **Vérifié par** : agent de veille (Haiku 5.5), session Claude Code

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://www.digitale-sammlungen.de/en/interfaces (version allemande : https://www.digitale-sammlungen.de/de/schnittstellen) | 2026-11-13 | EN : « Please note that there is a limit to the number of OCR downloads that can be made per 24 hours. Access to the Presentation API is unlimited. » / « Please note that there is a limit to the number of requests that can be made to the Image API per 24 hours. » — DE : « Bitte beachten Sie, dass die Zahl an OCR-Downloads, die pro 24 Stunden gemacht werden können, beschränkt ist. Der Zugang auf die Presentation API ist unbeschränkt. » / « …die Zahl an Requests, die pro 24 Stunden an die Image API gerichtet werden können, begrenzt ist. » |
| https://digitale-sammlungen.de/en/faq | 2026-11-13 | Aucune mention de quota ni de limite d'API (FAQ sur les droits, OCR, formats). |
| Conditions d'utilisation / « terms of use » de l'API | 2026-11-13 | Non trouvées sous une URL dédiée lors de la recherche ; la page d'interfaces renvoie seulement aux API. Chiffres absents. |

Chiffres (nombre de requêtes par 24 h) : **non publiés** dans la doc consultée.
Aucune mention de code 429 ni de Retry-After dans la doc.
Doc également : l'API sert `Access-Control-Allow-Origin: *` (accès navigateur autorisé).

## 2. Recherche élargie

- Termes cherchés : « MDZ Digitale Sammlungen API IIIF Dokumentation Rate Limit Quota » ; « digitale-sammlungen.de API OCR Downloads 24 Stunden Limit Image API Nutzungsbedingungen » ; lecture de la FAQ et de la page d'interfaces (EN et DE).
- Sources examinées : pages officielles interfaces (EN, DE), FAQ EN, page racine de l'hôte API (404). Résultats de recherche : aucun article, ticket GitHub ou forum donnant des chiffres. Pas d'examen Wayback (non nécessaire, la doc actuelle nomme les limites).
- Résultat : confirmation de limites **par 24 h** pour OCR et Image API ; aucun nombre trouvé. Le contact de l'institution reste la seule source pour les chiffres.

## 3. Tests d'appel (voir `tests/mdz.log`)

Tous en GET (un HEAD au départ, sur le point d'entrée). Budget API : 10 requêtes sur 15. Pause ≥ 6 s entre deux requêtes vers `api.digitale-sammlungen.de`.

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:04:55 | /iiif/ (point d'entrée saisi) | HEAD | 404 | aucun | 404 | — |
| 2 | 21:05:05 | / (racine de l'hôte) | GET | 404 | aucun | 404 | 10 s |
| 6 | 21:05:59 | /iiif/presentation/v2/{id}/manifest (exemple doc) | GET | 200 | aucun | JSON-LD Presentation 2 (33 Ko) | 18 s (après les doc 3–5) |
| 7 | 21:06:09 | /iiif/image/v2/{id}/info.json | GET | 200 | aucun | JSON-LD Image 2 (530 o) | 10 s |
| 8 | 21:06:15 | /iiif/presentation/v2/collection/top | GET | 200 | aucun | collection JSON (702 Ko) | 6 s |
| 9 | 21:06:22 | /ocr/{id}/{page} (exemple doc) | GET | 200 | x-ratelimit-limit: 5001 ; x-ratelimit-remaining: 5000 ; x-ratelimit-reset: 17 | hOCR (22 Ko) | 7 s |
| 10 | 21:06:28 | /iiif/ (rejoué en GET) | GET | 404 | aucun | 404 | 6 s |
| 11 | 21:06:43 | /ocr/{id}/{page} (même URL, 2e appel) | GET | 200 | x-ratelimit-limit: 5001 ; remaining: 5000 ; reset: 17 | hOCR (22 Ko) | 15 s |
| 12 | 21:06:50 | /iiif/image/v2/{id}/full/100,/0/default.jpg | GET | 200 | x-ratelimit-limit: 25001 ; remaining: 25000 ; reset: 3 | JPEG (2 Ko) | 7 s |
| 13 | 21:07:03 | idem 12 (2e appel) | GET | 200 | limit 25001 ; remaining 25000 ; reset 3 | JPEG (2 Ko) | 13 s |

Les pages de documentation (appels 3, 4, 5 : interfaces EN, FAQ, interfaces DE) ne sont pas comptées au budget API.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : **oui** — OCR et Image API limitées « per 24 hours » (https://www.digitale-sammlungen.de/en/interfaces, consultée le 2026-11-13). Chiffre : **non publié**.
- Limite **observée** (429 ou en-tête de quota reçu) : **non** pour un 429 (aucun reçu). En-têtes `x-ratelimit-*` reçus sur OCR et Image, mais ils ne décroissent pas d'un appel à l'autre (remaining reste à 5000 et à 25000) : **ne prouvent pas un mécanisme de limitation observé**.
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : **non** (aucun 403 sur les 13 requêtes).
- L'API annonce-t-elle ses limites dans la réponse ? **partiel** : en-têtes `x-ratelimit-limit/remaining/reset` sur OCR et image seulement ; rien sur manifestes ni info.json.
- Mécanisme observé (429 + Retry-After, en-têtes X-RateLimit, rien) : en-têtes X-RateLimit sur deux endpoints (OCR, image), sans décompte visible entre deux appels ; manifestes et info.json : rien.
- Valeurs trouvées (quota, fenêtre) : fenêtre « 24 heures » (doc). Valeurs en-têtes : OCR limit 5001 ; image limit 25001 (ce ne sont pas des quotas documentés, et leur sens n'est pas établi).
- Blocages rencontrés : point d'entrée saisi dans institutions.csv inexistant (404 sur /iiif/ et sur la racine). Pas de 403 ni 429.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la doc dit que les limites existent sans les chiffrer. Les conditions d'utilisation ne sont pas trouvées en ligne. La FAQ n'en parle pas.
- Hypothèses (étiquetées comme telles) : hypothèse 1 — les chiffres ne sont pas publiés pour ne pas figer un usage ; hypothèse 2 — la limite est une protection anti-abus, car la doc parle de « budget » pour l'OCR (FAQ : le problème est « a budget issue ») sans rapport direct avec un quota API.

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen (doc claire sur l'existence des limites ; en-têtes observés mais non interprétés).
- Ce qui reste à vérifier, et comment :
  - Chiffres (nombre par 24 h) : demander à MDZ (contact indiqué sur digitale-sammlungen.de) ou tester plus tard avec un nombre d'appels plus grand, respectueux, pour voir si `x-ratelimit-remaining` finit par baisser ou si une réponse 429 apparaît.
  - Sens de `x-ratelimit-reset` (17 et 3) : unité non documentée, à demander.
  - Corriger institutions.csv : point d'entrée réel à utiliser, `https://api.digitale-sammlungen.de/iiif/presentation/v2/{id}/manifest` (ou collection/top) ; l'URL `/iiif/` renvoie 404.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

a) **Endpoint de statut de quota** : non trouvé — termes cherchés : « digitale-sammlungen API status endpoint », « digitale-sammlungen API x-ratelimit-limit header OCR Image API 24 hours limit », « Bayerische Staatsbibliothek Digitale Sammlungen API Kontingent Anfragen 24 Stunden ». Page interfaces lue le 2026-11-13 (https://www.digitale-sammlungen.de/en/interfaces) : aucun endpoint `/status`, `/limits` ou `/me` ; guide IIIF (https://iiif.io/guides/guides/digitale-sammlungen.de/, lu 2026-11-13) : aucune phrase sur les limites.

b) **En-têtes de limite** : **en-têtes observés, non documentés** — le nom `x-ratelimit-*` n'apparaît dans aucune doc trouvée. Ce que dit la doc : « Please note that there is a limit to the number of requests that can be made to the Image API per 24 hours. » et « Please note that there is a limit to the number of OCR downloads that can be made per 24 hours. » (https://www.digitale-sammlungen.de/en/interfaces, 2026-11-13). Aucun nom d'en-tête ni chiffre. Sens des en-têtes : non établi. Nos réponses donnent `x-ratelimit-limit` 5001 (OCR) et 25001 (image), `x-ratelimit-remaining` 5000 et 25000, `x-ratelimit-reset` 17 et 3 (tests/raw/mdz/). Le « remaining » ne baisse pas entre deux appels (5000 aux appels 9 et 11 ; 25000 aux appels 12 et 13) : ce n'est pas un compteur observable. Le standard IETF `RateLimit-Reset` (draft-ietf-httpapi-ratelimit-headers, dernière version lue : -06, déc. 2022, non publiée en RFC) définit un délai en secondes ; nos en-têtes sont `x-ratelimit-*` (préfixe non standard) : on ne peut pas en déduire le sens. Recherche « x-ratelimit-reset » + digitale-sammlungen / GitHub : aucun résultat.

c) **Clé d'API ou compte** : non trouvé — la page interfaces ne mentionne ni clé, ni compte, ni procédure d'accès ; elle indique seulement que l'API Presentation est « unlimited » (« Access to the Presentation API is unlimited. »).

d) **Contact officiel** : **trouvé** — mdz@bsb-muenchen.de. Sources : https://www.digitale-sammlungen.de/en/contact (lue le 2026-11-13 : « General inquiries about digitization and long-term preservation » ; adresse Ludwigstr. 16, 80539 München) ; message d'erreur de la page interfaces (2026-11-13 : « If the error persists, please get in touch via mdz@bsb-muenchen.de »). Le re3data (https://www.re3data.org/repository/r3d100010148) cite la même adresse (source secondaire).

Conclusion : moyen d'interroger le quota : **non**. Aucun endpoint de statut ni en-tête documenté ; les en-têtes `x-ratelimit-*` observés ne sont ni documentés ni utilisables comme compteur. Pas de sonde ciblée lancée (rien de documenté à tester : pas de `scripts/config/mdz-quota.json`). Le chiffre des 24 h s'obtient par demande écrite à mdz@bsb-muenchen.de.
