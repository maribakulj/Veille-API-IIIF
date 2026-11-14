# Lancaster University Library — Lancaster Digital Collections (`lancaster-university-library`)

- **Classeur** : GLAM-065 · Royaume-Uni · Audit v2 le 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `digitalcollections.lancaster.ac.uk` (site, manifestes et collections IIIF Presentation 2), `iiif.digitalcollections.lancaster.ac.uk` (images, Cantaloupe 4.1.6, IIIF Image 2 niveau 1), `services.digitalcollections.lancaster.ac.uk` (TEI). Plateforme dérivée de Cambridge Digital Library (`cudl.lib.cam.ac.uk`, hôte cité).

## Sources
- Doc : pages About, Help (FAQ vide), Terms & Conditions de `digitalcollections.lancaster.ac.uk` (sources/doc4, doc6) ; pages bibliothèque (doc3) ; fiche IIIF Guides (doc3/06) : « Open an item, and select the IIIF icon on the "About" pane » ; aucune page de doc API, aucun quota.
- Terms : usage non commercial ; interdit de « systematically extract and/or re-utilise substantial parts of the Content » et de « create and/or publish your own database that features substantial parts of this site ».
- robots.txt : `digitalcollections` : `Disallow:` vide ; `www.lancaster.ac.uk` : Crawl-delay 5, rien sur la plateforme ; `iiif.` et `services.` : 404 (aucun robots.txt) ; `cudl.lib.cam.ac.uk` : 403 CloudFront en lecture directe (arrêt, non contourné), lu via Wayback : `Disallow: /search`.

## Tests (3 passes + 1 répétition, configs committées avant lancement, pauses 6 s)
Collection `/iiif/collection/davy` (133 manifestes, 18 ko) **200** ; `sitemap.xml` **200** ; page collection (HEAD) **200** ; manifeste `MS-DAVY-11306` (158 ko) : **timeout de lecture** à la 1re tentative (passe 2, pas un 429), **200** à la répétition (passe 2b) ; `info.json` **200** ; dérivé 200 px **200** ; TEI **301** (barre finale) puis **200**. Aucun 429, aucun 403, aucun en-tête de limite (serveur envoy).

## Web (4 recherches, une par catégorie)
Institution : IIIF utilisé, partenariat avec Cambridge. Présentations : lancement public 2021. Utilisateurs et tickets : aucun résultat.

## Conclusion
Limite chiffrée : aucune. Règle écrite : usage non commercial, pas d'extraction systématique de parties substantielles. Confiance : moyenne. Une lenteur ponctuelle (timeout 20 s) sur un manifeste de 158 ko.
