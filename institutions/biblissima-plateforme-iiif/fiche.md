# Biblissima+ – plateforme IIIF (`biblissima-plateforme-iiif`)

- **Classeur** : GLAM-017 · France · **Vérifié le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `data.biblissima.fr` (Wikibase, API de réconciliation), `portail.biblissima.fr` (manifestes IIIF), `iiif.biblissima.fr` (IIIF Collections, prototype), `doc.biblissima.fr`, `query.biblissima.fr` (SPARQL).

## Ce que dit la doc officielle (`doc.biblissima.fr/api/…`, lue en entier)
- API MediaWiki/Wikibase `data.biblissima.fr/w/api.php` : « mêmes accès par API que Wikidata ». API de réconciliation `…/reconcile/{fr,en}/api` (batch `queries`, `limit` par requête, exemple « 5 propositions maximum »). Manifestes IIIF du Portail : `portail.biblissima.fr/iiif/manifest/ark:/43093/{id}` (API Présentation 2.1) et `…/iiif/collection/…`.
- **SPARQL** (`query.biblissima.fr`, QLever depuis avril 2026) : « n'est pas encore accessible publiquement » ; accès sur demande à `team@biblissima-condorcet.fr`. `robots.txt` de l'hôte : 401. **Non testé** (non public).
- Licence des données : Licence Ouverte 2.0. **Aucun quota, aucune limite de débit, aucune politique de bots** dans les pages lues. `robots.txt` : 404 sur `data`, `doc`, `iiif`, `portail` (autorisé).
- `iiif.biblissima.fr/collections` : prototype de recherche qui moissonne les manifestes de nombreuses bibliothèques ; l'idée d'un moissonnage de masse est décrite, sans règle.

## Tests (1 passe, 5 requêtes de données, pauses 6 s)
Wikibase `wbgetentities` : **200** · réconciliation : **200** · `/entity/Q27392` : 303 puis 301 (http→https, non suivi) · manifeste du Portail (717 ko) : **200** · collection IIIF : **200**. Aucun 429 ni en-tête de limite.

Passes 2 et 3 (2026-11-14, configurations committées avant lancement) : réconciliation (racine, `preview`, `suggest/property`, `extend`) **200** ×4 · `Special:EntityData/Q27392` : 301 puis 303 puis `.json` **200** (chaîne de redirections lue dans les en-têtes) · manifestes de démonstration `demos.biblissima.fr` **200** ×2. Aucun 429 ni en-tête de limite. SPARQL (`query.biblissima.fr`) : 401, non public, non testé.

## Web
Pages lues en passe de rattrapage : `doc.biblissima.fr/iiif/introduction-iiif/` (pédagogique, sans quota), `doc.biblissima.fr/formation-iiif/`, robots.txt de `projet.biblissima.fr` (Drupal standard) et de `demos.biblissima.fr` (404). Trois recherches web de plus : aucune limite ni plainte trouvée (résumés de moteur, non vérifiés).
Aucune limite publiée ; contact conseillé : `team@biblissima-condorcet.fr`.

## Conclusion
Limite chiffrée : aucune. `limit` de la réconciliation = paramètre de requête (non un quota). Confiance : moyenne.
