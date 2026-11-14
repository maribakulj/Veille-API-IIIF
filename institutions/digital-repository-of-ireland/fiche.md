# Digital Repository of Ireland (`digital-repository-of-ireland`)

- **Classeur** : GLAM-070 · Irlande · audit v2 du 2026-11-14 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `repository.dri.ie` (dépôt, API, IIIF, OAI), `www.dri.ie` / `dri.ie` (site du projet) — tous deux derrière Cloudflare.

## Sources
- **Défi Cloudflare** : `robots.txt` de `www.dri.ie` et de `repository.dri.ie` répondent « Just a moment... » (403) dès la 1re requête (2026-11-14T03:40Z, `sources/a1/`). Hôtes arrêtés, pas de contournement. Pages lues dans le Wayback (`sources/wayback/wayback-dri.md`) : robots.txt (aucune règle active sur repository ; `Disallow: /?s=` et `/search/` sur dri.ie, pas de Crawl-delay), « Standards Adoption » (IIIF, OAI-PMH DC/EDM, « standards-compliant API »), About, End User Agreement (2016).
- **GitHub de l'institution** (lu directement, hôte GitHub) : `dri-documentation` renvoie la doc API vers `https://repository.dri.ie/api-docs` (non lisible : pas de capture Wayback) ; `dri-app/config/routes.rb` : `iiif/:id/manifest`, `iiif/collection/:id`, Riiif monté à `/images`, contrôleur `oai_pmh`, `rswag` à `/api-docs` ; `config/initializers/cloudflare_turnstile.rb` (Turnstile, `fail_open = true`) ; Gemfile : `riiif`, `iiif-presentation`, `blacklight_oai_provider`. Aucun throttling (pas de rack-attack dans les initialiseurs listés).
- Aucune limite de débit dans aucune page lue.

## Tests
Une passe (`config/passe1.json`, committée avant lancement) : 0 requête envoyée. La sonde a refusé l'endpoint `api-docs` car l'hôte est arrêté (403 défi) au registre partagé. Les autres familles (IIIF, Riiif, OAI) n'ont pas d'identifiant public donné par la doc et ne sont pas devinées. Aucun 429.

## Web (4 recherches, une par catégorie)
- Institution : page Standards Adoption (ci-dessus), pas de politique de bots.
- Utilisateurs : aucun résultat (résumé de moteur, non vérifié).
- Tickets : aucun résultat (résumé de moteur, non vérifié).
- Présentations : diaporama de l'institution (IIIF « bientôt », REST API d'ingest) ; une affiche du TCD (2017) n'a pas pu être lue (redirection signée, non suivie).

## Conclusion
Limite chiffrée : aucune trouvée. L'absence d'accès automatisé (Turnstile Cloudflare) est un refus d'accès à ce client, pas un quota. Confiance : faible. À vérifier à la main : `repository.dri.ie/api-docs` (voir `data.json`). Contact : dri@ria.ie. Étape g : impossible (aucun hôte testable).
