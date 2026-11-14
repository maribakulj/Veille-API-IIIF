# Waseda University Library — Kotenseki Sogo Database (`waseda-university-library-kotenseki`)

- **Classeur** : GLAM-078 · Japon · Audit v2 du 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `www.wul.waseda.ac.jp` (base et notices), `archive.wul.waseda.ac.jp` (images), `www.waseda.jp` (pages de la bibliothèque), `waseda.repo.nii.ac.jp` (dépôt d'articles).

## Sources (étape a)
- **Blocages du jour** : `www.wul.waseda.ac.jp`, `archive.wul.waseda.ac.jp` et `waseda.repo.nii.ac.jp` renvoient **503** (« Scheduled Maintenance » ; dépôt : maintenance JAIRO Cloud du NII depuis le 2026-10-28) ; `www.waseda.jp` renvoie **403 Cloudflare** (« Sorry, you have been blocked ») : hôte arrêté, aucun contournement (`sources/robots/`, `sources/robots-retry/`, `sources/wul/`).
- Lecture par Wayback (`sources/wayback/*.md`) : conditions d'usage (images et données bibliographiques non utilisables sans autorisation du Special Collections Office, contact `tks-info@list.waseda.jp`), robots.txt de `www.wul` (`Disallow: /opactest/j_honban/`) et de `archive.wul` (`Disallow: /*.pdf$`), notice d'exemple avec liens « IIIF Image(UV) » et « Manifest », bulletin Fumikura (2022).
- Aucun quota, aucune limite de débit, aucune page d'API publiés. Le schéma d'URL du manifeste n'est écrit dans aucune source lue : il n'a pas été deviné. robots.txt de `www.waseda.jp` non lu (403 direct ; seule capture Wayback, de 2013, contient en fait le robots.txt d'archive.org).

## Tests (1 passe, 3 requêtes, pause 6 s)
Notice d'exemple, guide du visualiseur IIIF et image : **503** (maintenance), aucun en-tête de limite. Aucun 429.

## Web (étape f)
- Institution : politique d'usage des images lue (Wayback) ; pas de politique de bots.
- Utilisateurs et tickets : aucun résultat (deux recherches).
- Présentations : bulletin Fumikura 102-3 (lu) : le projet de base date d'avril 2005 ; liens Manifest/IIIF Viewer dans la notice ; rapports annuels de la bibliothèque (résumé de moteur, non vérifié) : serveur de la base non compatible IIIF, images IIIF hébergées sur la « base de ressources culturelles ».

## Conclusion
Limite chiffrée : aucune. Règle écrite : usage soumis à autorisation. Impossible de tester l'API IIIF : maintenance du site au moment de l'audit et URL de manifeste non publiée. À refaire quand le site revient (lire le href du lien « Manifest » d'une notice). Confiance : faible. Crash test impossible.
