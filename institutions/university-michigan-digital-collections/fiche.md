# University of Michigan Library – Digital Collections (`university-michigan-digital-collections`)

- **Classeur** : GLAM-040 · États-Unis · audit v2 le 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `quod.lib.umich.edu` (DLXS : pages, manifestes IIIF, images IIIF, OAI-PMH), `www.lib.umich.edu` / `lib.umich.edu` (site de la bibliothèque), `blogs.lib.umich.edu` (billets).

## Sources
- Doc : aucune page « développeurs » ni « API » ; la doc se limite à des billets de blog et au pied de page de quod. Fichiers : `sources/a/` (robots.txt de quod, blogs, lib ; billet « Image Digital Collections Getting a Modern Interface » ; politique d'usage des ressources sous licence), `sources/a2/` (pages Digital Content and Collections, copyright, takedown, politiques), `sources/a3/` (billets OAI, écosystème DLXS, Project DOR).
- `quod.lib.umich.edu` renvoie un **défi Cloudflare (403)** pour les pages HTML : lues via Wayback (`sources/wayback/`, extraits verbatim). C'est là que se trouve l'URL du manifeste (« IIIF Manifest https://quod.lib.umich.edu/cgi/i/image/api/manifest/bhl:BL004079:BL004079 »).
- Billet OAI (blogs.lib.umich.edu) : « baseURL = http://quod.lib.umich.edu/cgi/o/oai/oai » ; l'UMProvider héberge les métadonnées HathiTrust domaine public et toutes celles des collections de texte et d'images.
- Guide d'aide (Wayback) : « Queries that return more than 10,000 items are truncated if you are not logged in. » (limite de profondeur de résultats, pas un quota de débit).
- robots.txt de quod : `User-agent: *` `Allow: /` ; bloc géré par Cloudflare qui interdit des robots d'entraînement d'IA nommés (ClaudeBot, GPTBot, CCBot…) et `Content-Signal: search=yes,ai-train=no,use=reference`. Notre User-Agent n'est pas nommé : autorisé.
- La politique « Statement on Appropriate Use of Electronic Resources » interdit « Use of robots, spiders or intelligent agents… » mais vise les ressources électroniques sous licence, pas les collections numériques ouvertes.

## Tests (1 passe, configuration committée avant lancement, 5 requêtes dont robots.txt)
- Manifeste IIIF Presentation 2 (bhl:BL004079:BL004079) : **200**, `application/json`, `access-control-allow-origin: *`, `cache-control: max-age=15552000, public` ; service d'image `https://quod.lib.umich.edu/cgi/i/image/api/image/bhl:BL004079:BL004079` (Image API 2, niveau 1).
- OAI `Identify` et `ListMetadataFormats` : **200** (`text/xml`).
- Page d'item HTML : **403, `cf-mitigated: challenge`** (défi Cloudflare) : l'hôte est arrêté, aucune autre requête (décision : pas de `info.json` d'image, pas de nouvelle passe).
- Aucun en-tête de limite (`RateLimit-*`, `Retry-After`, `X-RateLimit-*`) ; un cookie `__cf_bm` Cloudflare sur chaque réponse.

## Web (4 recherches, une par catégorie)
- Institution : aucune politique de bots ou de débit pour les collections numériques.
- Utilisateurs : aucun signalement de 429/403 propre à quod ; un site tiers (parse.bot) revendique un « API » non officiel pour quod (page 404 à la lecture, non vérifié).
- Tickets : aucun ticket GitHub sur quod.lib.umich.edu ; le dépôt mlibrary/uplift-viewer ne cite aucun endpoint ni limite.
- Présentations : session IIIF 2019 « IIIF and University of Michigan Libraries » (Powell, Espinosa), sans résumé ; billets sur DLXS/IIIF (`sources/a3/`).

## Pourquoi pas publié
Aucune limite n'est publiée. Les pages HTML sont derrière Cloudflare (défi), signe d'une protection contre les robots plutôt que d'un quota annoncé ; les API (manifeste, OAI) répondent sans défi dans notre test. Hypothèse : la bibliothèque protège les pages et laisse les API ouvertes (non vérifié).

## Conclusion
Limite chiffrée : aucune. Manifeste IIIF et OAI-PMH accessibles sans en-tête de limite ; pages HTML en défi Cloudflare. Confiance : moyenne. Contact : « Contact Us » de quod / dlps-help (annonce OAI 2007). Étape g : configuration `config/crash-oai-identify.json` prête, à lancer à la fin.
