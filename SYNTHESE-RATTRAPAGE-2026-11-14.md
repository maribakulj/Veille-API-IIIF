# Suivi de rattrapage — 14 novembre 2026

**Branche :** `chatgpt/rattrapage-documentation-2026-11-14`. **Base :** `claude/veille-iiif-quotas`. **PR :** https://github.com/maribakulj/Veille-API-IIIF/pull/1 (brouillon, ne pas fusionner sans validation).

## Mesure exhaustive de départ

Le 14/11, l'ensemble des **93 fichiers** `institutions/*/data.json` de la branche de référence a été interrogé, en sept lots successifs. Le champ `a_verifier_manuellement` contient **260 lignes** brutes au total (dont des liens doublonnés, des `mailto:`, des renvois vers d'autres institutions, des URL historiquement lues ou désormais déplacées). Les dossiers `bnf-gallica` et `bnf-openapi` sont présents dans le total de 93 mais comportent **zéro** ligne manuelle ; ils sont exclus des investigations du rattrapage conformément à la consigne.

Ces **260 lignes ne sont pas 260 défauts d'accès vérifiés**, ni 260 tâches qui exigent une intervention humaine. Aucun bilan « 260 contrôlés et terminés » n'est revendiqué.

Le registre **`data/reverifications-chatgpt-2026-11-14.csv`** contient **32 observations explicites**, de nature différente : URL effectivement lues, source institutionnelle de substitution, vérification de code, erreur 404/503/WAF, correction de catégorie, ressource technique non testée, etc. Toutes les observations ne correspondent pas à une URL initialement inscrite dans `a_verifier_manuellement` : certaines signalent une nouvelle source ou une incohérence du benchmark. Ces 32 observations **ne représentent donc pas 30 items clos**.

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

**L'outil de rapprochement :** `scripts/etat_reverifications.py` lit seulement les `data.json` et le registre CSV, puis génère un inventaire de reprise :

```bash
python scripts/etat_reverifications.py --root . --out data/etat-reverifications.csv
```

Il ne contacte **aucune API distante**, et ne modifie ni les données institutionnelles ni `BENCHMARK.xlsx`. Ce script est **ajouté mais non exécuté dans cet environnement** ; le rapprochement et son résultat doivent être vérifiés avant tout import dans le benchmark. Le rapport créé est une file de travail, pas une vérité canonique.

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
