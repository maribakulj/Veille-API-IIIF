# Rattrapage O — lecture effective des URL initialement classées manuelles
Date : 14 novembre 2026. Branche : `chatgpt/rattrapage-documentation-2026-11-14`.

## Périmètre et méthode
Cette passe **ouvre les URL originales**, d'abord avec l'outil de lecture web, puis avec un second extracteur public lorsque le premier ne rend rien. Une **lecture de la page d'origine**, une **extraction indexée de son contenu**, une **page de défi**, un **redirect** et un **JSON réellement extrait** sont des résultats différents. La date `acquired_at` est conservée pour le second extracteur ; elle peut être antérieure au jour de ce rapport. Aucun résultat n'est assimilé à une réponse HTTP de la sonde locale, à des en-têtes de quota, ni à une autorisation de moissonnage.

## Pages d'origine dont le contenu était récupérable directement par lecture web (14/11)
| Institution | URL initiale | Résultat documentaire |
|---|---|---|
| e-rara | https://www.e-rara.ch/wiki/apiinfo | **Texte actuel lu**, OAI-PMH, IIIF, ALTO, RIS, PDFs et dumps mensuels NER/NEL disponibles sur demande à contact@e-rara.ch ; les lots OAI de 10 notices ne sont pas un quota de requêtes/minute. |
| e-rara | https://www.e-rara.ch/wiki/termsOfUse | **Texte actuel lu**, Public Domain Mark ou CC BY-SA selon le document ; pas de rate limit déductible. |
| e-manuscripta | https://www.e-manuscripta.ch/wiki/apiinfo | **Texte actuel lu**, OAI-PMH, IIIF, exports PDF/RIS. Les lots OAI de 10 notices ne sont pas une limite de débit. |
| e-manuscripta | https://www.e-manuscripta.ch/wiki/termsOfUse | **Texte actuel lu** : la copie *systématique de fichiers sur d'autres serveurs* exige un accord écrit préalable de l'administration du portail ou des institutions détentrices ; point contractuel important indépendamment des quotas. |
| Cardiff | https://www.cardiff.ac.uk/help/termsofuse | **Texte actuel lu**, restrictions générales de reproduction du site ; pas un plafond IIIF. |
| Huntington | https://www.huntington.org/terms-and-conditions-use-photographs | **Texte actuel lu**, conditions pour des photographies fournies par l'institution, pas pour tous les manifestes IIIF. |
| Kyoto RMDA | https://rmda.kulib.kyoto-u.ac.jp/en/reuse | **Texte actuel lu**, réutilisation et JPEG de 2 000 pixels par côté pour certains fonds ; dimension d'image, pas débit. |
| National Library of Wales | https://www.library.wales/copyright | **Page actuelle lue**, politique de droits, pas politique de quotas IIIF. |
| Europeana | https://pro.europeana.eu/page/apis | **Redirection lue vers** https://api.europeana.eu/en, page générale des API ; l'ancienne URL n'est plus un blocage documentaire mais ne donne aucun plafond chiffré. |
| State Library Victoria | https://rosetta.slv.vic.gov.au/iiif/2 | **Texte de la page Cantaloupe lu** (indexée trois mois auparavant), Image API 2.x, exemples `/info.json` et JPEG, liens vers v1/v3 ; aucune preuve sur le débit. |
| NYPL | https://api.repo.nypl.org/ | **Texte original lu**, avertissement d'arrêt de l'ancienne Repo API au 1er août 2026 et absence de remplacement **public** annoncé ; quota 10 000/jour/jeton de la seule ancienne API. Ne pas confondre avec Collections API ni IIIF. |

## Pages effectivement retrouvées par un second extracteur de contenu
Ces résultats désignent du **texte extrait ou indexé**, pas nécessairement une lecture HTTP live. Dates `acquired_at` rapportées par l'extracteur :

| Institution | URL originale | Texte et portée | Date d'acquisition indiquée |
|---|---|---|---|
| NPM Taïwan | https://digitalarchive.npm.gov.tw/opendata/Json/NPMIIIF.pdf | **PDF textuel entier récupéré, 13 pages** ; guide d'utilisation du visualiseur, sans débit chiffré apparent dans le texte extrait. Donne **8 URL explicites** de manifestes : `/Antique/setJsonU?uid=43351&Dept=U`, et les UID 19613, 19906, 23165, 19908, 19611, 19907, 19911. Cette source fournit désormais des identifiants légitimes pour les contrôles ultérieurs. **Rendu visuel non effectué** (le lecteur PDF initial a expiré). | 2026-11-14 |
| Cambridge CUDL | https://cudl.lib.cam.ac.uk/terms/ | **Texte complet retrouvé**. Interdiction, sauf autorisation/licence explicite, d'extraire systématiquement ou de réutiliser des portions substantielles. Aucun plafond numérique des requêtes dans la section inspectée. La lecture web directe reste 403 ; copie indexée datée. | 2026-09-18 |
| Library of Congress | https://www.loc.gov/pictures/api | **Documentation PPOC JSON API complète récupérée**, malgré le 403 du lecteur web direct ; c'est **l'API Prints & Photographs**, distincte du IIIF Image Services à 150/min documenté ailleurs. | 2026-08-29 |
| State Library Victoria | https://rosetta.slv.vic.gov.au/delivery/iiif/presentation/2.1/IE145082/manifest | **JSON de manifeste IIIF Presentation 2 récupéré**, label `[Berkshire pig with points marked on image]`, canevas et images. La récupération par l'outil de lecture web direct échoue ; ne pas la convertir en constat d'en-têtes ou de débit. | 2026-11-05 |
| Waseda | https://www.wul.waseda.ac.jp/kotenseki/ga_IIIF/guide_UV_en.html | **Guide Universal Viewer récupéré**, malgré 503 de lecture directe ; contient un lien d'exemple vers `iiif.archive.waseda.jp/iiif/manifest/ktnsk/ro12_01134/manifest.json`. | 2026-07-22 |
| Finna | https://www.kiwi.fi/display/Finna/Finna+API+Terms+of+Use | **Conditions officielles récupérées** et URL actuelle retrouvée (`/spaces/Finna/pages/53839699/Finna+API+Terms+of+Use`). API publique sans inscription, réserves en cas de surcharge. Le 403 du premier lecteur ne bloque pas la lecture documentaire. | 2026-11-05 |
| BNE | https://www.bne.es/sites/default/files/repositorio-archivos/procedimiento_normas_reproduccion.pdf | **Contenu PDF extrait**, procédures de reproduction et de réutilisation, **pas un texte de limites d'API IIIF**. Le lecteur web direct a reçu 403 : aucune inspection visuelle PDF dans cette passe. | 2026-10-19 |
| National Library of Wales | https://www.library.wales/fileadmin/docs_gwefan/new_structure/about_nlw/about_us/governance/corporate_documents/Access_to_Collections_Items_Policy.pdf | **Document PDF de 9 pages lu par le lecteur web**, capture visuelle des pages 1 et 6 contrôlée ; restrictions de conservation, d'accès physique et d'accès à certaines collections numériques ; **aucun quota IIIF chiffré établi**. | Lecture web 2026-11-14 |
| NYPL | https://www.nypl.org/help/about-nypl/legal-notices/terms-conditions | **Conditions retrouvées**, la copie indexée renvoie au chemin actuel `/help/legal-notices/terms-conditions` ; à distinguer des conditions IIIF. | 2026-11-14 |
| NYPL | https://www.nypl.org/robots.txt | **Texte robots récupéré** ; `User-agent: *` avec `Crawl-delay: 10`, restrictions ciblées `GPTBot` et autres ; pas une preuve de quota IIIF. | 2026-11-14 |
| Art Institute of Chicago | https://www.artic.edu/open-access/public-api | **Contenu page API publique récupéré**, ancienne lecture 403 par premier outil ; incite à utiliser le lien de manifeste sur les fiches. Les chiffres de son **API métadonnées** restent distincts du serveur d'images IIIF. | 2026-11-04 |
| Art Institute of Chicago | https://www.artic.edu/terms | **Conditions générales de site récupérées** ; pas de transposition automatique aux requêtes sur les manifests. | 2026-11-07 |
| Cornell | https://digital.library.cornell.edu/about | **Page actuelle récupérée**, plateforme Blacklight, Solr et IIIF confirmée. | 2026-11-14 |
| Cornell | https://digital.library.cornell.edu/catalog/ss:549539 | **Notice de collection récupérée**, non-manifeste IIIF, malgré l'échec du premier lecteur. | 2026-08-11 |
| National Library of Scotland | https://maps.nls.uk/projects/api/ | **Contenu de la page API cartographique récupéré** ; les limites MapTiler et les tuiles ne doivent pas être attribuées aux API IIIF des fonds NLS. | 2026-11-11 |
| UCD | https://digital.ucd.ie/ | Résultat indexé avec titre de l'accueil, mais **aucun texte utile extrait** : ne pas classer « document lu ». | 2026-10-01 |

## URL toujours non résolues malgré deux modalités
| URL | Résultat observé cette passe | À faire |
|---|---|---|
| https://repository.dri.ie/api-docs | Lecteur direct inaccessible ; extracteur ne restitue que « Swagger UI » d'une copie du 2025-09-19. | OpenAPI JSON sous-jacent et politique de quota toujours non lus |
| https://iiif.library.leeds.ac.uk/presentation/cc/q8qkdfmm | Échec d'extraction (un outil rapporte un `fetch_error` avec `http_status_code=200`, sans contenu). | JSON manifeste et en-têtes à vérifier |
| https://app.cultural.jp/iiif-collection/collection.json | Échec d'extraction, malgré un signal `http_status_code=200` sans contenu. | **Ne pas annoncer JSON lu** |
| https://open.library.ubc.ca/docs | Contenu d'une **page de blocage WAF** récupéré, et non documentation API. | Version live et quotas IIIF encore inconnus |
| https://repository.library.brown.edu/studio/api-docs/ | Texte de **vérification humaine**, pas Swagger. | Nouvelles sources code ou contact, sans contourner |
| https://cudl.link/v1/metadata/ | Connexion échouée avec le second extracteur. | Endpoint technique non validé |
| https://eap.bl.uk/about-eap et https://eap.bl.uk/terms | 404 sur les anciennes URL dans le second extracteur. | Les pages de remplacement figurent dans le rapport C |
| https://digitalarchive.npm.gov.tw/opendata/Json/NPMIIIF.pdf | **Récupération textuelle accomplie**, mais le lecteur PDF initial expire ; pas de confirmation live par la sonde. | Pas de besoin de relecture manuelle du texte du guide ; contrôle visuel seulement si nécessaire |

## Points d'intégration
- **Le rattrapage ne doit plus demander une lecture humaine pour le simple contenu** des documents e-rara/e-manuscripta, du PDF guide NPM, des conditions CUDL/Finna et de la documentation PPOC, sous réserve de la distinction copie indexée / page live. Ceci ne ferme pas les contrôles HTTP techniques, les clés, les en-têtes ni les autorisations de moissonnage.
- Il reste essentiel de **ne pas attribuer** les limitations des API REST, des tuiles MapTiler, des licences d'images ou des tailles d'export au service IIIF.
- Aucun test de charge, contournement de WAF, usage de compte ou automatisation intensive n'a été fait.
