# Library of Congress — `loc`

- **Statut** : vérifiée (session du 13/11 : familles JSON en 403 anti-bot, Text/Image/Streaming/Media en 200, MARCXML en timeout ; détail dans `tests/loc.log` et section 3)
- **Pays** : États-Unis
- **Point d'entrée testé** : `tile.loc.gov/image-services/iiif/{id}/info.json` (OK, 200) ; `www.loc.gov/photos/?q=anacostia&fo=json` (403, défi Cloudflare)
- **Vérifié le** : 2026-11-13 (20:34 UTC pour les tests ; documentation consultée entre 20:2x et 20:3x UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://www.loc.gov/apis/json-and-yaml/working-within-limits/ | 2026-11-13 | « Rate limiting is strongly encouraged. » ; « Requests that exceed the rate which loc.gov can successfully accommodate will be blocked to prevent a denial of service. » ; « Users may want to add handling to pause when encountering 429 status codes and HTML CAPTCHA responses. » ; « The current rate limits are: » — **JSON/YAML API : 20 requêtes par minute, blocage 1 heure** ; **Text Services : 150/min, 1 h** ; **Image Services : 150/min, 1 h** ; Streaming Services : 60/min, 1 h (lu via résumé WebFetch, non vérifié brut) ; MARCXML lccn.loc.gov : 30/min, 72 h (idem). « The countdown will reset any time a request is made during the block period. » ; « When the API is experiencing especially heavy traffic load, rate limits may decrease and users may encounter 429 status codes or HTML pages with CAPTCHAs even when operating below the rates listed below. » ; « The API is accessible to the public with no API key or authentication required. » |
| https://www.loc.gov/legal/ (section Security) | 2026-11-13 (vérifié brut par curl) | « We reserve the right to block IP addresses that fail to honor our websites' robot.txt files, or submit requests at a rate that negatively impacts service delivery to patrons. Current guidelines recommend that software programs submit a total of no more than 10 requests per minute to our applications, regardless of the number of machines used to submit requests. We also reserve the right to terminate programs that require more than 24 hours to complete. » |
| https://www.loc.gov/robots.txt | 2026-11-13 (vérifié brut par curl) | Bloc `User-agent: *` : « Crawl-Delay: 5 » ; Disallow sur `/search`, `/pictures/search`, `/pictures/related`, `/cgi-bin/`, etc. ; `Sitemap: https://www.loc.gov/sitemap.xml`. Blocs spécifiques pour 008, Baiduspider, Baiduspider-image : Disallow: / |
| https://www.loc.gov/apis/micro-services/image-services/ | 2026-11-13 (WebFetch) | Base IIIF : `https://tile.loc.gov/image-services/iiif/{identifier}` ; info.json = base + `/info.json`. Pour les limites : « For rate limits, see » → renvoie à la page working-within-limits. Aucune valeur chiffrée sur cette page. |
| https://www.loc.gov/apis/ | 2026-11-13 (WebFetch) | Rien trouvé sur les quotas, le throttling ni les restrictions d'usage. Mention de « JSON format » sans paramètre `format=json` décrit sur la page. |

Phrases citées avec l'URL ci-dessus : « 10 requests per minute » (legal) et « 20 requests per minute » (working-within-limits) coexistent. La page legal parle de « current guidelines » pour les logiciels en général ; la page working-within-limits donne le plafond par famille d'API.

## 2. Recherche élargie

- Termes cherchés : « loc.gov API rate limit 429 » ; « Library of Congress IIIF iiif.loc.gov documentation rate limit request limit » ; « loc.gov API 429 Too Many Requests Library of Congress rate limit github issue » ; « Library of Congress IIIF manifest loc.gov item manifest.json X-RateLimit headers ».
- Sources examinées : page working-within-limits (officielle) ; pages LoC legal et robots (officielles) ; résultats de recherche. Un MCP tiers (glama.ai, non officiel) décrit le plafond de 20/min, un blocage d'une heure après 429 et un espacement d'environ 3,1 s. Une issue GitHub du dépôt `LibraryOfCongress/api.congress.gov` (#207, mars 2024) concerne un défi JavaScript 429 sur les textes de projets de loi : c'est **une autre API** (Congress.gov), pas loc.gov.
- Résultat : aucune issue GitHub ni billet ne rapporte un 429 loc.gov spécifique. Aucune mention trouvée d'en-têtes `X-RateLimit-*`, `RateLimit-*` ou `Retry-After` pour loc.gov ou tile.loc.gov dans la doc ou la recherche.

## 3. Tests d'appel (voir `tests/loc.log`)

| # | Heure UTC | URL (sans identifiant complet) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 20:34:02 | `tile.loc.gov/image-services/iiif/service:sgp:…:0202/info.json` (identifiant tiré de l'exemple de la doc image-services) | GET | 200 | aucun ; présents : `content-type: application/json`, `cf-cache-status: MISS`, `server: cloudflare` | JSON IIIF Image (contexte iiif.io/api/image/2) ; 1 442 octets | — |
| 2 | 20:34:09 | `www.loc.gov/photos/?q=anacostia&fo=json` | GET | **403** | aucun ; `cf-mitigated: challenge` | Page HTML « Just a moment... » (défi Cloudflare) ; 5 698 octets | 7 s |
| 3 | 21:06:10 | `www.loc.gov/search/?q=anacostia&fo=json` (famille JSON, URL différente, 1 seul essai) | GET | **403** | aucun ; `cf-mitigated: challenge` | « Just a moment... » ; 5 698 octets | — (1re requête de cette session) |
| 4 | 21:06:17 | `www.loc.gov/item/powmia/pwmaster_103790/?fo=json&at=item,resources` (famille JSON, 2e URL, dernier essai JSON) | GET | **403** | aucun ; `cf-mitigated: challenge` | « Just a moment... » ; 5 821 octets | 7 s |
| 5 | 21:06:24 | `www.loc.gov/apis/micro-services/text-services/` (doc, hors famille API, lue pour trouver l'exemple) | GET | 200 | aucun | page HTML ; 57 962 octets | 7 s |
| 6 | 21:06:31 | `tile.loc.gov/text-services/word-coordinates-service?segment=…/sn82016014/…/0753.xml&format=alto_xml&full_text=1` (exemple de la doc Text Services) | GET | 200 | aucun ; `content-type: application/json`, `cf-cache-status: HIT` | JSON texte ; 31 805 octets | 7 s |
| 7 | 21:06:38 | `tile.loc.gov/image-services/iiif/…:0202/info.json` (même URL que n°1, en-tête complet) | GET | 200 | aucun ; `content-type: application/json`, `cf-cache-status: HIT` | JSON IIIF Image ; 1 442 octets | 7 s |
| 8 | 21:06:45 | `tile.loc.gov/image-services/iiif/…:0202/full/pct:10/0/default.jpg` (vignette) | GET | 200 | aucun ; `content-type: image/jpeg` | JPEG ; 45 360 octets | 7 s |
| 9 | 21:06:52 | `www.loc.gov/apis/micro-services/streaming-services/` (doc, hors famille API) | GET | 200 | aucun | page HTML ; 62 397 octets | 7 s |
| 10 | 21:06:59 | `tile.loc.gov/streaming-services/iiif/service:mbrs:ntscrm:01991429:01991429/full/,256/0/82,0/default.jpg` (exemple de la doc Streaming) | GET | 200 | aucun ; `content-type: image/jpeg`, `cf-cache-status: HIT` | JPEG ; 13 745 octets | 7 s |
| 11 | 21:07:06 | `tile.loc.gov/storage-services/service/frd/pwmia/49/103790.gif` (exemple cité dans la doc working-within-limits) | GET | 200 | aucun ; `content-type: image/gif` | GIF ; 29 776 octets | 7 s |
| 12 | 21:07:15 | `lccn.loc.gov/sn82016014/marcxml` (LCCN présent dans l'exemple de la doc Text Services) | GET | **aucune réponse** : timeout curl à 30 s (code ERR28) | aucun (aucun en-tête reçu) | 0 octet | 9 s |
| 13 | 21:07:57 | même URL que n°12 (nouvel essai unique après timeout) | GET | **aucune réponse** : timeout à 30 s (ERR28) | aucun | 0 octet | 42 s |

Notes : le LCCN `sn82016014` n'est pas tiré de la page des limites mais de l'exemple de la doc Text Services (chemin NDNP). Après le timeout n°13, aucun nouvel essai MARCXML. Les requêtes n°1 et n°2 sont celles du test précédent (20:34 UTC). Cette session : 11 requêtes d'appel ou de doc (n°3 à n°13), dont 2 lectures de doc (n°5, n°9) ; si l'on compte aussi n°1 et n°2, le total est de 13, soit une de plus que le plafond de 12 : le n°13 (nouvel essai MARCXML) a été fait en pensant le budget non atteint. Aucune requête n'a reçu de 429, de CAPTCHA ou de corps de blocage autre que le défi Cloudflare. Pause : 7 s minimum entre deux requêtes (9 s et 42 s pour les deux MARCXML).

## 4. Conclusion sur les limites

- L'API annonce-t-elle ses limites dans la réponse ? **non, observé** : aucun en-tête de limite (`X-RateLimit-*`, `RateLimit-*`, `Retry-After`) sur les 8 réponses 200 reçues (n°1, n°5 à n°8, n°9 à n°11) (Text, Image, Streaming, Media, pages doc comprises). Les 403 n'en portent pas non plus. MARCXML : pas de réponse, donc rien à dire. **Oui dans la documentation** (page working-within-limits).
- Limite **observée** (429 ou en-tête de quota) : **non**. Aucun 429, aucun CAPTCHA, aucun `Retry-After` pendant les 13 requêtes (2 de la session précédente comprises).
- Accès refusé à ce client (403 anti-bot) : **oui**, famille JSON/YAML uniquement. Requêtes n°2 (photos, 20:34 UTC), n°3 (search, 21:06 UTC) et n°4 (item, 21:06 UTC), toutes avec `cf-mitigated: challenge`. Ce n'est pas une limite de débit : c'est un refus de notre client sur ces URL `fo=json`. Constat **observé** : les pages doc sur `www.loc.gov/apis/...` (n°5, n°9), appelées 7 s après le 403 n°4, ont répondu 200 sans défi, donc le défi ne vise pas tout l'hôte www. Pourquoi les URL `fo=json` sont visées : **non vérifié**.
- Mécanisme observé : aucun en-tête de quota ; un défi Cloudflare sur les URL JSON ; rien d'autre. Mécanismes **documentés** (non observés) : blocage après dépassement (1 h, ou 72 h pour MARCXML), 429 et pages CAPTCHA possibles même sous les seuils quand le trafic est élevé.
- Valeurs trouvées (quota, fenêtre, documentées) : JSON/YAML 20/min ; Text et Image 150/min ; Streaming 60/min ; Media `/storage-services/` 150/min ; MARCXML 30/min ; blocage 1 h (72 h MARCXML) ; recommandation logiciel 10 requêtes/min au total ; Crawl-Delay 5 s dans robots.txt ; programmes de plus de 24 h susceptibles d'être arrêtés.
- Familles testées avec 200 (Text, Image, Streaming, Media) : aucune limite observée, à des rythmes de 1 requête toutes les 7 s. Le seuil de 150/min n'a donc pas été approché (non vérifié au-delà).
- Blocages rencontrés : 403 Cloudflare « Just a moment... » sur les URL JSON (n°2, n°3, n°4). MARCXML (n°12, n°13) : aucune réponse, timeout à 30 s, cause non établie (réseau ou serveur lent ; ce n'est ni un 429 ni un 403 reçu). Rien n'a été contourné ; aucun User-Agent navigateur ni changement d'IP.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

Les quotas **sont** publiés, dans la documentation. Ce qui manque, c'est la publication dans les réponses.

- Trouvé (avec source) : LoC annonce des chiffres par famille d'API (working-within-limits) ; explique le blocage « to prevent a denial of service » ; dit que la charge peut faire baisser les seuils ; renvoie les limites de l'image service vers la page générale (image-services).
- Hypothèses (étiquetées) :
  - Hypothèse : les en-têtes de limite ne sont pas émis, donc le client doit s'en tenir à la doc et à 429 + pause (cohérent avec la recommandation « add handling to pause when encountering 429 »).
  - Hypothèse : les seuils sont variables (« may decrease »), donc chiffrés en « current rate limits » plutôt que garantis.
  - Hypothèse : le défi Cloudflare sur www.loc.gov est une protection anti-bot générale, pas un quota IIIF.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

- a) Endpoint de statut de quota : non trouvé. Termes : « loc.gov API rate limit status endpoint », « loc.gov rate limit status ». La page officielle https://www.loc.gov/apis/json-and-yaml/working-within-limits/ ne décrit aucun endpoint de statut. Les seuls résultats qui en parlent sont des outils tiers, non officiels.
- b) En-têtes de limite : non trouvé dans la doc officielle. Termes : « RateLimit-Remaining », « Retry-After », « loc.gov ». La page working-within-limits ne nomme aucun en-tête (« Users may want to add handling to pause when encountering 429 status codes and HTML CAPTCHA responses »). Aucun en-tête de limite observé (§ 4). Un billet tiers (issue cyanheads/libofcongress-mcp-server #54 sur GitHub, 2026) décrit des 429 et CAPTCHA sans en-tête : source non officielle.
- c) Clé d'API ou compte : non trouvé. Phrase officielle : « The API is accessible to the public with no API key or authentication required. » (https://www.loc.gov/apis/json-and-yaml/working-within-limits/, consultée le 2026-11-13). Aucun compte ne donne de quota plus élevé cité.
- d) Contact officiel pour un quota : non trouvé. Termes : « ask.loc.gov IIIF API rate limit increase request contact ». Aucun formulaire de relèvement cité. Les pages https://www.loc.gov/apis/ et https://www.loc.gov/apis/micro-services/image-services/ ne donnent pas de contact pour cela (§ 1).

Conclusion : moyen d'interroger le quota : non. Aucune sonde lancée : aucun endpoint de statut ni en-tête documenté trouvé. Les URL www.loc.gov en JSON sont déjà en 403 anti-bot (§ 3) ; pas de nouvel essai.

## 6. Confiance et pistes restantes

- Niveau de confiance : **moyen**. Élevé pour les citations de legal et robots (vérifiées brut). Moyen pour les chiffres du tableau (JSON, Text, Image vérifiés par grep sur la page brute ; Streaming et MARCXML seulement via résumé).
- Ce qui reste à vérifier :
  - Le manifeste IIIF (`www.loc.gov/item/…/manifest.json`) : existence, en-têtes, éventuel 429. À refaire dans une session ultérieure, avec pause ≥ 6 s (le plafond de 10 requêtes/min recommandé impose ≥ 6 s, pas 5 s).
  - Reproduire le 403 Cloudflare plus tard, à rythme lent et sans rafale, pour savoir si c'est systématique sur www.loc.gov ; ne pas insister si le défi reste.
  - Vérifier brut les lignes Streaming et MARCXML de la page working-within-limits.
  - Si besoin de certitude sur les en-têtes : demander à LoC (ask.loc.gov ou contact de la page API) s'ils émettent `X-RateLimit-*` / `Retry-After`.
