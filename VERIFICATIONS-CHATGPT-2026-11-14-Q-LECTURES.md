# Rattrapage Q — 30 URL manuelles supplémentaires, sources et refus (14 novembre 2026)

**Portée :** URL **exactes** du champ `a_verifier_manuellement` (Princeton, National Gallery of Art, Harvard, Yale, Washington, Toronto, UNT, St Andrews, KU Leuven, Jena, Radboud, SLUB). Lectures par extracteur public avec date `acquired_at` : souvent **copie indexée** antérieure à la présente passe, **pas preuve de réponse HTTP live**. On ne mesure ni quotas ni en-têtes de contrôle de débit, et on ne contourne pas les protections.

| Institution | URL d'origine | Résultat de lecture | Date source |
|---|---|---|---|
| NGA Washington | https://www.nga.gov/open-access-images/open-data-program.html | **403**, aucun texte de page | 2026-11-14 tentative |
| NGA | https://www.nga.gov/about-us/terms-use.html | **403**, conditions non lues | tentative |
| NGA | https://www.nga.gov/open-access-images/faqs.html | **403**, FAQ non lue | tentative |
| NGA | https://www.nga.gov/api/v1/iiif/presentation/manifest.json?cultObj:id=26 | **403**, manifeste non récupéré | tentative |
| Princeton Art Museum | https://artmuseum.princeton.edu/terms-and-conditions | **Contenu de page lu**. Conditions du site, non quota de l'API métadonnées ou IIIF. | 2026-11-10 |
| Princeton | https://artmuseum.princeton.edu/robots.txt | **Fichier robots complet récupéré**, directives d'indexation/ressources. Ne prouve pas un débit illimité. | 2026-11-13 |
| Princeton | https://artmuseum.princeton.edu/story/exploration-and-innovation-new-digital-tools-increase-engagement | **Article intégral récupéré**, évoque l'API introduite en 2017 pour les collections ; contexte historique plutôt que SLA 2026. | 2026-11-10 |
| Princeton | https://media.artmuseum.princeton.edu/robots.txt | **500** sans contenu utile : robots spécifique au sous-domaine média inconnu. | tentative |
| Harvard Art Museums | https://harvardartmuseums.org/article/1035 | **Article « The HAM API at 10 » retrouvé** malgré blocage antérieur, copie de 2025. L'API fête dix ans en 2023, mais ce document historique ne donne pas les quotas actuels. | 2025-11-30 |
| Yale YCBA | https://collections.britishart.yale.edu/ | **Texte du portail de recherche d'œuvres récupéré**, filtres, services collections, pas contrat IIIF. | 2026-11-06 |
| Yale LUX | https://lux.collections.yale.edu/content/technology | **Page Technology récupérée**, confirme IIIF comme standard de rendu et d'interopérabilité ; lecture historique, ne prouve pas configuration actuelle des backend privés. | 2026-02-06 |
| Yale YCBA | http://collection.britishart.yale.edu/id/page/object/1772 | **Erreur DNS**, pas de page ni de manifeste. | tentative |
| University of Washington | https://digitalcollections.lib.washington.edu/ordering.html | **403**, commande/reproduction non lue. | tentative |
| Washington | https://digitalcollections.lib.washington.edu/search-tips.html | **403**, conseils de recherche non lus. | tentative |
| Washington | https://digitalcollections.lib.washington.edu/digital/custom/terms | **Page 404 (« Page not found ») réellement récupérée** avec lien de politique générale de UW, mais pas conditions CONTENTdm actuelles. | 2026-11-14 |
| Washington | https://digitalcollections.lib.washington.edu/digital/about | **Texte du programme Digital Initiatives récupéré**, normes de métadonnées, pas limites d'accès API. | 2026-10-29 |
| Toronto | https://collections.library.utoronto.ca/explore/help | **Page Help récupérée**, cite explicitement IIIF pour les objets patrimoniaux ; pas de quota chiffré. | 2026-11-07 |
| UNT | https://texashistory.unt.edu/about/portal/policies/ | **Politique du portail récupérée**, droits/attribution et réutilisation des médias, pas plafond HTTP. | 2026-11-13 |
| UNT | https://texashistory.unt.edu/feed/ | **404**. Une racine feed manquante ne signifie pas que toutes les collections ont perdu leur flux. | tentative |
| St Andrews | https://www.st-andrews.ac.uk/collections/about | **Page officielle récupérée**, confirme l'utilisation d'IIIF et le lien de manifeste sur les notices. **Copie ancienne (février 2025)**. | 2025-02-11 |
| St Andrews | https://www.st-andrews.ac.uk/library/special-collections/help-and-support/find-and-research-materials | **Guide récupéré**, liens vers les outils d'annotations et PDF de ressources IIIF. | 2025-02-11 |
| St Andrews | https://www.st-andrews.ac.uk/terms/ | **Conditions générales récupérées**, pas quota IIIF chiffré dans ce document. | 2026-11-02 |
| KU Leuven | https://bib.kuleuven.be/english/libis/libis | **Présentation officielle de LIBIS récupérée**, Heron/Lias/Teneo, pas limite technique. | 2025-11-11 |
| KU Leuven | https://libis.be/teneo | **404**, ancienne route. Source alternative de Teneo à valider. | tentative |
| KU Leuven | http://services.libis.be/m2/manifest/IE11541569 | **404**, ancien endpoint, ne prouve pas panne de tous les manifestes. | tentative |
| KU Leuven | https://resolver.libis.be/IE978853/representation | **Texte « Le Couvent des Dominicains » récupéré** ; contenu de représentation mais **pas JSON IIIF**, ni débit. | 2026-11-14 |
| Thüringer Jena | https://zs.thulb.uni-jena.de/api/iiif/presentation/v2/jportal_derivate_00401748/manifest | **Page de protection mod_repudiator** (« {{ translate(pow.title) }} »), **pas un manifeste JSON**. Ce refus n'est pas un quota. | 2026-11-14 |
| Radboud | https://repository.ubn.ru.nl/rest/ | **404**, racine REST historique, endpoint non confirmé. | tentative |
| SLUB | https://kartenforum.slub-dresden.de/ | **Page d'accueil du Kartenforum récupérée**, cartographie géoréférencée, pas IIIF rate limit. | 2026-10-09 |
| SLUB | https://iiif.slub-dresden.de/ | **fetch_error avec code 200 sans corps exploitable** ; ne pas conclure accessible ou en panne de l'API IIIF depuis cette racine. | tentative |

## Règles de tri

1. Une **page de présentation, de contact, de conditions ou un robots.txt lu** satisfait une demande de *lecture du contenu* mais pas une vérification de débit du service IIIF. Les droits et la présence d'une API ne déterminent pas les seuils de requêtes.
2. **403, 500, 404, DNS, page de défi** restent distincts : la nouvelle doc institutionnelle éventuelle ne transforme pas ces réponses en 200.
3. Jena ne fournit **pas** le JSON de manifeste attendu; le front `mod_repudiator` confirme qu'il faut une source d'accès ou une procédure officielle plutôt que de répéter les requêtes.
4. Les pages indexées en 2025 peuvent éclairer l'histoire technique mais nécessitent une vérification de version pour les conditions courantes. Ne jamais déduire « aucun quota » du silence d'une page de droits.
5. Le rapport complète les recherches documentaires antérieures, sans cocher de nouvelles étapes a–g ni actualiser `BENCHMARK.xlsx` avant contrôle du pipeline.

**Synthèse :** 30 URL exactes tentées ; certaines récupérées, d'autres refusées. Les dates des copies et le statut de contenu sont préservés avant tout éventuel retrait de l'onglet manuel.
