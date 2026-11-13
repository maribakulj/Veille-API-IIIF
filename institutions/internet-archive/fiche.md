# Internet Archive — `internet-archive`

- **Statut** : vérifiée (doc, recherche élargie, tests faits ; Wayback non sondée)
- **Pays** : États-Unis
- **Point d'entrée testé** : `https://iiif.archive.org/iiif/img-8664_202009/manifest.json` (Presentation 3), `https://iiif.archive.org/image/iiif/2/img-8664_202009%2fIMG_8664.jpg/info.json` (Image 2) ; API de recherche `https://archive.org/advancedsearch.php` ; métadonnées `https://archive.org/metadata/<id>`. Ancien domaine `https://iiif.archivelab.org/` testé : échec TLS.
- **Vérifié le** : 2026-11-13 (UTC, environ 20:33 à 20:35)
- **Vérifié par** : agent de veille (Haiku 5.5), session Claude Code

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://archive.org/developers/bots.html (section « Rate Limiting ») | 2026-11-13 | « Automated tools should respect rate limits: » ; « Add delays between requests for bulk operations » ; « Honor `429 Too Many Requests` responses and `Retry-After` headers » ; « Consider using GNU Parallel with `-j` to limit concurrent requests » ; exemple « Limit to 4 concurrent downloads with 1 second delay ». **Aucun chiffre** (pas de req/s, pas de quota). 503 non mentionné. |
| https://archive.org/developers/md-write.html (« Rate limits », Item Metadata API Write) | 2026-11-13 | « Users are limited in the number of tasks they may submit over a period of time. » ; « Clients should be prepared to receive a `429 Too Many Requests` HTTP response » ; « The server may return a `Retry-After` header with the response. » ; « The client may use this value as a suggestion for the amount of time to pause. » Pas de chiffre. Concerne l'écriture de métadonnées / tâches, pas la lecture. |
| https://archive.org/developers/md-read.html | 2026-11-13 | Pas de section « Rate limits ». Rien sur 429 / 503 / débit. |
| https://archive.org/developers/index-apis.html | 2026-11-13 | Liste les APIs (dont « Bots, LLMs, and Automated Access ») ; sections « Rate Limiting » (bots), « Use Limits » (ias3), « Rate limits » (Item Metadata Write). Ne documente ni advancedsearch ni le CDX Wayback par leur nom. |
| https://archive.org/developers/internetarchive/updates.html (bibliothèque Python `internetarchive`) | 2026-11-13 | 5.6.0 (2025-10-10) : « Added support for the Retry-After HTTP header to improve handling of rate-limited API responses. » ; 5.2.0 (2025-01-10) : « Fixed bug where failed requests to IA-S3 check_limit API would be treated as a 503 slowdown error. » ; 0.7.0 (2014-07-23) : « Added support for retry on S3 503 SlowDown errors. » Montre que le S3 d'archive.org renvoie des 503 « SlowDown » (ias3), sans seuil publié. |
| https://archive.org/about/terms.php | 2026-11-13 | La page récupérée ne contenait que le titre : aucune clause sur l'accès automatisé, le débit ou les limites n'a pu être lue. **À relire manuellement.** |
| https://archive.org/details/termsofuse | 2026-11-13 | HTTP 404 (récupération via l'outil WebFetch). Non exploitable. |
| https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/ (Mark Graham, 15/09/2026) | 2026-11-13 | « has been hit by waves of high-volume automated traffic, and we've put protections in place to keep the service running. » ; « we rewrote the message you see when a request is blocked with a 429 error » ; « Those protections sometimes catch real people by mistake. » ; « If you think you were blocked in error, email info@archive.org ». **Ne mentionne aucun chiffre ni quota.** Concerne le Wayback Machine. |

Terme « fair use » : une synthèse tierce (Jentic) écrit que archive.org applique un « fair-use throttling » sans quota publié. Ce n'est pas la doc d'archive.org (voir §2).

## 2. Recherche élargie

- Termes cherchés : « archive.org API rate limit 503 too many requests advancedsearch metadata » ; « Internet Archive Terms of Use fair use API limits developers » ; « archivelab iiif.archivelab.org info.json IIIF Internet Archive ».
- Sources examinées : résultats de recherche web (agrégateurs et billets tiers, non retenus comme source primaire) ; billet IIIF officiel du 18/09/2023 (https://blog.archive.org/2023/09/18/making-iiif-official-at-the-internet-archive/) ; pages doc `archive.org/developers/*` citées au §1 ; billet Wayback du 15/09/2026. Articles tiers mentionnant un « Aitratelimit@archive.org » (message 429 d'archive.org) : non confirmés par une source officielle, adresse non testée.
- Billet 18/09/2023 (IIIF), citations exactes : « graduate the service from the iiif.archivelab.org domain to iiif.archive.org » ; « the IIIF API will move to the iiif.archive.org domain » ; « we strongly recommend using the iiif.archive.org endpoint ». Ce billet **ne mentionne aucune limite de débit**.
- Open Library (service de l'Internet Archive, hors périmètre) : sa doc dit « Violations may result in aggressive rate limiting or blocking » ; ce n'est pas l'API archive.org et n'est pas testée.
- Résultat : **aucun quota chiffré** trouvé pour les APIs archive.org (advancedsearch, metadata, IIIF) dans les sources primaires. Les seules consignes sont qualitatives (pauses, respect de 429 / Retry-After, concurrence limitée).

## 3. Tests d'appel (voir `institutions/internet-archive/tests/journal.log`)

10 requêtes GET directes (budget 15), UA honnête, pause de 6 à 14 s entre requêtes.

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 20:33:45 | iiif.archivelab.org/.../info.json | GET | échec TLS (000) | aucun | certificat non valide pour le nom d'hôte ; pas de `-k` | - |
| 2 | 20:33:56 | iiif.archive.org/iiif/…/info.json | GET | 302 | aucun | redirige vers le endpoint Image 2 | 11 s |
| 3 | 20:34:05 | iiif.archive.org/image/iiif/2/…/info.json | GET | 200 | aucun | JSON Image 2, Cantaloupe 5.0.6, 4032 × 3024 | 9 s |
| 4 | 20:34:14 | archive.org/advancedsearch.php (q mal ciblé, rows=1) | GET | 200 | aucun | numFound 0 (erreur de requête de ma part) | 9 s |
| 5 | 20:34:23 | archive.org/metadata/ (id vide) | GET | 200 | aucun | `{"error":"missing identifier"}` | 9 s |
| 6 | 20:34:33 | archive.org/advancedsearch.php (mediatype:texts, rows=1) | GET | 200 | aucun | numFound 53 174 561 ; 247 o | 10 s |
| 7 | 20:34:43 | archive.org/metadata/ddd_010120427_mpeg21 | GET | 200 | aucun | JSON item, 6838 o | 10 s |
| 8 | 20:34:53 | iiif.archive.org/iiif/…/manifest.json (suivi de redirection) | GET | 200 | aucun | IIIF Presentation 3, 3027 o | 10 s |
| 9 | 20:35:07 | archive.org/advancedsearch.php (répétition de 6) | GET | 200 | aucun | 247 o | 14 s |
| 10 | 20:35:14 | idem 9 | GET | 200 | aucun | 247 o | 7 s |

Aucun 429, 503, 403, ni connexion coupée sur les 10 requêtes. Aucun en-tête `X-RateLimit-*`, `RateLimit-*` ou `Retry-After` sur les réponses testées. Le seul `Retry-After: 3600` observé l'a été sur une 404 renvoyée à l'outil WebFetch (consultation de doc), pas sur nos requêtes directes ; à ne pas interpréter comme un quota.

## 4. Conclusion sur les limites

- L'API annonce-t-elle ses limites dans la réponse ? **non** (sur les 10 réponses testées, aucun en-tête de quota).
- Mécanisme observé : aucun. Mécanismes documentés ailleurs : 429 + `Retry-After` (consignes bots, doc Tasks/metadata write) ; 503 « SlowDown » côté S3 (ias3, bibliothèque Python) ; blocage par protections anti-trafic pour le Wayback (billet 15/09/2026, message 429 réécrit).
- Valeurs trouvées (quota, fenêtre) : **aucune**. Ni chiffre de req/s, ni quota journalier, ni fenêtre publiée pour les APIs testées.
- Blocages rencontrés : échec TLS sur l'ancien domaine `iiif.archivelab.org` (non contourné). Rien d'autre.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

Les limites ne sont pas chiffrées, ce qui est cohérent avec la situation trouvée :

- Trouvé (avec source) : la doc bots recommande de « respect rate limits » sans chiffre ; le billet Wayback du 15/09/2026 parle de « protections » contre le trafic automatisé massif, sans seuil ; la doc Python ne documente que la réaction (Retry-After, 503 SlowDown) ; le domaine IIIF est en migration vers `iiif.archive.org` (billet 18/09/2023).
- Hypothèses (étiquetées comme telles) :
  - Hypothèse : archive.org préfère une régulation adaptative (protections, 429 en cas de trafic anormal) plutôt qu'un quota publié. Le billet 2026 suggère qu'un seuil existe côté Wayback, mais il n'est pas public.
  - Hypothèse : les protections frappent surtout les IP VPN / Tor et les DNS tiers (commentaires du billet 2026), donc un test depuis une IP différente pourrait donner d'autres résultats. Non testé.
  - Hypothèse : le `Retry-After: 3600` vu sur une 404 de doc n'est probablement pas une limite d'API, mais je ne peux pas l'exclure.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

- a) Endpoint de statut de quota : partiel. Termes : « archive.org API rate limit status endpoint », « archive.org developers rate limits ». L'API Tasks (https://archive.org/developers/tasks.html, résumé de résultat 2026-11-13) indique le « task limit » et le nombre de tâches en vol de l'utilisateur. Elle exige les clés S3 du compte (accès authentifié) : non sondée. Le `check_limit` de ias3 (https://archive.org/developers/ias3.html) est un test de congestion de l'écriture, avec clé et bucket ; ce n'est pas un quota, et il n'est pas sondé.
- b) En-têtes de limite : trouvé, mais dans une doc datée. La doc IIIF v1 alpha (https://iiif.archivelab.org/iiif/documentation, résumé de résultat 2026-11-13, non lue brut) cite « X-RateLimit-Limit », « X-RateLimit-Remaining », « X-RateLimit-Reset ». La même source la présente comme datée. L'hôte iiif.archivelab.org a déjà échoué en TLS (config internet-archive.json) : non vérifié. Côté doc actuelle, https://archive.org/developers/bots.html dit « Honor `429 Too Many Requests` responses and `Retry-After` headers » (§ 1) ; aucun en-tête de quota nommé. Retry-After est aussi cité dans https://archive.org/developers/md-write.html et dans les notes de version 5.6.0 de la bibliothèque `internetarchive` (2025-10-10).
- c) Clé d'API ou compte donnant un quota : trouvé, partiel. Les clés S3 se trouvent sur https://archive.org/account/s3.php (cité par la doc ias3 et Tasks, résumé 2026-11-13). Elles donnent accès à ias3 et à l'API Tasks. Aucun quota de compte n'est publié. Ne pas confondre avec Archive API v2 (app.archive.com), service distinct avec quotas par plan : hors périmètre.
- d) Contact officiel pour un quota : non trouvé. Termes : « archive.org API quota request increase contact ». Le seul contact cité est info@archive.org, pour un blocage 429 jugé erroné (https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/, 15/09/2026, déjà en § 1). Aucun formulaire de relèvement.

Conclusion : moyen d'interroger le quota : oui, partiellement (API Tasks, « task limit » et tâches en vol) mais elle exige les clés S3 du compte : NON exécuté (aucune clé demandée ni utilisée). Pour les API lues testées (advancedsearch, metadata, IIIF) : non. Les en-têtes X-RateLimit de la doc IIIF v1 restent non vérifiés.

## 6. Confiance et pistes restantes

- Niveau de confiance : **moyen** (pour l'absence de chiffres, élevé ; pour le comportement réel sous charge, faible : 10 requêtes espacées seulement).
- Ce qui reste à vérifier :
  - Relire manuellement https://archive.org/about/terms.php (le contenu récupéré était vide) et la page « Terms of Use » pour une clause sur l'accès automatisé.
  - Demander à info@archive.org (ou à l'adresse de contact indiquée dans la doc) s'il existe un débit recommandé pour advancedsearch / metadata / IIIF. Adresse non testée ici.
  - Test de charge léger et espacé (plusieurs minutes), en surveillant 429 / 503 / Retry-After : à ne faire qu'avec accord, en respectant les règles de prudence.
  - Sonder l'endpoint Wayback CDX (non fait : aucune requête directe Wayback ; l'outil MCP `ia_find_snapshots` a été refusé pour paramètre manquant `mode`).
  - Vérifier si `iiif.archivelab.org` redevient joignable ou si le redirect annoncé en 2023 est fermé (échec TLS constaté le 13/11/2026).
