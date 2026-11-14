# Brown University Digital Repository (BDR) — `brown-university-digital-repository`

- **Statut** : audit v2 a à f ; g impossible (hôte en défi Cloudflare Turnstile)
- **Pays** : États-Unis (GLAM-056) · **Hôtes** : `repository.library.brown.edu` (site, API, IIIF), `library.brown.edu` (blog)
- **Vérifié le** : 2026-11-14 (UTC)

## Sources

- `repository.library.brown.edu/robots.txt` (200) : `Crawl-delay: 30` ; Disallow `/storage`, `/iiif`, `/iiif/image`, `/services`, `/viewers`, `/studio/login/`. `/api/` n'est pas interdit. Preuve : `sources/doc/raw/01.html`, `sources/wayback/robots-20250401.md`.
- `repository.library.brown.edu/studio/api-docs/` : **défi Cloudflare Turnstile** à 02:30:44Z (`sources/doc/raw/02.html`). Lue via Wayback (capture du 2025-03-31) : `sources/wayback/api-docs-20250331.md`.
- Wiki GitHub de l'institution (`bdr_api_documentation`) : `sources/wiki/`, `sources/wiki2/` (Overview, Item, Collection, Search). Aucune limite chiffrée.
- Outils `bdr-api-tools` : `sources/doc/text/06.txt`, `sources/github/`.
- robots.txt de `library.brown.edu` (Crawl-delay 30), `iiif.io`, `github.com`, `brown-university-library.github.io` (404), `raw.githubusercontent.com` (404).
- Blog `library.brown.edu/create/digitaltechnologies/?p=185` et `?p=19` : 410 (supprimés) ; `sources/blog/`.
- Incident de politesse : `fetch_doc.sh` a envoyé 3 requêtes en 6 s à `repository.library.brown.edu` (02:30:41, :44, :47) malgré `Crawl-delay: 30` (l'outil ne lit pas ce délai) ; pas de 429. Les requêtes suivantes vers `library.brown.edu` ont respecté 30 s.

## Tests

Passe 1 (`config/passe1-api.json`, 3 endpoints, committée avant) : **0 requête envoyée**. La sonde a sauté l'hôte (registre partagé : défi Turnstile). Journal : `tests/journal.log`. Les trois API (Item, Collection, Search) sont donc non testées. Aucun 403, aucun 429, aucun en-tête de limite observé.

## Web

- Institution (officielle) : « In Spring 2025 we added features from Cloudflare to protect against bot traffic. This may affect users of the API, particularly if you are requesting a large volume of items at a high rate. » (wiki, lu).
- Présentations / outils : « We've had to enable certain protections to prevent problems due to excessive bot-traffic. If you're on VPN, you'll minimize the chance of being blocked » (bdr-api-tools, lu).
- Tickets : aucun résultat (page des tickets du dépôt lue : vide). Utilisateurs : aucun résultat (résumé de moteur, non vérifié).

## Conclusion

- **Limite documentée chiffrée** : non. **Crawl-delay** robots.txt : 30 s.
- **Limite observée** : non (aucun test possible).
- **Accès refusé à ce client** : oui, défi Turnstile (protection ajoutée au printemps 2025, documentée par l'institution). Ce n'est pas un quota.
- **À refaire autrement** : navigateur / VPN Brown, ou demande via un ticket sur le dépôt `bdr_api_documentation`.
- **Étape g** : impossible (hôte arrêté).
