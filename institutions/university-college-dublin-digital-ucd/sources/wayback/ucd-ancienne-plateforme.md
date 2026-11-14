# Extraits verbatim de l'ancienne plateforme digital.ucd.ie (Wayback Machine, lus via le MCP internet-archive le 2026-11-14)

Raison : www.ucd.ie répond 403 (CloudFront « Request blocked ») à la sonde ; l'ancienne plateforme digital.ucd.ie a été retirée (voir about.html actuel) ; ces pages ne sont lisibles que par Wayback.

## 1. https://digital.ucd.ie/research/ — « Services » / Data Services APIs
Réplique : https://web.archive.org/web/20241204154507/https://digital.ucd.ie/research/

> The following APIs are available: Geospatial Data API International Image Interoperability Framework (IIIF) Quantitative Data API OpenSearch API Linked Data API unAPI

> UCD Digital Library has implemented support for the IIIF Image and Presentation APIs, which serve images and metadata that enable IIIF-aware clients to view and compare images.

> Calls to the API follow this template: https://iiif.ucd.ie/loris/{identifier}/{region}/{size}/{rotation}/{quality}{.format}

> Request metadata for object ivrla:439: https://iiif.ucd.ie/loris/ivrla:439/info.json

> Request JPEG image of object ivrla:439, width of image is 600px: https://iiif.ucd.ie/loris/ivrla:439/full/600,/0/default.jpg

> UCD Digital Library implements support for the IIIF Presentation API 2.0 . [...] Templates: http://data.ucd.ie/api/img/{identifier}/info.json (request metadata about an image) http://data.ucd.ie/api/img/manifests/{identifier} (request a manifest for an object that links to image data) http://data.ucd.ie/api/img/collection/{identifier} (request metadata about a collection of objects that link to image data)

> Request manifest of an object linking to a single image: http://data.ucd.ie/api/img/manifests/ucdlib:30860

> UCD Digital Library's implementation of Mirador is experimental while we evaluate its deployment and the performance of the IIIF APIs.

> The OpenSearch implementation at UCD DIgital Library is described in an OpenSearch Description Document at http://digital.ucd.ie/ . [...] template : http://data.ucd.ie/api/search/v1/?q={searchTerms}&start={startIndex?}&count={count} live example : http://data.ucd.ie/api/search/v1/?q=General+Post+Office&start=1&count=1

> http://data.ucd.ie/api/quant/v1/getStudyList

> Documentaiton for the API is available at: http://data.ucd.ie/docs/apiQuant.pdf

> Full documentation of the API is available at: http://data.ucd.ie/docs/apiLOD.pdf

> http://digital.ucd.ie/view/ivrla.31285.json (JSON) ; .dc (OAI-compliant Dublin Core) ; .rdf ; .ttl

> The unAPI endpoint is at http://digital.ucd.ie/api/unAPI.

> http://data.ucd.ie/.well-known/void

Aucune phrase de cette page ne mentionne de quota, de limite de débit ni de clé d'API.

## 2. https://digital.ucd.ie/terms/ — Terms and Conditions of Use
Réplique : https://web.archive.org/web/20250104024022/https://digital.ucd.ie/terms/

> This content is being made available solely for the purposes of research and education and as an alternative to directly accessing the analogue originals [...] Duplication of this content, other than as permitted by copyright legislation or authorised by the parent repository, is prohibited.

> Metadata is licensed under the CC BY-SA 4.0 license, and as such, any use of metadata elements should be acknowledged and cited.

Aucune mention de débit, de robots ni d'API.

## 3. https://digital.ucd.ie/help/ — « Save (download) »
Réplique : https://web.archive.org/web/20241205194601/https://digital.ucd.ie/help/

> The largest image size that can be downloaded automatically is 2000 pixels wide

(limite de taille d'image, pas de débit)

## 4. https://digital.ucd.ie/ (accueil, 2024-12-31) — « Return to Service - October 2024 »
Réplique : https://web.archive.org/web/20241231012939/https://digital.ucd.ie/

> UCD Digital Library is back working after a period of disruption. Our Mirador image viewer has been replaced with Universal Viewer, while we continue to make improvements; and some of our collections are not working as expected yet. As we update our documentation, please contact the team at digital.library@ucd.ie

## 5. https://www.ucd.ie/robots.txt (réplique du 2025-10-01 ; la sonde reçoit un 403)
Réplique : https://web.archive.org/web/20251001041446/https://www.ucd.ie/robots.txt

> User-agent: *
> Disallow: /webteam/ [...] /webtest1/ ... /microcredentials/explorecourses/medicineandhealth/entryrequirements/

Pas de Crawl-delay. Aucun Disallow ne vise /library/.
