# Passe X, 15 novembre 2026 : quatre nouvelles URL manuelles lues, trois politiques originales, une migration IIIF officielle

## Périmètre et méthode

Cette passe est centrée sur les URL **exactes** de la file `a_verifier_manuellement` et les documentations officielles qu'elles appellent. La récupération a été faite via un lecteur public de pages, qui fournit une date `acquired_at` pouvant désigner une **copie indexée**, et non une réponse HTTP **live** du client de la sonde. Aucun test de débit, aucune authentification, aucun contournement de défi ou de `robots.txt`.

## 1. Quatre URL originales dont le texte était encore non démontré

| Institution | URL **exacte** de la liste | Contenu réellement extrait | Date de la copie | Conséquence |
|---|---|---|---|---|
| National Library of Finland / Finna, GLAM-014 | https://www.kiwi.fi/spaces/Finna/pages/440828359/Finna+API+Documentation+In+English | **Page complète de 3 848 caractères** intitulée *Finna API Documentation In English* ; dernière mise à jour affichée **24/08/2026**, liens vers API REST, conditions, API d'authentification, OAI-PMH et OIDC | 05/11/2026 | C'est bien une **page d'index de documentation** lisible, pas la spécification REST elle-même |
| Finna, GLAM-014 | https://www.kiwi.fi/pages/viewpage.action?pageId=75202667 | **Page anglophone Finna API complète de 38 323 caractères**, exemples `/v1/search`, `/v1/record` et filtres | 15/11/2026 | Le texte est lu, mais il comporte un historique documentaire : **ne pas traiter ses anciens exemples comme un Swagger actuel** |
| National Gallery of Art, Washington, GLAM-049 | https://www.nga.gov/contact-us.html | **Page Contact Us intégrale, 10 929 caractères** avec contacts et navigation institutionnelle ; annonce le programme d'images Open Access | 09/11/2026 | Page de contact lue, mais **aucune règle de débit IIIF** n'en découle ; les autres pages NGA restent 403 |
| Parliamentary Archives / UK National Archives, GLAM-069 | https://www.nationalarchives.gov.uk/archives-sector/case-studies-and-research-reports/case-studies/digital/digital-preservation/the-parliamentary-archives | **Étude de cas intégrale, 13 266 caractères**, sur la préservation numérique et les deux fournisseurs de stockage cloud du Parlement | 27/08/2026 | **Cas d'architecture de conservation**, non documentation de quota IIIF ni de Developer API |

Les quatre entrées sont les seules de cette section à promouvoir la **lecture du contenu de l'URL d'origine**, par extraction de copies indexées. Le domaine de la sonde et les en-têtes HTTP ne sont pas validés par cette lecture.

## 2. Internet Archive : remplacer une URL historique, et récupérer un vrai JSON

- **URL originale toujours non extraite** : `https://iiif.archivelab.org/iiif/mma_irises_436528/info.json`.
- **Migration officielle documentée** : le code institutionnel `https://github.com/internetarchive/iiif` et l'annonce IIIF/Internet Archive du **18 septembre 2023** `https://iiif.io/news/2023/09/18/making-iiif-official-at-the-internet-archive/` confirment que **`iiif.archive.org` remplace l'ancien `iiif.archivelab.org` expérimental**, avec Image / Presentation v3, et prise en charge de compatibilité v2.
- **Exact même identifiant historique sur le nouvel hôte** : `https://iiif.archive.org/iiif/mma_irises_436528/info.json` a fourni un **JSON Image API 2 valide, intégral de 902 caractères**, acquis le **15/11/2026**, avec `@id` sur `iiif.archive.org/image/iiif/2/.../436528.jpg`, **3 811 × 3 058 pixels**, **tuiles 512**, profil `level2.json`.
- Le guide officiel IIIF, actualisé le **23/09/2026**, `https://iiif.io/guides/guides/archive.org/` donne le format de manifestes : `https://iiif.archive.org/iiif/{identifier}/manifest.json`.
- **Important** : ceci **résout la migration et procure un équivalent exploitable** ; cela ne prouve pas que l'ancien domaine répond, ni que les contraintes de débit de Wayback, Tasks API ou Open Library s'appliquent au service IIIF.

## 3. Brown University : protection Cloudflare explicitement documentée par l'institution

Le **wiki officiel** `https://github.com/Brown-University-Library/bdr_api_documentation/wiki`, lu en entier dans une copie indexée du **15/09/2026**, comporte une section « Important notice about Cloudflare Bot Protection ». Brown y écrit qu'au **printemps 2025**, des protections Cloudflare ont été déployées et peuvent affecter l'API, surtout les requêtes nombreuses à un rythme élevé. La consigne est de **créer un ticket** si le contrôle interfère avec un usage légitime ; Brown précise que l'accès à son réseau via VPN institutionnel peut aider **les membres autorisés de Brown**, non tous les chercheurs étrangers.

La page originale `https://repository.library.brown.edu/studio/api-docs/` a restitué une **page de vérification humaine**, pas un contrat OpenAPI. Le wiki officiel est donc une **source institutionnelle alternative complète** mais **non équivalente à l'URL swagger protégée**. Les exemples IIIF du rapport T (Image 2 `info.json` et manifeste Presentation 2) restent des preuves de contenu, pas des preuves de limites HTTP.

## 4. Finna : politique de réutilisation et accès, et non quota extrapolé

- **Conditions officielles complètes** : `https://www.kiwi.fi/display/Finna/Finna+API+Terms+of+Use` : texte de **6 895 caractères**, copie indexée au **05/11/2026**, dernière mise à jour affichée **25/10/2024**.
- Le **REST Metadata API est ouvert sans inscription** au moment de la rédaction du texte. La National Library of Finland **se réserve le droit d'introduire une inscription** en cas de charge excessive des serveurs. Aucune quantité de requêtes/minute n'y est annoncée.
- Les **métadonnées distribuées par l'API sont sous CC0**, mais **les images et ressources liées n'héritent pas de cette licence** : consulter `imageRights` et `accessRestrictions` et les conditions de chaque fournisseur.
- La documentation technique actuelle pointe vers le **JSON OpenAPI 3.0.3** `https://api.finna.fi/api/v1/?openapi` (version logicielle **11.0.3**, six chemins, déjà récupérée en T). La route historique `https://api.finna.fi/v1?swagger` renvoie toujours **403** au lecteur ; elle ne doit **pas** être marquée comme lue.
- Les documents `https://www.kiwi.fi/spaces/Finna/pages/440828359/Finna+API+Documentation+In+English` et `https://www.kiwi.fi/pages/viewpage.action?pageId=75202667` sont eux-mêmes les deux **URL originales** de la file retrouvées dans cette passe.
- Le `robots.txt` du domaine API (`Disallow: /` dans une copie du 14/11) doit être conservé comme politique distincte. Ne pas utiliser une lecture du corps du Swagger pour conclure automatiquement à une permission de moissonner les images.

## 5. Échecs confirmés sans tentative de contournement

Sur les URL originales encore non lues : `app.cultural.jp/iiif-collection/collection.json` n'a rendu aucun JSON malgré un signal 200 ; `iiif.dc.library.northwestern.edu/.../info.json` également ; le manifeste Villanova reste **403** ; l'OAI-pmh Bologna `?verb=Identify` reste **400** pour cet extracteur ; le service `repository.dri.ie/api-docs` ne donne qu'une enveloppe Swagger UI ; le `info.json` du National Palace Museum demeure **timeout**. Le défi Anubis Digital Commonwealth persiste sur `search/opensearch.xml`.

Cette passe n'a pas modifié les données canoniques ni Excel à elle seule. Les changements seront réunis avec les sources et vérifiés par le pipeline de construction du classeur.
