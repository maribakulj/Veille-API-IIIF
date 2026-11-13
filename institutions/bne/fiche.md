# Biblioteca Nacional de España (BNE) — `bne`

- **Statut** : en cours (doc officielle non lue ; 5 requêtes de sonde faites sur 15 ; aucun endpoint IIIF officiel documenté trouvé ; complément BDH dans la section 2 bis)
- **Pays** : Espagne
- **Point d'entrée testé** : `https://datos.bne.es/` (303, non suivi par la sonde) et `http://datos.bne.es/sparql` (404, annonce 2014 seulement). Aucun endpoint IIIF (manifeste, info.json) ni de recherche n'a pu être identifié dans une doc officielle lisible.
- **Vérifié le** : 2026-11-13 (sonde à 21:07:36Z et 21:07:42Z UTC ; recherches et lecture doc entre 21:0x et 21:0x UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://datos.bne.es/ (portail officiel des données liées) | 2026-11-13 — **non lue** : 403 via WebFetch (outil, UA non maîtrisé) | rien lu. Sonde `probe.py` (UA honnête) : 303, pas de 403. Le contenu reste à lire depuis un navigateur. |
| https://www.bne.es/en/catalogs/linked-data-at-the-bne (page « Linked data at the BNE ») | non lue directement (résultat de recherche seulement, 2026-11-13) | rien lu. À relire. |
| http://datos.bne.es/sparql (endpoint SPARQL, cité par l'annonce de 2014 : http://datos.bne.es/sparql) | sonde 2026-11-13 | Annonce de 2014 (source : OKFN open-glam, « ANN: datos.bne.es », 2014-12) : endpoint SPARQL public. Aujourd'hui : 404 (corps HTML « Not Found », page Cloudflare). Document ancien, non confirmé. |
| https://datos.gob.es (article de 2016 sur le plan de réutilisation de la BNE) | recherche, 2026-11-13, non lu en entier | « licence CC0 » pour le portail en bêta (2016). Ancien, à vérifier sur bne.es. Aucune limite de débit trouvée. |

Conclusion documentaire : aucune limite chiffrée (quota, fenêtre, débit) trouvée. Les conditions de réutilisation vigueur ne sont pas lues (page du portail non accessible à l'outil WebFetch).

## 2. Recherche élargie

- Termes cherchés : « Biblioteca Nacional de España IIIF manifest API documentación límites uso » ; « bdh-rd.bne.es iiif manifest json Biblioteca Digital Hispánica » ; « datos.bne.es API SPARQL endpoint documentation condiciones de reutilización ».
- Sources examinées (résultats seulement) : entrées de presse et blogs (Real Biblioteca, neelsmith.quarto.pub sur les manifestes Complutense de la BNE, qui sont des manifestes communautaires hébergés sur GitHub, non publiés par la BNE), datos.gob.es (2014 / 2016 / 2018), OKFN open-glam (2014), api.store (portail BDH, métadonnées seulement).
- Résultat : aucun URL de manifeste officiel BNE (pattern bdh-rd.bne.es non trouvé), aucune doc IIIF BNE, aucune limite. Les limites trouvées ailleurs (BSB/MDZ : OCR par 24 h) ne concernent pas la BNE et ne sont pas retenues.

## 2 bis. Biblioteca Digital Hispánica (bdh.bne.es, bdh-rd.bne.es) — complément

- Termes cherchés (espagnol et français) : « Biblioteca Digital Hispánica bdh.bne.es manifiesto IIIF » ; « bdh-rd.bne.es IIIF "límite de peticiones" OR "uso de la API" Biblioteca Nacional de España » ; « BNE API IIIF condiciones de reutilización ».
- Lecture directe : https://bdh.bne.es/ et https://www.bne.es/en/catalogs/hispanic-digital-library renvoient 403 à WebFetch (outil, UA non maîtrisé) ; non lus. Pas contourné.
- Pages BNE citées par une source tierce (article neelsmith, 2024, lu via WebFetch) : https://bdh.bne.es/bnesearch/Inicio.do et http://bdh-rd.bne.es/viewer.vm?id=0000050739&page=1 (visionneuse). Ces pages sont des interfaces web, pas une documentation d'API. Les manifestes IIIF cités par cet article sont hébergés sur GitHub (dépôt de l'auteur), pas par la BNE : non retenus comme endpoints BNE.
- Résultat : aucune doc IIIF BNE trouvée (manifeste, image) ; aucune limite de requêtes ni condition d'usage d'API trouvée. L'article tiers ne mentionne aucun quota et dit les images « openly licensed » (source tierce, non BNE).

## 3. Tests d'appel (voir `institutions/bne/tests/journal.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:07:36Z | https://datos.bne.es/ | GET (probe) | 303 | aucun | corps vide (non suivi) | - |
| 2 | 21:07:42Z | http://datos.bne.es/sparql | GET (probe) | 404 | aucun | page HTML 404 « Not Found » avec script Cloudflare | 6 s |
| 3 | 21:08:40Z | https://bdh.bne.es/bnesearch/Inicio.do | GET (probe, `bne-suite.json`) | 308 | aucun | corps vide (non suivi) | - |
| 4 | 21:08:40Z | http://bdh-rd.bne.es/viewer.vm?id=0000050739&page=1 | GET (probe) | 301 | aucun | corps vide (non suivi) | hôte différent |
| 5 | 21:08:46Z | https://bdh.bne.es/ | GET (probe) | 308 | aucun | corps vide (non suivi) | 6 s |

Non réalisés : aucun endpoint IIIF (pas documenté dans une source lue). Les redirections (303, 308, 301) n'ont pas été suivies : la sonde ne suit pas les redirections et ne journalise pas le `Location`, donc la cible reste inconnue. Budget utilisé : 5 requêtes sur 15.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non (rien trouvé dans les sources lues, y compris BDH).
- Limite **observée** (429 ou en-tête de quota reçu) : non.
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : non pour la sonde (requêtes 1 à 5). **Oui pour l'outil WebFetch** sur https://datos.bne.es/, https://bdh.bne.es/ et https://www.bne.es/en/catalogs/hispanic-digital-library (403, hors budget de la sonde, UA non maîtrisé). Ce n'est pas une limite de débit ; on n'a pas tenté de contourner.
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucun en-tête de limite sur 2 réponses).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : 403 sur WebFetch (doc, trois pages) ; pas de 403 ni 429 de la sonde (redirections 301/303/308 seulement). Le 404 de `/sparql` et la présence de Cloudflare indiquent un front CDN, sans défi observé.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : rien de publié sur un quota BNE dans les sources lues.
- Hypothèses (étiquetées comme telles) : hypothèse 1 : la BNE ne publie pas de politique de quota pour ses données (non vérifié). Hypothèse 2 : la doc IIIF BNE est sur un autre hôte que datos.bne.es (non vérifié).

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Méthode : termes en espagnol et en anglais, WebSearch (mode extended), WebFetch sur les pages officielles, recherche GitHub limitée à github.com (org BNElab). Aucune requête vers l'API. Pages `datos.bne.es` et `bdh.bne.es` : 403 au niveau de l'outil WebFetch, non contourné.

- a) Endpoint de statut de quota : **non trouvé** — termes cherchés : « límite de peticiones », « uso de la API », « rate limit », « límites de uso » (web) ; « BNElab IIIF rate limit » (GitHub, org BNElab : aucune doc d'API trouvée).
- b) En-têtes de limite documentés : **non trouvé** — termes cherchés : « X-RateLimit », « Retry-After », « RateLimit-Remaining » combinés à « BNE » / « datos.bne.es ». Aucun résultat BNE.
- c) Clé ou compte donnant un quota : **non trouvé** — aucune page BNE ne décrit de clé d'API. Source la plus proche : bnelab.bne.es/datos (extrait de recherche, 2026-11-13) : « Descarga y reutilización libre de los datos de la BNE » (formats XML, MARC, CSV, JSON, RDF, OAI). Ce n'est pas un quota.
- d) Contact officiel pour un quota : **non trouvé** — aucune adresse ou formulaire d'API trouvé dans les extraits lus. Pistes à relire depuis un navigateur : https://bnelab.bne.es/datos/ et la page de contact de la BNE.

Conclusion : moyen d'interroger le quota : **non**. Rien d'annoncé ni de documenté côté BNE ; aucun fichier `scripts/config/bne-quota.json` écrit.

## 6. Confiance et pistes restantes

- Niveau de confiance : faible (aucune doc officielle lue ; aucun endpoint IIIF identifié).
- Ce qui reste à vérifier, et comment :
  1. Lire https://datos.bne.es/ et la page « Linked data at the BNE » sur bne.es depuis un navigateur ordinaire (sans contournement) : endpoints, conditions de réutilisation, licence actuelle.
  2. Trouver l'URL officielle d'un manifeste IIIF BNE (Biblioteca Digital Hispánica) depuis la doc du site, puis l'ajouter dans une configuration `institutions/bne/config/bne-suite.json`.
  3. Vérifier la cible des redirections (303 sur datos.bne.es, 308 sur bdh.bne.es, 301 sur bdh-rd.bne.es) : la sonde ne les suit pas ; à consigner si la sonde journalise le `Location`.
  4. Demander par écrit au service numérique de la BNE s'il existe une limite de débit pour IIIF.
