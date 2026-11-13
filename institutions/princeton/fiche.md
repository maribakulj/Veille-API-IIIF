# Princeton University Library — `princeton`

- **Statut** : vérifiée partiellement (doc et recherche faites ; 8 requêtes sur 4 hôtes ; aucun 403, aucun 429 ; manifeste de bibliothèque non trouvé)
- **Pays** : États-Unis
- **Point d'entrée testé** : https://iiif.princeton.edu/ (racine : JSON listant les points d'accès IIIF v2 et v3, sans limite annoncée)
- **Vérifié le** : 2026-11-13 (UTC, 21:07)
- **Vérifié par** : agent de veille (Haiku 5.5), session Claude Code

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://dpul.princeton.edu/1762-archive/about/princeton-university-library (page DPUL) | 2026-11-13 | Aucune mention de quota, débit, API ni conditions d'usage. Seule mention IIIF : « PUL has served as the main repository for high resolution, IIIF scans institutions without such hosting capabilities ». Pas de date affichée. |
| https://pul-confluence.atlassian.net/wiki/spaces/IT/pages/1933600/DPUL+PUL+s+Curated+Collections+Platform (extrait de recherche, non lu en entier) | 2026-11-13 | Extrait : pour la moissonnage des données IIIF de Princeton, « contact us » (canal #digital_library et adresse de la bibliothèque numérique). Pas de chiffre. |
| https://pul-confluence.atlassian.net/wiki/spaces/ALMA/pages/1769787/Z39.50+Access (extrait de recherche, non lu en entier) | 2026-11-13 | Extrait : PUL « committed to sharing its catalog metadata » ; attribution demandée. Rien sur le débit. |
| https://iiif.princeton.edu/ (racine du serveur, lue par le test n° 1 et 5) | 2026-11-13 | Pas de texte de conditions. JSON : liens « IIIF Image API v2 endpoint » (`/iiif/2/{:id}`) et « v3 endpoint » (`/iiif/3/{:id}`), plus une liste de versions de logiciels. |
| Conditions d'utilisation / termes d'accès Princeton | 2026-11-13 | **Introuvables** dans la recherche (aucune page Princeton de conditions d'accès API ou IIIF). |

## 2. Recherche élargie

- Termes cherchés : « Princeton University Library IIIF API rate limit terms of use iiif.princeton.edu » ; « iiif.princeton.edu manifest example URL Princeton IIIF image server info.json » ; « Princeton University Library digital collections terms of use API bulk access rate limit ».
- Sources examinées : DPUL (page « about » ; « What is Digital PUL » en titre seulement) ; wiki interne Princeton (DPUL, Z39.50) en extraits ; guides IIIF ; résultats tiers (non applicables à Princeton : Leiden, eScholarship, Duke, Berkeley).
- Résultat : aucune limite de débit ni condition IIIF propre à Princeton trouvée. Les exemples de manifestes trouvés concernent le **Princeton University Art Museum** (data.artmuseum.princeton.edu, media.artmuseum.princeton.edu), pas la bibliothèque. Un exemple d'image de la bibliothèque (libimages1.princeton.edu, serveur Loris, cité dans un exemple OpenSeadragon) a été testé comme repère.

## 3. Tests d'appel (voir `institutions/princeton/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent (même hôte) |
|---|---|---|---|---|---|---|---|
| 1 | 21:07:07 | iiif.princeton.edu/ | GET | 200 | aucun | JSON : points d'accès IIIF v2 et v3, versions | 1re requête |
| 2 | 21:07:08 | data.artmuseum.princeton.edu/iiif/objects/32773 | GET | 200 | aucun | manifeste IIIF Presentation 3 (4571 o), musée (non bibliothèque) | 1re requête sur cet hôte |
| 3 | 21:07:14 | media.artmuseum.princeton.edu/iiif/3/collection/y1982-103/info.json | GET | 200 | aucun | info.json IIIF Image API 3 (661 o), musée | 1re requête sur cet hôte |
| 4 | 21:07:14 | libimages1.princeton.edu/loris/…/info.json | GET | 301 | aucun | redirection vers iiif.princeton.edu (HTTP/2 nginx) | 1re requête sur cet hôte |
| 5 | ~21:07:20 | iiif.princeton.edu/ | GET | 200 | aucun | même racine, sauvegardée pour lecture complète | ~6 s |
| 6 | ~21:07:20 | libimages1.princeton.edu/loris/…/info.json | HEAD | (301) | location relevée ; aucune limite | redirection vers iiif.princeton.edu | ~6 s |
| 7 | 21:07:29 | iiif.princeton.edu/loris/…/info.json | GET | 200 | aucun | info.json IIIF Image API 2 (941 o) | 9 s |
| 8 | 21:07:36 | iiif.princeton.edu/iiif/2/…/info.json | GET | 200 | aucun | même info.json, chemin `/iiif/2/` documenté sur la racine | 6 s |

Notes : la requête 6 est une requête HEAD (autorisée par la méthode) faite à la main, consignée dans le journal. Identifiant d'image : celui de l'exemple OpenSeadragon (pudl0001/4609321/s42/00000001), non vérifié comme actuel par la doc, mais il répond 200 sur `/iiif/2/`. Budget : 8 requêtes sur 15.

Non faits : manifeste de la bibliothèque (aucun identifiant de manifeste Princeton trouvé dans la doc) ; rafale (pas de besoin pour ce test).

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : **non** (aucune phrase de quota ou débit trouvée).
- Limite **observée** (429 ou en-tête de quota reçu) : **non** (8 réponses, aucun en-tête de limite).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : **non** (aucun 403).
- L'API annonce-t-elle ses limites dans la réponse ? **non observé**
- Mécanisme observé : **aucun**
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : aucun. Particularité : l'ancien hôte libimages1 redirige en 301 vers iiif.princeton.edu.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : rien sur les quotas. Le wiki DPUL invite à contacter l'équipe pour la moissonnage IIIF (extrait de recherche).
- Hypothèses (étiquetées comme telles) :
  - Hypothèse : les accès IIIF de la bibliothèque sont gérés par demande directe (moissonnage sur contact), sans quota publié.
  - Hypothèse : les conditions d'accès sont dans une page non indexée par la recherche.

## 6. Confiance et pistes restantes

- Niveau de confiance : **faible** (peu de doc, pas de manifeste de bibliothèque testé).
- Ce qui reste à vérifier, et comment :
  1. Lire la page DPUL « harvesting » ou « terms » complète, depuis un navigateur ordinaire.
  2. Demander à Princeton (digital-library, via le canal indiqué dans le wiki) les limites d'usage IIIF et la forme d'un manifeste de la bibliothèque.
  3. Re-tester avec un manifeste de la bibliothèque une fois trouvé, à ≤ 1 requête toutes les 6 s.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Recherche faite en plus de la § 1 à § 5 : web (standard et extended), doc DPUL et wiki Princeton lus par WebFetch ou extraits de recherche. Aucune requête supplémentaire envoyée (aucun endpoint de statut ni en-tête documenté trouvé, donc pas de sonde `scripts/config/princeton-quota.json`).

- a) Endpoint de statut de quota : **non trouvé** — termes cherchés : « Princeton University Library IIIF rate limit quota API status endpoint », « iiif.princeton.edu rate limit ». La racine `https://iiif.princeton.edu/` (déjà consignée, § 3) ne liste que des points d'accès IIIF v2/v3 et des versions logicielles, sans statut.
- b) En-têtes de limite documentés : **non trouvé** — aucun en-tête de limite dans nos 8 réponses (institutions/princeton/tests/journal.log) ; aucune page lue n'en décrit.
- c) Clé ou compte donnant un quota : **non trouvé** — aucune mention d'inscription, de clé ni de compte pour l'accès IIIF.
- d) Contact officiel pour un quota : **partiel, sans quota** — extrait du wiki DPUL (pul-confluence, « DPUL: PUL's Curated Collections Platform », lu en extrait, 2026-11-13) : pour la moissonnage des données IIIF, « contact us » (canal #digital_library et adresse de la bibliothèque numérique). Aucun courriel ni formulaire précis lu en entier. Dépôt pulibrary/dpul lu par WebFetch (2026-11-13) : aucune mention de quota, de débit ni de contact pour l'accès en masse.

Pour information non vérifiée : un projet tiers (natemoo93/whatiiif-mcp, 2026-11-13) affirme que Figgy (backend de DPUL) a un robots.txt « Disallow: / » et que DPUL refuse les clients automatisés. Affirmation de seconde main, non vérifiée sur le robots.txt de Princeton. À vérifier directement (https://dpul.princeton.edu/robots.txt, lecture seule, une requête) avant toute suite.

Conclusion : moyen d'interroger le quota : **non**. Seule piste : contacter l'équipe DPUL (canal indiqué dans le wiki) pour les limites d'usage.
