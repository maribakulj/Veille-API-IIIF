# New York Public Library — `nypl`

- **Statut** : vérifiée partiellement (doc et recherche faites ; 6 requêtes sur 3 hôtes ; aucun 403, aucun 429 ; info.json IIIF non testé faute d'identifiant d'image documenté)
- **Pays** : États-Unis
- **Point d'entrée testé** : https://iiif.nypl.org/ (page Cantaloupe 5.0.7, 200) ; manifestes sur https://api-collections.nypl.org/manifests/… (hôte distinct) ; API REST https://api.repo.nypl.org/api/v1/items/search (hôte distinct)
- **Vérifié le** : 2026-11-13 (UTC, 21:07 à 21:09)
- **Vérifié par** : agent de veille (Haiku 5.5), session Claude Code

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://api.repo.nypl.org/api_documentation_v1 (documentation de l'API Digital Collections, lue via WebFetch) | 2026-11-13 | « The limit per authentication token while connecting from an application or curl request is 10,000 requests per day. » (section « API Request Limitations »). Ce texte porte sur l'API REST **v1**, et non sur IIIF. |
| Même page : statut de la v1 | 2026-11-13 | **Contredit par le test n° 5** : la v1 répond 410 « The v1 API has been disabled. Please switch to the v2 API ». La page documentaire décrit donc une API désactivée. |
| https://iiif.nypl.org/ (racine du serveur d'images) | 2026-11-13 | Pas de documentation ni de conditions : page Cantaloupe, sans texte d'usage. |
| https://live-legacy-admin.nypl.org/help/legal-notices/open-metadata (politique métadonnées ouvertes, extrait de recherche) | 2026-11-13 | **Non lue** : la lecture WebFetch a échoué (erreur sans contenu). Extrait de recherche : demande de suivre les « community norms » (diffusion des améliorations sous les mêmes conditions). Pas de chiffre. |
| Conditions d'utilisation des images IIIF NYPL | 2026-11-13 | **Introuvables** dans la recherche et la page légale des collections numériques (page lue vide via WebFetch). |

## 2. Recherche élargie

- Termes cherchés : « NYPL IIIF API rate limit usage terms iiif.nypl.org developer documentation » ; « NYPL Digital Collections API v2 rate limit requests per day token documentation » ; « "iiif.nypl.org/iiif" info.json example identifier NYPL image ».
- Sources examinées : api.repo.nypl.org (doc v1) ; iiif.nypl.org (racine) ; pages légales NYPL (extraits) ; billets NYPL 2013 (API annoncée) ; résultats tiers (archive.com, jentic, gist) non officiels.
- Résultat :
  - Le seul chiffre trouvé (10 000 requêtes par jour et par jeton) est celui de la **doc v1**, désactivée à la date du test. Un extrait tiers dit que la v1 est dépréciée depuis juillet 2022 et que la v2 est actuelle (source non officielle, non lue en entier). La doc v2 n'a pas été trouvée.
  - Aucun identifiant d'image `iiif.nypl.org` documenté trouvé. Les manifestes trouvés (api-collections) ne contiennent ni canvas ni service image dans les deux exemples testés.

## 3. Tests d'appel (voir `institutions/nypl/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent (même hôte) |
|---|---|---|---|---|---|---|---|
| 1 | 21:07:42 | iiif.nypl.org/ | GET | **échec de connexion** (pas de code HTTP, curl) | aucun | vide | 1re requête |
| 2 | 21:08:12 | api-collections.nypl.org/manifests/333ce2c0-… | GET | 200 | aucun | manifeste IIIF Presentation 3 (7527 o), sans canvas ni service image | 1re requête sur cet hôte |
| 3 | 21:08:24 | iiif.nypl.org/ (reprise) | GET | 200 | aucun | nouvelle tentative, réussie ; l'échec de la requête 1 est donc transitoire | ~6 s |
| 4 | ~21:08:30 | iiif.nypl.org/ | GET | 200 | aucun | page Cantaloupe 5.0.7 (618 o), sauvegardée pour lecture ; aucun lien d'exemple | ~6 s |
| 5 | 21:08:34 | api.repo.nypl.org/api/v1/items/search?q=… | GET | **410** | aucun | `{"error":"The v1 API has been disabled. Please switch to the v2 API"}` | 1re requête sur cet hôte |
| 6 | ~21:08:40 | api-collections.nypl.org/manifests/999d3890-… | GET | 200 | aucun | manifeste Presentation 3 (8245 o), sans canvas ni service image | ~6 s |

Notes : la requête 1 a échoué sans réponse HTTP ; elle est consignée telle quelle dans le journal, et la requête 3 est la reprise. Aucun appel à une API nécessitant un jeton (aucun identifiant envoyé). Budget : 6 requêtes sur 15.

Non faits, et pourquoi : info.json IIIF (`iiif.nypl.org/iiif/…/info.json`) non testé : aucun identifiant d'image documenté n'a été trouvé, et deviner un identifiant est interdit par la méthode. API v2 non testée : sa doc n'a pas été trouvée et tester un chemin non documenté est exclu.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : **oui, mais hors IIIF** : 10 000 requêtes par jour et par jeton, pour l'API REST v1 (api.repo.nypl.org, doc non datée). Cette API est désactivée (410) : la limite ne s'applique plus telle quelle. Aucune limite IIIF documentée.
- Limite **observée** (429 ou en-tête de quota reçu) : **non** (6 réponses, aucun en-tête de limite ; le seul refus est un 410 de désactivation, qui n'est pas une limite de débit).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : **non** (aucun 403).
- L'API annonce-t-elle ses limites dans la réponse ? **non observé**
- Mécanisme observé : **aucun** (un échec de connexion transitoire à la requête 1, sans lien avec un quota)
- Valeurs trouvées (quota, fenêtre) : 10 000 par jour (API v1, désactivée). Rien pour IIIF.
- Blocages rencontrés : 410 sur l'API v1 ; échec de connexion ponctuel sur iiif.nypl.org (résolu à la reprise).

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la seule limite chiffrée concerne l'API REST v1, désactivée. La doc v1 n'a pas été mise à jour (elle annonce encore la limite alors que l'API répond 410).
- Hypothèses (étiquetées comme telles) :
  - Hypothèse : l'image IIIF est servie par Cantaloupe sans quota publié, la limite chiffrée étant propre à l'API de métadonnées.
  - Hypothèse : la v2 de l'API porte sa propre limite, non trouvée dans la recherche.

## 6. Confiance et pistes restantes

- Niveau de confiance : **faible** (doc v2 introuvable, pas d'info.json testé, aucun 429 observé).
- Ce qui reste à vérifier, et comment :
  1. Trouver la doc de l'API v2 Digital Collections (page développeurs NYPL) et ses limites, depuis un navigateur ordinaire.
  2. Lire la page « open metadata » et les conditions d'utilisation NYPL complètes (lecture WebFetch en échec).
  3. Obtenir auprès de NYPL un identifiant d'image IIIF documenté, puis tester un info.json à ≤ 1 requête toutes les 6 s.
  4. Signaler à NYPL que la doc v1 annonce une limite pour une API désactivée.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Recherche faite en plus de la § 1 à § 5 : web (standard et extended), page d'accueil et page d'inscription de l'API Repo lues par WebFetch. Aucune requête supplémentaire envoyée (aucun endpoint de statut ni en-tête documenté trouvé, donc pas de sonde `scripts/config/nypl-quota.json`).

- a) Endpoint de statut de quota : **non trouvé** — termes cherchés : « NYPL Digital Collections API usage status endpoint », « api.repo.nypl.org rate limit status ». La page `https://api.repo.nypl.org` (WebFetch, 2026-11-13) ne décrit aucun endpoint d'usage ; `/items/total` renvoie le nombre d'items, pas l'usage. L'API v1 répond 410 (§ 3, test 5).
- b) En-têtes de limite documentés : **non trouvé** — la page d'accueil de l'API Repo indique « Rate-limit response headers : None documented » (résumé WebFetch, 2026-11-13). Aucun en-tête de limite dans nos 6 réponses.
- c) Clé ou compte donnant un quota : **trouvé, pour l'API Repo seulement** — `https://api.repo.nypl.org/sign_up` (WebFetch, 2026-11-13) : « API Request Limit (Default): 10000 » et « NYPL has established quota limits for the NYPL Repository API. » ; `https://api.repo.nypl.org` : « The limit per authentication token while connecting from an application or curl request is 10,000 requests per day. » Mais la même page annonce : « The Repo API is being deprecated and will no longer be available starting August 1st, 2026. » (au 2026-11-13, cette date est passée). La doc v2 n'est pas trouvée : `https://api.repo.nypl.org/api_documentation_v2` répond 400 « The path that you entered is invalid » (WebFetch, 2026-11-13). Pour les manifestes et images IIIF (api-collections, iiif.nypl.org), aucune clé ni quota trouvé.
- d) Contact officiel pour un quota : **trouvé** — page d'accueil de l'API Repo (2026-11-13) : « Questions/feedback? Write to: repoapi@nypl.org » ; pour la fin de l'API : digitaldam@nypl.org (même page, cité par le résumé). Aucun formulaire de demande de quota relevé.

Conclusion : moyen d'interroger le quota : **non**. Une clé a un quota documenté (10 000 par jour), mais l'API qui le porte est annoncée comme arrêtée le 1er août 2026, aucun endpoint de statut ni en-tête n'existe dans la doc, et la v2 n'est pas documentée à l'URL attendue. Le quota IIIF de NYPL reste sans chiffre.
