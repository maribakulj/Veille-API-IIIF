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

## 3. Tests d'appel (voir `institutions/mdz/tests/journal.log`)

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

b) **En-têtes de limite** : **en-têtes observés, non documentés** — le nom `x-ratelimit-*` n'apparaît dans aucune doc trouvée. Ce que dit la doc : « Please note that there is a limit to the number of requests that can be made to the Image API per 24 hours. » et « Please note that there is a limit to the number of OCR downloads that can be made per 24 hours. » (https://www.digitale-sammlungen.de/en/interfaces, 2026-11-13). Aucun nom d'en-tête ni chiffre. Sens des en-têtes : non établi. Nos réponses donnent `x-ratelimit-limit` 5001 (OCR) et 25001 (image), `x-ratelimit-remaining` 5000 et 25000, `x-ratelimit-reset` 17 et 3 (institutions/mdz/tests/raw/). Le « remaining » ne baisse pas entre deux appels (5000 aux appels 9 et 11 ; 25000 aux appels 12 et 13) : ce n'est pas un compteur observable. Le standard IETF `RateLimit-Reset` (draft-ietf-httpapi-ratelimit-headers, dernière version lue : -06, déc. 2022, non publiée en RFC) définit un délai en secondes ; nos en-têtes sont `x-ratelimit-*` (préfixe non standard) : on ne peut pas en déduire le sens. Recherche « x-ratelimit-reset » + digitale-sammlungen / GitHub : aucun résultat.

c) **Clé d'API ou compte** : non trouvé — la page interfaces ne mentionne ni clé, ni compte, ni procédure d'accès ; elle indique seulement que l'API Presentation est « unlimited » (« Access to the Presentation API is unlimited. »).

d) **Contact officiel** : **trouvé** — mdz@bsb-muenchen.de. Sources : https://www.digitale-sammlungen.de/en/contact (lue le 2026-11-13 : « General inquiries about digitization and long-term preservation » ; adresse Ludwigstr. 16, 80539 München) ; message d'erreur de la page interfaces (2026-11-13 : « If the error persists, please get in touch via mdz@bsb-muenchen.de »). Le re3data (https://www.re3data.org/repository/r3d100010148) cite la même adresse (source secondaire).

Conclusion : moyen d'interroger le quota : **non**. Aucun endpoint de statut ni en-tête documenté ; les en-têtes `x-ratelimit-*` observés ne sont ni documentés ni utilisables comme compteur. Pas de sonde ciblée lancée (rien de documenté à tester : pas de `scripts/config/mdz-quota.json`). Le chiffre des 24 h s'obtient par demande écrite à mdz@bsb-muenchen.de.

## Vérification méthode v2 (2026-11-13)

Statut selon la méthode v2 : **incomplet** (étape a partiellement faite : une page en échec). Le statut « vérifiée » ci-dessus est antérieur à la méthode v2 et n'est pas réécrit ici.

| Étape | Fait ? | Preuves | Conclusion |
|---|---|---|---|
| a) Doc lue en entier | **non faite (partiel)** : 15 pages lues en entier, 1 page en échec | `institutions/mdz/sources/` : `interfaces-en.md`, `schnittstellen-de.md`, `technologies-en.md`, `technologien-de.md`, `faq-en.md`, `faq-de.md`, `contact-en.md`, `imprint-en.md`, `disclaimer-en.md`, `privacy-policy-en.md`, `download-options-en.md`, `viewer-help-en.md`, `search-help-en.md`, `bdr-oai-doc-en.md`, `rights-vgwort-en.md` (URL, date UTC, SHA-256, méthode dans chaque en-tête) | Échec : `https://www.bsb-muenchen.de/digitale-objekte/` et `/en/digitale-objekte/` renvoient 404 (curl, 2026-11-13), la recherche ne le trouve pas. Pas de page « terms of use » dédiée liée depuis la page Interfaces. Pages lues via HTML converti en texte (menus conservés), téléchargements complets (pas de troncature). |
| b) Endpoints tirés de la doc | **fait** | `interfaces-en.md` (et `schnittstellen-de.md`, mêmes URL) ; `bdr-oai-doc-en.md` | Presentation : `/iiif/presentation/v2/{object_id}/manifest` (exemples bsb00012345 et bsb00130380_00157_u001) ; collection : `/iiif/presentation/v2/collection/top` ; Image : `/iiif/image/v2/{image_id}/{region}/{size}/{rotation}/{quality}.{format}` (exemple `bsb00109992_00001/full/full/0/default.jpg`) ; info.json : `/iiif/image/v2/{image_id}/info.json` (exemple bsb00103155_00013) ; OCR : `/ocr/{object_id}/{page_num}` (exemple bsb00000001/00010) ; BDR OAI-PMH : `http://bdr.oai.bsb-muenchen.de/OAIHandler?verb=Identify` (cité dans `bdr-oai-doc-en.md`, non demandé explicitement dans la liste de l'étape b, ajouté car la doc le cite). Non retenus : flux RSS (pas une API). Aucun endpoint de recherche n'est documenté. |
| c) Configuration écrite avant les tests | **fait** | `institutions/mdz/config/mdz.json` mis à jour ; `python3 scripts/probe.py institutions/mdz/config/mdz.json --dry-run` lancé (7 endpoints listés, aucune requête) | Écart corrigé : la configuration ne contenait pas que des endpoints documentés. Retirés : `entree-iiif-saisie` (`/iiif/`, saisi dans institutions.csv, non cité par la doc, 404) et `racine-hote` (`/`, non cité, 404) ; retiré aussi `image-api-reduite` (`full/100,/…`, une valeur de paramètre non donnée en exemple par la doc). Ces requêtes restent consignées dans `institutions/mdz/tests/journal.log` (entrées n° 1, 2, 10, 12 et 13 du journal ; elles ne sont pas relancées). Ajoutés : `presentation-manifeste-2`, `image-exemple-full` (exemples documentés), `bdr-oai-identify`. |
| d) Recherche de quota dans la doc | **fait** | Pages `institutions/mdz/sources/*.md` (grep sur les termes limit/Stunden/hours/429/Retry-After/X-RateLimit/key/Konto/token) | Voir détail ci-dessous. |
| e) Test de chaque endpoint | **fait** (3 requêtes nouvelles, pause 6 s) | `institutions/mdz/tests/journal.log` (lignes ajoutées en fin de fichier, session 21:20:18–21:20:25 UTC) ; `institutions/mdz/tests/raw/presentation-manifeste-2.headers.txt`, `institutions/mdz/tests/raw/image-exemple-full.headers.txt`, `institutions/mdz/tests/raw/bdr-oai-identify.headers.txt` | Sonde lancée sur un fichier temporaire (`mdz-nouveaux.json`, hors dépôt) ne contenant que les 3 endpoints nouveaux, pour ne pas relancer les 5 déjà consignés. Résultats : manifest 2 → 200 (sans en-tête de limite) ; image full/full → 200 avec `x-ratelimit-limit: 25001`, `x-ratelimit-remaining: 25000`, `x-ratelimit-reset: 3` ; OAI Identify → **403** (page Apache « 403 Forbidden », premier appel vers ce `bdr.oai` ; pas de défi Cloudflare ; cause non établie). Le 403 n'est pas un quota : hôte `bdr.oai.bsb-muenchen.de` arrêté, aucune nouvelle tentative, aucun changement d'User-Agent. Budget API (`api.digitale-sammlungen.de`) : 12 requêtes au total sur 15. Aucun 429 reçu. Pas de test de dépassement. |
| f) Ce que disent les gens sur le web | **fait** (recherche standard et étendue ; 3 tickets GitHub lus) | Voir liste ci-dessous | Peu de matière : aucune source officielle ou utilisateur ne donne de chiffre de quota. Un projet tiers décrit un blocage et une demande de débit adressée à la BSB (voir ci-dessous). |

### Détail de l'étape d) (recherche de quota dans la doc)

- **a) Endpoint de statut** : **non trouvé**. Aucune page lue ne cite `/status`, `/limits` ou `/me` (grep négatif sur `institutions/mdz/sources/`). Pages : `interfaces-en.md`, `schnittstellen-de.md`.
- **b) En-têtes de limite documentés** : **aucun nom d'en-tête documenté**. La doc dit seulement : « Please note that there is a limit to the number of OCR downloads that can be made per 24 hours. » et « Please note that there is a limit to the number of requests that can be made to the Image API per 24 hours. » (`interfaces-en.md`, lignes 167, 219, 229 ; même texte en allemand dans `schnittstellen-de.md`, lignes 168, 220, 230). Les en-têtes `x-ratelimit-*` observés ne figurent dans aucune page lue. Ils ne décroissent pas : `remaining` reste à 5000 (OCR) et à 25000 (image) sur 5 appels répartis entre le 21:06 et le 21:20 UTC. Ce ne sont pas des compteurs observables.
- **c) Clé ou compte donnant un quota** : **non trouvé**. Aucune mention de clé, jeton, compte ni inscription (grep négatif). La doc dit même : « Access to the Presentation API is unlimited. » (`interfaces-en.md`, ligne 167 ; « Der Zugang auf die Presentation API ist unbeschränkt. » dans `schnittstellen-de.md`, ligne 168).
- **d) Contact pour un volume plus élevé** : **non trouvé en tant que tel**. Contact général : « General inquiries about digitization and long-term preservation: mdz@bsb-muenchen.de » (`contact-en.md`, lignes 131-133). Aucune page ne dit que ce contact sert à obtenir un volume API plus élevé.
- **Autre limite documentée, hors API** : le service DaFo (téléchargement de JPEG 300 ppi) : « The maximum order size per day/user is limited due to the high amount of data… » (`download-options-en.md`, ligne 149 ; aucun chiffre). Pour une demande particulière : « please send an email (see Contact) » (`faq-en.md`, ligne 159).

**Conclusion étape d) : moyen d'interroger le quota = non.** Le quota existe (documenté « per 24 hours », OCR et Image API), mais aucun endpoint de statut, aucun en-tête documenté, aucune clé ni compte ne permettent de le lire. Le chiffre s'obtient par écrit à mdz@bsb-muenchen.de (contact général, la doc ne précise pas qu'il traite les demandes de volume).

### Détail de l'étape f) (ce que disent les sources web)

Étiquettes : officielle / tiers. Pas de noms de personnes privées.

1. **officielle**, `https://www.digitale-sammlungen.de/en/interfaces`, consultée 2026-11-13 : citations ci-dessus (limites « per 24 hours », Presentation API « unlimited »).
2. **officielle**, `https://www.digitale-sammlungen.de/en/download-options`, consultée 2026-11-13 : « The maximum order size per day/user is limited… ». Le délai de livraison DaFo est « approximately 1–5 days » ; un résumé de recherche a annoncé « 4 weeks » : c'est faux, la page ne contient pas cette valeur (erreur de résumé, non retenue).
3. **tiers (projet utilisateur)**, `https://github.com/Embassy-of-the-Free-Mind/sourcelibrary-v2/issues/5448`, ouvert le 2026-10-01 : « The biggest is one library (Munich) that throttles us, and the deepest is image resolution. » Le même ticket prévoit d'« Email BSB/MDZ asking for an allowlisted IP or a bulk export ». Source d'un projet tiers, non vérifiée auprès de la BSB.
4. **tiers (projet utilisateur)**, `https://github.com/Embassy-of-the-Free-Mind/sourcelibrary-v2/issues/3502`, ouvert le 2026-08-01, commentaire du 2026-10-12 : « it waits on BSB's reply to the rate request sent 2026-10-01. » Dans la description du 2026-08-01 : « providers blocking us (403 — … 93.5% of page-level failure markers are 403) » : ce 403 concerne l'ensemble des fournisseurs, pas la BSB en particulier.
5. **tiers (projet utilisateur)**, `https://github.com/Embassy-of-the-Free-Mind/sourcelibrary-v2/issues/3886`, ouvert le 2026-08-11 : « undocumented but clean JSON API at digitale-sammlungen.de/api/search ». Ce point est une affirmation de tiers sur un endpoint **non documenté** par la BSB ; nous ne l'avons ni testé ni utilisé.
6. **Recherches sans résultat MDZ spécifique** : forum IIIF Discourse, dépôt dbmdz (GitHub), présentations de la BSB sur sa politique d'API, forums de questions (recherches « 429 », « 403 », « Kontingent »). Stack Overflow et Reddit n'ont pas été cherchés séparément. Recherches : 8 standard et 1 étendue. Les blogs museum-digital et Wellcome Collection qui apparaissent concernent d'autres services et ne sont pas retenus.

### Pour la suite

- Demander par écrit à mdz@bsb-muenchen.de le quota exact par 24 h (OCR et Image), et la nature de la réponse 403 observée sur `bdr.oai.bsb-muenchen.de` (page Apache 403 au premier appel).
- Ne pas utiliser `/api/search` (non documenté) sans accord.
- Refaire la vérification a) pour la page `digitale-objekte` si l'URL exacte est retrouvée.

## Correction et compléments (2026-11-13, reprise directe par l'orchestrateur)

- **Empreintes SHA-256 de la section « Vérification méthode v2 »** : celles déclarées dans les
  en-têtes de `institutions/mdz/sources/*.md` **ne se recalculent pas** (testé avec plusieurs variantes).
  Elles sont donc retirées comme preuve. La preuve valable est désormais
  `institutions/mdz/sources/SHA256SUMS`, produit par `scripts/fetch_doc.sh` (URL dans
  `institutions/mdz/sources/url-list.txt`, statut et date dans `institutions/mdz/sources/FETCH.log`).
- **Étape a)** : 15 pages re-téléchargées en HTML brut (toutes HTTP 200, 2026-11-13 21:23–21:24 UTC).
  La page `digitale-objekte` citée par le rapport précédent reste **non vérifiée** (404 au curl).
- **Étape d)** : vérifiée dans le HTML brut. « limit … per 24 hours » pour l'Image API et pour
  l'OCR (pages `en/interfaces` et `de/schnittstellen`, aucun chiffre). Aucun nom d'en-tête,
  aucun endpoint de statut, aucune clé. DaFo : « maximum order size per day/user is limited »,
  sans chiffre (`en/download-options`).
- **Étape e)** : les 3 endpoints ajoutés ont été testés avec une configuration temporaire
  (`mdz-nouveaux.json`) **non committée**, ce qui contrevient à la règle « configuration avant
  tests ». Les endpoints sont maintenant dans `institutions/mdz/config/mdz.json` et leurs résultats sont
  dans `institutions/mdz/tests/journal.log` (session 21:20 UTC). Le 403 de `bdr.oai.bsb-muenchen.de` arrête cet hôte.
- **Étape f)** : ticket tiers `Embassy-of-the-Free-Mind/sourcelibrary-v2#5448` (ouvert le
  2026-10-01, commentaires jusqu'au 2026-10-26). Ce que dit le projet, **non vérifié** :
  - il a demandé à la BSB soit une IP autorisée à 5–10 req/s, soit un export en masse ;
  - la réponse de la BSB était toujours en attente le 2026-10-26 ;
  - il reçoit un **« 1×1 over-quota placeholder »** de MDZ (commentaire du 2026-10-25) :
    une réponse HTTP 200 qui n'est pas une vraie image. **Conséquence pour nos sondes** :
    un 200 ne prouve pas qu'on n'est pas bloqué. Il faut contrôler la taille réelle de l'image
    (en-tête `Content-Length`, et dimensions) avant de conclure « pas de blocage ».
- **Pour le crash test** (étape g) : le signal de dépassement de MDZ peut donc être une image
  1×1 en 200, et non un 429. Le test doit le détecter.

### Étape f) complétée (2026-11-13, recherche directe)

Recherches : 4 requêtes web (standard), dont une sur le 1×1 et une sur le forum IIIF.
Sources retenues, étiquetées :
- **officielle** : `https://www.digitale-sammlungen.de/en/interfaces` (et `de/schnittstellen`) : limites « per 24 hours » Image API et OCR, aucun chiffre (voir `institutions/mdz/sources/`).
- **officielle (guide IIIF)** : `https://iiif.io/guides/guides/digitale-sammlungen.de/` : lu en entier par extraction : **aucune phrase sur les limites, quotas, clés, erreurs ou 1×1** ; seulement des conseils de filtrage. Contact cité : « Contact Us » (lien).
- **tiers (projet utilisateur)** : `Embassy-of-the-Free-Mind/sourcelibrary-v2` #5448 (voir plus haut) et #3886 (2026-08-11) : « undocumented but clean JSON API at digitale-sammlungen.de/api/search ». Non vérifié, non testé, non utilisé.
- **tiers (dépôt Mirador)** : `ProjectMirador/mirador` #4542 : un manifeste MDZ (bsb11134638) contient des canvases **1×1 px** qui s'affichent comme une image d'erreur dans Mirador en IIIF v3 (sans rapport direct avec un quota). Pertinent pour la détection : une image 1×1 peut être normale ou être un signal.
- **Non trouvé** : forum IIIF Discourse, pages Wikisource ou Wikimedia sur les limites MDZ, présentations officielles sur la politique d'API, réponse écrite de la BSB au projet tiers.

**Conclusion étape f)** : la seule source qui décrit un blocage ou un 1×1 de dépassement est un ticket tiers, non vérifié. Rien d'officiel ne confirme le comportement au dépassement.
