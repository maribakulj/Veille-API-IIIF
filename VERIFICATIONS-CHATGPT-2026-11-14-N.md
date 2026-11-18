# Revérifications N : frontières entre API, authentification et quotas (14 novembre 2026)

Les trois lectures ci-dessous proviennent **des dépôts de code institutionnels officiels**, récupérés via le connecteur GitHub le 14/11/2026. La présence d'une valeur dans un dépôt ne constitue ni un test HTTP, ni une preuve du déploiement actuel sur l'hôte public. Aucun test de débit ni accès avec jeton n'a été effectué.

## GLAM-051 : University of British Columbia, Open Collections

**Source primaire :** [ubc-library/docs-open-collections-api, `data/api.twig.html`](https://github.com/ubc-library/docs-open-collections-api/blob/master/data/api.twig.html) ; fichier SHA Git `5625eea06eca3a8344dd6182f4b54a8a23836070`, lignes 34–60.

- Le modèle de page officiel affiche explicitement « no more than 200 requests per minute ».
- Le tableau sous « API Keys » distingue **Public API Key : 10req/min** et **Your API Key : 200req/min**.
- Il s'agit d'une **documentation source versionnée du portail API Open Collections**, non d'une annonce chiffrée documentée sur les deux serveurs IIIF `iiif.library.ubc.ca/image/` et `/presentation/`.
- **À vérifier** : date de publication de cette version du code, existence et périmètre du déploiement actuel, limite éventuelle sur manifestes et `info.json`, différence entre clé publique et accès vraiment anonyme.

**Décision pour le benchmark :** conserver les chiffres avec le qualificatif *source historique du code officiel / API Open Collections*, sans les propager aux endpoints IIIF.

## HORS-084 : New York Public Library, nouvelle Collections API

**Source primaire :** [NYPL/digital-collections, `ENVIRONMENTVARS.md` (branche qa)](https://github.com/NYPL/digital-collections/blob/qa/ENVIRONMENTVARS.md), SHA Git `34ee3dfb32e36b810ff36c41a8c82750e3b5e0a8`, lignes 26–29.

- Le client NYPL prévoit `COLLECTIONS_API_URL`, avec les hôtes QA et production distincts.
- Il prévoit aussi `COLLECTIONS_API_AUTH_TOKEN` (ainsi qu'un jeton QA), désigné comme **secret GitHub utilisé dans le déploiement**.
- **Cela n'établit pas** que toute requête de lecture publique à la Collections API exige un jeton. Cela établit seulement que le **client officiel dispose d'un mécanisme de jeton**.
- Il n'y a **aucun chiffre de quota** dans cette section. L'ancien plafond de **10 000/jour/jeton** cité par `api.repo.nypl.org` concerne **l'ancienne Repo API** annoncée arrêtée le **1er août 2026** selon le constat antérieur. Ne pas le présenter comme plafond de la nouvelle API.

**Décision pour le benchmark :** distinguer explicitement la cessation de l'ancienne API, les éléments de code sur la nouvelle et les limites encore inconnues des hôtes IIIF.

## GLAM-011 : Europeana, implémentation du Manifest API et endpoint public

**Source primaire :** [europeana/iiif-manifest-api, `README.md`](https://github.com/europeana/iiif-manifest-api/blob/master/README.md), SHA Git `ca84463ef11c62ee15bfd47b4a1540427ef60126`, lignes 1–17.

- Le **projet logiciel IIIF Manifest API** indique une requête avec `wskey` : `/presentation/<collectionId>/<recordId>/manifest?wskey=<apikey>`.
- Il décrit la génération de manifestes IIIF v2 ou v3 à partir de la **Record API** et, selon le cas, de l'API Full-Text.
- La **documentation institutionnelle de l'API IIIF publique** indique, elle, qu'aucune clé n'est nécessaire pour son service public. Le dépôt contient déjà des requêtes effectivement testées sans clé sur `iiif.europeana.eu`, conservées dans les journaux de l'audit précédent.
- **Aucune contradiction démontrée** : un README d'application (possiblement autre instance/version/route) n'établit pas la configuration d'authentification de `iiif.europeana.eu`. Ne pas importer la règle `wskey` dans la ligne du benchmark qui décrit le service public.

**Décision pour le benchmark :** créer au besoin deux couches distinctes « projet logiciel/implémentation » et « service IIIF public testé », sans quota chiffré attribué au second par extrapolation.

## Conséquences techniques

1. Enrichir les `data.json` de **notes de provenance par famille d'API et par version**, sans surinterpréter les sources.
2. Lier les URL sources dans le registre, puis rapprocher les résultats de `a_verifier_manuellement` **sans supprimer les blocages techniques existants**.
3. Vérifier localement `python -m unittest discover -s tests -p 'test_etat_reverifications.py'` et `python scripts/etat_reverifications.py --root . --out data/etat-reverifications.csv` avant intégration.
4. Appliquer les corrections canoniques **avec régénération du classeur par le pipeline local**, pas par mise à jour isolée du JSON. Conserver la PR en brouillon tant que les contrôles de cohérence et la provenance HTTP ne sont pas satisfaits.
