# Yale Center for British Art (YCBA) — fiche d'audit v2

## Sources
- Doc lue en entier (sources/doc, doc2, doc3, doc6) : Collections Data Sharing (annonce LIDO par OAI-PMH, images IIIF, base harvester-bl.britishart.yale.edu/oaicatmuseum/), Open Data and Data Services Terms of Use, Terms of Use, Using Images, Using collections, LUX technology (application JavaScript sans texte lisible), robots.txt de 8 hôtes.
- Seule règle de débit écrite (Open Data and Data Services Terms of Use) : « Where you make, use, or distribute software that makes requests of the Center's services, you should ensure that your software will not perform excessive requests. » et « The Center reserves the right to limit or block any user or client for excessive use. » ; User-Agent : « should include details of your software application and your contact details including an e-mail address and URL ». Aucun chiffre. (Notre User-Agent contient l'URL du projet mais pas d'e-mail : écart signalé, non modifiable par l'agent.)
- collections.britishart.yale.edu (catalogue en ligne) : 403 Cloudflare (« Just a moment... ») dès le robots.txt ; non contourné ; robots.txt lu dans la Wayback Machine (capture 2026-01-01, Drupal standard).
- Pages Confluence yaleits.atlassian.net (doc IIIF/LUX) : réponse 202 vide ; non lisibles, aucune capture Wayback.

## Tests (3 passes, 12 requêtes d'appel)
- IIIF Presentation v3 et v2 (manifests.collections.yale.edu, objet 1772) : 200, aucun en-tête de limite ; v3 par défaut, v2 par « v2/ ».
- OAI-PMH OAICat (Identify, ListMetadataFormats, ListSets, GetRecord lido) : 200, aucun en-tête de limite.
- IIIF Image 2 (images.collections.yale.edu) : info.json et dérivé 200, aucun en-tête de limite.
- Vignette media.collections.yale.edu : 307 vers une URL S3 pré-signée de 60 s (non suivie, hôte différent ; signature redigée dans les en-têtes archivés).
- Données liées http://collection.britishart.yale.edu/id/page/object/1772 : l'hôte ne se résout plus (DNS).

## Web
Aucun résultat sur des plaintes 429/503 ou des tickets d'outils visant le YCBA ; présentation 2015 (SlideShare) citée seulement en résumé de moteur ; article InfoDocket 2017 lu (70 000 images IIIF).

## Conclusion
Aucun quota ni limite de débit chiffrés : seulement la clause « excessive use » et l'exigence d'un User-Agent identifiable. OAI-PMH et IIIF répondent sans en-tête de limite. Le catalogue en ligne est derrière Cloudflare (refus d'accès, pas un quota). Raison supposée (hypothèse) de l'absence de chiffre : politique de courtoisie et de blocage discrétionnaire.
