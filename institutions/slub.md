# SLUB Dresden (Sächsische Landesbibliothek — Staats- und Universitätsbibliothek Dresden) — `slub`

- **Statut** : vérifiée (documentation et recherche élargie faites ; 4 requêtes d'appel sur un budget de 15, arrêt volontaire, motif dans `tests/slub.log`)
- **Pays** : Allemagne
- **Point d'entrée testé** : `iiif.slub-dresden.de` (racine : 200, corps vide) ; manifeste `https://iiif.slub-dresden.de/iiif/2/1741646995-18800000/manifest.json` (200, JSON Presentation 2.x, 583 Ko, 198 vues) ; `info.json` de l'image sur `images.iiif.slub-dresden.de` (200, 910 o)
- **Vérifié le** : 2026-11-13 (tests entre 21:04:59 et 21:06:16 UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://digital.slub-dresden.de/ | 2026-11-13 (WebFetch) | Redirection 301 vers https://sachsen.digital/ ; la page suivie ne mentionne ni API IIIF, ni manifestes, ni quotas, ni conditions d'utilisation (rien trouvé). |
| https://sachsen.digital/ | 2026-11-13 (WebFetch) | Rien trouvé : aucune mention d'API IIIF, de quota, de rate limit ni de conditions d'usage. Liens vers « Hilfe zur Suche », « Datenschutzerklärung », « Impressum », « Erklärung zur Barrierefreiheit » (contenus non lus). |
| https://iiif.slub-dresden.de/ | 2026-11-13 (requête GET n° 1) | Aucune page de documentation : la racine répond 200 avec un corps vide (`Content-Length: 0`). Pas de documentation IIIF trouvée sur cet hôte. |
| Contact pour les conditions d'utilisation (cité par une page de l'université de Heidelberg, https://digi.ub.uni-heidelberg.de/en/wgd/projekt/slub_lizenz.html) | 2026-11-13 (résultat de recherche, non lu en entier) | « for further questions regarding the terms of use as well as the prices for reproductions please contact SLUB directly, at Digital (at) slub-dresden.de » — renvoi à un contact, aucune limite chiffrée. |
| Manifeste de l'exemple (champ `metadata`, rights) | 2026-11-13 (requête n° 2) | Mention de droits : « Rechteinformationen: Public Domain Mark 1.0 » (propre à cet objet, pas à l'API). |

**Aucune doc officielle SLUB sur les quotas, les limites de débit ou les conditions d'usage de l'API IIIF n'a été trouvée.**

## 2. Recherche élargie

- Termes cherchés : « SLUB Dresden IIIF API documentation iiif.slub-dresden.de manifest rate limit » ; « SLUB Dresden digital.slub-dresden.de IIIF Schnittstelle Nutzungsbedingungen API » ; « SLUB Dresden IIIF manifest "iiif.slub-dresden.de" Presentation API Image API documentation » (mode étendu) ; « github slub iiif manifest.json "iiif.slub-dresden.de/iiif/2" example identifier » ; « SLUB Dresden Digitale Sammlungen IIIF Manifest Beispiel ID … Nutzung Lizenz » ; « SLUB Dresden IIIF Schnittstelle Nutzungsbedingungen Fair Use Limit Anfragen … » ; Wayback : `iiif.slub-dresden.de/` (historique, 20 premières captures).
- Sources examinées :
  - README d'une extension MediaWiki tierce (non officielle), https://github.com/tyrann0us/InstantIIIF : donne le motif de manifeste `https://iiif.slub-dresden.de/iiif/2/$1/manifest.json`, un motif d'identifiant `^[0-9]+-[0-9]+$`, SLUB « officiellement supporté », multi-pages « Yes », et une note sur le champ de licence dans `metadata`. C'est la source de l'URL testée. Aucune limite mentionnée.
  - Article SLUB « Größtmögliche Offenheit » (titre trouvé en recherche, non ouvert) : décrit une licence libre pour les objets numérisés ; source secondaire.
  - Wikipédia (résumé de recherche) : plus de 95 000 volumes numérisés, libres d'usage dans les « Digital Collections ».
  - Deutsche Digitale Bibliothek : les mentions de droits varient selon l'objet (Public Domain Mark 1.0, « In copyright », CC BY-SA 4.0) ; à vérifier par objet.
  - Wayback Machine (`iiif.slub-dresden.de/`) : 20 captures de 2021 à 2023, toutes 200, HTML de 300 à 600 octets, empreinte identique sur toutes les captures. Pas de page de documentation archivée, rien sur les limites.
- Résultat : aucune limite publiée trouvée, aucune page de conditions d'usage pour l'API IIIF trouvée. Le seul contact cité est `Digital@slub-dresden.de`.

## 3. Tests d'appel (voir `tests/slub.log`)

| # | Heure UTC | URL (sans identifiant complet) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:04:59 | `iiif.slub-dresden.de/` | GET | 200 | aucun ; `Server: Apache`, `Content-Type: text/html` | corps vide (0 o) | — |
| 2 | 21:05:48 | `iiif.slub-dresden.de/iiif/2/1741646995-18800000/manifest.json` (identifiant tiré de l'exemple du README tiers) | GET | 200 | aucun ; `Content-Type: application/json; charset=utf-8` | Presentation 2.x, 583 231 o, 198 vues, champ `metadata` (Eigentümer : SLUB Dresden) | 48 s |
| 3 | 21:05:59 | `images.iiif.slub-dresden.de/iiif/2/<id image tiré du manifeste>/info.json` | GET | 200 | aucun ; `Content-Type: application/json;charset=utf-8` | Image API 2.x, 1000 × 1461 px, 910 o | — (hôte différent) |
| 4 | 21:06:16 | `iiif.slub-dresden.de/iiif/2/1741646995-18800000/manifest.json` (répétée) | GET | 200 | aucun ; même taille (583 231 o) | identique à n° 2 | 28 s |

Total : 4 requêtes d'appel sur 15. Arrêt volontaire après 4 : aucune limite ni aucun 403/429 observé, et aucune autre URL documentée à tester. Aucun endpoint de recherche n'est documenté par SLUB : **non testé, faute de doc**. Le manifeste complet n'a pas été reparsé au-delà des 198 vues.

Note : la requête n° 2 utilise un identifiant issu de l'exemple du README tiers, non confirmé par SLUB. Il a répondu, donc le motif est fonctionnel, mais l'identifiant n'a pas été vérifié comme officiel.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : **non** (aucune source officielle trouvée ; seul un contact pour les conditions d'utilisation est cité).
- Limite **observée** (429 ou en-tête de quota reçu) : **non** (4 requêtes, aucun en-tête `Retry-After`, `X-RateLimit-*` ou `RateLimit-*`).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : **non** (aucun 403 ; pas de Cloudflare sur les hôtes testés).
- L'API annonce-t-elle ses limites dans la réponse ? **non** (aucun en-tête de limite sur les réponses 200).
- Mécanisme observé : rien (aucun en-tête de quota, aucun 429).
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : aucun. Un seul point d'attention : la racine `iiif.slub-dresden.de/` répond 200 avec un corps vide, sans page d'accueil de documentation.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : aucune explication publiée. Les conditions d'utilisation renvoient à un contact (`Digital@slub-dresden.de`), sans précision sur l'API. La licence libre des objets numérisés est annoncée dans un article SLUB (source secondaire).
- Hypothèses (étiquetées comme telles) :
  - Hypothèse : SLUB ne publie pas de limite parce que l'accès IIIF est traité au cas par cas via le contact de la bibliothèque numérique (non vérifié).
  - Hypothèse : la limite éventuelle est gérée côté serveur sans en-têtes visibles (non vérifié : 4 requêtes seulement).

## 6. Confiance et pistes restantes

- Niveau de confiance : **faible** (documentation SLUB absente, URL de manifeste issue d'un README tiers, 4 requêtes seulement).
- Ce qui reste à vérifier, et comment :
  - Demander par écrit à `Digital@slub-dresden.de` s'il existe une politique d'usage ou un débit recommandé pour l'API IIIF.
  - Vérifier la page de documentation des « Digital Collections » une fois l'adresse exacte connue (non trouvée par la recherche).
  - Refaire un petit lot de requêtes espacées (≥ 6 s) plus tard, pour voir si des en-têtes de quota apparaissent sur un nombre d'appels plus élevé.
  - Confirmer le motif d'identifiant et la liste des objets via un identifiant SLUB officiel (non trouvé).

## 5 bis. Recherche ciblée des quotas (2026-11-13)

a) **Endpoint de statut de quota** : non trouvé — termes cherchés : « SLUB Dresden IIIF API documentation rate limit », « SLUB Dresden IIIF API Nutzung Limit Anfragen Kontakt », « SLUB Dresden digital collections IIIF manifest API terms of use usage limits github ». Conditions d'usage des collections numériques lues le 2026-11-13 (https://nutzungshinweis.slub-dresden.de/en) : aucune mention d'API, de limite, de quota ni d'endpoint de statut. Aucun dépôt GitHub SLUB d'API IIIF trouvé.

b) **En-têtes de limite documentés** : non trouvé — aucun en-tête de limite cité ; les 4 requêtes de la sonde n'en renvoient aucun (tests/slub.log).

c) **Clé d'API ou compte** : non trouvé — aucune clé ni compte mentionné dans les résultats ni dans les conditions lues.

d) **Contact officiel** : **trouvé** — digital@slub-dresden.de. Sources : https://nutzungshinweis.slub-dresden.de/en (lue le 2026-11-13 : « the listed contact is Annika-Valeska Walzel, Digital Library: digital@slub-dresden.de ») ; et la page de conditions citée par Heidelberg (https://digi.ub.uni-heidelberg.de/en/wgd/projekt/slub_lizenz.html, résultat de recherche : « please contact SLUB directly, at Digital (at) slub-dresden.de »). Une adresse générale information@slub-dresden.de apparaît dans un résultat de recherche (non vérifiée sur le site).

Conclusion : moyen d'interroger le quota : **non**. Aucun endpoint, en-tête ni compte documenté ; aucune sonde ciblée lancée (pas de `scripts/config/slub-quota.json`).
