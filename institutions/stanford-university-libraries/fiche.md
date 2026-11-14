# Stanford University Libraries (`stanford-university-libraries`)

- **Classeur** : GLAM-039 · États-Unis · **Audit v2 le** 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `purl.stanford.edu` (manifestes, XML, MODS), `stacks.stanford.edu` (images IIIF, fichiers), `embed.stanford.edu` (oEmbed), `library-hours.stanford.edu` (heures), `api.library.stanford.edu` (doc).

## Sources
Doc officielle : `api.library.stanford.edu/docs/{iiif,purl,digital-stacks,embed,library-hours}/api/` (sources/api-*), page `library.stanford.edu/iiif`, politiques (`/general-policies`, `/copyright-notice`, `stanford.edu/site/terms/`) dans sources/b et c, README GitHub de `sul-dlss/stacks` et `purl` (sources/a), billet SDR (sources/e). Aucune mention de quota, limite de débit, clé ou compte dans ces pages. Termes d'usage : « User may download material from the Sites only for User's own personal, non-commercial use » (sites).
robots.txt : purl et stacks libres ; `embed.stanford.edu` et `library-hours.stanford.edu` : `Disallow: /` (testés avec l'autorisation C12) ; `library.stanford.edu` : `crawl-delay: 30` (site, non sondé) ; searchworks : Crawl-delay 60 pour quelques robots nommés seulement.
Note : `fetch_doc.sh` a classé `api.library.stanford.edu` en « défi » à tort (le mot reCAPTCHA du formulaire de retour) ; pages récupérées une par une.

## Tests (2 passes, 16 requêtes au total, configs committées avant lancement, pauses 6 s)
Passe 1 : PURL manifeste v2 (722 ko), v3, XML, MODS, page, stacks `info.json`, dérivée 200 px, HEAD fichier, HEAD archive : **200** ×9. Passe 2 : oEmbed et iframe, Library Hours (3 URL) : **200** ×5. Aucun 403, 429, CAPTCHA ; aucun en-tête `RateLimit-*` ni `Retry-After` (journal : « aucun en-tête de limite »).

## Web (4 catégories, 5 recherches)
Institution : billet SDR 2024 (crawling des PURL ouvert), aucune politique de bots. Utilisateurs : aucun résultat. Tickets : allmaps#689 (erreur navPlace d'un manifeste Stanford, sans lien avec un quota). Présentations : aucun résultat.

## Conclusion
Limite chiffrée : aucune publiée ; rien observé en 16 requêtes. Pourquoi pas publiée : pas de raison trouvée (hypothèse : les services reposent sur Cantaloupe et l'infrastructure du campus, sans politique écrite). Confiance : moyenne. À faire hors audit : demander par le formulaire de contact s'il existe une limite non publiée. Crash test (g) : configuration `config/crash-stacks-info.json` prête, non lancée.
