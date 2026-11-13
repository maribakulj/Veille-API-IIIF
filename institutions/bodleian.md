# Bodleian Libraries (Oxford) — `bodleian`

- **Statut** : vérifiée (documentation lue, recherche élargie faite, 13 requêtes d'appel sur 15, aucun blocage, aucun 429, aucun 403)
- **Pays** : Royaume-Uni
- **Point d'entrée testé** : `https://iiif.bodleian.ox.ac.uk/` (303 vers `/info.json`), `/info.json`, `/iiif/collection/top`, `/iiif/manifest/6dc81588-a83a-4855-8bee-65264f291d73.json` (Presentation v2, et v3 par négociation de contenu), `/iiif/image/f27e28db-0b08-4f16-9bdf-3565f591fb71/info.json` et une vignette `full/200,/0/default.jpg`, puis la recherche documentée `https://digital.bodleian.ox.ac.uk/search/?q=unicorns` (JSON-LD via `Accept`).
- **Vérifié le** : 2026-11-13 (21:04 à 21:0x UTC pour les appels ; documentation consultée entre 21:0x et 21:1x UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://digital.bodleian.ox.ac.uk/developer/iiif | 2026-11-13 (WebFetch, deux passes) | Aucune mention de quota ni de limite de débit. Passage « Harvesting » cité mot pour mot : « You are welcome to harvest our manifests for the purposes of indexing or making our content available in aggregator services. » ; « However, if are expecting to harvest a significant number of manifests, we would ask that you get in touch with us » ; « and let us know. » ; « You can do this by contacting our digital support team, or by adding your e-mail address to the User-Agent string. » ; « We would prefer that you do not download and re-host our images. » (préférence d'usage, pas un chiffre). |
| https://digital.bodleian.ox.ac.uk/developer/data/ | 2026-11-13 (WebFetch) | Pas de quota, pas de limite, pas de politique d'usage. Documente `/search` (paramètres `q`, `fq`, `sort`, `page`, `rows` ∈ {20, 40, 100}), réponse JSON-LD. Aucune authentification décrite pour la recherche. |
| https://digital.bodleian.ox.ac.uk/developer/ | 2026-11-13 (WebFetch) | Liste deux sections seulement (IIIF, Search and Data). Aucune mention de quota. |
| https://digital.bodleian.ox.ac.uk/terms/ | 2026-11-13 (WebFetch) | Aucune phrase sur l'accès automatisé, le scraping, la fréquence ou les quotas. Seule occurrence de « limit » : « We do not exclude or limit in any way our liability to you… ». |
| https://digital.bodleian.ox.ac.uk/faq | 2026-11-13 (WebFetch) | « We also have a public data API. » (sans détail). Pas de mention d'accès automatisé, de limite ni d'usage abusif. |
| https://bodreader.web.ox.ac.uk/…/imaging-services-terms-of-use.pdf | 2026-11-13 (WebFetch puis lecture PDF pages 1-4) | Conditions de réutilisation des images (CC-BY-NC 4.0, usages admis ou interdits, durée des licences). Aucune limite de débit ni de volume de requêtes. Les pages 5 et suivantes n'ont pas été lues. |

Ce qui manque : aucune limite de débit (requêtes/s, /min, /jour) n'est publiée dans les sources consultées. Le seul mécanisme annoncé est un contact préalable pour un moissonnage « significatif ».

## 2. Recherche élargie

- Termes cherchés : « Bodleian Libraries IIIF API documentation rate limit terms of use » ; « Digital Bodleian IIIF API harvesting manifests "get in touch" rate limit 429 github ».
- Sources examinées : pages officielles listées ci-dessus ; spécification IIIF v2.0.0 (adresse de support `digital-bodleian@bodleian.ox.ac.uk`) ; fil iiif-discuss (« Bodleian IIIF Updates ») ; un profil tiers APIs.io (dit qu'il existe une « Change Discovery API », non confirmé par la doc Bodleian) ; des forums Zotero (sans rapport : cartes, pas IIIF).
- Résultat : aucune limite publiée, aucune issue GitHub ni billet rapportant un 429 de l'API Bodleian. La question reste à poser à l'équipe.

## 3. Tests d'appel (voir `tests/bodleian.log`)

| # | Heure UTC | URL (sans identifiant complet) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:04:53 | `iiif.bodleian.ox.ac.uk/` | HEAD | 303 | aucun | redirige vers `/info.json` | — |
| 2 | (log) | `iiif.bodleian.ox.ac.uk/info.json` | GET | 200 | aucun | JSON discovery (446 o) | 51 s après la 1re (21:05:44) |
| 3 | (log) | `iiif.bodleian.ox.ac.uk/iiif/collection/top` | GET | 200 | aucun | collection Presentation v2 (1 592 o) | ≥ 6 s |
| 4 | 21:05:58 | `iiif.bodleian.ox.ac.uk/iiif/manifest/{uuid}.json` (v2) | GET | 200 | aucun | manifeste v2 (239 605 o) | 7 s |
| 5 | 21:06:06 | `iiif.bodleian.ox.ac.uk/iiif/image/{id}/info.json` | GET | 200 | aucun | Image API 2 (1 131 o), 2 363 × 2 363 px | 8 s |
| 6 | (log) | `digital.bodleian.ox.ac.uk/search?q=unicorns` | GET | 301 | aucun | redirige vers `/search/?q=unicorns` | ≥ 6 s |
| 7 | (log) | `digital.bodleian.ox.ac.uk/search/?q=unicorns` | GET | 200 | aucun | page HTML (10 966 o) | ≥ 6 s |
| 8 | (log) | idem, sans `Accept` précis (doublon de la 7, ajouté avant la correction du script) | GET | 200 | aucun | HTML (10 966 o) | ≥ 6 s |
| 9 | (log) | idem avec `Accept: application/ld+json` | GET | 200 | aucun | JSON-LD, `totalItems` = 50 (27 044 o) | ≥ 6 s |
| 10 | (log) | manifeste v3 par négociation (`Accept` Presentation 3) | GET | 200 | aucun | `@context` Presentation 3 (451 694 o) | ≥ 6 s |
| 11 | (log) | `iiif.bodleian.ox.ac.uk/iiif/image/{id}/full/200,/0/default.jpg` | GET | 200 | aucun | JPEG 200 × 200 (24 355 o), `iipsrv/1.3` | ≥ 6 s |
| 12 | (log) | `…/info.json` (répétition de la 5) | GET | 200 | aucun | identique à la 5 | ≥ 6 s |
| 13 | (log) | `digital.bodleian.ox.ac.uk/search/?q=unicorns` JSON-LD (répétition de la 9) | GET | 200 | aucun | identique à la 9 | ≥ 6 s |

Les horaires des appels 2 à 13 sont dans le journal (`tests/bodleian.log`). Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*` n'a été reçu. Aucun 429, aucun 403, aucune page de défi. Total : 13 requêtes (budget 15). Pause minimale observée entre deux requêtes : 6 s (imposée par le script).

Note sur la requête 8 : elle est un doublon ajouté par erreur avant correction du script (le paramètre `Accept` n'était pas transmis). Elle ne change rien aux conclusions.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : **non**. Aucun chiffre de quota ni de débit trouvé. Seule formulation : demande de prendre contact avant un moissonnage « significatif » (https://digital.bodleian.ox.ac.uk/developer/iiif).
- Limite **observée** (429 ou en-tête de quota reçu) : **non**, sur 13 requêtes.
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : **non**.
- L'API annonce-t-elle ses limites dans la réponse ? **non** (aucun en-tête de limite, sur JSON, image ou recherche).
- Mécanisme observé : **rien** (pas de 429, pas d'en-tête de quota).
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : aucun.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la doc IIIF demande de contacter l'équipe pour un moissonnage important (https://digital.bodleian.ox.ac.uk/developer/iiif). Elle indique aussi qu'on peut « ajouter son e-mail au User-Agent » pour se faire connaître. **Ce projet n'ajoute pas d'e-mail** (UA imposé : `VeilleAPIIIF/0.1 …`, sans donnée personnelle) ; c'est un choix de la veille, pas un refus de la doc. La FAQ ne mentionne aucune limite.
- Hypothèses (étiquetées) :
  - Hypothèse : pas de quota publié parce que le moissonnage est traité au cas par cas (par contact), et non par seuil technique. Cohérent avec la phrase « get in touch ».
  - Hypothèse : la faible charge des manifestes et des vignettes IIIF rend un seuil inutile à ce stade. Non vérifié.

## 6. Confiance et pistes restantes

- Niveau de confiance : **moyen**. Élevé sur « aucun quota publié dans les sources lues » (plusieurs pages lues, dont la spec). Moyen sur « aucun en-tête de limite » (13 requêtes seulement, pas de rafale testée).
- Ce qui reste à vérifier, et comment :
  - Demander à `digital-bodleian@bodleian.ox.ac.uk` (adresse de la spec) s'il existe une limite de débit, et quel volume est acceptable pour un moissonnage de manifestes. Le message doit venir de l'utilisateur, avec son propre e-mail ; la veille ne l'envoie pas.
  - Lire la suite du PDF des conditions d'imagerie (pages 5 et plus) et la page « API Documentation » complète pour l'image API (section cachée par WebFetch).
  - Vérifier la « Change Discovery API » évoquée par un tiers (APIs.io) : non confirmée par la doc Bodleian, ne pas la compter.
  - Test de rafale (non fait, hors budget ou contraire à la prudence) : seulement si l'équipe répond que c'est acceptable.
