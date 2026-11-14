# Rattrapage documentaire L — 14 novembre 2026

## Périmètre
Huit dossiers du dépôt ajoutés hors des **84 institutions** d'origine, **hors BnF Gallica et BnF OpenAPI** : Internet Archive, British Library (hors EAP), SLUB Dresden, Herzog August Bibliothek (HAB), KB Pays-Bas, KB Danemark, Biblioteca Nacional de España (BNE), NYPL. La BnF est délibérément exclue conformément au `PLAN-RATTRAPAGE-CHATGPT.md`.

Toutes les constatations de ce rapport proviennent de la lecture des dossiers `institutions/*/data.json`, des sources publiques officielles et de leur documentation. **Lecture web ≠ test HTTP fiable depuis le poste de la sonde.**

## Internet Archive
- `https://iiif.archivelab.org/iiif/mma_irises_436528/info.json` : certificat TLS discordant lors de l'audit initial ; la nouvelle politique Internet Archive renvoie aussi vers `iiif.archive.org`. **Ne pas forcer un certificat invalide** ni affirmer un basculement complet de l'ancien hôte sans documentation de migration.
- `https://archive.org/services/tasks.php?rate_limits=1&cmd=modify_xml.php` exige une authentification S3 valide. Les chiffres de l'exemple `modify_xml.php` ne doivent pas être généralisés à IIIF.
- Le blog tiers Techdirt bloqué reste **secondaire**. La documentation officielle https://archive.org/developers/bots.html présente des recommandations de modération et de respect de `429` / `Retry-After`, sans quota universel.
- **Statut :** endpoint legacy et quotas de services authentifiés non vérifiés.

## British Library
- `https://iiif.bl.uk/` est toujours bloqué dans le dossier initial. Les manifestes actifs `bl.digirati.io` documentés auparavant ne doivent pas être présentés comme la preuve que **le même** service `iiif.bl.uk` est disponible.
- Une page officielle actuelle https://www.bl.uk/about/projects/medieval-england-and-france (consultée via moteur le 14/11) précise que **400 manuscrits British Library** du projet médiéval commun avec la BnF sont **indisponibles sur le site de comparaison**. C'est une information d'accessibilité **d'un corpus**, pas un quota d'API.
- La page historique `https://www.bl.uk/help/how-to-reuse-images-of-unpublished-manuscripts` demeure déplacée vers le portail générique ; les droits ne peuvent pas être inférés d'une simple URL `rights` au sein de manifestes.
- **Statut :** blocage technique et conditions d'images à confirmer.

## SLUB Dresden
- La documentation API officielle **LOD** https://data.slub-dresden.de/ est lisible ; elle décrit notamment la recherche exploratoire et un endpoint de réconciliation `/reconcile`. Le plafond de **10 000 résultats** du dossier se rapporte à cette API LOD, **pas à IIIF**. 
- `https://iiif.slub-dresden.de/` racine vide n'est pas une absence de service IIIF ; l'URL `kartenforum.slub-dresden.de` est soumise à des restrictions robots. Aucune limite Image/Presentation chiffrée n'est confirmée.
- **Statut :** politique et schéma d'URL IIIF à demander à l'institution ; services LOD séparés.

## Herzog August Bibliothek (HAB)
- La page institutionnelle https://www.hab.de/en/iiif-international-interfaces-for-digitised-cultural-assets/ explicite l'adoption d'IIIF avec la Bodleian et les quatre APIs (Image, Presentation, Authentication et Search). Elle ne publie pas un seuil de débit.
- `https://image.hab.de/robots.txt` reste 403 dans la preuve originale, et `https://iiif.bodleian.ox.ac.uk/robots.txt` est un **contrôle d'institution partenaire** à ne pas compter comme une lacune propre à HAB.
- **Alerte qualité** : la ligne `limites_documentees` « aucune limite de débit documentée » est actuellement **justifiée par une source sur le domaine public des images**, ce qui ne prouve en rien une absence de limitation du débit. Déplacer la preuve vers **droits et réutilisation** et laisser **quota inconnu**.
- **Statut :** documentation générale IIIF récupérée, robots et politiques de débit non établis.

## Koninklijke Bibliotheek — Pays-Bas
- La KB est officiellement **membre du consortium IIIF depuis le 6 février 2025**, source institutionnelle : https://www.kb.nl/en/news/kb-joins-iiif-consortium-new-opportunities-digital-heritage . La bibliothèque annonce le projet de rendre ses images accessibles via IIIF sur son site et des plateformes partenaires ; **ce n'est pas la preuve d'un endpoint** `https://iiif.kb.nl/`.
- Le portail https://www.kb.nl/onderzoeken-vinden/voor-onderzoekers/dataservices-apis-en-downloads explique les formats, APIs et téléchargements en masse des collections et recommande **l'accès par jeux de données** quand il s'agit d'exploiter de grands corpus, sous réserve du droit des collections.
- Un exemple **non officiel** publié sur Wikimedia Commons en juillet 2026 renvoie vers `https://iiif.bibliotheken.nl/KW-128-G-30` et `presentation-api.dlc.services`. Les deux liens **n'ont pas pu être vérifiés dans le lecteur web** et le lien ne provient pas d'une page KB démontrant l'appartenance de l'infrastructure. **NE PAS remplacer automatiquement `iiif.kb.nl` par ces hôtes**. Ces pistes restent de priorité élevée pour établir le véritable serveur IIIF.
- `data.bibliotheken.nl` linked data, Delpher robots et OAI ANP (400 notices par paquet et moissonnage conseillé hors heures de bureau) sont **trois familles différentes**.
- **Statut :** hébergement réel de l'IIIF KB et quotas par famille **ouverts**.

## Det Kongelige Bibliotek — Danemark
- `https://github.com/kb-dk/access-digital-objects/blob/master/oai-pmh.md` est bien une documentation officielle **historique** donnant deux hôtes `www.kb.dk/cop/oai/` et `oai.kb.dk/oai/provider`, avec opérations `Identify`, `ListSets`, `ListRecords`, `GetRecord`.
- `http://oai.kb.dk/oai/provider?verb=ListSets` est signalé **DNS introuvable** par la sonde initiale ; aucune preuve de migration ou de fonctionnement de `www.kb.dk/cop/oai/` n'a été obtenue dans cette passe. Ne pas appeler « remplacement opérationnel » une simple autre URL d'un README ancien.
- Le projet GitHub `kb-dk/cop3-backend` reçoit des mises à jour en 2026, mais sa présence ne prouve pas le statut des anciennes interfaces OAI.
- **Statut :** deux familles d'hôtes citées, aucune confirmation live d'endpoint ni de quota.

## Biblioteca Nacional de España
- `bnedigital.bne.es`, `datos.bne.es` et `www.bne.es` restent bloqués par la plateforme de lecture web dans cette passe, comme lors des précédents essais.
- Le PDF `procedimiento_normas_reproduccion.pdf` n'a pas été lu ; ne pas résumer une politique sur la base d'un résultat de recherche.
- La licence CC0 des **données** `datos.bne.es` n'établit pas les licences des images BNE Digital ni une absence de quota IIIF.
- **Statut :** non résolu, protection de domaine.

## New York Public Library — changement majeur pour le benchmark

- **Page de production actuelle** `https://api.repo.nypl.org/` (lecture le 14/11/2026) annonce explicitement : **Repo API dépréciée, indisponible à compter du 1er août 2026, aucun remplacement public annoncé à cette date**, contact `digitaldam@nypl.org`.
- Les anciennes pages `https://api.repo.nypl.org/api_documentation_v1` et `https://api.repo.nypl.org/sign_up` sont **toujours consultables** et peuvent afficher **10 000 requêtes/jour par jeton**. **Ce plafond est un chiffre historique du service déprécié**, et **ne doit plus être présenté comme quota actuel des API de la NYPL** sans mention de dépréciation.
- **Autre OpenAPI trouvée** : `https://api-collections.nypl.org/docs` (« NYPL Collections API », OAS 3.1, `https://api-collections.nypl.org/openapi.json` accessible en lecture JSON). Routes documentées : `GET /search`, `/search/suggestions`, `/captures/{uuid}/metadata`, `/collections`, `/collections/{uuid}`, `/items/{uuid}`, `/items/{uuid}/search`, etc.
- **MAIS** : aucune déclaration de remplacement de l'ancienne Repo API par la nouvelle Collections API n'a été retrouvée, et aucun quota/clé spécifique à cette nouvelle API n'est établi. Il faut **créer une ligne distincte avec statut “API documentée, gouvernance/auth/quotas à vérifier”**, et conserver le caractère déprécié de `api.repo.nypl.org`. Un endpoint lisible ne suffit pas à certifier un service stable ou destiné au public.
- `www.nypl.org/robots.txt`, `digitalcollections.nypl.org/robots.txt` et `www.nypl.org/help/about-nypl/legal-notices/terms-conditions` **demeurent filtrés Incapsula** dans la sonde ; les sources de l'API ne les remplacent pas.

## Recommandations de correction structurée
1. **Priorité absolue : NYPL**. Déclasser `10 000/j` de « actuel » à « historique : Repo API dépréciée au 2026-08-01 » ; ajouter le service `api-collections.nypl.org` avec statut séparé et quota inconnu.
2. **HAB** : déplacer citation de licences publiques hors des preuves sur les limites de débit.
3. **KB NL** : chercher la documentation institutionnelle qui relie un manifeste IIIF à une URL d'image, plutôt qu'écrire `iiif.kb.nl` par habitude.
4. **KB DK** : distinguer anciennes routes OAI et nouvelles infrastructures d'accès aux objets.
5. **British Library** : portée par corpus, pas par institution entière ; le projet de manuscrits médiévaux n'est pas une règle de l'IIIF de la BL.
6. **IA, BNE, SLUB** : les hôtes protégés, les quotas de logiciels ou de plateformes partenaires et les restrictions de copie doivent rester typés.


## Addendum : preuve de l'authentification de la nouvelle NYPL Collections API

Le code **officiel** `https://github.com/NYPL/digital-collections/blob/qa/ENVIRONMENTVARS.md` ainsi que `https://github.com/NYPL/digital-collections/blob/qa/.env.example` distingue expressément :
- `API_URL=https://api.repo.nypl.org` avec `AUTH_TOKEN` pour l'ancienne Repo API ;
- `COLLECTIONS_API_URL=https://api-collections.nypl.org` avec `COLLECTIONS_API_AUTH_TOKEN` pour la **nouvelle Collections API** ;
- `QA_COLLECTIONS_API_AUTH_TOKEN` distinct pour l'environnement de qualification.

Ces variables servent à l'application cliente de la NYPL et constituent une **preuve de prise en charge / utilisation d'un token d'accès**, **pas** la preuve que tous les endpoints publics exigent effectivement une authentification. Il est donc erroné de classifier `api-collections.nypl.org` « libre et sans clé » au seul motif que Swagger/OpenAPI est lisible.

**Statut corrigé :** nouvelle API documentée et active du point de vue de l'application NYPL, mode d'accès public, distribution de clés et rate limits non établis. Le bandeau de l'ancienne Repo API conserve la phrase « No public API replacement is planned ». Ces deux constats ne se contredisent pas nécessairement : une nouvelle API peut être réservée aux applications internes/autorisées.

Sources consultées 2026-11-14 :
- https://github.com/NYPL/digital-collections/blob/qa/ENVIRONMENTVARS.md
- https://github.com/NYPL/digital-collections/blob/qa/.env.example
- https://api-collections.nypl.org/openapi.json
- https://api.repo.nypl.org/
