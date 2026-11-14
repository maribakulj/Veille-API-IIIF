# Göttingen State and University Library – GDZ (`gottingen-state-gdz`)

- **Classeur** : GLAM-025 · Allemagne · audit v2 du 2026-11-14 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `gdz.sub.uni-goettingen.de` (site, OAI-PMH `/oai2/`), `manifests.sub.uni-goettingen.de` (IIIF Presentation), `images.sub.uni-goettingen.de` (IIIF Image 2), `www.sub.uni-goettingen.de` (site de la SUB, doc).

## Sources
- GDZ : accueil, aide à la recherche (`/site/help`), mentions légales, contact, confidentialité (sources/a1, a2) : aucune page de doc d'API ni de conditions d'usage des API ; `/api` renvoie un JSON de genres (aide à la recherche, pas une API documentée) ; `/about` : 404.
- `robots.txt` des quatre hôtes (gdz, www.sub, images, manifests) : `User-agent: *` puis `Disallow:` vide (www.sub : `Allow: /`) ; aucun `Crawl-delay` ni `Request-rate` (sources/a1, a2, a3).
- Pages de la SUB (IIIF, TIFY, Digital Policies) : les URL actuelles renvoient la page d'accueil (site restructuré, sources/a3) ; lues dans la Wayback (sources/wayback/*.md). Elles disent : IIIF Image et Presentation « unterstützen diverse bildbasierte digitale Bibliotheken der SUB » (dont le GDZ) ; politique : « möglichst freien Nutzung und Offenheit [...] (offene Schnittstellen und Vernetzung) », CC / Public Domain Mark. Aucun chiffre de débit, aucun quota, aucune règle sur les robots.
- Fotografieren und Digitalisieren (sources/a2) : règles pour les copies physiques et tarifs de reproduction, rien sur les API.

## Tests (2 passes, configurations committées avant lancement, pauses 6 s, 9 requêtes d'API au total, plus 3 robots.txt)
- Passe 1 (gdz) : OAI `Identify`, `ListMetadataFormats`, `ListSets`, `GetRecord` (PPN519929969), page ouvrage, flux RSS : **200** partout.
- Passe 2 : manifeste IIIF, `info.json` (Image 2), dérivé 200 px : **200** partout.
- Aucun 429, aucun en-tête de limite (`X-RateLimit-*`, `Retry-After`, `RateLimit-*`) ; en-têtes : `x-powered-by: PHP/8.4.27`, `cache-control: s-maxage=86400` sur `info.json`, HSTS. `ListRecords` non lancé (volume). Le `baseURL` annoncé par `Identify` est en `http://`.

## Web (4 catégories)
- Institution : la politique numérique de la SUB (Wayback) parle d'ouverture sans chiffre ; aucune politique de bots.
- Utilisateurs : aucune plainte 429/blocage trouvée.
- Tickets : un ticket de `sourcelibrary-v2` (#3510) liste `images.sub.uni-goettingen.de` parmi des hôtes qu'un proxy n'autorise pas (liste d'autorisation du proxy, pas un blocage du serveur).
- Présentations : IIIF Conference 2019 Göttingen (GDZ cité comme dépôt IIIF) ; rien sur le trafic ni les limites.

## Pourquoi pas publié ?
Hypothèse (non étayée par une source) : service public, sans limite chiffrée, la politique est l'ouverture « avec le moins de restrictions possible » ; le profil apis.io (tiers, non vérifié) indique « no published rate limits ».

## Conclusion
Limite chiffrée : aucune. Règle écrite : usage ouvert ; reproduction commerciale à demander (hsd@sub.uni-goettingen.de). Contact : gdz@sub.uni-goettingen.de. Confiance : moyenne. Crash test (g) : configuration `config/crash-image-info.json` prête, à lancer à la fin.
