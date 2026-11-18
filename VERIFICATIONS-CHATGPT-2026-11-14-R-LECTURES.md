# Rattrapage R — 20 URL historiques et deux lectures approfondies (14/11/2026)

**Principe de preuve :** ouverture des URL originales par un lecteur de pages et un extracteur, sans contourner les défis. Les dates `acquired_at` sont reportées lorsqu'il s'agit d'une copie indexée et ne certifient pas un accès HTTP live, des en-têtes ni une limite de débit. Le PDF Duke a en plus été **ouvert dans le lecteur PDF avec contrôle visuel des pages 1 et 5**.

## Résultats URL par URL

| Institution | URL originale | Contenu ou erreur | Date de la copie |
|---|---|---|---|
| Internet Archive | https://iiif.archivelab.org/iiif/mma_irises_436528/info.json | Erreur réseau, ancien serveur non validé | aucune |
| Internet Archive | https://archive.org/services/tasks.php?rate_limits=1&cmd=modify_xml.php | **401**, service exigeant authentification ; aucun quota IIIF à déduire de cette API Tasks | aucune |
| Internet Archive | https://techdirt.com/2026/02/17/preserving-the-web-is-not-the-problem-losing-it-is | **Contenu d'article tiers récupéré**, débat sur archivage et robots.txt ; ne prouve pas la politique IIIF actuelle | 2026-11-10 |
| British Library / EAP | https://iiif.bl.uk/ | **403**, service original toujours inaccessible | aucune |
| British Library | https://www.bl.uk/help/how-to-reuse-images-of-unpublished-manuscripts | **Page générique Research**, pas l'ancien document spécifique sur les droits des manuscrits | 2026-11-11 |
| National Library of Scotland | https://maps.nls.uk/help/ | **FAQ cartographique récupérée**, navigation et usage du visualiseur, pas plafond IIIF | 2026-11-01 |
| NLS | https://digital.nls.uk/robots.txt | Erreur réseau, règles non lues | aucune |
| NLS | https://digital.nls.uk/ | **Page 301 CloudFront** seulement, destination finale non confirmée | 2026-11-03 |
| NLS | https://maps.nls.uk/view/help/ | **Guide cartographique complet récupéré** : la fonction `Show IIIF` fournit base URI et `info.json`. Exemple officiel : `https://map-view.nls.uk/iiif/2/21644%2F216443310/info.json`. | 2026-11-06 |
| NLS | https://maps.nls.uk/robots.txt | Erreur réseau, règles non lues | aucune |
| NLS | https://data.nls.uk/about/ai-statement/ | **Texte de la page AI Statement récupéré** ; document de politique joint non lu | 2026-10-11 |
| Wellcome | https://stacks.wellcomecollection.org/crawlers-floods-and-fleets-a-year-of-keeping-our-digital-collections-open-10af777199c4 | **Article technique intégral récupéré** (22 435 caractères), politique des bots et des budgets IIIF, résumé ci-dessous | 2026-10-16 |
| Wellcome | https://stacks.wellcomecollection.org/ten-years-and-counting-wellcome-collection-and-iiif-9015cdcdefd8 | **Article intégral récupéré**, architecture DLCS / iiif-builder, Presentation v3 et conversion v2, chiffres de collections, résumé ci-dessous | 2026-11-13 |
| Wellcome | https://data.wellcomecollection.org/robots.txt | **403**, texte robots non récupéré | aucune |
| Vatican | https://spotlight.vatlib.it/ | **Page Thematic Pathways récupérée**, IIIF annotation de manuscrits, pas politique de débit | 2026-10-01 |
| Vatican | https://www.digitavaticana.org/?lang=en | Erreur connexion, site non lu | aucune |
| Vatican | https://www.vatlib.it/en/the-library/photographic-laboratory.html | **Page laboratoire photographique récupérée**, procédures d'acquisition et standards, pas un contrat de quota API | 2026-11-14 |
| Biblioteca Nacional de Portugal | https://purl.pt/32689/1/ | Délai dépassé, aucune preuve d'accès | aucune |
| Bologna AMS Historica | https://historica.unibo.it/oai | **400**, l'endpoint OAI brut n'est pas une réponse valide `Identify` dans ce contrôle ; éviter de confondre défaut de requête et panne générale | aucune |
| Finna | https://api.finna.fi/v1?swagger | **403**, Swagger non récupéré | aucune |

## Vérification supplémentaire à partir du guide NLS

L'exemple d'URL IIIF Image 2 publié par le visualiseur écossais, `https://map-view.nls.uk/iiif/2/21644%2F216443310/info.json`, **a bien fourni du JSON** via l'extracteur le **14/11/2026** : `@context` Image API 2, dimensions **10 000 × 8 090**, tuiles **512 × 512** avec facteurs 1, 2, 4, 8, 16, 32, 64, profil `level2`. C'est une preuve de **contenu IIIF** récupéré, pas d'en-têtes de quota.

## Wellcome : politique concrète de protection des API (source institutionnelle 2026)

L'article de **Robert Kenny**, [*Crawlers, floods and fleets*](https://stacks.wellcomecollection.org/crawlers-floods-and-fleets-a-year-of-keeping-our-digital-collections-open-10af777199c4), analyse les incidents de juin à septembre 2026. Il **distingue expressément les pages de recherche destinées aux humains et l'API IIIF destinée aux programmes** :

- Les pages de recherche ont reçu une protection JavaScript et des règles CDN/WAF contre les flux de bots ; ces mesures ne sont pas appliquées de façon identique aux manifestes et images IIIF, sous peine de briser les visualiseurs tiers.
- Wellcome cite des téléchargements massifs répartis sur de nombreuses IP (dans un cas, **6 To de PDF en deux semaines**) et explique avoir mis en place des **budgets de requêtes par moissonneur ou réseau**, indépendamment du nombre d'adresses IP utilisées, en coordination avec son fournisseur IIIF.
- Les clients déclarant clairement leur projet/identité et conservant un débit acceptable ne sont pas traités comme les flottes anonymes réparties sur des milliers d'IP. La bibliothèque oriente le moissonnage du catalogue complet vers des **snapshots quotidiens**.
- **Aucune valeur universelle en requêtes/minute n'est annoncée dans l'article.** Cela documente **une politique d'application des limites** et une relation aux utilisateurs, pas un plafond numérique applicable à toute l'API IIIF.

L'article de **Jonathan Cates**, [*Ten years and counting: Wellcome Collection and IIIF*](https://stacks.wellcomecollection.org/ten-years-and-counting-wellcome-collection-and-iiif-9015cdcdefd8), décrit le serveur d'images DLCS (Digirati), puis `iiif-builder` créé en 2020 qui produit des manifestes Presentation v3 depuis 2021 et sert aussi la v2. Il donne **361 783 œuvres dotées de manifestes**, et environ **56 millions d'images de pages**, mais ce sont des volumes de collection, pas des quotas techniques. La lecture éclaire les familles Image/Presentation et leur architecture.

## Duke : PDF Anubis, contenu intégral (rappel du complément Q)

Le PDF officiel `https://dukespace.lib.duke.edu/server/api/core/bitstreams/816ef134-55cf-49f6-9a8b-1e8a2324b1ff/content`, auparavant non lu intégralement, est **maintenant documenté page par page** au complément du rapport Q, dont contrôle visuel de deux pages. Il décrit le filtrage 2025 de trois applications Duke, mais **pas** de quota fixe IIIF.

**À ne pas conclure :** bots bloqués ≠ API sans authentification ; volume de trafic ≠ plafond ; erreur 400 sans paramètre ≠ absence d'OAI ; source indexée ≠ réponse HTTP live. Aucune donnée canonique ni workbook n'est modifié par cette passe.
