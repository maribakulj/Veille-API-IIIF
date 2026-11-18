# Passe AA : deux URL originales lues, Cardiff 28/29

Date des vérifications : **18 novembre 2026**. La cible est la file de 260 URL manuelles des 93 institutions IIIF. Les extraits publics comportent une date d'acquisition **indexée** ; cela n'établit pas le statut HTTP live, l'accès depuis tout client ni l'absence de quotas. Aucun test de charge ou contournement anti-bot.

## NPM Taiwan : véritable info.json original

- URL exacte : `https://iiifod.npm.gov.tw/iiif/2/K1F%2FK1F000001N000000000PAA/info.json`.
- Extraction **complète**, parsée comme JSON : **893 caractères**, copie indexée acquise le **2026-11-18**. Le fichier a été **enregistré dans le dépôt** : [info-K1F000001N000000000PAA-indexed.json](institutions/national-palace-museum-taiwan/sources/lectures-2026-11-18/info-K1F000001N000000000PAA-indexed.json).
- `@context=http://iiif.io/api/image/2/context.json` ; `@id` conforme à l'URL exacte ; **width 3055, height 2291**, `tiles` **512 × 512**, `scaleFactors` **1/2/4/8/16/32**, profil `level2.json`. `maxArea=6999005` correspond aux **pixels²** (3055 × 2291), pas à un quota HTTP.
- Le **timeout historique de la sonde** reste exact, et un second lecteur web n'ouvre toujours pas la ressource. La présence d'une copie indexée intégrale ne prouve pas un accès automatisé pour tous. Aucun en-tête de limitation n'a été lu.

## Europeana Pro : robots.txt original

- URL exacte : `https://pro.europeana.eu/robots.txt`. **Corps complet** retrouvé dans une copie datée du **2026-11-05**, suivi du contexte de 24+ commentaires (noms de robots et directives précédées de `#`).
- Les **seules directives effectives** du bloc final sont `User-agent: *` puis `Disallow: /admin/`.
- Domaine concerné : **pro.europeana.eu**, pas les hôtes techniques `api.europeana.eu` ou IIIF. Ceci ne fournit **aucun débit**, ne confirme ni n'infirme la limite historique **120 requêtes/10 secondes** issue d'un échange Europeana API daté de 2024, déjà documenté dans la fiche.

## Cardiff : lecture réelle de trois diapositives encore manquantes

PDF original : `https://igelu.org/wp-content/uploads/2022/10/Unlocking-your-collections-with-Alma-Digital-and-IIIF.pdf`. **29 pages**. La passe Y avait **25 pages réellement vues**, et les pages humaines 20, 23, 24 et 28 non inspectées.

Le lecteur de pages PDF a **affiché** les nouvelles pages suivantes :
- **20 (index PDF 19)** : paysage « Grimstunga » dans un visualiseur, dialogue d'intégration `iframe` et choix de dimensions 560×420, 640×480, 800×600 ou custom. Les tailles de l'interface ne sont pas des quotas IIIF.
- **23 (index 22)** : plateforme **Exhibit**, création et partage d'expositions numériques, références à St Andrews et à la British Library.
- **28 (index 27)** : capture **Mirador** avec autoportrait de Vincent van Gogh et peinture du Bodleian, exemple d'agrégation IIIF interinstitutionnelle.

**Page 24 (index PDF 23)** : le lecteur a échoué **deux fois**, sans affichage. Bilan fidèle : **28/29 pages inspectées visuellement**, **une manquante**. La présentation de 2022 ne devient pas « intégralement lue » ; parmi les pages consultées, aucun plafond de débit IIIF n'est démontré.

## Contrôles négatifs et statut des autres URL

Les URL IIIF exactes **Cultural Japan Collection**, **Northwestern Image** et **Northwestern API `?as=iiif`** ont renvoyé `fetch_error` avec indicateur 200 mais sans JSON ; **Villanova** 403 ; **NPM iiifod2** connect_error ; **DRI Swagger** simple titre d'interface ; **Bologna OAI Identify** 400 ; **KB DK OAI** connect_error ; **UBC OAI** timeout ; **Jena manifest** page de défi `mod_repudiator` ; **Digital Commonwealth OpenSearch** écran de défi Anubis, pas XML. Aucune de ces URL n'est requalifiée en document lu.

Sur une seconde passe de `robots.txt`, les réponses de **Harvard MPS, LCCN LoC et archives.parliament.uk** étaient des pages HTML hors sujet, et plus de vingt autres URL ont renvoyé des erreurs. **Seule Europeana Pro a fourni des directives robots originales exploitables**.

## Suite

Registre URL → constat, fiches et `data.json` à synchroniser ; Excel généré par le pipeline du dépôt, pas d'édition indépendante. La PR reste brouillon tant que les accès techniques et les procédures humaines utiles ne sont pas qualifiés.
