# UBC Library Open Collections — `university-british-columbia-open-collections`

- **Classeur** : GLAM-051 · Canada · Audit v2 le 2026-11-14 (Sonnet 5.5).
- **Hôtes** : `open.library.ubc.ca` (site et doc, WAF), `oc-index.library.ubc.ca` (REST), `iiif.library.ubc.ca` (IIIF 2.0), `oce-index.library.ubc.ca` (OAI-PMH, injoignable).

## Sources
- `open.library.ubc.ca/docs` : le WAF renvoie une page de blocage (HTTP 200) ; doc lue via Wayback du 2026-02-16 (`sources/wayback/open-library-ubc-docs.md`) : « Unregistered users will be limited in the number of requests that can be made. » ; paramètre `key` : « Requests without an api key will be rate limited » ; OAI-PMH : clé API obligatoire dans l'en-tête ; IIIF 2.0 à `iiif.library.ubc.ca`. Aucun chiffre.
- `robots.txt` : iiif `Disallow:` vide ; oc-index : aucun ; open/bchistory : page de blocage WAF ; oce-index : timeout ; oce : DNS.
- Tiers (apis.io, non vérifié) : 10 req/min par IP sans clé, 200 req/min avec clé, 429 JSON nommant l'IP, pas de `Retry-After`.

## Tests (2 passes, configurations committées avant lancement, 10 requêtes, ~7 s d'écart)
REST sans clé : collection, `_total`, item, `search/help`, `search/8.5?q=cat&size=1`, `/collections`, liste paginée : **200**. IIIF : `info.json` 200 (HEAD 404), manifeste 200. Aucun 429, aucun en-tête de limite. Pas de clé demandée ni utilisée ; OAI non testé (clé exigée, hôte injoignable).

## Web
Institution : doc (Wayback). Utilisateurs/tiers : apis.io (limites chiffrées, non vérifiées). Tickets : aucun résultat. Présentations : ateliers Research Commons, dépôt GitHub de la doc.

## Conclusion
Limite documentée non chiffrée (clé gratuite par e-mail) ; chiffres tiers non confirmés ; WAF sur le site web. Confiance : moyenne. Crash test (g) à la fin : `config/crash-iiif-info.json`.
