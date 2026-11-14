# Harvard Library — `harvard`

- **Statut** : audit v2 a–f complet ; g (crash test) à faire en fin de boucle
- **Vérifié le** : 2026-11-14 · **Vérifié par** : agent de veille (Claude Sonnet 5.5, lot E)
- L'ancienne fiche (passe Haiku du 2026-11-13) est remplacée ; son journal (requêtes de 21:05-21:07 UTC, configuration committée après) est archivé verbatim dans `tests/archive/` et rejoué en 4 passes.

## 1. Sources (documentation lue)
Fichiers : `sources/a1` à `a4` (HTML brut, texte extrait, `text-adf/` = texte intégral des pages wiki Atlassian, dont le corps est dans du JSON), `sources/wayback/`, `sources/web/`.
- **Wiki LTS « LibraryCloud APIs »** (officielle, lue en entier) : « The LibraryCloud API is limited to an average of 300 requests per 5 minutes; if, after 5 minutes, that limit is exceeded, the client will receive a 5 minute timeout before they can resume requests. Please limit your requests to no more once per second. » `limit` ≤ 250, pagination ≤ 100 000. Contact : LTS Support.
- **Wiki « MPS Delivery API »** : NRS (`nrs.harvard.edu/URN-3:…:MANIFEST[:2|:3]`, `:THUMBNAIL`, `:IMAGE/info.json`), API de résolution `nrs.harvard.edu/api/resolve/<URN>`, proxy « causes additional load on the Name Resolution Service (NRS), does not provide performance guarantees ». MPS a remplacé les anciens services d'image et de pages en 2025. Taille de livraison par défaut 5 000 px.
- **Wiki « LibraryCloud OAI-PMH Data Provider »** : `api.lib.harvard.edu/oai` (10 résultats par page, resumptionToken).
- library.harvard.edu : pages IIIF et jeux de données (métadonnées CC0, « Community Norms », aucune limite de débit) ; iiif.harvard.edu : exemple IDS `ids.lib.harvard.edu/ids/iiif/25286607/…`.
- enterprisearchitecture.harvard.edu : 403 Akamai, non contourné ; lu via Wayback (document HUIT générique de 2020, sans chiffre).
- robots.txt par hôte : voir `data.json` `hotes_robots` (nrs : `Disallow: /` ; api, iiif.lib, ids, iiif.harvard.edu : 404 ; mps et viewer : 202 vide = défi AWS WAF ; wiki Atlassian : Crawl-delay 1).
- Étape d : endpoint de statut de quota : aucun ; en-têtes de limite documentés : aucun ; clé : aucune pour LibraryCloud public ; contact : LTS Support.

## 2. Tests (voir `tests/journal.log`, `tests/raw/`)
- Passe 1, LibraryCloud (8 requêtes + robots) : Items (XML et JSON), Collections, `collections/2/items`, OAI Identify, ListSets, ListMetadataFormats, GetRecord : tous 200, 6 s d'intervalle.
- Passe 2, NRS/IDS/viewer (7 + robots) : manifestes et vignette NRS en 303 vers mps.lib.harvard.edu ; `api/resolve` 200 ; ids.lib : info.json 302 vers MPS, image 500 px 200 ; viewer.lib : 202 vide, `x-amzn-waf-action: challenge` (défi, arrêt).
- Passe 3, MPS (4) : manifestes IIIF 3 et 2, info.json, vignette : 200.
- Passe 4, compléments (3) : proxy NRS 200, OAI ListIdentifiers 200, `collections/2/` 500 (la doc le dit « currently unavailable »).
- Aucun 429, aucun `Retry-After`/`X-RateLimit-*`. Réponses LibraryCloud derrière `istio-envoy`. L'en-tête `x-mps-client-ip` de MPS renvoie l'IP de Marcel : redigée dans les fichiers du dépôt.

## 3. Web (f)
Voir `sources/web/recherches-web-2026-11-14.md` : limite officielle trouvée dans le wiki ; talk code4lib 2023 de l'équipe LTS (sans limite) ; aucune plainte d'utilisateur ni ticket d'outil tiers trouvés.

## 4. Conclusion
- Limite documentée : LibraryCloud 300 req / 5 min (60 req/min), timeout de 5 min ; services IIIF : aucune limite publiée.
- Limite observée : non (aucun 429 à 6 s d'intervalle, donc 10 req/min).
- Les réponses n'annoncent pas la limite (aucun en-tête de débit).
- Pourquoi les services IIIF n'ont pas de limite publiée : non trouvé ; hypothèse (étiquetée) : gestion par le WAF AWS (défi) plutôt que par quotas annoncés.
- Confiance : moyenne. Crash test (g) : `config/crash-librarycloud-items.json` prêt (limite documentée 60 req/min, plafond 2×).

## Crash test (étape g)

Crash test fait le 2026-11-14 : lc-items-q-peanuts sur api.lib.harvard.edu : aucun blocage jusqu'à 120 req/min (plafond 120 req/min).
Journal : `tests/crash/harvard.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
