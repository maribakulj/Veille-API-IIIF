# BnF — Gallica (IIIF) — `bnf-gallica`

- **Statut** : vérifiée partiellement (doc et recherche faites ; tests arrêtés après 403 dès la 1re requête)
- **Pays** : France
- **Point d'entrée testé** : https://gallica.bnf.fr/iiif/ark:/12148/btv1b550076223/manifest.json (ark d'exemple publié dans la doc api.bnf.fr ; l'ark `bpt6k9761234x` de `institutions.csv` n'a pas été utilisé, il n'est pas vérifié)
- **Vérifié le** : 2026-11-13 (UTC, entre 20:32 et 20:40)
- **Vérifié par** : agent de veille (Haiku 5.5), session Claude Code

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://api.bnf.fr/fr/node/232 (« API Gallica », BnF API et jeux de données) | 2026-11-13 | « Durant cette phase transitoire, des limites d'usage ont été mises en place sur les API Gallica : » ; « API IIIF Image : 5 appels par minute en mode mode /full/full/ ou full/>1000 pixels. » ; « Bande passante de téléchargement limitée à 832 Ko/s » ; « API .TexteBrut : 5 appels par minute » ; « API .PDF : 4 appels par minute » ; « API image .highres : 50 appels par minute » ; « En cas de dépassement, le code erreur renvoyé est » … « 429 : "Too Many Requests" ». Aucune date de publication ou de mise à jour affichée (seul « © 2020 BnF »). Même page : « La BnF est en train de déployer un gestionnaire d'API. » |
| https://api.bnf.fr/fr/api-iiif-de-recuperation-des-images-de-gallica (fiche technique, « Version 2 ») | 2026-11-13 | Aucune mention de quota, limite ou débit. Renvoie vers « Conditions d'utilisation des contenus de Gallica » (champ Licence). Date affichée : « Date de dernière mise à jour: 2025 ». Exemples : image `.../btv1b90017179/f15/0,1900,2400,1200/full/0/native.jpg`, manifeste `.../btv1b550076223/manifest.json`. |
| https://www.data.gouv.fr/dataservices/api-gallica-iiif | 2026-11-13 | « Son accès est ouvert sans restriction, sauf en cas d'usage abusif. » ; « Limite d'appels non documentée » (signalé comme manque dans la fiche). Pas de date de mise à jour. |
| https://www.bnf.fr/fr/actualites/un-captcha-pour-gallica | 2026-11-13 | « à compter du 18 décembre 2025 » : CAPTCHA « afin de préserver la qualité de service et renforcer la sécurité de Gallica ». Le seul accès cité est la **recherche** (« à chaque première recherche de la journée »). IIIF, texteBrut, API et accès automatisé ne sont pas mentionnés. |
| https://gallica.bnf.fr/html/und/conditions-dutilisation-des-contenus-de-gallica | tentée le 2026-11-13 via WebFetch | **Non lue : 403 Forbidden.** Pas de contournement tenté. |

## 2. Recherche élargie

- Termes cherchés : « Gallica API IIIF documentation quota limite requêtes conditions d'utilisation » ; « gallica.bnf.fr IIIF rate limit 429 captcha » ; « Gallica IIIF manifest 429 Too Many Requests OR "connection reset" OR Retry-After github issue » (mode extended).
- Sources examinées : data.gouv.fr (API Gallica IIIF, API Gallica Document, API Gallica Recherche) ; api.bnf.fr ; bnf.fr (CAPTCHA, portail API) ; bnf.fr CGV (2019, non lu en détail) ; Wikisource « gallica.py » (script communautaire, cité par la recherche : délai d'environ 12 s conseillé en cas de « Too many requests », non vérifié directement) ; README du paquet R `bnfimage` (tiers : une requête toutes les 3 s, non vérifié directement) ; issues GitHub génériques sur les 429 (hors Gallica).
- Résultat : aucune issue GitHub trouvée sur un 429 Gallica IIIF précis. La seule source officielle chiffrée est la page api.bnf.fr/fr/node/232 (voir § 1). Les chiffres des wrappers tiers ne sont pas des sources officielles.

## 3. Tests d'appel (voir `tests/bnf-gallica.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 2026-11-13T20:33:22Z | gallica.bnf.fr/iiif/ark:/…/manifest.json | GET | **403** (HTTP/2, server cloudflare) | aucun Retry-After, X-RateLimit-* ni RateLimit-* | HTML 403, 5662 o, corps non lu | n/a |

Arrêt après la requête 1, conformément à la méthode (403 = arrêt immédiat). Non faits : info.json, requête ALTO, texteBrut, rafale de 5 appels pour voir le 429. Aucun 429, 503 ni captcha observé en test direct.

## 4. Conclusion sur les limites

- L'API annonce-t-elle ses limites dans la réponse ? **non observé** (le seul appel fait a renvoyé 403 sans en-tête de limite).
- Mécanisme observé : 403 Cloudflare sur un GET avec User-Agent honnête (voir § 6). Le mécanisme 429 + limites par minute est **annoncé dans la doc** (api.bnf.fr) mais **non vérifié** par nos appels.
- Valeurs trouvées (doc api.bnf.fr, non datée) : IIIF Image en `full` : 5 appels/min ; IIIF Image en `full >1000 px` : 5 appels/min ; texteBrut : 5 appels/min ; PDF : 4 appels/min ; highres : 50 appels/min ; bande passante de téléchargement : 832 Ko/s. Fenêtre : la minute. Erreur attendue : 429.
- Blocages rencontrés : 403 sur la 1re requête (Cloudflare) ; page des conditions d'utilisation en 403 via WebFetch. Pas de 429 ni de connexion coupée lors de nos tests (un seul appel).

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

Ce n'est pas le cas : les limites **sont** publiées (api.bnf.fr), mais de façon peu visible et sans date.

- Trouvé (avec source) :
  - « des limites d'usage ont été mises en place » pendant « une phase transitoire », avec « un gestionnaire d'API » en cours de déploiement (api.bnf.fr/fr/node/232).
  - Le captcha du 18/12/2025 concerne la recherche, pas le IIIF (bnf.fr, actualité « Un captcha pour Gallica »).
  - Accès « ouvert sans restriction, sauf en cas d'usage abusif » et « Limite d'appels non documentée » (data.gouv.fr, fiche API Gallica IIIF : contradictoire avec api.bnf.fr sur ce point).
- Hypothèses (étiquetées comme telles) :
  - H1 : les limites ne figurent pas dans les réponses car elles sont appliquées par le gestionnaire d'API en cours de déploiement, pas par les serveurs IIIF (non vérifié).
  - H2 : le 403 Cloudflare du test vise les clients scriptés (non vérifié ; le même constat est noté dans les notes locales de Marcel pour Python).
  - H3 : la fiche data.gouv n'a pas été mise à jour après la phase transitoire (hypothèse, date absente des deux sources).

## 5 bis. Recherche ciblée des quotas (2026-11-13)

- a) Endpoint de statut de quota : non trouvé. Termes cherchés : « Gallica API quota endpoint », « gallica rate limit status », « api.bnf.fr gestionnaire d'API clé d'accès quota ». Seule mention : « La BnF est en train de déployer un gestionnaire d'API » (https://api.bnf.fr/fr/node/232, consultée le 2026-11-13). Ce gestionnaire n'est pas décrit comme exposant un statut.
- b) En-têtes de limite : non trouvé. Termes : « RateLimit », « X-RateLimit », « Retry-After » avec « gallica ». Seule source : « En cas de dépassement, le code erreur renvoyé est … 429 : "Too Many Requests" » (https://api.bnf.fr/fr/node/232, 2026-11-13). Aucun nom d'en-tête cité.
- c) Clé d'API ou compte donnant un quota : non trouvé. La fiche data.gouv de l'API Gallica Recherche dit que l'accès est « ouvert sans restriction, sauf en cas d'usage abusif » (https://www.data.gouv.fr/dataservices/api-gallica-recherche, résumé de résultat, non lu brut). Aucune clé n'est exigée dans les sources lues.
- d) Contact officiel : trouvé, partiel. La fiche data.gouv de l'API Gallica IIIF indique « Contact: gallica@bnf.fr » (https://www.data.gouv.fr/dataservices/api-gallica-iiif, vu dans un résumé de résultat le 2026-11-13, non lu brut). Formulaire « Écrire à la BnF » : https://www.bnf.fr/fr/contacter-la-bnf (déjà cité en § 6, non vérifié ici). Aucune procédure de relèvement de quota trouvée.

Conclusion : moyen d'interroger le quota : non. Aucune sonde lancée : aucun endpoint de statut ni en-tête de limite documenté n'a été trouvé. L'hôte gallica.bnf.fr avait déjà répondu 403 anti-bot (§ 3) ; on n'y a pas refait d'essai.

## 6. Confiance et pistes restantes

- Niveau de confiance : **moyen** sur la doc (chiffres explicites, mais page non datée) ; **faible** sur le comportement réel (un seul appel, 403).
- Ce qui reste à vérifier, et comment :
  1. Lire la page de conditions d'utilisation (403 via cet outil) : à faire depuis un navigateur ordinaire par Marcel, ou à demander à la BnF.
  2. Demander à la BnF (formulaire « Écrire à la BnF » : https://www.bnf.fr/fr/contacter-la-bnf) la date d'entrée en vigueur des limites d'usage et si elles sont annoncées dans les en-têtes.
  3. Re-tester plus tard, à faible débit (≤ 5 appels/min, pauses ≥ 12 s), un manifeste puis un info.json, pour voir si le 403 persiste. Ne pas tester un 429 par rafale (notes locales : connexions coupées après une rafale).
  4. Ne pas utiliser de User-Agent de navigateur pour passer le 403 : contraire à la méthode.

## Vérification méthode v2 (2026-11-13, reprise directe)

| Étape | Statut | Preuves |
|---|---|---|
| a) Doc lue en entier | **fait, une page incomplète** | `sources/bnf-gallica/` (5 pages, `SHA256SUMS`, `FETCH.log`) ; `sources/bnf-gallica/suite/` (`node/2620`, `wrapper-python`, `node/2748` **incomplète** : délai dépassé à 7,6 ko sur 21,8 ko, à refaire) ; `sources/bnf-gallica/suite2/` (page « évolution des modalités d'accès » et page « Un captcha pour Gallica »). Page des conditions d'utilisation : **403** à la récupération, non réessayée. |
| b) Endpoints tirés de la doc | **fait** | Pattern IIIF image : `gallica.bnf.fr/iiif/ark:/12148/…/full/0/native.jpg` et manifeste : `gallica.bnf.fr/iiif/ark:/12148/…/manifest.json` (api.bnf.fr, page IIIF). |
| c) Configuration avant tests | **fait** | `scripts/config/bnf-gallica.json` réécrit à partir de la doc (2 endpoints) ; `--dry-run` OK. |
| d) Recherche de quota dans la doc | **fait** | Voir ci-dessous. |
| e) Test de chaque endpoint | **non fait : hôte bloqué** | `gallica.bnf.fr` renvoie 403 anti-bot depuis 20:33Z (premier appel, `tests/bnf-gallica.log`). Règle : on ne réessaie pas un hôte en 403. Les 2 endpoints de la configuration restent non testés. |
| f) Ce que disent les gens sur le web | **fait, à compléter** | Voir ci-dessous. |
| g) Crash test | **à faire après l'audit de toutes les institutions** | — |

### Étape d) — ce que disent les pages officielles

1. **Officiel, ancien** (`https://api.bnf.fr/fr/node/232`, lu le 2026-11-13) : « Durant cette phase transitoire, des limites d'usage ont été mises en place sur les API Gallica » : IIIF Image **5 appels/min** (mode `full/full` ou `full/>1000 px`), TexteBrut **5/min**, PDF **4/min**, highres **50/min**, bande passante **832 Ko/s**, dépassement = **429 « Too Many Requests »**. Pas de date.
2. **Officiel, plus récent** (`https://api.bnf.fr/fr/evolution-des-modalites-dacces-aux-api-de-gallica`, lu le 2026-11-13) : « Dans le cadre du renforcement de la sécurité de ses infrastructures, la BnF a mis en place de nouvelles mesures de protection des services de Gallica. Ces mesures entraînent des restrictions temporaires d'accès aux API de Gallica, notamment aux services IIIF, SRU et API Document. Les modalités d'accès à ces services sont actuellement en cours de définition. » **Donc les chiffres de la page 1 ne décrivent plus l'accès actuel : l'accès IIIF est restreint et ses modalités ne sont pas publiées.**
3. **Officiel** (`https://www.bnf.fr/fr/actualites/un-captcha-pour-gallica`) : « un CAPTCHA est mis en place à compter du 18 décembre 2025 » ; « À chaque première recherche de la journée » une case à cocher. Le captcha concerne la recherche, pas l'IIIF (la page ne le dit pas explicitement).
4. **Officiel** (`https://data.gouv.fr/…api-gallica-iiif`, lu le 2026-11-13) : « Son accès est ouvert sans restriction, sauf en cas d'usage abusif. » et « Limite d'appels non documentée ». **Contradictoire** avec les points 1 et 2 : à signaler, pas à trancher.
5. **Pas de clé, pas de compte, pas d'endpoint de statut, pas d'en-tête documenté** (vérifié dans les pages lues).

**Conclusion étape d)** : moyen d'interroger le quota = **non**. Les chiffres (5/min, 429) existent mais datent d'avant les restrictions annoncées ; la page la plus récente dit que les modalités ne sont pas encore définies.

### Étape f) — sources web (2026-11-13)

- **Officiel** : la page « évolution » et la page captcha ci-dessus.
- **Tiers, presse** : ActuaLitté, « Gallica installe un CAPTCHA : le web patrimonial face aux bots » (`https://actualitte.com/article/128618/numerisation/gallica-installe-un-captcha-le-web-patrimonial-face-aux-bots`) : signale des blocages d'IP jugés très stricts par les utilisateurs. Lu en résumé uniquement.
- **Tiers, presse** : IA Tech au Quotidien (`https://www.iatechauquotidien.com/gallica-paralysee-des-robots-dia-aspirent-massivement-ses-contenus/`) : la BnF attribue les difficultés à une forte hausse du moissonnage automatisé, dont des robots d'IA. Lu en résumé.
- **Tiers, code** : `https://github.com/Antonio-Faure/mnemosyne/pull/69` : documente des **403 de type Cloudflare sur les chemins SRU** de Gallica, et conclut à un blocage **au niveau IP/ASN**, pas à un bug de code. Non vérifié par nous.
- **Tiers, code** : `rekyt/bnfimage` (client R) annonce « au maximum 1 requête toutes les 3 secondes », et le SDK `mdeville/gallica` 250 ms d'écart : chiffres de tiers, contradictoires entre eux et avec la page officielle.
- **Non trouvé** : plainte formelle, fil de forum dédié, réponse écrite de la BnF sur le quota IIIF.
