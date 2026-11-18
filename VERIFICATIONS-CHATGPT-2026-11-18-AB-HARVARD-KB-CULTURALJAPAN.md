# Passe AB, 18 novembre 2026 : trois pages originales et une architecture IIIF historique

**Cadre :** revue de documents publics et de copies indexées **datées**. Le contenu des pages a été effectivement récupéré, mais cela ne garantit pas leur accessibilité HTTP directe ni leur validité réglementaire actuelle. Aucun test de charge, de clé ou de contournement.

## 1. Harvard University, GLAM-033 : principes réels de la plateforme API

**URL originale** : https://enterprisearchitecture.harvard.edu/api-principles-and-practices-use-api-gateway-and-portal

Le lecteur a récupéré **13 940 caractères** de texte substantiel, copie indexée au **23/08/2026**. Le document **Harvard University Information Technology (HUIT)** décrit l'architecture et les règles de gouvernance d'une **API Platform** avec deux fonctions distinctes :

- **API portal** : publication de la documentation, visibilité et onboarding des développeurs.
- **API gateway** : authentification, centralisation des contrôles d'accès, journalisation, suivi et **application possible de rate limiting**.
- Plateforme nommée dans le texte : **Apigee API Management**.
- Tableau de catégories : API de fournisseur SaaS déjà administrées (**portail oui, gateway non**) ; API de fournisseurs administrées par Harvard (**portail oui, gateway oui**) ; API internes partagées (**portail oui, gateway oui**), sous réserve de cas particuliers.

**Limite d'interprétation :** ceci est une **politique d'architecture HUIT** applicable à certaines API Harvard, **pas un contrat de quota IIIF**, ni une preuve que chaque service d'images de Harvard passe par Apigee. Le document ne donne aucun seuil numérique de débit d'image IIIF.

## 2. Harvard Library Technology Services : page originale de support, mais historique

**URL originale** : https://harvardwiki.atlassian.net/wiki/spaces/LibraryStaffDoc/pages/43286896/LTS+Support

Page **LTS Support** récupérée en texte intégral de **4 926 caractères**, copie datée du **15/11/2026**. Le document lui-même indique une création/mise à jour au **11/12/2018**. Il répertorie des guides d'accès, des formulaires DRS, d'anciens tableaux de bord et des plannings d'hiver jusqu'en 2026-2027. Il **ne contient pas de contrat d'API Image/Presentation, de débit ni de quotas**. Le caractère lisible de cette page ne donne pas accès à d'autres espaces privés Atlassian.

## 3. Koninklijke Bibliotheek, Pays-Bas : portail LOD original lisible

**URL originale** : https://data.bibliotheken.nl/

Le lecteur a obtenu **2 729 caractères** de présentation substantive du portail **Linked Open Data** de la KB, copie datée du **16/11/2026**. Le site présente :
- plateforme **Triply** d'édition/exposition RDF ;
- ensembles de données **Nederlandse Bibliografie Totaal**, **STCN**, **Nederlandse Thesaurus van Auteursnamen**, **DBNL**, manuscrits médiévaux et thésaurus ;
- indication que les **données de ce portail** sont publiées en **CC0** ; page affichant **259 366 042 triples** au moment de la copie ;
- liens publics `https://docs.triply.cc/triply-api` et contact Linked Data KB.

**Ne pas amalgamer** : ce portail RDF et les permissions CC0 qu'il annonce ne sont ni les manifestes IIIF `iiif.kb.nl`, ni des quotas `req/min` de l'API Image ou du service OAI/MDO. L'URL `https://iiif.kb.nl/` ne livrait pas de contenu exploitable ; `services.kb.nl/mdo/browse?set=anp` demeurait en erreur de connexion.

## 4. Cultural Japan : source technique primaire, pas une lecture du JSON inaccessible

Source : https://nakamura196.hatenablog.com/entry/2021/07/23/003143

Article technique daté du **23/07/2021**, publié par Satoru Nakamura, **5 712 caractères** lus dans une copie indexée au **15/06/2026**. L'auteur pointe expressément sur la collection problématique `https://app.cultural.jp/iiif-collection/collection.json`.

**Architecture décrite à cette date** : la collection agrège des manifestes IIIF de plusieurs bases ; pour certains objets disposant d'une image haute définition `jps:accessInfo/schema:associatedMedia`, Cultural Japan produit **dynamiquement** des manifestes JSON grâce à **AWS Lambda**, en interrogeant à chaque demande les graphes RDF de **Japan Search et Cultural Japan**. Ces manifestations dynamiques peuvent ne contenir qu'une partie des images de l'objet original, celles reliées par `associatedMedia`.

**Conséquence** : il ne faut pas présenter une éventuelle lenteur ou erreur sur `app.cultural.jp` comme un quota de requêtes. La source apporte une **description d'architecture de 2021, pas de garantie sur le déploiement de 2026**. Le contenu du `collection.json` original demeure **non récupéré** dans cette passe ; la collection `nakamura196.github.io/iiif/data/collection/collection.json` lue précédemment reste un **jeu distinct**, non un remplacement.

## 5. URL originales réessayées mais non promues

À titre de contrôle : `https://purl.pt/32689/1/` timeout, `https://iiif.bl.uk/` 403, `https://services.kb.nl/mdo/browse?set=anp` connect_error, `https://collection.britishart.yale.edu/id/page/object/1772` connect_error, `https://repository.ubn.ru.nl/rest/` timeout, `https://texashistory.unt.edu/feed/` 404, deux pages Digital Washington 403. Plusieurs anciennes URL Göttingen ou British Library renvoyaient des pages **génériques non équivalentes**. Le portail `digital.nls.uk/` renvoyait une simple redirection 301. Elles restent donc classées non lues, et non « closes » pour gonfler les statistiques.

**Réconciliation prévue** : les trois premières URL sont des lectures originales à inscrire dans le registre ; l'article Cultural Japan est une **source complémentaire historique** hors des 260 URL et ne doit pas compter dans le ratio de lecture originale. Reporter les distinctions dans les fiches et le classeur, conserver les anciens refus HTTP et les captures datées.
