# Getty (Open Content / Linked Art) — `getty`

- **Statut** : vérifiée (doc partielle ; tests faits, 7 requêtes, aucun blocage)
- **Pays** : États-Unis
- **Point d'entrée testé** : `https://data.getty.edu/` (page « Getty API Documentation », 200), avec les endpoints documentés listés dans `https://data.getty.edu/museum/collection/docs/_payload.json` : manifeste `https://media.getty.edu/iiif/manifest/<MANIFEST_ID>`, image `https://media.getty.edu/iiif/image/<IMAGE_ID>`, REST `https://data.getty.edu/museum/collection/<ENTITY_TYPE>/<ENTITY_ID>`, activity stream, SPARQL.
- **Vérifié le** : 2026-11-13 (tests 21:07:59Z à 21:08:29Z ; doc consultée le même jour)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://data.getty.edu/museum/collection/docs/_payload.json (données de la page « API Documentation », lues par WebFetch) | 2026-11-13 | Liste les endpoints ci-dessus. Aucune mention de quota, limite de débit, rate limit ni fair use. Phrases lues sur les conditions : données « as is », « Images are not always available under the same terms as the dataset », « different terms and conditions apply » pour certaines images, jeu de données librement utilisable « sauf deux exceptions (images et descriptions écrites) » ; ne pas induire en erreur sur la source. |
| https://data.getty.edu/museum/collection/docs/ et /docs/revision/ | 2026-11-13 (WebFetch) | Page tronquée par l'outil (« Content truncated due to length ») : seul le titre a été lu. Rien d'autre lu. |
| https://www.getty.edu/legal/terms-of-use/ (redirection de /legal/copyright.html) | 2026-11-13 (WebFetch) | Page tronquée : seul le titre lu. Aucune phrase sur l'usage automatisé ou les limites n'a pu être lue. |
| https://www.getty.edu/projects/open-data-apis et https://www.getty.edu/about/whatwedo/opencontent.html | non consultées directement | Citées par le moteur de recherche ; non lues. |

Conclusion documentaire : **aucune limite chiffrée** trouvée dans les pages lues (données de la doc API, complètes). Les pages « docs » et « terms » ont été tronquées, donc l'absence de mention dans leur texte intégral n'est **pas** établie.

## 2. Recherche élargie

- Termes cherchés : « Getty Museum Open Content IIIF API rate limit terms of use » ; « data.getty.edu museum collection iiif manifest info.json endpoint Linked Art ».
- Sources examinées : résultats de recherche (résumés secondaires, non lus en entier) renvoyant vers les pages Getty ci-dessus, un article de 2017 (infodocket, 30 000 images publiées en IIIF), une page de conditions Getty, et le dépôt de notebooks Linked-Art (tgra) cité pour la structure des données.
- Résultat : aucun quota ni rate limit publié pour l'API IIIF Getty trouvé. Le résumé du moteur indique que les images relèvent de conditions distinctes du jeu de données (rights@getty.edu pour les questions de droits) et que les images Open Content sont CC0 selon la FAQ Getty citée dans un billet de blog (source secondaire, non lue en direct). Pas de forum ni d'issue GitHub consacrée aux limites de débit trouvée.

## 3. Tests d'appel (voir `tests/getty.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:07:59 | https://data.getty.edu/ | GET | 200 | aucun | page HTML « Getty API Documentation » | - |
| 2 | 21:08:06 | https://data.getty.edu/museum/collection/docs/ | GET | 200 | aucun | page HTML (même titre) | 7 s |
| 3 | 21:08:13 | https://data.getty.edu/museum/collection/activity-stream | GET | 200 | aucun | JSON ActivityStreams, « Getty Museum Collection Data », totalItems présent | 7 s |
| 4 | 21:08:20 | https://data.getty.edu/museum/collection/sparql | GET | 400 | aucun | « No query parameter included » (JSON) | 7 s |
| 5 | 21:08:27 | https://data.getty.edu/museum/collection/sparql-ui | GET | 200 | aucun | page YASGUI | 7 s |
| 6 | 21:08:28 | https://media.getty.edu/iiif/manifest/53be857e-41e8-4198-b45d-2e0f52d3051b | GET | 200 | aucun | JSON IIIF Presentation 3 (homepage getty.edu, objet 103JNH) | 1 s (autre hôte) |
| 7 | 21:08:29 | https://www.getty.edu/legal/terms-of-use/ | GET | 200 | aucun | page HTML (titre seul, tronquée côté outil) | 1 s (autre hôte) |

Remarque : l'identifiant de manifeste (n° 6) provient d'un résumé de moteur de recherche citant la doc Getty ; il n'a pas été relu dans le texte brut de la doc. Il répond 200 avec un manifeste IIIF valide : exemple vérifié, pas une preuve de présence dans la doc.

Non réalisés : `info.json` d'image (aucun `IMAGE_ID` documenté lu ; le corps du manifeste n'est pas journalisé au-delà de 200 octets, donc l'ID n'a pas été extrait) ; `…/collection/object/<ID>` (aucun ID d'exemple documenté lu). Budget : 7 requêtes sur 15.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non trouvée (doc API lue en entier : pas de quota ; pages « docs » et « terms » tronquées, non lues en entier).
- Limite **observée** (429 ou en-tête de quota reçu) : non. 7 requêtes, aucun en-tête `Retry-After`, `X-RateLimit-*` ou `RateLimit-*`.
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : non (aucune réponse 403 ni défi).
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucun en-tête de limite).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : aucun. Le 400 du SPARQL sans requête est une réponse normale de l'API (paramètre `query` manquant).

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la doc API ne mentionne aucune limite ; l'accès est décrit comme données « as is » ; les images ont des conditions propres (cf. section 1).
- Hypothèses (étiquetées comme telles) : hypothèse 1 : pas de quota formalisé pour les endpoints publics, la politique étant le respect des conditions de réutilisation (non vérifié, les pages de conditions n'ont pas été lues en entier). Hypothèse 2 : les limites éventuelles, si elles existent, ne se voient qu'en cas de charge (non vérifié, 7 requêtes espacées ne suffisent pas à tester).

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Méthode : termes en anglais, WebSearch (mode extended), WebFetch sur la doc API Getty (page tronquée), recherche GitHub limitée à github.com. Aucune requête supplémentaire vers l'API.

- a) Endpoint de statut de quota : **non trouvé** — termes cherchés : « rate limit », « rate limit status », « throttling », « usage », « quota », « automated access » (data.getty.edu/museum/collection/docs/ : page tronquée, seul le titre lu, 2026-11-13 ; GitHub : org thegetty, arrt, quire : aucune mention de limite pour Linked Art ni IIIF).
- b) En-têtes de limite documentés : **non trouvé** — termes cherchés : « X-RateLimit », « RateLimit-Remaining », « Retry-After » avec « Getty » / « data.getty.edu ». Les résultats de limite trouvés concernent Getty Images (service commercial distinct, 403 au dépassement, 2026-11-13) : hors sujet, non retenus.
- c) Clé ou compte donnant un quota : **non trouvé** — aucune clé requise par la doc Getty lue (données « as is »). Un scraper tiers (Apify) affirme que l'API et le SPARQL sont « fully public and keyless » : affirmation tierce, non vérifiée. Les images sous conditions distinctes sont à licencier auprès de rights@getty.edu (doc API, extrait lu via recherche, 2026-11-13).
- d) Contact officiel pour un quota : **non trouvé pour les quotas** — adresses trouvées dans la doc API (extrait de recherche) : MuseumCollections@getty.edu pour l'intégrité du jeu de données ; rights@getty.edu pour les droits d'images. Aucune adresse dédiée à la charge ou aux limites. Page https://www.getty.edu/about/contact/ : non lue.

Conclusion : moyen d'interroger le quota : **non**. Aucun endpoint de statut, aucun en-tête documenté, aucune clé. La question reste à poser par écrit à MuseumCollections@getty.edu. Aucun fichier `scripts/config/getty-quota.json` écrit.

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen (endpoints confirmés en 200 ; doc API lue via son JSON de données ; conditions non lues).
- Ce qui reste à vérifier, et comment :
  1. Lire https://www.getty.edu/legal/terms-of-use/ et https://www.getty.edu/projects/open-data-apis en entier depuis un navigateur, et chercher « automated », « bulk », « rate », « fair use ».
  2. Relever un `IMAGE_ID` dans une réponse du manifeste (corps complet, hors de la sonde journalisée) puis tester `https://media.getty.edu/iiif/image/<IMAGE_ID>/info.json` avec la sonde.
  3. Tester un `…/collection/object/<ID>` (Linked Art, Accept JSON) avec un ID tiré de la doc.
  4. Demander par écrit à Getty (rights@getty.edu pour les droits ; contact API pour la charge) s'il existe une limite de débit.
