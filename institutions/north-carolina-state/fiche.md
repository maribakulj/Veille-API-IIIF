# North Carolina State University Libraries (`north-carolina-state`)

- **Classeur** : GLAM-052 · États-Unis · **Vérifié le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `iiif.lib.ncsu.edu` (serveur d'images IIIF), `d.lib.ncsu.edu` (Rare and Unique Digital Collections : notices, manifestes, recherche ; détection de bots 401), `www.lib.ncsu.edu` (site de la bibliothèque).

## Sources
- Doc très mince : le billet « Slow Looking » (www.lib.ncsu.edu/node/51279, 2018) donne l'URL `https://iiif.lib.ncsu.edu/iiif/mc00227-003-ff0073-000-001_0004/info.json` ; annonce IIIF 2016 (iiif.io) ; README du dépôt Ocracoke (IIIF Content Search). Aucune page de doc API, aucun quota, aucune politique de moissonnage dans les pages lues (`sources/a`, `sources/b`).
- `d.lib.ncsu.edu` : réponse 401 « NC State University Libraries Bot Detection » (défi de preuve de travail) dès la première requête : arrêt, pas de contournement. Pages À propos et robots.txt lues via Wayback (`sources/wayback/`) : réutilisation libre pour l'enseignement, la recherche et l'étude privée ; robots.txt interdit les facettes et GPTbot, sans Crawl-delay.
- robots.txt : iiif (200, aucune règle), www (200, Drupal standard), d (401, Wayback).

## Tests (1 passe, 3 requêtes dont robots.txt, pauses 6 s)
`info.json` de l'image d'exemple : **200** (Apache, fichier statique de 2016) ; image `/full/500,/0/default.jpg` : **200**. Aucun en-tête de limite, aucun 429. Manifestes et recherche (d.lib.ncsu.edu) non testés : détection de bots. Aucune URL de manifeste publiée, aucune devinée.

## Web
Quatre catégories : doc officielle (billet), utilisateurs (aucun résultat), tickets (aucun résultat), présentations (annonce IIIF 2016, README Ocracoke). Les billets de bibliothèques voisines sur la détection de bots (Duke, UTA, UNC) sont des résumés de moteur non vérifiés, sans rapport direct avec NC State.

## Pourquoi pas de quota publié ?
Hypothèse, non confirmée : la bibliothèque protège ses pages (d.lib) par une détection de bots plutôt que par des quotas annoncés, et ne publie pas de doc d'API en dehors de l'exemple d'image.

## Conclusion
Limite chiffrée : aucune. Contact : adresses de la page À propos (Wayback). Confiance : moyenne. Crash test (g) : à faire à la fin sur le serveur d'images (hôte sans réseau protégé visible, Apache).
