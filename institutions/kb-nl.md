# Koninklijke Bibliotheek (KB, Pays-Bas) — `kb-nl`

- **Statut** : vérifiée (partiellement : pas d'endpoint IIIF documenté ni joignable, voir §3 et §6)
- **Pays** : Pays-Bas
- **Point d'entrée testé** : `https://iiif.kb.nl/` (point d'entrée demandé par la veille ; aucune doc ne le cite comme endpoint). Endpoints réellement testés : `https://jsru.kb.nl/sru/sru` (SRU, recherche) et `https://services.kb.nl/mdo/oai` (OAI-PMH, métadonnées).
- **Vérifié le** : 2026-11-13 (sondes 21:08:00 à 21:08:16 UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://www.kb.nl/en/research-find/for-researchers/data-services-apis-and-downloads (« Data services: APIs and downloads ») | 2026-11-13 (WebFetch, résumé par un petit modèle) | Aucun endpoint nommé, aucun quota. Citations : « If copyright law allows it, anyone can use the data, free of charge and without conditions. » ; « If the material is copyrighted, access to the data for non-commercial scientific research purposes is sometimes possible. » ; « Usually open data (…) can be downloaded without prior registration. » ; « you may first have to sign a contract or access to the data may be limited to the KB building ». Aucune mention de débit ni d'usage automatisé. |
| https://lab.kb.nl/data-services (KB lab, « Data services ») | 2026-11-13 (WebFetch, résumé) | Renvoie vers la page ci-dessus. Mentionne « via APIs (Application Programming Interfaces) », « as bulk downloads », « via Wikimedia Commons ». Pas d'URL d'API, pas de quota. |
| https://www.kb.nl/en/contact/conditions-use (« Terms of Use ») | 2026-11-13 (WebFetch, résumé) | Aucune phrase sur robots, scraping, quota ou API. Renvoie à un PDF de « house rules » non lu. |
| https://github.com/KBNLresearch/intro-kb-apis (dépôt officiel KB Research, README) | 2026-11-13 (WebFetch, résumé) | Donne les URL de base : SRU `http://jsru.kb.nl/sru/sru` (exemple `?operation=explain`) et OAI-PMH `http://services.kb.nl/mdo/oai` (exemple `?verb=Identify`). « Aucune limite de requêtes, aucun quota ni aucune consigne d'usage pour les API. » (résumé du modèle) |
| https://iiif.io/news/2025/02/06/KB/ (annonce IIIF Consortium) | 2026-11-13 (WebFetch, résumé) | La KB est membre à part entière du consortium IIIF depuis février 2025 ; vise un accès « through Linked Data and IIIF standards ». **Aucune URL de manifeste, de collection ou d'API KB n'est donnée.** |

Ce qui n'a **pas** été trouvé dans la doc : URL d'un manifeste IIIF KB, URL d'une Image API, format d'identifiant, conditions propres aux API.

## 2. Recherche élargie

- Termes cherchés : « Koninklijke Bibliotheek IIIF API documentatie manifest iiif.kb.nl » ; « KB Nederland Koninklijke Bibliotheek data services API IIIF manifest terms of use » ; « iiif.kb.nl manifest jsonld Koninklijke Bibliotheek » ; « KB Netherlands national library API documentation endpoint "api.kb.nl" OR "data.kb.nl" OR "iiif.kb.nl" OR "jsru.kb.nl" » ; « KB Koninklijke Bibliotheek Delpher IIIF manifest endpoint rate limit developers ».
- Sources examinées : résultats de recherche ci-dessus (non lus en entier) ; dépôts `KBNLresearch/KB-python-API` et `intro-kb-apis` (repérés, le second lu) ; Wikipedia GLAM (tiers, non lu) ; article de 2018 (Od nr. 5, Zenodo) mentionnant un manifeste par publication libre de droits dans Delpher (source ancienne, non vérifiée).
- Résultat : **aucune doc publique KB ne décrit une API IIIF ni une limite de débit.** Les seuls endpoints documentés sont SRU et OAI-PMH. Une page de wiki tiers indique qu'il faut écrire à l'équipe data services avant usage ; non vérifié sur la source officielle.
- Un 2018 mentionne un manifeste par publication Delpher : **non vérifié aujourd'hui**, à ne pas considérer comme un endpoint actuel.

## 3. Tests d'appel (voir `tests/kb-nl.log`, en-têtes bruts dans `tests/raw/kb-nl/`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:08:00 | https://iiif.kb.nl/ | GET | Aucune réponse : **échec DNS** (`gaierror`, nom non résolu) | - | - | - |
| 2 | 21:08:03 | http://jsru.kb.nl/sru/sru?operation=explain | GET | 301 → https (même hôte) | aucun | - | 3 s (hôte différent) |
| 3 | 21:08:03 | http://services.kb.nl/mdo/oai?verb=Identify | GET | 301 → https (même hôte) | aucun | - | 0 s |
| 4 | 21:08:10 | https://jsru.kb.nl/sru/sru?operation=explain | GET | 200 | aucun | XML SRW `explainResponse` | 7 s |
| 5 | 21:08:10 | https://services.kb.nl/mdo/oai?verb=Identify | GET | 200 | aucun | XML OAI-PMH (758 o) | 0 s |
| 6 | 21:08:16 | https://jsru.kb.nl/sru/sru?operation=searchRetrieve&version=1.2&maximumRecords=1&query=dc.title%3Damsterdam | GET | 200 | aucun | XML `searchRetrieveResponse` (780 o) | 6 s |
| 7 | 21:08:16 | https://services.kb.nl/mdo/oai?verb=ListSets | GET | 200 | aucun | XML OAI-PMH (116 397 o) | 6 s |

Total : 7 requêtes sur un budget de 15 (les redirections comptent). Aucun 403, aucun 429, aucun captcha. Le jeu de requêtes 2–3 (http) a servi à constater la redirection ; la configuration complémentaire `scripts/config/kb-nl-suite.json` a relancé les mêmes endpoints en https.

Note : l'outil WebFetch a aussi renvoyé `ENOTFOUND` pour `iiif.kb.nl` ; la sonde a obtenu le même résultat au niveau DNS. Le nom ne se résout pas depuis ce poste à cette heure.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non. Aucune limite chiffrée ni consigne de débit trouvée dans les pages consultées (§1). Les conditions générales et le PDF de « house rules » n'ont pas été lus en entier.
- Limite **observée** (429 ou en-tête de quota reçu) : non. Sur les 4 réponses HTTP 200 et les 2 redirections, aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`.
- Accès refusé à ce client (403 anti-bot / défi) : non.
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucun en-tête de limite ; pas de champ de quota dans les XML lus).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : `iiif.kb.nl` non résolu (DNS, pas HTTP). Aucun autre.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : l'API IIIF KB n'a pas d'URL publique documentée dans les pages consultées ; le consortium IIIF annonce seulement l'intention d'accès IIIF (annonce de 2025). Les API réellement documentées (SRU, OAI-PMH) sont des services de métadonnées, pas IIIF.
- Hypothèses (étiquetées comme telles) : hypothèse 1 : le nom `iiif.kb.nl` est prévu mais pas encore en service (non vérifié ; le DNS ne le résout pas aujourd'hui). Hypothèse 2 : les manifestes passent par le viewer ou par Delpher, dont l'URL n'a pas été identifiée (non vérifié).

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen sur les endpoints SRU/OAI (testés en direct, 200) ; faible sur IIIF (aucune URL documentée, hôte non résolu).
- Ce qui reste à vérifier, et comment :
  1. Demander à l'équipe data services de la KB (lien « contact » de la page data services) : URL IIIF actuelle, politique de débit pour SRU/OAI et images.
  2. Relire le PDF « house rules » / conditions d'utilisation depuis un navigateur ordinaire (sans contournement) pour d'éventuelles clauses sur l'accès automatisé.
  3. Refaire une sonde sur `iiif.kb.nl` plus tard si le nom se résout ; ne pas deviner de chemin de manifeste.
  4. Chercher l'URL des manifestes dans la page source d'un visualiseur KB (Delpher, collections numériques), puis la tester avec la sonde.
