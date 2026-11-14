# Folger Shakespeare Library (`folger-shakespeare-library`)

- **Classeur** : GLAM-057 · États-Unis · audit v2 du 2026-11-14 · suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `www.folger.edu` (site, textes numériques), `digitalcollections.folger.edu` (collections numériques, héritière de la plateforme Miranda / `collections.folger.edu`), `catalog.folger.edu` (catalogue TIND), `luna.folger.edu` et `hamnet.folger.edu` (anciens systèmes, redirections), `flgr.sh` (liens courts vers les téléchargements, Cloudflare), `folger-main-site-assets.s3.amazonaws.com` (fichiers).

## Sources (étape a)
- Conditions d'usage `www.folger.edu/terms-of-use/` : aucune règle sur les robots ni le débit ; contact `webmaster@folger.edu` (`sources/a2`).
- Politique de droit d'auteur : contenu sous CC BY-SA 4.0 sauf mention ; Folger Digital Texts en CC BY-NC 3.0 ; pages « Images and permissions » : pas de frais pour le domaine public/CC0.
- Billets « Enter Miranda » (2017) : annoncent des « API services » ; « And that's IIIF to you, too » (2019) : manifestes IIIF accessibles depuis les boutons Mirador, sans URL ni limite. Le portail développeurs `wiki.folger.edu` n'a plus de DNS : lu dans Wayback (`sources/wayback/wiki-miranda.md`) ; il décrit une API GraphQL, Cantaloupe pour IIIF, aucune limite.
- `robots.txt` : `www.folger.edu` `Disallow: /admin/*` ; `catalog.folger.edu` **Crawl-delay 5**, `Disallow: /search` ; `digitalcollections.folger.edu` (liste « bad bots » de 1 400 lignes, groupe `*` avec **Crawl-delay 120** et règles Drupal) ; `luna.folger.edu`, `hamnet.folger.edu`, `flgr.sh` (signaux Cloudflare Content-Signal, `ai-train=no`, ClaudeBot/GPTBot interdits, notre UA non nommé) ; `findingaids.folger.edu` : 403 (défi Cloudflare) ; bucket S3 : 403 AccessDenied ; `collections.folger.edu` et `wiki.folger.edu` : pas de DNS.

## Tests (étape e, 1 passe, 14 requêtes, configuration committée avant lancement)
- `digitalcollections.folger.edu/` : 302 vers `/turnstile-challenge` puis page « Verifying Connection » (Cloudflare Turnstile) : **défi, aucun contournement** ; hôte arrêté.
- `catalog.folger.edu/` : **202 vide avec `x-amzn-waf-action: challenge`** (défi AWS WAF) ; arrêté.
- `luna.folger.edu/luna/servlet/s/r5941p` : 301 vers `digitalcollections.folger.edu/img9150` (non suivi, hôte défié).
- `flgr.sh/txtfssHamxml` (HEAD) : 301 vers un fichier zip S3 (non suivi) ; `www.folger.edu/.../download/` (HEAD) : 200 ; `hamnet` : 301 vers HTTPS puis 301 vers `catalog.folger.edu`.
- Aucun 429, aucun en-tête de limite (`Retry-After`, `X-RateLimit-*`, `RateLimit-*`).

## Web (étape f, 4 recherches, une par catégorie)
Aucune plainte, aucun ticket d'outil tiers, aucune présentation avec chiffre de quota trouvés ; présentations de l'institution : wiki Miranda et billets (sans limite).

## Conclusion
Aucun quota ni limite de débit publiés. Seuls signaux : Crawl-delay 5 s (catalogue) et 120 s (collections numériques) dans les robots.txt, et des défis anti-bot (Turnstile, AWS WAF) sur les collections numériques et le catalogue, ce qui n'est pas un quota. Aucune URL de manifeste IIIF n'est documentée ; la plateforme d'origine (`collections.folger.edu`) a disparu. Confiance : moyenne (hôtes principaux non lisibles par la sonde, à vérifier à la main).
