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

## 6. Confiance et pistes restantes

- Niveau de confiance : **moyen** sur la doc (chiffres explicites, mais page non datée) ; **faible** sur le comportement réel (un seul appel, 403).
- Ce qui reste à vérifier, et comment :
  1. Lire la page de conditions d'utilisation (403 via cet outil) : à faire depuis un navigateur ordinaire par Marcel, ou à demander à la BnF.
  2. Demander à la BnF (formulaire « Écrire à la BnF » : https://www.bnf.fr/fr/contacter-la-bnf) la date d'entrée en vigueur des limites d'usage et si elles sont annoncées dans les en-têtes.
  3. Re-tester plus tard, à faible débit (≤ 5 appels/min, pauses ≥ 12 s), un manifeste puis un info.json, pour voir si le 403 persiste. Ne pas tester un 429 par rafale (notes locales : connexions coupées après une rafale).
  4. Ne pas utiliser de User-Agent de navigateur pour passer le 403 : contraire à la méthode.
