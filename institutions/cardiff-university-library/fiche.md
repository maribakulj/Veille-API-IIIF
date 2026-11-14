# Cardiff University Library — Digital Special Collections (GLAM-056)

## Sources
- www.cardiff.ac.uk : défi Cloudflare « Just a moment » dès la 1re requête (robots.txt, 2026-11-14T02:35:06Z) : arrêt ; pages lues via Wayback (sources/wayback/cardiff-www.md) : « All of our IIIF-enabled digital content is freely available to view and re-use under a Creative Commons licence. » ; contact specialcollections@cardiff.ac.uk ; aucun quota, API ni bot cité. robots.txt (Wayback 2026-05-01) : sans Crawl-delay.
- Digital Special Collections est servi par librarysearch.cardiff.ac.uk (Primo VE, Alma Digital), URL citée par le billet de lancement (sources/doc-b/text/05.txt). robots.txt : Crawl-delay: 10, Disallow /primaws, /discovery/search, /nde/search, plusieurs robots nommés interdits (GPTBot, etc.).
- Motif d'URL Alma /view/iiif/presentation/{RepresentationID}/manifest décrit par la ZB Zurich (sources/doc-c/raw/05.html) ; Ex Libris : IIIF natif depuis août 2017 (sources/doc-c/text/02.txt) ; seuil d'API Alma : 1000 appels par licence nommée et par jour (sources/doc-c/text/03.txt), lié à l'API Alma, pas établi pour le IIIF.
- Rien de Cardiff sur les quotas, les bots ou les API de données.

## Tests
- Passe 1 (cardiff-passe1-librarysearch.json, 10 s) : page de découverte 302 puis 200 (coquille JS), siteindex.xml 200 (index vide), 4 requêtes dont robots.txt.
- Passe 2 (cardiff-passe2-manifest.json) : manifeste IIIF Presentation 2 200 (107 ko), JSON de livraison 200 ; identifiant 12204337930002420 publié par un blog tiers lu en original. 3 requêtes dont robots.txt.
- Passe 3 (cardiff-passe3-image.json) : service d'images annoncé par le manifeste sur eu-img02.ext.exlibrisgroup.com : NON LANCÉ (hôte arrêté par le registre après le 403 « Missing Authentication Token » de son robots.txt, réponse de passerelle d'API) ; 0 requête.
- Aucun en-tête RateLimit ou Retry-After sur librarysearch ; pas de 429.

## Web
- institution : page Digital collections (Wayback) ; presentations : billet de lancement 2022 (blog de l'université) et diapositives IGELU de Cardiff (illisibles, listées à vérifier à la main).
- utilisateurs et tickets : aucun résultat propre à Cardiff (résumés de moteur, non vérifiés) ; un blog tiers montre le manifeste fonctionnel dans Universal Viewer, sans mention de limite.

## Conclusion
Aucun quota ni politique de débit publiés par Cardiff ; hypothèse non vérifiée : Cardiff s'en remet à la plateforme hébergée Ex Libris et ne publie pas de règle propre. Seule règle écrite : Crawl-delay 10 s. Observé : manifeste et JSON en 200 sans en-tête de limite ; défi Cloudflare sur le site www (pas un quota). Le service d'images Ex Libris reste à tester (URL dans a_verifier_manuellement). Crash test (g) : config crash-delivery-json.json préparée.
