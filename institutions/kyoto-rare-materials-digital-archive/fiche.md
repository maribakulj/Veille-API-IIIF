# Kyoto University Rare Materials Digital Archive (GLAM-073)

## Sources
- Pages officielles (sources/v2, b, c ; empreintes dans SHA256SUMS) : about, howto, reuse (conditions de réutilisation), page d'item, robots.txt de rmda et de kulib.
- L'URL du manifeste vient de la page officielle d'item (`/iiif/metadata_manifest/RB00000122/manifest.json`), celle du service d'image du manifeste lui-même.
- Citation : « Users should download the Images from this Website by themselves. The Images output in JPEG format with a maximum size of 2000pixel per side. » Aucun quota, aucune limite de débit, aucune doc d'API.

## Tests
- Passe 1 : manifeste IIIF 3 d'un item : 200, 95 ko, aucun en-tête de limite (access-control-allow-origin: *).
- Passe 2 : info.json (Cantaloupe/5.0.6), image 200 px, page Mirador : 200 partout, aucun en-tête de limite. Aucun 403, 429, CAPTCHA.
- Pauses 6 s ; robots.txt sans Crawl-delay.

## Web
- institution : conditions de réutilisation (lues) ; présentations : annonce 2017 (lue), article IIAI 2018 (résumé de moteur, non vérifié).
- utilisateurs, tickets : aucun résultat (requêtes dans data.json).

## Conclusion
Aucun quota publié ni observé. Raison probable (hypothèse) : service académique Drupal + Cantaloupe, sans politique de débit écrite. Contact : adresse e-mail de /en/about. Étape g : à faire (crash-image-info.json préparé).

## Crash test (étape g)

Crash test fait le 2026-11-14 : image-info-json sur rmda.kulib.kyoto-u.ac.jp : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/kyoto-rare-materials-digital-archive.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
