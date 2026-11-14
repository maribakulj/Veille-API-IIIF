# Yale Peabody Museum — `yale-peabody-museum`

- **Statut** : audit v2 a–f complet ; g (crash test) à faire en fin de boucle
- **Vérifié le** : 2026-11-14 · **Vérifié par** : agent de veille (Claude Sonnet 5.5, lot E)
- Première passe de cette institution (aucun travail antérieur).

## 1. Sources (documentation lue)
Fichiers : `sources/a1` à `a5` (HTML brut, SHA-256, texte extrait), `sources/web/`.
- `peabody.yale.edu/about/terms-of-use` (lue en entier) : « users may download these files for their personal or educational use, subject to any additional terms or restrictions » ; usage au-delà du fair use : permission écrite du détenteur des droits ; attribution « YPM » ; contact permissions `peabody.permissions@yale.edu`. Aucune règle de débit, de bots ou d'API. « Collections Policies » : accès aux collections physiques.
- `peabody.yale.edu/explore/collections` : lien vers le catalogue ; le guide IIIF (`guides.iiif.io/guides/collections.peabody.yale.edu`) renvoie au bouton IIIF du catalogue pour copier un lien de manifeste.
- LUX (Yale) : dépôts `project-lux` (lux-middletier `docs/api-endpoints.md` : `/api/search/:scope`, `/data/{id}`, `/api/facets/:scope`, `/api/related-list/:scope`, `/api/stats`, `/api/advanced-search-config`…) ; aucune limite de débit ni politique d'usage ; le backend exige une authentification interne.
- Formation IIIF (`training.iiif.io`) : manifestes `manifests.collections.yale.edu/{unité}/obj/{id}` (v3 par défaut, `/v2/` pour la v2).
- robots.txt (par hôte, détail dans `data.json`) : peabody.yale.edu (Drupal standard) ; lux et peabody.collections : `Disallow: /view/results/`, pas de Crawl-delay ; manifests et images : 404.
- Étape d : pas d'endpoint de statut, pas d'en-tête de limite documenté, pas de clé pour l'accès public, contact : permissions du Peabody (aucun contact technique trouvé).

## 2. Tests (voir `tests/journal.log`, `tests/raw/`)
Passe 1 (10 requêtes dont 4 robots.txt) : accueil Peabody 200 ; catalogue `collections.peabody.yale.edu` 302 vers `peabody.collections.yale.edu` ; LUX `/api/stats` et `/api/advanced-search-config` 200 ; manifestes Yale YCBA (v3) et YUAG (v2) cités par la formation IIIF : 200.
Passe 2 (4 requêtes) : accueil et `/api/stats` de `peabody.collections.yale.edu` 200 ; images IIIF 2 (`info.json` et dérivé 200 px, identifiant lu dans le manifeste YCBA) 200.
Aucun 429, aucun en-tête de limite ; chaîne Varnish + CloudFront devant LUX, Cantaloupe 4.1.9 pour les images.
Non testé : recherche et données LUX (format de requête non documenté), manifestes propres au Peabody (aucun identifiant publié).

## 3. Web (f)
Voir `sources/web/recherches-web-2026-11-14.md` : conditions du Peabody ; article arXiv 2023 citant le YPM ; aucune plainte ni ticket trouvés.

## 4. Conclusion
- Limite documentée : aucune de débit ; seule consigne : `Disallow: /view/results/` (LUX).
- Limite observée : non (14 requêtes, aucun 429).
- Les réponses n'annoncent pas de limite.
- Pourquoi non publié : non trouvé ; hypothèse (étiquetée) : politique gérée au niveau de LUX/Yale et du réseau CloudFront plutôt que dans la doc du Peabody.
- Confiance : moyenne. À vérifier à la main : wiki Yale ITS (202 vide), contact Peabody pour une limite non publiée.
- Crash test (g) : `config/crash-images-info.json` prêt (serveur d'images commun, sans limite documentée, réseau CloudFront).
