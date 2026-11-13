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
