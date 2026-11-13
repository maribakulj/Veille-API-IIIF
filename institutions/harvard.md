# Harvard Library — `harvard`

- **Statut** : vérifiée partiellement (doc et recherche faites ; tests faits, 9 requêtes GET sur 4 hôtes ; aucun 403, aucun 429)
- **Pays** : États-Unis
- **Point d'entrée testé** : https://iiif.lib.harvard.edu/ (racine : 404 « Cannot GET / ») ; manifeste de test `https://iiif.lib.harvard.edu/manifests/ids:11927378` (identifiant d'exemple publié dans la page Harvard Library « iiif manifests digital objects », cf. § 2 ; voir § 3)
- **Vérifié le** : 2026-11-13 (UTC, 21:05 à 21:07)
- **Vérifié par** : agent de veille (Haiku 5.5), session Claude Code

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://library.harvard.edu/services-tools/iiif-manifests-digital-objects (page Harvard Library, IIIF manifests) | 2026-11-13 | Rien sur quota, débit ni conditions d'usage automatisé. Seul pied de page lu : « Except where otherwise noted, this work is subject to a Creative Commons Attribution 4.0 International License ». Pas de date de page. |
| https://harvardwiki.atlassian.net/wiki/spaces/LibraryStaffDoc/pages/43392530/IIIF+Redesign (wiki interne Harvard Library, lu via WebFetch) | 2026-11-13 | « aucune mention » de limitation de débit, throttling ou quota. Page tronquée (navigation seule), accessible à qui a le lien ; statut public incertain. |
| https://iiif.lib.harvard.edu/ (racine du serveur) | 2026-11-13 | Pas de documentation : la racine répond 404 « Cannot GET / » (test, cf. § 3). |
| https://library.harvard.edu/terms-use (conditions d'utilisation supposées) | 2026-11-13 | **404** via WebFetch. Aucune page de conditions trouvée à cette adresse. |
| Recherche : LibraryCloud (api.lib.harvard.edu), fiche wiki « LibraryCloud » (harvardwiki) | 2026-11-13 | **Extrait de recherche, non lu en entier** : « LibraryCloud metadata is openly available to the public » ; un répertoire d'API tiers (apievangelist) cite une entrée « rate limits » pour Harvard sans chiffre visible. Rien de chiffré trouvé. |

## 2. Recherche élargie

- Termes cherchés : « Harvard Library IIIF API documentation rate limit quota iiif.lib.harvard.edu » ; « iiif.lib.harvard.edu manifests view drs example manifest URL documentation » ; « Harvard LibraryCloud API v2 documentation limit rate usage terms api.lib.harvard.edu ».
- Sources examinées : pages Harvard (iiif.harvard.edu « About IIIF », « Harvard Library » ; library.harvard.edu « iiif manifests digital objects » ; wiki interne « IIIF Redesign », « Harvard Library Viewer », « LibraryCloud », « LibraryCloud Metadata ») ; répertoires tiers (apis.io, apievangelist) ; compte rendu code4lib 2023 (titre seulement).
- Résultat : aucune limite de débit IIIF documentée trouvée. Un rapport de projet de 2013 (Harvard Library Lab, PDF, extrait de recherche non lu en entier) listait comme travail restant « implement rate limit throttling for authenticated and non authenticated requests » : document ancien, ne décrit pas l'état actuel. LibraryCloud v2 : pagination documentée seulement dans une diapositive de 2012 (limit / start), non vérifiée.

## 3. Tests d'appel (voir `tests/harvard.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent (même hôte) |
|---|---|---|---|---|---|---|---|
| 1 | 21:05:56 | iiif.lib.harvard.edu/ | GET | 404 | aucun | « Cannot GET / » (istio-envoy) | 1re requête |
| 2 | 21:06:03 | iiif.lib.harvard.edu/manifests/ids:… | GET | 200 | aucun | HTML « meta refresh » 15 s vers nrs.lib.harvard.edu (pas du JSON) | 7 s |
| 3 | 21:06:08 | api.lib.harvard.edu/v2/items?q=iiif&limit=1 | GET | 200 | aucun | XML, résultats LibraryCloud | 1re requête sur cet hôte |
| 4 | 21:06:09 | iiif.lib.harvard.edu/manifests/view/ids:… | GET | 200 | aucun | HTML « This Resource Has Moved » | 6 s |
| 5 | ~21:06:15 | iiif.lib.harvard.edu/manifests/ids:… | GET | 200 | non relevés | refait pour lire la cible du rafraîchissement (saisie manuelle, consignée dans le log) | ~6 s |
| 6 | 21:06:25 | nrs.lib.harvard.edu/URN-3:…:MANIFEST:2 | GET | 303 | aucun | « See Other » vers mps.lib.harvard.edu | 1re requête sur cet hôte |
| 7 | 21:06:31 | mps.lib.harvard.edu/iiif/2/URN-3:… | GET | 200 | aucun | manifeste IIIF Presentation 2 (JSON, 3287 o) | 1re requête sur cet hôte |
| 8 | ~21:06:37 | mps.lib.harvard.edu/iiif/2/URN-3:… | GET | 200 | aucun | même manifeste, sauvegardé pour lire l'identifiant d'image | ~6 s |
| 9 | 21:06:47 | mps.lib.harvard.edu/assets/images/drs:…/info.json | GET | 200 | aucun | JSON IIIF Image API 2 (806 o) | ~6 s |

Notes de méthode : la colonne « délai » du journal affichait, jusqu'à la requête 9, le délai avant la pause de sécurité ; les horodatages UTC donnent l'écart réel (≥ 6 s entre requêtes vers un même hôte). Le script a été corrigé ensuite. Requête 5 faite à la main (même règles), consignée dans le journal. Budget : 9 requêtes sur 15.

Non faits : image par tuile (pas nécessaire, aucun besoin de débit pour le test) ; recherche LibraryCloud au-delà d'une requête.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : **non** (aucune phrase de quota ou de débit trouvée dans les pages Harvard lues ; conditions d'utilisation introuvables, 404).
- Limite **observée** (429 ou en-tête de quota reçu) : **non** (9 réponses, aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : **non** (aucun 403 ; le 404 de la racine n'est pas un refus d'accès).
- L'API annonce-t-elle ses limites dans la réponse ? **non observé**
- Mécanisme observé : **aucun**
- Valeurs trouvées (quota, fenêtre) : aucune. Pour LibraryCloud, 250 résultats maximum par requête (signalé par un répertoire tiers, non vérifié).
- Blocages rencontrés : aucun. Particularité : le manifeste d'exemple ne renvoie pas le JSON directement mais une page de redirection (200 HTML puis 303) vers un autre hôte Harvard.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la doc Harvard accessible ne dit rien des quotas IIIF. Le texte le plus proche est le rapport de 2013 (« implement rate limit throttling », travail restant, non daté de l'état actuel).
- Hypothèses (étiquetées comme telles) :
  - Hypothèse : le débit n'est pas limité côté serveur IIIF (mps / iiif), aucun signe observé sur 9 requêtes.
  - Hypothèse : une limitation éventuelle relèverait de la passerelle Harvard (istio-envoy observé sur les réponses), non documentée publiquement.

## 6. Confiance et pistes restantes

- Niveau de confiance : **faible** (doc Harvard pauvre, 9 requêtes seulement, pas de test de rafale).
- Ce qui reste à vérifier, et comment :
  1. Retrouver les conditions d'utilisation de Harvard Library (page « terms of use » ou équivalent) : URL à identifier depuis une page Harvard ouverte dans un navigateur.
  2. Demander à Harvard Library (Library Technology Services) s'il existe un plafond de requêtes IIIF et s'il est annoncé dans les en-têtes.
  3. Re-tester plus tard, à faible débit (≤ 1 requête toutes les 6 s), en gardant le même jeu de 9 requêtes, pour voir si un en-tête de limite apparaît.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Recherche faite en plus de la § 1 à § 5 : web (standard et extended), doc Harvard lue par WebFetch, pages wiki Harvard. Aucune requête supplémentaire envoyée à l'API (aucun endpoint de statut ou en-tête documenté trouvé, donc aucune sonde `scripts/config/harvard-quota.json`).

- a) Endpoint de statut de quota : **non trouvé** — termes cherchés : « LibraryCloud rate limit status endpoint », « api.lib.harvard.edu usage status », « iiif.lib.harvard.edu rate_limit ». `https://api.lib.harvard.edu/v2/` répond 404 à la lecture WebFetch (2026-11-13) : pas de page de doc à cet emplacement.
- b) En-têtes de limite documentés : **non trouvé** — termes cherchés : « Harvard LibraryCloud X-RateLimit », « Retry-After LibraryCloud ». Nos 9 réponses n'en contiennent aucun (tests/harvard.log).
- c) Clé ou compte donnant un quota : **non trouvé pour LibraryCloud** — une source tierce (api-evangelist, apis.io) dit que l'API d'items est sans clé ; un projet tiers (STLee-blacklight) mentionne une « LibraryCloud API key », sans source officielle. La clé de l'API Harvard Art Museums (api.harvardartmuseums.org) est un autre service, hors de cette fiche.
- d) Contact officiel pour un quota : **non trouvé** — aucune page Harvard lue ne cite de formulaire ou de courriel pour demander un quota (la page « library.harvard.edu/terms-use » reste en 404, cf. § 1).

Doc relevée sur un quota de débit (non vérifiée sur la page) : extrait de recherche d'une page wiki Harvard (LibraryCloud APIs, page 43287734, « Updated May 11 », année non lisible) puis d'une page tierce : « an average of 300 requests per 5 minutes », dépassement suivi d'un blocage de 5 minutes, et « Please limit your requests to no more once per second ». Attribution incertaine (les deux résultats de recherche ne sont pas du même auteur). WebFetch de la page wiki tronquée : la phrase n'a pas pu être relue. Statut : **documenté par un extrait, non vérifié en entier**.

Conclusion : moyen d'interroger le quota : **non**. Un chiffre de débit est annoncé (extrait non vérifié), mais aucun endpoint, en-tête ni contact pour le quota n'a été trouvé.

## 5 ter. Standard IIIF : en-têtes de quota

Recherche générale faite une seule fois pour l'ensemble des institutions de la veille (2026-11-13).

- IIIF Image API 3.0 (https://iiif.io/api/image/3.0/) et 2.1 (https://iiif.io/api/image/2.1/), lues par WebFetch le 2026-11-13 : aucune mention de limitation de débit, quota, throttling, 429, `Retry-After`, `RateLimit-*` ni d'endpoint de statut. Seule mention de charge : code 503 « The server is busy/temporarily unavailable due to load/maintenance issues. » et « Server applications implementing this API should consider possible denial-of-service attacks ».
- IIIF Presentation 3.0 : non lue (la recherche n'a rien remonté sur iiif.io à ce sujet).
- Recherche « iiif.io rate limiting throttling 429 Retry-After » (extended) : aucun résultat de iiif.io ; seul un ticket de projet tiers (Embassy-of-the-Free-Mind/sourcelibrary-v2, issue #7771) propose une pratique de politesse (1 à 2 connexions par hôte, pause, Retry-After respecté) : pratique de projet, pas une norme IIIF.
- Standards HTTP (sources de recherche, non relues en entier) : `Retry-After` défini par RFC 9110 ; statut 429 défini par RFC 6585. Les en-têtes `RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset` relèvent d'un brouillon IETF (httpapi-ratelimit-headers), selon les résultats de recherche encore non publié en RFC (statut à la date non vérifié).

Conclusion : le standard IIIF ne définit **aucun** en-tête ni endpoint de quota. Un serveur IIIF qui limite son débit le fait hors standard (ou via la passerelle), et le signale au mieux par 429 / `Retry-After`, à vérifier au cas par cas.
