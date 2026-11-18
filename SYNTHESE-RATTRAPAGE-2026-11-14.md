# Suivi de rattrapage — 14 novembre 2026

**Branche :** `chatgpt/rattrapage-documentation-2026-11-14`. **Base :** `claude/veille-iiif-quotas`. **PR :** https://github.com/maribakulj/Veille-API-IIIF/pull/1 (brouillon, ne pas fusionner sans validation).

## Mesure exhaustive de départ

Le 14/11, l'ensemble des **93 fichiers** `institutions/*/data.json` de la branche de référence a été interrogé, en sept lots successifs. Le champ `a_verifier_manuellement` contient **260 lignes** brutes au total (dont des liens doublonnés, des `mailto:`, des renvois vers d'autres institutions, des URL historiquement lues ou désormais déplacées). Les dossiers `bnf-gallica` et `bnf-openapi` sont présents dans le total de 93 mais comportent **zéro** ligne manuelle ; ils sont exclus des investigations du rattrapage conformément à la consigne.

Ces **260 lignes ne sont pas 260 défauts d'accès vérifiés**, ni 260 tâches qui exigent une intervention humaine. Aucun bilan « 260 contrôlés et terminés » n'est revendiqué.

Le registre **`data/reverifications-chatgpt-2026-11-14.csv`** contient désormais **360 observations explicites**, de nature différente : URL effectivement lues, source institutionnelle de substitution, vérification de code, erreur 404/503/WAF, correction de catégorie, ressource technique non testée, etc. Toutes les observations ne correspondent pas à une URL initialement inscrite dans `a_verifier_manuellement` : certaines signalent une nouvelle source ou une incohérence du benchmark. Ces 360 observations **ne représentent pas 360 items clos**.

## Rapports détaillés

- `VERIFICATIONS-CHATGPT-2026-11-14.md` : Europeana, e-rara, e-manuscripta, Cardiff.
- `VERIFICATIONS-CHATGPT-2026-11-14-B.md` : AIC, BNE, Cornell, Brown, LoC, Huntington, Kyoto, Finna, UCD, Wales.
- `VERIFICATIONS-CHATGPT-2026-11-14-C.md` : Bodleian, British Library EAP, Cambridge CUDL, Édimbourg et Écosse.
- `VERIFICATIONS-CHATGPT-2026-11-14-D.md` : National Gallery Londres, Norvège, Leiden, EPFL et Biblissima.
- `VERIFICATIONS-CHATGPT-2026-11-14-E.md` : MDZ, Göttingen, Heidelberg, ÖNB, Bologne, Vatican.
- `VERIFICATIONS-CHATGPT-2026-11-14-F.md` : Smithsonian, Harvard Art Museums, Yale YCBA.
- `VERIFICATIONS-CHATGPT-2026-11-14-G.md` : Michigan et LUX Yale.
- `VERIFICATIONS-CHATGPT-2026-11-14-H.md` : Northwestern, Duke, UCLA, Princeton.
- `VERIFICATIONS-CHATGPT-2026-11-14-I.md` : UBC et GLAM-050 à GLAM-057.
- `VERIFICATIONS-CHATGPT-2026-11-14-J.md` : GLAM-058 à GLAM-069.
- `VERIFICATIONS-CHATGPT-2026-11-14-K.md` : GLAM-070 à GLAM-084.
- `VERIFICATIONS-CHATGPT-2026-11-14-L.md` : institutions hors liste (Internet Archive, BL, SLUB, HAB, KB NL/DK, BNE, NYPL).
- `VERIFICATIONS-CHATGPT-2026-11-14-M.md` : confirmation de la cible IIIF Collection Cultural Japan et licences 1MP/6MP NPM Taïwan.
- `VERIFICATIONS-CHATGPT-2026-11-14-N.md` : sources de code officielles UBC, NYPL et Europeana, et distinction entre couche applicative et endpoint IIIF public.

**L'outil de rapprochement :** `scripts/etat_reverifications.py` lit seulement les `data.json` et le registre CSV, puis génère un inventaire de reprise :

```bash
python scripts/etat_reverifications.py --root . --out data/etat-reverifications.csv
```

Il ne contacte **aucune API distante**, et ne modifie ni les données institutionnelles ni `BENCHMARK.xlsx`. Ce script est maintenant **exécuté avec succès en CI GitHub Actions**, avec cinq tests automatisés. Il produit un inventaire CSV en artefact téléchargeable, sans requête aux API patrimoniales : [exécution vérifiée](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43611154666). Le rapprochement ne vaut pas validation HTTP et son résultat doit être examiné avant tout import dans le benchmark. Le rapport créé est une file de travail, pas une vérité canonique.

## Corrections prioritaires avant intégration au benchmark

1. **NYPL — P0 :** bannière officielle d'arrêt de l'ancienne Repo API au **1er août 2026**. Quota historique **10 000/jour/jeton**, à dater. Nouvelle `api-collections.nypl.org` avec OpenAPI mais jeton client `COLLECTIONS_API_AUTH_TOKEN` attesté dans le code de l'application NYPL ; accessibilité anonyme et quotas inconnus. Ne pas marquer comme remplaçante publique.
2. **Heidelberg, EPFL, HAB — P0 :** corriger les inférences erronées « numérisations libres de droit/gratuites ou absence de Crawl-delay = absence de limite de débit ».
3. **UBC — P0 :** anciennes valeurs **10 req/min clé publique et 200 req/min clé personnelle** retrouvées **dans le code officiel (2021)**, non attribuables d'office à IIIF et à confirmer comme actuelles.
4. **ÖNB — P1 :** manifeste IIIF v3 et identifiant `10168F8E` trouvés dans la documentation institutionnelle ; tester poliment son URL depuis une sonde autorisée.
5. **DRI — P1 :** chemin Swagger `/api-docs/v1/swagger.json` et `GET /iiif/{id}/manifest` confirmés par les tests/code officiels, dont une voie publique sans authentification pour les manifestes publiés ; l'hôte reste filtré.
6. **Leeds — P1 :** manifeste médiéval exact `https://iiif.library.leeds.ac.uk/presentation/cc/q8qkdfmm` retrouvé dans la notice `372687`. Route non exécutée.
7. **Digital Commonwealth — P1 :** API JSON / OAI / IIIF officiellement documentées ; ancienne page Institutions en 404 et OpenSearch sous Anubis.
8. **KU Leuven, CUDL, Yale LUX, Michigan — P1 :** cartographier les couches (intérieures, APIs publiques, fournisseurs IIIF et gestionnaires de clés) sans transposer un quota global institutionnel à toutes les familles.
9. **Waseda, e-Museum, SLV — P1 :** des guides/conditions auparavant inaccessibles sont lisibles ; manifestes ou protections d'hôtes techniques restent à vérifier.
10. **Cultural Japan/NPM Taïwan — P1 :** la collection IIIF du premier est bien référencée depuis son site, mais JSON bloqué ; les conditions officielles du second distinguent 1 MP CC0 et 6 MP CC BY 4.0, hors quotas.
11. **Contacts institutionnels — P2 :** les limites volontairement non publiées ou les permissions de moissonnage (Biblissima SPARQL, e-codices, Utrecht, etc.) nécessitent une réponse humaine. Les inscrire « contact requis » et non « page web à débloquer ».

## État non achevé

Le **travail documentaire de rattrapage a parcouru les établissements**, mais **pas toutes les 260 URL en lecture directe** ; les rapports sont différenciés en fonction des URL réellement consultées. Le registre et le script favorisent une reprise mécanisée avec vérification explicite.

Le `data.json` de référence, les étapes a–g et `BENCHMARK.xlsx` sont **inchangés** : le passage des faits retenus aux données canoniques et la régénération du classeur constituent une étape distincte, à faire de façon cohérente avec `scripts/suivi.py` et `scripts/build_benchmark.py`.

Aucun test de charge, contournement de WAF, création d'identifiant ni demande institutionnelle n'a été effectué. Les quotas et droits doivent rester rattachés à leur service, leur version et leurs dates de preuve.

## État vérifié du rapprochement (après les rapports A, B, C et N)

Le script `scripts/etat_reverifications.py` a été corrigé pour **conserver tous les statuts** sur une URL : le cas de Cultural Japan combine `BLOCAGE_ACCES` et `LIEN_OFFICIEL_CIBLE_CONFIRME` ; le second ne supprime pas le premier. Les tests d'intégration sont dans `tests/test_etat_reverifications.py`.

Résultats de [l'exécution GitHub Actions réussie](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43611154666) du 14/11/2026, après inscription des constats des rapports A à C :

| Mesure | Résultat | Interprétation |
| --- | ---: | --- |
| Dossiers institutionnels lus | 93 | 2 BnF sans entrée manuelle, écartés du rattrapage |
| Entrées manuelles initiales | 260 | Une ligne peut être une URL non consultée, un doublon ou un contact |
| Observations inscrites au registre | 84 | Sources A, B, C, N et lots précédents ; pas toutes liées aux 260 lignes |
| Entrées correspondant à au moins un constat du registre | **70** | Correspondance exacte par slug et URL normalisée, **pas 70 vérifications achevées** |
| Entrées sans constat relié dans ce registre | **190** | Certaines sont déjà discutées dans les rapports D–M, à indexer |
| Constats du registre sans entrée manuelle correspondante | 13 | Informations supplémentaires, nécessaires mais hors file initiale |
| Entrées avec plusieurs constats | 1 | Cultural Japan : deux statuts, conservés ensemble |
| Entrées répétées dans un même dossier | 2 | Signal heuristique du script |
| Références inter-institutions | 10 | Ne pas attribuer automatiquement le service au mauvais établissement |

Les **4 tests sur 4** et la production du CSV ont réussi. Le rapport C a également été rapproché, notamment la contradiction documentaire sur les droits des images d'Édimbourg, à arbitrer avec les périmètres de collections. Les statistiques proviennent du journal de CI, non d'un recalcul approximatif.

**Prochain ordre de travail :** indexer les rapports D–M dans le registre ; distinguer les statuts documentaires des contrôles HTTP ; examiner les 190 entrées sans constat rapproché ; traiter ensuite les erreurs de portée des plafonds NYPL/UBC/EPFL/Heidelberg/HAB et confirmer les endpoints IIIF. L'intégration des `data.json` avec la régénération de `BENCHMARK.xlsx` reste une étape distincte et non accomplie. Ne pas fusionner la PR.

## Recentrage sur l'objectif initial : lire les URL auparavant « manuelles » (passe O)

La reprise ne doit pas se limiter à consigner les résultats précédents : **la tâche prioritaire est de récupérer le contenu des URL originales**. Nouveau rapport [`VERIFICATIONS-CHATGPT-2026-11-14-O-LECTURES-REELLES.md`](VERIFICATIONS-CHATGPT-2026-11-14-O-LECTURES-REELLES.md). La passe a essayé des pages en direct avec un lecteur web, puis une extraction publique alternative pour les pages bloquées. Les dates d'indexation antérieures ont été conservées.

**Résultat CI vérifié du 14/11/2026 :** [exécution réussie](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43612532734), cinq tests automatisés réussis, 93 `data.json`, 260 entrées manuelles historiques :

| Indicateur | Nombre | Portée |
|---|---:|---|
| Observations du registre | **114** | Une URL peut avoir plusieurs constats |
| Entrées de la file originale avec ≥ 1 constat exact | **73 / 260** | Pas 73 clôtures |
| Entrées sans constat dans le registre | **187 / 260** | Beaucoup figurent dans les rapports antérieurs non indexés |
| **Contenu lu par lecteur web dans la passe O** | **10** | Lecture du texte original ou redirection documentée |
| **Contenu récupéré en copie datée dans la passe O** | **14** | Texte ou JSON récupéré via un second extracteur, pas nécessairement live |
| Entrées dont le contenu n'est pas certifié par la passe O | **236** | Cela ne veut pas dire que les 236 sont définitivement illisibles, ni que les rapports antérieurs ne les ont pas étudiées |
| URLs avec plusieurs constats reliés | 24 | Historique de blocage et lecture retrouvée conservés |
| Observations hors des URL initiales | 16 | Sources institutionnelles supplémentaires |

**Nouvelles lectures particulièrement utiles :**
- PDF IIIF du National Palace Museum (Taiwan) : texte extrait, 13 pages, et huit URL de manifestes explicitement publiées ; la lecture PDF directe avait expiré. L'extraction ne constitue pas un rendu visuel intégral.
- Conditions de Cambridge Digital Library récupérées (copie datée du 18/09), malgré le 403 en lecture web : restriction contractuelle sur l'extraction systématique substantielle.
- Documentation **PPOC JSON** de la Library of Congress récupérée (copie du 29/08), distincte du quota IIIF Image Services.
- Manifeste **IIIF Presentation 2** de State Library Victoria effectivement extrait en JSON (copie du 05/11), mais en-têtes HTTP non testés.
- Conditions et `robots.txt` de NYPL récupérés par extraction : le site annonce que son ancienne Repo API a cessé au 1er août 2026 et qu'aucun remplacement **public** n'était prévu.
- Textes des pages initiales e-rara et e-manuscripta consultés directement ; e-manuscripta requiert un accord écrit pour copie systématique des fichiers vers d'autres serveurs.

**Toujours non récupérés avec les deux lecteurs :** fichier JSON Collection de Cultural Japan, manifeste de Leeds, OpenAPI de DRI (seul le shell Swagger UI apparaît), API-docs Brown (vérification humaine), entre autres.

Le nouveau CSV généré par GitHub Actions contient la colonne `lecture_documentaire`, avec les états `TEXTE_LU_PAR_LECTEUR_WEB`, `TEXTE_RECUPERE_COPIE_DATEE` et `CONTENU_NON_DEMONTRE_PAR_REPRISE_O`. **Filtrer cette colonne plutôt que renvoyer à Marcel sans distinction toutes les 260 URL.** L'historique des 403/WAF et les tests de quotas demeurent séparés et non certifiés par ces lectures. La PR reste brouillon et les `data.json` canoniques / `BENCHMARK.xlsx` ne sont pas modifiés.

## Dernière mesure : lectures P et URL de manifestes complémentaires (CI du 14/11)

La passe P s'attaque aux **URL initialement manuelles** en reprenant les dossiers GLAM-009 à GLAM-084 : [rapport P détaillé](VERIFICATIONS-CHATGPT-2026-11-14-P-LECTURES.md). Les extraits datés des URL d'origine sont conservés, même lorsque le lecteur HTTP alternatif échoue. Les nouveaux **JSON réellement récupérés** incluent Michigan Image v2, National Diet Library Presentation v2, et des extraits des manifestes Michigan et Heidelberg v2/v3. **Ne pas déduire des en-têtes ou des plafonds de débit d'une extraction de contenu.**

**Dernier calcul vérifié :** [GitHub Actions #43613670803](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43613670803), CI réussie, cinq tests réussis :

| Indicateur à date | Valeur | Lecture correcte |
|---|---:|---|
| Dossiers / lignes manuelles initiales | 93 / 260 | Périmètre inchangé |
| Constats sourcés dans le registre | **159** | Inclut les découvertes hors liste |
| Entrées ayant ≥ 1 constat lié par URL | **108 / 260** | Ne signifie ni accessible live ni terminé |
| Entrées encore sans constat relié | **152 / 260** | File restante à rapprocher et à tenter |
| Entrées avec contenu lu via un lecteur web | **10 / 260** | Selon états du script sur les passes précédentes |
| Entrées avec texte/JSON récupéré en copie datée | **43 / 260** | Pas nécessairement live |
| Entrées sans preuve de contenu selon l'inventaire des passes O/P | **207 / 260** | Inclut des pages de contact, erreurs, doublons et les rapports non rapprochés |
| Entrées avec plusieurs observations | **29** | Ancien blocage et nouvelle extraction conservés |
| Observations hors URL initiale | **22** | Liens manifestes et documents de substitution |

Les principales nouvelles découvertes sont : **le contenu historique de l'ancienne documentation National Gallery** (paramètre `limit` jusqu'à 100 = nombre de résultats, **pas de requêtes/minute**), le fichier robots de la **bibliothèque de Leiden** (distinct de l'hôte IIIF), le **JSON Image 2 du Michigan** avec tailles de tuiles, le **manifeste IIIF v2 de la NDL**, le **lien officiel du manuscrit Waseda**, les catalogues datasets ÖNB, et des textes des pages FAQ, droits et contact préalablement sous blocage.

**Priorité de la suite :** lire les 207 entrées dont le contenu n'est pas démontré par les passes O/P, et distinguer dans cette file les véritables documents illisibles des URL historiques déplacées, contacts humains, robots et endpoints HTTP nécessitant une sonde. Les chiffres des sections précédentes restent des **instantanés historiques**, supplantés par le tableau ci-dessus. Données canoniques et Excel inchangés ; PR toujours brouillon.

## Nouvelle mesure : lectures Q et R, dont PDF Duke (14/11/2026)

**Livrables :**
- [`VERIFICATIONS-CHATGPT-2026-11-14-Q-LECTURES.md`](VERIFICATIONS-CHATGPT-2026-11-14-Q-LECTURES.md) : **30 URL initialement manuelles** (Princeton, Harvard, Yale, Washington, Toronto, St Andrews, LIBIS, Jena, SLUB). Addendum : **PDF Duke Anubis (13 pages) lu intégralement**, avec contrôle visuel des pages 1 et 5.
- [`VERIFICATIONS-CHATGPT-2026-11-14-R-LECTURES.md`](VERIFICATIONS-CHATGPT-2026-11-14-R-LECTURES.md) : **20 URL manuelles** (Wellcome, NLS, IA, British Library, Vatican, Bologne, Finna, etc.) et un **vrai `info.json` IIIF Image 2** de National Library of Scotland retrouvé par le guide cartographique officiel.
- Sources nouvelles majeures : les articles institutionnels Wellcome 2026 sur les bots et sur dix années d'IIIF (DLCS / iiif-builder). Le premier décrit la **limitation par budget de moissonneur ou réseau** plutôt que des quotas publics fixes : c'est exactement une réponse pertinente au problème « institutions sans quota documenté ».

**Bilan GitHub Actions confirmé :** [exécution #43614739419 réussie](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43614739419), **5 tests réussis** et génération de l'inventaire :

| Indicateur | État actuel | Ce que cela mesure |
|---|---:|---|
| Dossiers / entrées historiques manuelles | **93 / 260** | Base inchangée |
| **Observations totales du registre** | **211** | Peut inclure plusieurs constats par URL |
| **Entrées avec ≥ 1 constat relié** | **155 / 260** | Ne signifie pas 155 URL closes |
| Entrées encore sans constat relié | **105 / 260** | À reprendre en priorité |
| Entrées ayant contenu lu par lecteur web | **11** | Selon qualification stricte du script |
| Entrées ayant contenu extrait en copie datée | **66** | Cache ou extraction, HTTP live non certifié |
| **Total ayant un contenu documenté dans les passes O–R** | **77 / 260** | Lecture réussie du contenu, pas contrôle HTTP technique |
| Entrées sans contenu démontré par ces passes | **183 / 260** | Comprend contacts, anciens chemins, refus et entrées encore non tentées |
| Entrées avec constats multiples | **33** | Historique conservé, ne pas écraser un refus par une lecture indexée |
| Observations hors liste initiale | **23** | Sources de substitution, exemples de manifestes |

Ces chiffres **supplantent** les instantanés des sections précédentes. La priorité demeure de récupérer le **contenu** des 183 autres entrées ou de justifier pourquoi le document n'est pas publiquement lisible, puis de réduire la liste destinée à une intervention humaine. Les `data.json` canoniques et `BENCHMARK.xlsx` restent inchangés en attendant la validation simultanée du pipeline ; la PR est toujours en brouillon.

## Dernière passe S (14/11) : 20 URL Yale, Folger, NC State, Princeton, Huntington

[Rapport S](VERIFICATIONS-CHATGPT-2026-11-14-S-LECTURES.md) : vingt URL de la file d'origine à nouveau tentées, en privilégiant la lecture réelle de contenu. Deux preuves de ressources machine viennent de **Yale University Library** : `GET /catalog/oai?verb=Identify` donne le texte de la réponse OAI-PMH, et `GET /iiif/2/32352934/info.json` donne un JSON Image API 2 (5 095 × 6 784 px, tuiles 512). Aucune mesure d'en-têtes ni plafond IIIF n'est déduit. **Folger Digital Collections** reste devant une page de vérification humaine, et le `robots.txt` de **Huntington** a été récupéré. La copie du portail n'équivaut jamais à un contrôle du serveur d'images.

**État du registre et de la file manuelle selon [GitHub Actions #43615051749](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43615051749) réussi (5 tests sur 5)** :

| Indicateur | Dernier état |
|---|---:|
| Institutions / entrées manuelles de départ | **93 / 260** |
| Observations au registre | **231** |
| Entrées avec au moins un constat exact | **172 / 260** |
| Entrées sans constat associé | **88 / 260** |
| Entrées avec contenu lu au lecteur web | **11** |
| Entrées avec texte/JSON récupéré en copie datée | **80** |
| **Entrées disposant d'une lecture documentaire du contenu** | **91 / 260** |
| **Entrées sans preuve de contenu dans les passes O–S** | **169 / 260** |
| Entrées avec plusieurs constats | **36** |
| Sources supplémentaires hors de la file initiale | **23** |

La qualification des 169 **ne veut pas dire** « 169 pages bloquées ». Elle inclut les URLs qui sont des contacts, des anciennes routes, des réponses HTTP refusées, des pages de protection sans document, et celles qui n'ont pas encore été reprises.

**À poursuivre en priorité :** les 88 entrées sans aucune correspondance avec le registre; puis les autres sans contenu. Ne pas demander à l'utilisateur de tout relire : seul le résidu qui exige réellement un navigateur humain, un compte ou une réponse institutionnelle est à conserver comme « vérification manuelle ». Les anciennes sections ci-dessus sont des mesures historisées; **ce tableau est l'état courant**. La source de vérité `data.json` et le classeur `BENCHMARK.xlsx` restent inchangés jusqu'à régénération validée.

## Reprise du 15 novembre 2026 — passes T et U, résultats de la dernière CI

- **Rapport T** : [`VERIFICATIONS-CHATGPT-2026-11-15-T-LECTURES.md`](VERIFICATIONS-CHATGPT-2026-11-15-T-LECTURES.md). Les **88 URL historiques** qui n'avaient encore aucun constat lié ont été **classées**, non pas déclarées toutes lues. Les plus importants documents extraits sont les API JSON Brown (dont manifeste IIIF et `info.json` associés), e-rara Content Search, OAI-PMH MDZ, LoC JSON, IIIF Image 2 SLV et l'**OpenAPI Finna REST version 11.0.3** (six chemins). Deux PDF de diapositives, Cardiff et Yale, ont été ouverts avec **échantillonnage visuel explicitement daté**, et non validés page par page.
- **Rapport U** : [`VERIFICATIONS-CHATGPT-2026-11-15-U-LECTURES.md`](VERIFICATIONS-CHATGPT-2026-11-15-U-LECTURES.md). Deuxième passe sur les **126 entrées à contenu non démontré** après T : réexamens ciblés des pages BNE, AIC, Cardiff, CUDL, Europeana, e-rara, LoC, Finna, etc. Les pages de contenu réellement récupérées sont promues au statut `COPIE_...` ; les **403/404, shells SPA, redirections sur pages génériques et fichiers JSON non extraits** gardent un statut ouvert. Les sources de substitution EAP et Göttingen sont documentées sans être confondues avec les anciennes URL.

[**GitHub Actions #43709360396, réussite des 5 tests et génération du CSV**](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43709360396), dernière métrique :

| Mesure | État au 15/11 |
| --- | ---: |
| Dossiers institutionnels / lignes initiales | **93 / 260** |
| Observations documentaires inscrites dans le registre | **345** |
| Lignes possédant un constat par URL et dossier | **260 / 260** |
| Lignes **sans** constat de triage | **0** |
| Lignes avec contenu **lu par le lecteur web** | **11** |
| Lignes avec texte/JSON **récupéré en copie indexée datée** | **139** |
| **Total de lignes dont le contenu a été obtenu au cours des passes** | **150 / 260** |
| Lignes avec contenu **non démontré** | **110 / 260** |
| Lignes disposant de plusieurs constats conservés | **61** |
| Observations supplémentaires hors des 260 URL | **23** |

**Rappel indispensable :** `260/260 classées` mesure la couverture de la **file de vérifications**, **pas** la disponibilité HTTP ni l'absence de protection ; `150 contenus obtenus` inclut **139 copies datées potentiellement non valides aujourd'hui** et des pages de conditions, robots ou contacts qui ne prouvent pas un quota IIIF. Les **110** incluent notamment des liens obsolètes, des documents sous WAF/SSO, des éléments réellement non lus, des formulaires et des PDF seulement partiellement inspectés. Les classer en `non obtenu` est plus fidèle que de les renvoyer tous à l'utilisateur pour une lecture manuelle.

**Constats techniques à prioriser :** reprendre les véritables JSON manquants (Cultural Japan Collection, IIIF Image AIC, manifeste Villanova, NPM Taïwan, QDL, Northwestern), les descriptions OpenAPI impossibles à extraire (DRI Swagger), puis **distinguer les contacts et comptes humains obligatoires** des erreurs historiques. Pour les quotas, ne pas inférer de limite depuis `robots.txt`, `maxArea`, le nombre de résultats d'une recherche, le nombre de collections, une licence ou l'existence d'une clé sur un autre service.

**État des livrables canoniques :** `institutions/*/data.json`, les `fiche.md` et `BENCHMARK.xlsx` restent à reprendre dans une intégration cohérente avec validation du générateur. **Ne pas fusionner la PR** avant cette intégration et contrôle du résidu.

## Passe V du 15/11/2026 : lectures et triage des interventions

Le manifeste original Qatar Digital Library a été récupéré en JSON Presentation v2 intégral (16 709 caractères, copie datée du 23/10). Les autres nouvelles sources sont le manifeste Cambridge (247 499 caractères), l'OpenAPI de Northwestern v2 et une collection de 30 sous-collections d'IIIF Discovery in Japan, **distincte** du service original Cultural Japan. Les conditions de droits Qatar et e-Museum ont été retrouvées sur des pages institutionnelles de remplacement. Détails : [rapport V](VERIFICATIONS-CHATGPT-2026-11-15-V-SOURCES-ET-TRIAGE.md).

Un outil reproductible a été ajouté : `scripts/triage_interventions.py`, avec tests, et CI qui publie `data/triage-interventions-humaines.csv` et `data/resume-triage-interventions.json` en artefact GitHub Actions. La [shortlist des démarches](ACTIONS-HUMAINES-PRIORITAIRES-2026-11-15.md) décrit seulement trois demandes institutionnelles et deux contrôles de compte potentiels (ces derniers périphériques à IIIF). Aucun compte, formulaire ni courriel envoyé.

**[Dernière CI validée #43730045511](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43730045511)** : 93 dossiers, 260 URL initiales, **349 observations**, 151 contenus obtenus (**11 lectures web et 140 copies datées**), **109 sans preuve de contenu original**. Ces 109 ont été réparties en **82 cas sans lecture humaine par défaut**, **22 interventions conditionnelles** et **5 démarches explicites de contact ou de compte**. Les catégories reflètent une aide à la décision, pas un statut HTTP ni un quota.

Les données canoniques, fiches et BENCHMARK.xlsx sont toujours à réconcilier/régénérer ensemble ; la PR reste brouillon.

## Dernière reprise : passe W, correction canonique et Excel synchronisé (15/11/2026)

**Rapport W** : [`VERIFICATIONS-CHATGPT-2026-11-15-W-IIIF-IMAGES.md`](VERIFICATIONS-CHATGPT-2026-11-15-W-IIIF-IMAGES.md). Le `info.json` **original** de l'Art Institute of Chicago a été récupéré **en JSON complet et analysé**, avec dimensions 6 679 × 4 577 px, tuiles 256, profil IIIF Image 2 level2, copie indexée du 15/11. Les 403 de l'autre client et le témoignage d'utilisateurs Cloudflare restent conservés. Le serveur NPM donne des exemples Cantaloupe IIIF v2, mais l'image NPM ciblée est encore en timeout.

**État de rapprochement validé par [GitHub Actions #43741287143](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43741287143)** : 93 dossiers, 260 URL historiques rapprochées, **351 observations au registre**, **152/260 contenus documentaires récupérés** (11 lectures web et 141 copies datées), **108/260 sans preuve de contenu**. Sur ces 108 : **81** sans lecture humaine requise par défaut, **22** démarches conditionnelles et **5** contacts/comptes explicites. Ces chiffres ne représentent aucun contrôle HTTP live supplémentaire ni mesure de débit.

**Première intégration canonique atomique** : commit [`7302096`](https://github.com/maribakulj/Veille-API-IIIF/commit/7302096bd81f2581f9879f9097dcdb411f594d88) modifiant ensemble les `data.json` et les `fiche.md` des dossiers **Art Institute of Chicago**, **Qatar Digital Library**, **National Palace Museum** et **Northwestern**. Les entrées `web` précisent les dates de copies et pointent vers les rapports enregistrés. Les anciennes observations 403/timeout restent inchangées, aucun quota inventé.

**Regénération effective de `BENCHMARK.xlsx`** : [GitHub Actions #43741867021](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43741867021) **réussie** après `fetch-depth: 0` (nécessaire au contrôle des antériorités de configuration). `scripts/suivi.py validate` indique **VALIDATION OK : 93 institutions** ; le générateur canonique a produit le classeur **290 420 octets** (12 feuilles), vérifié comme archive ZIP/XML valide, **1 498 / 1 498 preuves présentes**, et l'a **committé en binaire** sous [`1464820`](https://github.com/maribakulj/Veille-API-IIIF/commit/1464820dea251900752cc535874d249ff5b4e14e). Le workbook reste fondé sur les `data.json` canoniques, tandis que le triage des anciennes URL conserve son propre CSV séparé.

**Important** : l'onglet historique `À vérifier à la main` contient toujours 260 URL, pour assurer la traçabilité. Ce n'est **pas** la liste des 108 preuves manquantes ni celle des cinq décisions humaines identifiées. La liste de travail active et son triage sont dans l'artefact `rattrapage-inventaire-manuel` de la CI documentaire et dans [`ACTIONS-HUMAINES-PRIORITAIRES-2026-11-15.md`](ACTIONS-HUMAINES-PRIORITAIRES-2026-11-15.md).

**PR maintenue en brouillon** : les réponses HTTP sur Cultural Japan, Northwestern Image, Villanova, NPM Image, Digital Commonwealth et DRI restent incomplètes malgré les alternatives documentaires. Pas de test de charge ni de contournement des protections.

## Passe X/Y du 15 novembre : 157 URL avec contenu démontré et 7 dossiers réconciliés

**Rapport [X](VERIFICATIONS-CHATGPT-2026-11-15-X-DOCUMENTS-ORIGINAUX.md)** : quatre URL manuelles originales ont désormais leur **texte lu en copie indexée datée** : deux pages Finna (index des documentations et documentation REST complète), une page Contact Us de National Gallery of Art et l'étude de cas de préservation numérique des Parliamentary Archives. Les copies anciennes restent datées et ne certifient pas la réponse HTTP en direct. Trois recherches de remplacement officielles ont été corroborées : migration du service expérimental IIIF d'Internet Archive (`iiif.archivelab.org`) vers `iiif.archive.org` (exemple *Iris* en JSON Image v2), avis de Cloudflare Bot Protection publié par Brown (mise en œuvre printemps 2025) et conditions Finna (REST métadonnées sans inscription obligatoire, droit de réserver des restrictions en cas de charge ; CC0 des métadonnées **non** applicable automatiquement aux images). **Les quotas IIIF ne sont pas déduits** des règles REST ou d'une copie indexée.

**Rapport [Y](VERIFICATIONS-CHATGPT-2026-11-15-Y-PDF-IIIF.md)** : la présentation CNI sur Yale LUX (2022), **texte des 26 diapositives analysé** et figures représentatives contrôlées, documente JSON-LD, Linked Art et IIIF Change Discovery mais ne présente pas de valeur chiffrée de débit. Celle de Cardiff (Alma Digital/Universal Viewer) est **essentiellement composée d'images : 25 des 29 diapositives inspectées visuellement**, avec **pages 20, 23, 24, 28 non lues** en raison de délais d'accès. Elle n'est **pas** classée document intégralement lu.

**Données canoniques :** commit [`921a0a3`](https://github.com/maribakulj/Veille-API-IIIF/commit/921a0a3cd0a6502e16caa83154cb67314faab39c) : `data.json` et `fiche.md` de **cinq dossiers** Internet Archive, Brown, Finna, National Gallery of Art et Parliamentary Archives. Commit [`064381e`](https://github.com/maribakulj/Veille-API-IIIF/commit/064381e0813bc1b7bd1586652ea64474283620ee) : deux dossiers supplémentaires **Yale Peabody et Cardiff**. Dates de copie et statuts HTTP historiques conservés.

**Validation [GitHub Actions #43748080199](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43748080199), succès :**

| Mesure | Situation actualisée |
| --- | ---: |
| Institutions et URL historiques | **93 / 260** |
| Observations documentaires dans le registre | **360** |
| URL d'origine avec au moins un constat relié | **260/260** |
| Lecture par lecteur web | **11/260** |
| Contenu récupéré en copie datée, y compris texte complet Yale PDF | **146/260** |
| **Contenus dont une lecture est démontrée** | **157/260** |
| **Contenus sans preuve de lecture** (notamment les quatre diapositives Cardiff) | **103/260** |
| Parmi les 103 : sans lecture humaine par défaut | **80** |
| Parmi les 103 : intervention conditionnelle | **18** |
| Parmi les 103 : contact ou compte éventuel identifié | **5** |

**Classeur intégré :** [workflow de reconstruction #43748080192](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43748080192) **réussi**, après validation stricte **93 institutions / aucune preuve manquante**, Excel de **292 212 octets** régénéré et committé (commit `ff26f51`). L'onglet historique des 260 URL reste volontairement conservé pour la traçabilité ; **le CSV de triage produit par la CI est la liste active**. Les anciens résumés chiffrés du présent document sont des photographies de versions antérieures, pas l'état courant.

Les endpoints encore bloqués (Cultural Japan Collection, Northwestern IIIF Image, Villanova, NPM IIIF Image, DRI Swagger) et la vérification de l'accès HTTP réel restent ouverts. **PR en brouillon.**

## Reprise de fiabilité au 16 novembre 2026 : synchronisation garantie et Bodleian GLAM-002

**Anomalie détectée et corrigée** : le workflow Excel ne se déclenchait jusqu'alors que pour `data.json` et `fiche.md`, **pas pour les changements de `CONSIGNE-ET-SUIVI.md`** pourtant lus par le générateur. Après modification, [`benchmark-sync-rattrapage.yml`](.github/workflows/benchmark-sync-rattrapage.yml) écoute les changements de **`institutions/**`** (données, suivis, sources, tests, fiches), du script générateur, du validateur, de la méthode et des dépendances. La CI valide les 93 dossiers, puis crée un Excel uniquement depuis ces sources. Une course réelle entre le lancement et des commits GitHub avait causé un **push refusé** ([ancienne exécution #43773958508](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43773958508)). Un nouvel algorithme **recharge la branche avancée, réexécute validation et génération, puis retente le push** sans force-push ni rebase d'un tableur calculé sur une source périmée. Il limite les tentatives à quatre et échoue en cas d'impossibilité, plutôt que de publier un résultat potentiellement obsolète.

**Nouveau garde-fou de provenance** : `scripts/valider_preuves_rattrapage.py` exige, pour chaque entrée `web` ajoutée avec `preuve=VERIFICATIONS-CHATGPT-...`, une **URL originale**, une **date de consultation**, un **résumé**, un **rapport présent dans le dépôt citant exactement la même URL** et une citation de ce rapport depuis `fiche.md`. Quatre nouveaux tests unitaires négatifs vérifient le rejet d'une URL introuvable dans le rapport, d'une preuve non reprise en fiche et d'une date absente. **Il ne remplace pas les captures originales SHA-256 exigées par l'étape a** : les notes de lecture provenant de copies indexées sont clairement qualifiées comme telles.

**Résultats CI contrôlés après correction** :
- [Contrôle documentaire #43774439255](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43774439255) : **20 tests réussis**, **16 nouvelles observations `web` avec liens probants validés, 0 erreur** ; le périmètre reste à **157 contenus récupérés / 260 URL**, **103 sans contenu original démontré**, dont 5 démarches de contact/compte éventuelles.
- [Synchronisation Excel #43774367720](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43774367720) : **succès**, validation `93 institutions`, aucune preuve manquante, classeur **292 265 octets** reconstruit et **poussé sur la branche** ; jamais édité cellule par cellule.

**Reprise ordonnée de GLAM-002, Bodleian** : le fil historique [« Crawler Etiquette — a request » (13/11/2017)](https://groups.google.com/g/iiif-discuss/c/Z3GVdj6s61w), auparavant cité seulement par extraits, a été **lu intégralement** via copie datée au 15/11. Il recommande un User-Agent de contact, cite une **pause volontaire de 500 ms** comme exemple de courtoisie, et demande de contacter la bibliothèque pour les récoltes importantes. La réponse d'un autre participant évoque `429` et `Retry-After` comme bonnes pratiques ; **aucun de ces chiffres ou en-têtes n'est un quota appliqué en 2026**. Lecture et méthode de provenance inscrites dans [`institutions/bodleian/sources/lectures-2026-11-16/IIIF-DISCUSS-2017-NOTE.md`](institutions/bodleian/sources/lectures-2026-11-16/IIIF-DISCUSS-2017-NOTE.md), ainsi que `data.json` et `fiche.md`. Le `robots.txt` du serveur IIIF reste en réponse **400**, sans règle récupérée.

**Ce qui demeure hors garantie CI** : l'authenticité d'un contenu extrait par un index public, la bonne interprétation d'un contrat d'accès, la capture brute horodatée de chaque nouvelle source avec SHA-256 et la disponibilité HTTP en temps réel. Toute étape méthode a–g **non faite ne doit pas être cochée à partir d'un simple rapport**. Aucun nouveau crash test n'a été entrepris.

## Correctif méthodologique du 16 novembre : **un chiffre n'est pas un quota**

L'inspection **du vrai classeur** (génération précédente) a révélé un risque de lecture : le KPI « 81 limites officielles chiffrées » agrégeait des valeurs de nature disparate, notamment `Crawl-delay: 30 s`, une largeur d'image de 1 200 px, une taille de pagination de 500 résultats, des restrictions de droits et des débits d'API. **81 ne voulait donc pas dire 81 quotas HTTP.**

Le générateur `scripts/build_benchmark.py` utilise désormais le module sans réseau `scripts/classification_limites.py` pour afficher **deux mesures distinctes**, avec un libellé plus prudent :
- **81 restrictions officielles contenant un chiffre, toutes natures confondues**. Cet indicateur décrit les sources numériques documentées, **pas** un nombre de quotas.
- **3 seuils de débit explicitement identifiés dans une classification conservatrice** (ne retient que les natures « limite de débit » et « limite WAF », avec valeur numérique et fenêtre de temps, source officielle et étape d validée). **Ce nombre est un minimum typologique, pas l'inventaire exhaustif des limitations réelles ni des quotas spécifiquement IIIF.** Certaines limites sont sur des API REST/métadonnées ou un WAF.

L'onglet « Limites » contient à présent la colonne **« Catégorie indicative »** (robots, pagination/dimensions, recommandations, droits, débits, autres), un filtre et un en-tête « Chiffre officiel ? (≠ quota de débit) ». Le tableau de bord rappelle explicitement la différence.

**[CI documentaire #43775094377](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43775094377) : 26 tests sur 26 réussis**, dont six nouveaux contrôles sur les erreurs de catégorie (robots, images, pagination, recommandations et quotas hors IIIF). **[CI Excel #43775094412](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43775094412) : succès**, validation des 93 institutions et 16 observations complémentaires, puis création du nouveau `BENCHMARK.xlsx` **293 686 octets, 12 feuilles**, commit binaire `1eaeb27`. Le classeur a ensuite été **réimporté avec un lecteur de tableur indépendant** et les deux valeurs **81 / 3** ainsi que la colonne de typologie ont été vérifiées directement.

Ce correctif **ne modifie aucune observation de la source institutionnelle** : il répare la présentation d'une donnée hétérogène qui aurait pu être prise pour un nombre de quotas IIIF. La typologie demeure explicitement **indicative** pour les enregistrements anciens.


## Nouvelle reprise des 18 novembre 2026 : passes AA et AB, contenus et intégration

Les deux rapports [AA](VERIFICATIONS-CHATGPT-2026-11-18-AA-NPM-EUROPEANA-CARDIFF.md) et [AB](VERIFICATIONS-CHATGPT-2026-11-18-AB-HARVARD-KB-CULTURALJAPAN.md) documentent **cinq URL historiques réellement obtenues en plus**, distinguées des autres échecs d'accès. **Les dates d'acquisition des copies ne sont pas une preuve de réponse HTTP live**.

- **NPM Taïwan (GLAM-080)** : URL Image API v2 `.../K1F%2FK1F000001N000000000PAA/info.json` enfin retrouvée sous forme de **893 caractères JSON complets**, analysés et [sauvegardés dans le dépôt](institutions/national-palace-museum-taiwan/sources/lectures-2026-11-18/info-K1F000001N000000000PAA-indexed.json). Dimensions **3 055 × 2 291**, tuiles **512**, profil **level2**, capture indexée du **18/11**. Le `timeout` de la sonde de novembre est conservé comme observation distincte ; `maxArea` est une surface d'image, pas un quota.
- **Europeana Pro** : le `robots.txt` original, copie du **05/11**, contient des directives actives `User-agent: *` et `Disallow: /admin/`. Cela ne vaut **pas** pour les hôtes d'API Europeana et ne fournit aucune limite de débit.
- **Harvard** : texte complet (13 940 caractères, copie du **23/08**) de la politique HUIT de plateforme **Apigee**, distinction documentation-portail/gateway, contrôles et `rate limiting` *possibles*. **Ce n'est pas un contrat d'API IIIF de Harvard Library**. Page Harvard LTS Support ancienne (2018) récupérée aussi, sans quota.
- **KB Pays-Bas** : vrai accueil LOD `data.bibliotheken.nl` (2 729 caractères, copie du **16/11**), services Triply/RDF et licence CC0 des données ; **pas** le serveur IIIF KB.
- **Cardiff** : trois pages PDF supplémentaires **20, 23 et 28**, réellement inspectées visuellement. Bilan **28/29 diapositives**, la page **24** demeure inaccessible. Ne pas présenter le diaporama comme intégralement lu.
- **Cultural Japan** : article technique **de 2021** de Satoru Nakamura lu en entier : AWS Lambda et graphes RDF de Japan Search/Cultural Japan utilisés pour des manifestes générés dynamiquement. **Cette source historique est hors de la liste initiale et ne clôt pas** le `collection.json` original (qui demeure sans contenu).

**Mises à jour canoniques** : dossiers `national-palace-museum-taiwan`, `europeana`, `cardiff-university-library`, `harvard`, `kb-nl` et `cultural-japan`, chacun avec `data.json` et `fiche.md`. Le registre compte **367 observations**, dont des sources complémentaires hors liste initiale.

### Indicateurs confirmés par la CI du 18/11

[CI documentaire #44403182532](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/44403182532) **réussie** : **28 tests**, **23 observations supplémentaires intégrées aux données vérifiées structurellement**, aucune erreur de preuve. [CI Excel #44403182221](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/44403182221) **réussie** : `scripts/suivi.py validate` OK pour les **93 institutions**, **0 preuve référencée manquante**, classeur `BENCHMARK.xlsx` reconstruit et committé (`7212ead`).

| Mesure | Au 18 novembre 2026 |
| --- | ---: |
| Institutions / URL manuelles historiques | **93 / 260** |
| Lignes avec au moins une observation | **260 / 260** |
| Contenu réellement obtenu dans le registre | **162 / 260** |
| Dont lecture directe / copie datée | **11 / 151** |
| Contenu non démontré | **98 / 260** |
| Parmi les 98 : sans nouvelle lecture humaine par défaut | **77** |
| Parmi les 98 : intervention seulement si indispensable | **16** |
| Parmi les 98 : contact ou compte explicitement identifiable | **5** |

**Ne pas confondre** : 162 extraits documentaires, 162 services HTTP actuels accessibles et 162 politiques de quota connues sont trois mesures **différentes**. Les 98 entrées restantes incluent des `robots.txt` inaccessibles, de vieux chemins, des exigences de compte et des vrais endpoints restés sans JSON. La liste de travail active reste le CSV d'artefact CI, pas les 260 références conservées dans l'onglet historique du classeur. **PR en brouillon**, aucun test de charge ni contournement réalisé.

