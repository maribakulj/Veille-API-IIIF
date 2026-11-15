# Passe V — vrais manifestes récupérés, documentation technique et triage des blocages

Date : **15 novembre 2026**. Suite des passes T et U sur les 110 entrées dont le contenu original restait non démontré, avec lecture des **documents originaux** et de sources institutionnelles alternatives lorsqu'un endpoint ne répondait pas.

> **Méthode et limites** : extraction publique de pages et de JSON, avec date `acquired_at` restituée par le lecteur. Une copie indexée du 23 octobre **n'est pas** une réponse HTTP du 15 novembre depuis notre sonde, ne supprime pas l'ancien 403 observé par un autre client, et ne renseigne pas les en-têtes RateLimit. Pas de test de charge, de captcha contourné, de connexion non autorisée ou de promesse d'un accès libre sans quota.

## 1. Qatar Digital Library — original manifeste vraiment lu

**URL exacte de la liste manuelle :**

`https://www.qdl.qa/en/iiif/81055/vdc_100023807156.0x000001/manifest`

Un **document JSON complet de 16 709 caractères** a été extrait par le lecteur public (date de copie **2026-10-23**) et **parsé comme JSON** :

- `@context`: `http://iiif.io/api/presentation/2/context.json`
- `@type`: `sc:Manifest`, `sequences` : **1**
- `@id` correspond à l'URL originale ; label de l'ouvrage de Thomas Elwon sur les côtes de la mer Rouge et d'Aden

Il ne s'agit donc ni de l'écran Cloudflare ni d'un simple lien vers le manifeste. **La lecture documentaire originale est désormais satisfaite grâce à la copie datée**, mais sa disponibilité HTTP depuis tous les réseaux et ses en-têtes de limite restent ouverts.

**Source institutionnelle officielle** : `https://www.qdl.qa/en/image-options`, copie textuelle du **2026-10-03**. Elle explique la construction des URLs Image API et Presentation API et documente un **maximum de 1 200 pixels du plus grand côté** des images récupérables, avec procédure de contact pour les versions plus haute résolution. C'est une **limitation de dimension d'image**, non un quota de nombre de requêtes par minute. Cette information figurait déjà dans le `data.json` de QDL, on ne la présente pas comme nouvellement découverte.

## 2. Cambridge Digital Library — manifeste récupéré et source du middleware

**URL institutionnelle supplémentaire explicite :**

`https://cudl.lib.cam.ac.uk/iiif/MS-ADD-03996`

Le lecteur a obtenu le **JSON IIIF Presentation 2 complet (247 499 caractères)**, analysé comme `sc:Manifest` avec **1** séquence, label **Trinity College Notebook (MS Add. 3996)** et services Image API. Date de copie **2026-11-15**.

Le code de l'institution, `https://github.com/cambridge-collection/cudl-services/blob/main/README.md`, décrit les routes du middleware **`/v1/metadata/`** et **`/v1/transcription/`**, ainsi que l'existence de plusieurs instances (dev/staging/live). Le README précise que l'API de services est généralement publique sans authentification mais conçue principalement pour le visualiseur CUDL. La route `/v1/iiif/` de ce middleware est mentionnée comme non utilisée dans le README consulté. Il faut **distinguer ce middleware des véritables endpoints `cudl.lib.cam.ac.uk/iiif/` et `images.lib.cam.ac.uk/iiif/`**. Les deux URL originales `cudl.link/v1/metadata/` et `cudl.link/v1/transcription/...` n'ont toujours **pas** fourni de contenu via le lecteur, et ne doivent pas être marquées 200.

## 3. Northwestern — OpenAPI actuelle, confidentialité des chemins

**Source institutionnelle** : `https://api.dc.library.northwestern.edu/docs/v2/spec/openapi.yaml`.

Spécification **OpenAPI 3.1.0**, version applicative **2.0.0**, serveur `https://api.dc.library.northwestern.edu/api/v2`, corps YAML de **19 463 caractères** extrait le **15/11**. Le fichier contient les schémas `bearerAuth` / JWT et un choix de sécurité global incluant l'anonymat, mais la combinaison exacte des droits dépend des endpoints ; **ne pas conclure que toutes les routes exigent une clé**. Aucune règle `rate-limit` ou `quota` chiffrée trouvée dans le YAML. Le `429` dans ce fichier apparaît également comme sous-chaîne d'un UUID, **pas comme une réponse de limitation**.

Documentation officielle : `https://api.dc.library.northwestern.edu/docs/v2/index.html`, section IIIF : la représentation d'une œuvre peut être demandée avec `?as=iiif`, exemple `https://api.dc.library.northwestern.edu/api/v2/works/9f9a7032-717f-4446-a0c3-193404a4c090?as=iiif`. Cet exemple **n'a pas rendu de corps JSON** via notre extracteur (signal `fetch_error`, code 200 isolé), pas de validation live. La description institutionnelle distingue API REST de données, images et manifestes IIIF.

L'URL *originale* `https://iiif.dc.library.northwestern.edu/iiif/3/e814609e-ddfd-4427-b4cf-1a70d6e49129/info.json` **demeure sans JSON récupéré**. La documentation publique complète **la fiche de stratégie et de procédure d'accès**, mais **ne transforme pas le statut de cet `info.json`**.

## 4. Cultural Japan — collection de remplacement d'un autre producteur, pas équivalente

Le JSON original `https://app.cultural.jp/iiif-collection/collection.json` demeure non extrait, alors que le site Cultural Japan documente la recherche transcollections et les APIs.

On a cependant retrouvé un jeu **distinct** du contributeur « IIIF Discovery in Japan » : `https://nakamura196.github.io/iiif/data/collection/collection.json`, **JSON Collection IIIF Presentation 2 complet (6 765 caractères)**, `sc:Collection`, 30 sous-collections, copie au **15/11**. Documentation du producteur : `https://github.com/nakamura196/iiif`.

**Important :** cette source donne accès à une **partie contributrice** du domaine de recherche Cultural Japan, **pas** à la collection IIIF globale hébergée sur `app.cultural.jp`. Elle sert de **jeu alternatif immédiatement exploitable pour un cas de recherche**, et non de preuve que l'URL originale a été lue.

## 5. Règle de triage pour les 110 URL sans lecture

Construire désormais une file **séparée et strictement qualifiée**. Éviter d'affecter une lecture manuelle à un `robots.txt` inaccessible, à une URL obsolète, ou à une démarche exigeant une clé ; ces trois cas demandent des interventions de nature différente.

| Type de suite | Action appropriée |
|---|---|
| `CONTACT_OU_COMPTE` | Courriel institutionnel, clé API, compte, formulaire ou consentement ; **nécessite décision et éventuellement action de l'utilisateur**, pas relecture d'une page |
| `URL_OBSOLETE_REPLACEE` | Consigner URL de remplacement et date ; **pas de travail humain de lecture** de l'ancienne URL 404 |
| `CONTROLE_TECHNIQUE_AUTORISE` | Vérification de la réponse, du corps JSON, des en-têtes sur une connexion autorisée, sans provoquer de dépassement |
| `ACCES_PROTEGE` | Demander accès officiel / point de contact lorsque la protection empêche réellement un cas d'usage ; ne pas contourner WAF/CAPTCHA |
| `SOURCE_HISTORIQUE_OU_PARTIELLE` | Version intégrale/actuelle du document, ou pages et figures d'un PDF partiellement inspectées, lorsque cela affecte une décision |
| `INFORMATION_RECUPEREE_ALTERNATIVE` | Vérifier l'identité de la source de substitution et conserver l'URL originale non lue ; **pas forcément une action humaine** |

La séparation doit aboutir à une liste réellement actionnable : **« une preuve/lecture manque » n'est pas synonyme de « fais-la manuellement ».**

Les `data.json` des institutions et `BENCHMARK.xlsx` ne sont pas régénérés par ce rapport. PR en brouillon.
