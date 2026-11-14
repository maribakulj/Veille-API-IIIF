# Suivi de rattrapage — 14 novembre 2026

**Branche :** `chatgpt/rattrapage-documentation-2026-11-14`. **Base :** `claude/veille-iiif-quotas`. **PR :** https://github.com/maribakulj/Veille-API-IIIF/pull/1 (brouillon, ne pas fusionner sans validation).

## Mesure exhaustive de départ

Le 14/11, l'ensemble des **93 fichiers** `institutions/*/data.json` de la branche de référence a été interrogé, en sept lots successifs. Le champ `a_verifier_manuellement` contient **260 lignes** brutes au total (dont des liens doublonnés, des `mailto:`, des renvois vers d'autres institutions, des URL historiquement lues ou désormais déplacées). Les dossiers `bnf-gallica` et `bnf-openapi` sont présents dans le total de 93 mais comportent **zéro** ligne manuelle ; ils sont exclus des investigations du rattrapage conformément à la consigne.

Ces **260 lignes ne sont pas 260 défauts d'accès vérifiés**, ni 260 tâches qui exigent une intervention humaine. Aucun bilan « 260 contrôlés et terminés » n'est revendiqué.

Le registre **`data/reverifications-chatgpt-2026-11-14.csv`** contient désormais **114 observations explicites**, de nature différente : URL effectivement lues, source institutionnelle de substitution, vérification de code, erreur 404/503/WAF, correction de catégorie, ressource technique non testée, etc. Toutes les observations ne correspondent pas à une URL initialement inscrite dans `a_verifier_manuellement` : certaines signalent une nouvelle source ou une incohérence du benchmark. Ces 114 observations **ne représentent pas 114 items clos**.

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

Il ne contacte **aucune API distante**, et ne modifie ni les données institutionnelles ni `BENCHMARK.xlsx`. Ce script est maintenant **exécuté avec succès en CI GitHub Actions**, avec quatre tests automatisés. Il produit un inventaire CSV en artefact téléchargeable, sans requête aux API patrimoniales : [exécution vérifiée](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43611154666). Le rapprochement ne vaut pas validation HTTP et son résultat doit être examiné avant tout import dans le benchmark. Le rapport créé est une file de travail, pas une vérité canonique.

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
