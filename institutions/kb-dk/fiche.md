# Det Kongelige Bibliotek (Bibliothèque royale, Danemark) — `kb-dk`

- **Statut** : en cours (tests faits ; documentation lue en résumé seulement, à relire en brut)
- **Pays** : Danemark
- **Point d'entrée testé** : `http://kb-images.kb.dk/` (IIIF Image API, info.json) et `https://www.kb.dk/cop/oai/` (OAI-PMH). Le point d'entrée `https://www.kb.dk/` est une page d'accueil sans API.
- **Vérifié le** : 2026-11-13 (tests vers 21:08–21:09 UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://www.kb.dk/ (accueil) | 2026-11-13 (WebFetch, résumé) | Aucune mention d'API, IIIF, manifeste ni quota. Renvoie vers pro.kb.dk, reglementer, ophavsret et kb@kb.dk pour les questions d'accès. |
| https://api.kb.dk/data/documentation (page « documentation » de l'API) | 2026-11-13 (WebFetch, résumé) | Aucun endpoint listé. Renvoie vers le dépôt GitHub « Det-Kongelige-Bibliotek/access-digital-objects ». Aucune mention de quota. |
| https://github.com/Det-Kongelige-Bibliotek/access-digital-objects (doc officielle, dépôt de l'institution, 329 commits, GFDL) | 2026-11-13 (WebFetch, résumé) | « Our dissemination API is OAI-PMH » ; « Virtually all content in COP is delivered as images » ; « our metadata is basically public domain » (CC0) ; « our content is provided with a much more restrictive CC license » (souvent CC BY-NC-ND 2.0) ; « Everything that's free comes with no guarantee ». **Aucune limite de débit, quota ni clé API.** |
| https://raw.githubusercontent.com/Det-Kongelige-Bibliotek/access-digital-objects/master/image-delivery.md | 2026-11-13 (WebFetch, résumé) | Décrit l'Image API IIIF (info.json JSON-LD, `full/!2000,/0/native.jpg`). « you retrieve images up to 8000x8000px. » Aucune mention de quota, débit, IIIF Presentation ou manifeste. |
| https://raw.githubusercontent.com/Det-Kongelige-Bibliotek/access-digital-objects/master/oai-pmh.md | 2026-11-13 (WebFetch, résumé) | Base `http://www.kb.dk/cop/oai/` ; verbes Identify, ListSets, ListRecords, GetRecord ; préfixes mods, oai_dc, ese. « you need to store them in a database or index of your own ». **Aucune limite de débit.** |
| https://raw.githubusercontent.com/Det-Kongelige-Bibliotek/access-digital-objects/master/cop-backend.md | 2026-11-13 (WebFetch, résumé) | Services `/cop/syndication/…` (RSS/MODS/KML), `/cop/navigation/…` (OPML), `/cop/content/…`. Pagination par blocs de 40. Aucune mention de quota, IIIF ou manifeste. |
| https://www.kb.dk/en/find-materials/collections/netarkivet/research-access/delivery-data et https://www.kb.dk/en/services/cultural-heritage-research-and-study/access-data | 2026-11-13 (WebFetch, résumé) | Accès aux données « sur demande » : « Under certain conditions, data may be released for research use. » ; « We cannot provide newspapers that are less than 140 years old for research use. » ; « we will in some cases charge a fee for handing it over ». Pas de quota ni de débit. |
| https://www.kb.dk/reglementer (règlements) | 2026-11-13 (WebFetch, résumé) | Rien sur usage automatisé, scraping, API ni quota. Les textes complets sont sur des pages liées, **non lues**. |

Conclusion documentaire : aucune limite chiffrée (quota, fenêtre, débit) ni règle sur l'usage automatisé trouvée dans les pages consultées. Le texte intégral du règlement d'utilisation (« Brugerreglement ») n'a pas été lu.

## 2. Recherche élargie

- Termes cherchés : « Det Kongelige Bibliotek IIIF API dokumentation manifest » ; « api.kb.dk Det Kongelige Bibliotek rate limit OR quota OR "fair use" digital objects ».
- Sources examinées : résultats de recherche (non lus en entier), api.kb.dk, dépôt access-digital-objects, page kb.dk « Access to data ». Pas de Wayback consulté.
- Résultat : aucun billet, issue ni forum trouvé sur un quota ou un débit de l'API KB. Un document Zenodo (30/03/2026, présentation IIIF pour une réunion à la KB) n'est qu'une présentation générale, sans endpoint.
- Aucun manifeste IIIF Presentation KB trouvé dans la doc ni dans les résultats.

## 3. Tests d'appel (voir `institutions/kb-dk/tests/journal.log`)

Configurations : `institutions/kb-dk/config/kb-dk.json` (10 requêtes) et `institutions/kb-dk/config/kb-dk-suite.json` (2 requêtes, variantes https). Total : 12 requêtes sur 15.

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:08:31 | http://www.kb.dk/cop/oai/?verb=Identify | GET | 301 (vers https, non suivi) | aucun | vide | – |
| 2 | 21:08:37 | http://www.kb.dk/cop/oai/?verb=GetRecord… (oai_dc) | GET | 301 (non suivi) | aucun | vide | 6 s |
| 3 | 21:08:38 | http://oai.kb.dk/oai/provider?verb=Identify | GET | erreur réseau : DNS non résolu | – | – | 1 s |
| 4 | 21:08:40 | http://kb-images.kb.dk/…/kbb_alb_2_191_friis_011/info.json | GET | 200 | aucun | JSON-LD IIIF Image 2 | 2 s |
| 5 | 21:08:50 | http://kb-images.kb.dk/…/dfs_1906_6a_16_001/info.json | GET | 200 | aucun | JSON-LD IIIF Image 2 | 10 s |
| 6 | 21:09:00 | http://kb-images.kb.dk/…/full/!2000,/0/native.jpg | GET | 200 | aucun | JPEG (iipsrv 1.3-8.2026…) | 10 s |
| 7 | 21:09:00 | https://www.kb.dk/cop/syndication/images/billed/2010/okt/billeder/ | GET | 200 | aucun | RSS XML | 0 s (autre hôte) |
| 8 | 21:09:07 | https://www.kb.dk/cop/navigation/images/billed/2010/okt/billeder/subject841/ | GET | 200 | aucun | OPML XML | 7 s |
| 9 | 21:09:14 | https://www.kb.dk/cop/images/billed/2010/okt/billeder | GET | 404 | aucun | page d'erreur Tomcat | 7 s |
| 10 | 21:09:20 | http://www.kb.dk/imageService/w640/…kbb_alb_2_191_friis_011.jpg (ancienne syntaxe, dépréciée) | GET | 301 (non suivi) | aucun | vide | 6 s |
| 11 | 21:09:26 | https://www.kb.dk/cop/oai/?verb=Identify | GET | 200 | aucun | OAI-PMH XML | 6 s |
| 12 | 21:09:33 | https://www.kb.dk/imageService/w640/…kbb_alb_2_191_friis_011.jpg | GET | 404 | aucun | page HTML danoise | 7 s |

Notes sur le test :
- Le journal écrit « 301 OK » et « 200 OK » : le libellé « OK » du script signifie seulement « statut < 400 ». Les 301 ne sont pas suivis par la sonde (pas de redirection suivie) ; les URL https (tests 11) ont été ajoutées pour atteindre la cible.
- Les URL des tests 4–6 ont été reconstituées à partir d'un résumé de `image-delivery.md` (chemins reconstitués segment par segment). Elles fonctionnent, mais la forme exacte de l'identifiant IIIF (slashes non encodés) n'a pas été vérifiée dans le texte brut du document.
- L'hôte `oai.kb.dk` cité comme exemple dans `oai-pmh.md` ne se résout pas depuis notre poste (DNS). Non suivi.
- Aucun 403, aucun 429, aucun CAPTCHA, aucun en-tête `Retry-After`, `X-RateLimit-*` ou `RateLimit-*`.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non (aucune limite de débit ou quota trouvée dans les pages consultées ; texte intégral du règlement non lu).
- Limite **observée** (429 ou en-tête de quota reçu) : non (12 requêtes espacées de 6 s ou plus, sans 429 ni en-tête de quota).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : non.
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucun en-tête de limite sur les réponses 200).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : pas de 403. Erreur DNS sur `oai.kb.dk` (test 3). Redirections http→https non suivies par la sonde (tests 1, 2, 10). Ancienne syntaxe `imageService` en 404 en https (test 12).
- Points d'usage (documentés, non quotas) : images jusqu'à 8000 × 8000 px ; métadonnées CC0 ; contenus sous licence CC plus restrictive ; données de recherche « sur demande », parfois payantes, journaux de moins de 140 ans non fournis pour la recherche.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : aucun quota ni règle de débit dans la doc de l'institution. La doc dit que les métadonnées sont « basically public domain » et que la diffusion des métadonnées est OAI-PMH.
- Hypothèses (étiquetées comme telles) : hypothèse 1 : pas de quota formalisé, l'accès se fait par usage raisonnable (non vérifié). Hypothèse 2 : pour les données de recherche, la limite est une question de procédure (« sur demande », disponibilité de la bibliothèque), non de débit (non vérifié).

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Recherche menée après la sonde, sans nouvelle requête vers l'API. Aucun endpoint de statut ni en-tête de quota trouvé, donc aucune configuration `scripts/config/kb-dk-quota.json` n'a été écrite.

a) **Endpoint de statut de quota** : non trouvé — termes cherchés : « Det Kongelige Bibliotek API rate limit X-RateLimit IIIF kb-images » ; « kb-labs-api github rate limit OR fair use OR throttl OR requests per » ; « Det Kongelige Bibliotek IIIF API dokumentation manifest ». Pages lues (2026-11-13) : https://www.kb.dk/en/find-materials/systems-and-services/api (WebFetch) : aucune phrase sur quota, clé ou inscription ; https://github.com/Det-Kongelige-Bibliotek/access-digital-objects (README, fiche) : aucune mention de limite.
b) **En-têtes de limite documentés** : non trouvé. Observé (12 requêtes, fiche) : aucun en-tête `Retry-After`, `X-RateLimit-*` ou `RateLimit-*`.
c) **Clé ou compte donnant un quota** : non trouvé. Source tierce (non officielle) : AgentAccess, https://agentaccess.dk/sites/kb/api/kb-labs (2026-11-13) : « Auth required | Public ». Le kb-labs-api n'est pas le service IIIF testé.
d) **Contact officiel pour un quota** : trouvé, générique — kb@kb.dk et téléphone +45 3347 4747, sur https://www.kb.dk/en/find-materials/systems-and-services/api (2026-11-13, WebFetch). La page précise que ce sont des coordonnées générales de la bibliothèque, non propres à l'API. Adresse à utiliser pour la demande.

Standard : le brouillon IETF `draft-ietf-httpapi-ratelimit-headers` (RateLimit-*) n'est pas une norme ; la spécification IIIF n'a pas été relue sur ce point.

Conclusion : moyen d'interroger le quota : **non**. Piste : demander à kb@kb.dk une politique de débit pour l'Image API et l'OAI-PMH, et si un manifeste IIIF est prévu.

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen (tests réels cohérents, doc lue surtout en résumé).
- Points IIIF : seule l'**Image API** est documentée (info.json, JPEG). Aucun **manifeste IIIF Presentation** n'a été trouvé. Le manifeste reste à demander à l'institution ou à chercher dans un viewer KB.
- Ce qui reste à vérifier :
  1. Lire en brut le `image-delivery.md` et le `README.md` du dépôt access-digital-objects (noter la forme exacte de l'identifiant IIIF).
  2. Lire le texte intégral du règlement (Brugerreglement) sur kb.dk/reglementer et la page ophavsret : chercher « automatisk », « robot », « masse ».
  3. Demander par écrit à kb@kb.dk s'il existe une limite de débit pour l'Image API et l'OAI-PMH, et si un manifeste IIIF est prévu.
  4. Refaire un suivi des redirections http→https (suivre le Location) si l'on veut consigner la cible exacte.
