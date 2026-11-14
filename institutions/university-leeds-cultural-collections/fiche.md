# University of Leeds Libraries – Cultural Collections — `university-leeds-cultural-collections`

- **Statut** : audit v2 a à f ; g préparée (configuration crash, non lancée)
- **Pays** : Royaume-Uni (GLAM-066) · **Hôtes** : `iiif.library.leeds.ac.uk` (IIIF, CloudFront/Digirati), `explore.library.leeds.ac.uk` (catalogue, Cloudflare), `library.leeds.ac.uk`
- **Vérifié le** : 2026-11-14 (UTC)

## Sources

- robots.txt : `explore` (200 : `Allow: /` pour `*`, `Content-Signal ai-train=yes`, agents d'IA « utilisateur » interdits, pas de Crawl-delay), `iiif` (404), `library` (200 vide). `sources/doc/raw/01.html` à `04.html`.
- Page d'item `explore.library.leeds.ac.uk/special-collections-explore/372687` : **403 Cloudflare « Just a moment... »** à 02:39:38Z (`sources/doc/raw/03.html`). Lue via Wayback : `sources/wayback/explore-372687-20241224.md`.
- Support d'atelier IMC Leeds 2025 (tiers) : manifestes d'exemple de `iiif.library.leeds.ac.uk/presentation/cc/` (`sources/doc/text/05.txt`).
- Actualité de la bibliothèque (2025-05-28) et notice de panne : `sources/web/`. **Aucune page de doc d'API ni de conditions de moissonnage trouvée.**

## Tests

- Passe 1 (`config/passe1-manifeste.json`) : 1 manifeste Presentation 3 : 200.
- Passe 2 (`config/passe2-images.json`, identifiant tiré du manifeste) : info.json Image 3, Image 2, miniature, dérivé 200×151 : 200.
- 6 requêtes vers `iiif.library.leeds.ac.uk` (plus 2 robots.txt), pauses ≥ 6 s ; **aucun 429, aucun en-tête de limite** ; en-têtes CloudFront (`x-cache`, `x-amz-cf-id`). Catalogue `explore` : non testé (403).

## Web

Institution : actualité de la bibliothèque (IIIF, 2025-05-28), pas de règle de débit. Présentations : support d'atelier. Tickets : dépôt `uol-library/eprints-iiif-manifest` sans ticket pertinent. Utilisateurs : aucun résultat.

## Conclusion

- **Limite documentée** : aucune. **Limite observée** : non (6 requêtes IIIF).
- **403 anti-bot** : oui sur le catalogue (Cloudflare), pas sur le service IIIF.
- **Contact** : `specialcollections@library.leeds.ac.uk`.
- **Étape g** : configuration `config/crash-manifest-thumbs.json` prête, non lancée.
