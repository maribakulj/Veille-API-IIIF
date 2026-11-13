# Library of Congress — `loc`

- **Statut** : vérifiée (tests arrêtés à la requête n°2 : 403 Cloudflare, motif écrit dans `tests/loc.log`)
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
| 3 à 5 | — | manifeste, JSON répété, info.json répété | — | non lancés | — | — | — |

Arrêt à la requête 2 (403 = règle « arrêt immédiat »). Le manifeste `www.loc.gov/item/2002700091/manifest.json` n'a pas été testé. Total de requêtes d'appel : 2 (budget 15). Les trois GET de documentation (robots, legal, working-within-limits) et les pages lues par WebFetch sont hors budget d'appel, espacés de 5 s.

## 4. Conclusion sur les limites

- L'API annonce-t-elle ses limites dans la réponse ? **non** (aucun en-tête de limite observé sur la réponse 200 ; le 403 n'en porte pas non plus). **Oui dans la documentation** (page working-within-limits).
- Mécanisme observé : rien de consigné côté en-têtes. Mécanismes **documentés** : blocage après dépassement (1 h, ou 72 h pour MARCXML), 429 et pages CAPTCHA possibles même en dessous des seuils quand le trafic est élevé.
- Valeurs trouvées (quota, fenêtre) : JSON/YAML 20/min ; Text et Image 150/min ; Streaming 60/min ; MARCXML 30/min ; blocage 1 h (72 h MARCXML) ; recommandation logiciel 10 requêtes/min au total ; Crawl-Delay 5 s dans robots.txt ; programmes de plus de 24 h susceptibles d'être arrêtés.
- Blocages rencontrés : 403 avec défi Cloudflare « Just a moment... » sur `www.loc.gov/photos/` au 2e appel de test, 7 s après le premier appel (tile.loc.gov, lui, répond 200). Cause non établie : (a) défi bot déclenché par l'empreinte du client ou par les requêtes de doc précédentes sur www.loc.gov, (b) limitation liée à la charge, ou (c) limitation propre à l'hôte www. Non contourné.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

Les quotas **sont** publiés, dans la documentation. Ce qui manque, c'est la publication dans les réponses.

- Trouvé (avec source) : LoC annonce des chiffres par famille d'API (working-within-limits) ; explique le blocage « to prevent a denial of service » ; dit que la charge peut faire baisser les seuils ; renvoie les limites de l'image service vers la page générale (image-services).
- Hypothèses (étiquetées) :
  - Hypothèse : les en-têtes de limite ne sont pas émis, donc le client doit s'en tenir à la doc et à 429 + pause (cohérent avec la recommandation « add handling to pause when encountering 429 »).
  - Hypothèse : les seuils sont variables (« may decrease »), donc chiffrés en « current rate limits » plutôt que garantis.
  - Hypothèse : le défi Cloudflare sur www.loc.gov est une protection anti-bot générale, pas un quota IIIF.

## 6. Confiance et pistes restantes

- Niveau de confiance : **moyen**. Élevé pour les citations de legal et robots (vérifiées brut). Moyen pour les chiffres du tableau (JSON, Text, Image vérifiés par grep sur la page brute ; Streaming et MARCXML seulement via résumé).
- Ce qui reste à vérifier :
  - Le manifeste IIIF (`www.loc.gov/item/…/manifest.json`) : existence, en-têtes, éventuel 429. À refaire dans une session ultérieure, avec pause ≥ 6 s (le plafond de 10 requêtes/min recommandé impose ≥ 6 s, pas 5 s).
  - Reproduire le 403 Cloudflare plus tard, à rythme lent et sans rafale, pour savoir si c'est systématique sur www.loc.gov ; ne pas insister si le défi reste.
  - Vérifier brut les lignes Streaming et MARCXML de la page working-within-limits.
  - Si besoin de certitude sur les en-têtes : demander à LoC (ask.loc.gov ou contact de la page API) s'ils émettent `X-RateLimit-*` / `Retry-After`.
