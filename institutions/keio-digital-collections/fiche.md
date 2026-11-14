# Keio University Libraries – Digital Collections (GLAM-079)

## Sources
- Page About (en) : « The IIIF image server enables viewers to browse high-resolution images, and PDF files are provided for the collections below. » ; « Reprinting or reproducing all or parts of the digital data, including images, audio, video material, etc. ... is prohibited. » Aucune règle de débit.
- Page Contact (ja) : « 本サイトでは、高精細画像閲覧のためのIIIFサーバを利用しています » ; même interdiction de reproduction.
- robots.txt de dcollections.lib.keio.ac.jp : Drupal standard (/search/ interdit), pas de Crawl-delay ; iiif.lib.keio.ac.jp : 404.
- Page de notice : manifeste IIIF (« IIIF Manifest »), service d'image IIPImage sur iiif.lib.keio.ac.jp, PDF, visionneuse Universal Viewer.

## Tests
Passe 1 (4 requêtes) : manifeste 200 (31 ko), info.json d'image 200 deux fois, aucun en-tête de limite ; la page de visionneuse uv.php a subi une connexion réinitialisée : hôte arrêté, pas de contournement. Aucun 403, 429 ni CAPTCHA.

## Web
Non fait : le budget de recherche web de la session était épuisé (voir notes de data.json).

## Conclusion
Aucun quota ni limite de débit publiés ; interdiction écrite de reproduction des données numériques. IIIF Presentation 2 et Image 2 répondent en 200 sans en-tête de limite. Étape f à faire. Confiance faible.
