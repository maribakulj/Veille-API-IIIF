# Passe T (15 novembre 2026) — reprise des 88 URL sans constat relié

## Périmètre, méthode, précautions

Source de la liste : l'artefact CSV de [GitHub Actions #43615142350](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43615142350), sur la branche `chatgpt/rattrapage-documentation-2026-11-14`. Il contient **260 lignes manuelles historiques**, dont **88 sans observation associée** à cette date. La présente passe cherche leur **contenu original**, et non seulement des sources parlant du même sujet.

Sources employées : extracteur public de pages avec `acquired_at` (souvent une **copie indexée** dont l'horodatage ne démontre pas une disponibilité HTTP live), lecteur de pages/PDF et, pour le code, dépôt officiel. Le lecteur PDF a **ouvert et affiché visuellement** les pages indiquées ci-dessous, sans lecture systématique de toutes les diapos image. Les réponses 403, 404, 500, timeout et défis restent distinctes. Aucun test de débit, contournement WAF, inscription, formulaire envoyé ou téléchargement en masse.

## Lectures apportant des preuves techniques directement exploitables

### 1. Deux JSON IIIF supplémentaires, grâce à Brown

- **Fiche API d'objet** `https://repository.library.brown.edu/api/items/bdr:80246/` : **JSON de 14 223 caractères obtenu**, source indexée au 15/11/2026. Cette fiche expose précisément le lien Image `https://repository.library.brown.edu/iiif/image/bdr:80246/info.json` et le lien Presentation `https://repository.library.brown.edu/iiif/presentation/bdr:80246/manifest.json`.
- Ces **deux documents liés ont également pu être extraits** : Image API **2** `info.json`, dimensions **6 335 × 8 560**, tuiles **512**, profil **level2** ; Presentation API **2**, `sc:Manifest`, titre *Abe Lincoln as a babe, as a boy and youth*. Tous acquis le 15/11. **Aucun quota HTTP identifié**.

### 2. e-rara Search API : un vrai résultat JSON

L'URL initialement classée manuelle `https://www.e-rara.ch/i3f/manifest/6341733/search?q=Bibel` fournit réellement un **JSON valide IIIF Content Search v1** (`@context` `http://iiif.io/api/search/1/context.json`, `sc:AnnotationList`, `total:0`, `resources:[]`, `hits:[]`), copie datée du 15/11. **Zéro résultat n'est ni une panne ni une limite de requêtes.**

### 3. BSB/MDZ : réponse OAI-PMH qui avait été refusée par la sonde

`http://bdr.oai.bsb-muenchen.de/OAIHandler?verb=Identify` : **contenu de la réponse OAI-PMH Identify récupéré**, donnant `Bavarian Digital Repository`, `protocolVersion=2.0`, `baseURL=http://bdr.oai.bsb-muenchen.de/OAIHandler`, courriel de contact et granularité. Extraction horodatée 15/11. **Le précédent 403 HTTP est conservé comme résultat de son client**, et ne se transforme pas en preuve d'une configuration actuelle universellement accessible.

### 4. Finna : spécification officielle complète, mais pas un quota IIIF

`https://api.finna.fi/api/v1/?openapi` : **JSON de spécification OpenAPI 3.0.3, version Finna 11.0.3**, **138 454 caractères** réellement analysés. Six chemins `/record`, `/search`, `/authority/record`, `/authority/search`, `/bazaar/browse`, `/list`. Aucun schéma `securitySchemes`, aucune sécurité OpenAPI globale, **pas de réponse 429 déclarée** et **pas de quota numérique identifié dans le document**. La portée de cette spécification est **REST Search, pas IIIF Image ou Presentation**. Copie indexée au 10/11.
`https://api.finna.fi/robots.txt` : texte effectivement obtenu au 14/11, `User-agent: *` et `Disallow: /`. Le `robots.txt` de `www.finna.fi` (14/11) distingue bots et chemins interdits, et comporte `Crawl-delay: 1` pour le groupe générique. Ces **directives robots ne sont pas des quotas d'API**. Le `robots.txt` de `www.kiwi.fi` du 15/11 affiche des **Content-Signal** via Cloudflare ; la politique propre au portail documentation n'est pas celle de `api.finna.fi`.

### 5. Library of Congress : JSON exact récupéré malgré le blocage précédent

`https://www.loc.gov/item/powmia/pwmaster_103790/?fo=json&at=item,resources` : **JSON d'objet et ressources** d'environ **4 688 caractères**, acquis le 15/11, comprenant `document_id=PWMASTER_103790`, `digitized=true`, ressource PDF au domaine `tile.loc.gov`. Il s'agit de l'**API de notices LoC**, pas d'un manifeste IIIF ni d'une limite `Image Services`.

### 6. State Library Victoria : info.json sur l'ancien port, contenu validé

`https://rosetta.slv.vic.gov.au:2083/iiif/2/IE145082:FL21000768.jpg/info.json` : **JSON Image API v2 complet, 929 caractères**, acquis le 15/11. `@id` sans le port `:2083`, dimensions **7 000 × 5 257**, tuiles **1 024**, profil **level2**, `maxArea: 36 799 000`. L'ancien constat de refus 403 de la sonde demeure historiquement exact pour ce client. Aucune conclusion sur des quotas.

### 7. Université de Genève, Bodmer Lab / Hedera

- `https://www.unige.ch/eresearch/en/services/hedera` : contenu de présentation Hedera retrouvé (copie 12/09), **manifestes IIIF générés à partir de jeux RDF**, Collections IIIF et visionneuse Mirador.
- `https://www.unige.ch/eresearch/en/services/hedera/what-iiif` : page d'explication IIIF récupérée (copie 17/09).
- `https://www.unige.ch/robots.txt` : fichier lu en copie du **04/11**, comprenant `Crawl-delay: 5` dans le groupe générique. Il ne faut pas appliquer cette valeur au serveur `iiif.unige.ch` sans contrôle du propre domaine.

### 8. Robots et accès : quelques règles révélatrices

- `https://www.cardiff.ac.uk/robots.txt` : contenu texte du 15/11, exclusions de routes site/recherche, pas de règle prouvée pour serveurs IIIF.
- `https://era-prod11.ethz.ch/robots.txt` : **long fichier de directives récupéré**, nombreuses exclusions sur le moteur de recherche et les fonctionnalités de la plateforme e-rara ; version extraite 15/11, **ne vaut pas permis de crawler**.
- `https://www.delpher.nl/robots.txt` : robots du 15/11 : `User-Agent: * Disallow: /` avec exceptions pour moteurs nommés, pertinent pour les conditions d'usage de Delpher, **pas pour toutes les APIs KB**.
- `https://www.library.wales/robots.txt` : copie 12/08 avec `Crawl-delay: 5` ; **datée**, pas vérification actuelle directe.
- `https://open.library.ubc.ca/robots.txt` : extraction indexée du 07/11 qui affiche `Crawl-delay: 12`; format des lignes parfois compacté par l'extracteur, à ne pas confondre avec les 10/200 requêtes/min de l'API Open Collections.
- `https://www.ucd.ie/robots.txt` : texte de règles du site universitaire principal extrait au 15/11 ; distinct des services de `digital.ucd.ie`.
- `https://objects.library.uu.nl/robots.txt` : fichier du 15/11 excluant notamment `/manifest`, `/iiif_manifest`, `/fcgi-bin/iipsrv.fcgi` ; **restriction robots importante** sur un hébergeur d'images.
- `https://digitalcollections.nypl.org/robots.txt` : copie du 15/11 avec restrictions ciblées de certains robots ; **spécifique à ce sous-domaine**.
- `https://www.huntington.org/robots.txt` : non inclus dans les 88 de départ de cette passe, déjà récupéré dans S ; éviter de le compter deux fois.

## Autres pages originales dont le contenu est retrouvé

- Cambridge Digital Library `/about` : texte de présentation de la bibliothèque et du réemploi permis par licence, **copie du 18/09**, sans quota.
- Digital Repository of Ireland `/about-us/` (copie 16/09), organisation GitHub (18/10), API GitHub listant ses dépôts (15/11), et **fichier `dri-app/config/routes.rb`** (15/11) confirmant `get 'iiif/:id/manifest'`, `get 'iiif/collection/:id'` et le montage de Rswag sur `/api-docs`. **`/api-docs/v1/swagger.json` n'a pas pu être récupéré (403)**.
- Durham `/departments/library/about-us/policies/` (copie 20/09) et `discover.durham.ac.uk` (14/10) : pages documentaires lisibles ; ne résolvent pas les quotas IIIF.
- ColBase (NICH) : l'accueil de l'application auparavant considéré comme SPA vide fournit du **texte réel** en japonais et des liens d'œuvres (copie 29/10), sans documentation de débit.
- Harvard Library Viewer : page d'accueil indexée au 06/07 et exemples MPS ; un défi AWS WAF dans la sonde reste possible.
- Getty `https://data.getty.edu/tools/id_manager/docs/` : **documentation d'un service de gestion d'identifiants** retrouvée (copie 16/10), distincte de l'Image API.
- Harvard Art Museums `https://github.com/harvardartmuseums/api-docs/issues/29` : ticket de problèmes 429 chez `ids.lib.harvard.edu` consultable, à distinguer d'une règle de quota publique. 
- British Library / KB / autres hôtes : ne pas déduire de quotas quand seules des pages d'accueil ou d'erreurs sont récupérées.
- UK Parliament `developer.parliament.uk` : répertoire d'APIs publiques récupéré (copie 09/11), mais **ne documente pas un endpoint IIIF des Archives**. Site des Archives et page copyright également indexés, tandis que `archives.parliament.uk/robots.txt` renvoie le **HTML de la page d'accueil, pas un fichier robots**.
- Qatar Digital Library `qdl.qa/node/372` : page de contact « Comments or concerns » lue (copie 02/11). Aucun plafond d'API.
- UCD Digital Library `https://digital.ucd.ie/` : accueil **temporaire** retrouvé (copie 01/10), avec exports **CSV et JSON** pour « Collection as Data » ; alternative de téléchargement de métadonnées intéressante, sans prouver l'état actuel du TLS de la sonde.
- University of Washington `jewishstudies.washington.edu/sephardic-studies/reading-ladino-21st-century-mirador` : tutoriel Mirador indexé (12/03), explique l'usage de l'URL manifeste dans un visualiseur.
- Villanova `https://digital.library.villanova.edu/` : accueil retrouvé (copie 06/09), **pas** le manifeste ciblé `/Item/vudl:92879/Manifest` qui demeure en 403.
- Yale `collections.library.yale.edu/catalog/opensearch.xml` : métadonnées **extraites** de la description OpenSearch (15/11), mais **pas de structure XML réutilisable conservée par l'extracteur**. `web.library.yale.edu/lit/servicecatalog/164929` renvoie une **page d'authentification Yale SSO**, et les trois pages `yaleits.atlassian.net/wiki/x/...` ne restituent que **« Browser not supported »** : aucun contenu Confluence documenté par ces réponses.
- National Palace Museum : formulaire `contactus.npm.gov.tw/Web/case-apply.jsp?l=1&TArea=1` **lisible sans soumission**, exige identité et captcha ; reste une **intervention humaine**, pas une lacune de lecture.

## PDF et diapositives (pas de quota démontré)

- **Cardiff University** : [`Unlocking your collections with Alma Digital and IIIF`, Alison Harvey (29 diapositives)](https://igelu.org/wp-content/uploads/2022/10/Unlocking-your-collections-with-Alma-Digital-and-IIIF.pdf) : PDF ouvert le 15/11, pages **1, 11, 21, 29 affichées visuellement**. Projet de numérisation et usage d'IIIF, pas de plafond public établi dans les éléments inspectés. **Ne pas déclarer les 29 pages analysées diapo par diapo**.
- **Yale LUX** : [`LUX: Cross-Collection Discovery at Yale`, Susan Gibbons/Robert Sanderson, 26 diapositives, 2022](https://www.cni.org/wp-content/uploads/2022/12/LUX-CNI-Susan-Rob-Rob-Sanderson.pdf) : extraction de texte, pages **1 et 18 affichées** ; décrit **Linked Art, IIIF, IIIF Change Discovery** et architecture de découverte, **pas une documentation de quotas**. Le document entier est récupérable et n'a plus besoin d'être catalogué comme « PDF inaccessible ».
- **St Andrews** : chemin ancien `eprints.st-andrews.ac.uk/.../IIF%20resources.pdf` toujours inaccessible ; **copie textuelle** de l'emplacement actuel `www.st-andrews.ac.uk/assets/university/library/documents/IIF%20resources.pdf` retrouvée, guide de localisation des liens de manifestes, indexée 11/02/2025. Le lecteur PDF visuel échoue sur l'URL actuelle ; **ne pas prétendre contrôle visuel**.
- **National Palace Museum, Taiwan** : le PDF 2021 Presidential Hackathon d'URL historique n'est toujours pas consultable ici ; la page institutionnelle de l'événement est accessible mais ce n'est **pas le PDF**. Ne pas réutiliser ses éventuels chiffres d'une autre source.

## URL toujours ouvertes, sans contenu original ou sous compte

**Véritables blocages** : robots Cornell, DRI repository, Durham, Getty Media 503, HAB Image 403, Bodleian `robots.txt` 400, portail Finna Swagger `v1?swagger` 403, ancien `mps.lib.harvard.edu/robots.txt` (page vide), KB MDO, National Palace Museum Image `info.json` (timeout), lien PDF Keio non téléchargé, PDF NPM hackathon inaccessible, robots SLV 403, IIIF Villanova manifeste 403, DRI Swagger direct 403 et certaines pages de politique non récupérées.

**Actions humaines / règles contractuelles** : `mailto:` de la BNP, clé API Harvard Art Museums (formulaire Google), formulaire National Palace Museum, et demandes techniques à des administrations. **Ne pas les requalifier comme une page illisible**.

**Échecs ou chemins obsolètes à ne pas surinterpréter** : Delpher (robots excluant la plupart des agents), `rijks-web.azurewebsites.net/en/data/terms-of-use` 403, `id.rijksmuseum.nl/robots.txt` 400, `rosetta.slv.vic.gov.au/delivery/general/termsofuse.jsp` 404, `www.leventhalmap.org/robots.txt` 404, `www.nationalarchives.gov.uk/.../case-studies/digital-archives/` 403, et `digital.library.villanova.edu/robots.txt` sans contenu (304).

## Suite à donner

1. Inscrire les résultats dans le registre URL → constat, en conservant les copies datées et les anciens statuts HTTP.
2. **Ne pas confondre 88 URL examinées et 88 pages lues** : plusieurs sont non-web, bloquées ou ne rendent qu'un shell SPA/SSO.
3. Regrouper le résidu manuel par : documents inaccessibles, authentification, contacts, robots distincts d'IIIF et demandes de politique de débit. Préparer seulement les demandes humaines indispensables.
4. **Pas d'édition des données canoniques ni de `BENCHMARK.xlsx`** avant validation et régénération cohérente. Cette branche reste en PR brouillon.
