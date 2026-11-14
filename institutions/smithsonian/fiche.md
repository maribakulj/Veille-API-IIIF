# Smithsonian Institution (Open Access) — `smithsonian`

- **Statut** : audit méthode v2 complet a à f ; l'API à clé n'a pas été testée avec une clé (la méthode interdit d'en demander une) ; étape g préparée (crash test à la fin, C15).
- **Pays** : États-Unis (GLAM-032)
- **Hôtes** : `api.si.edu` (API Open Access), `edan.si.edu` (doc), `www.si.edu`, `api.data.gov` (plateforme de clés), `smithsonian-open-access.s3-us-west-2.amazonaws.com` (données en vrac), `github.com`, `registry.opendata.aws`
- **Vérifié le** : 2026-11-14 (UTC), Sonnet 5.5, lot D. Travail précédent (Haiku, 1 requête) repris : session du 2026-11-13T21:07:54Z archivée verbatim dans `tests/archive/journal-sessions-avant-config-committee.log` (configuration committée après le lancement) et **rejouée** en passe 1 avec une configuration committée avant.

## Sources (étapes a, d)

| Page | Preuve | Lecture |
|---|---|---|
| `edan.si.edu/openaccess/apidocs/` (apiDoc rendu par JavaScript) + `api_project.js`, `api_data.js` | `sources/doc/`, `sources/doc2/` | la page HTML affiche « Loading... » ; la doc réelle est dans `api_data.js` : 5 routes `GET /api/v1.0/{search, category/:cat/search, content/:id, terms/:category, stats}` sur `https://api.si.edu/openaccess`, paramètre `api_key` obligatoire ; « The Open Access API requires an API key to access the endpoints. Please register with https://api.data.gov/signup/ » ; **aucun quota** |
| `edan.si.edu/openaccess/docs/` | `sources/doc/` | « The API is open and all that we require is that you get a key » ; contact `openaccess@si.edu` ; aucune limite chiffrée |
| `api.data.gov/docs/developer-manual/` | `sources/doc/` | « Hourly Limit: 1,000 requests per hour » (défaut, « may vary by service ») ; DEMO_KEY « 30 requests per IP address per hour », « 50 requests per IP address per day » ; en-têtes `X-RateLimit-Limit`, `X-RateLimit-Remaining` « returned on every API response » ; dépassement : clé « temporarily blocked », levée « by waiting an hour » ; plus de volume : « contact the API owner at the agency » |
| `www.si.edu/openaccess/devtools`, `/termsofuse`, `/openaccess` | 403 direct ; Wayback dans `sources/wayback/` | devtools et termsofuse lues via captures de 2025 (verbatim) : aucune limite de débit ; `/openaccess` non lue (sautée) |
| GitHub `Smithsonian/OpenAccess`, registre AWS | `sources/doc/` | S3 public `s3://smithsonian-open-access`, mise à jour hebdomadaire, licence CC0, contact `openaccess@si.edu` |
| robots.txt : `edan.si.edu` **`Disallow: /`** (lu avec l'accord de Marcel, C12), `www.si.edu` (règles Drupal), `api.si.edu` 404, `api.data.gov` 404, S3 404, `github.com` 200 (Crawl-delay: 1 pour certains agents), `registry.opendata.aws` DNS non résolu | `sources/doc/`, `sources/doc3/` | lus avec les yeux ; aucun Crawl-delay applicable à notre UA |

## Endpoints (étape b)

Voir `data.json` (`endpoints_documentes`) : API Open Access (5 routes, clé requise), index S3 public, dépôt GitHub.

## Tests (étape e)

Une passe, 4 requêtes de sonde (robots.txt compris : 6 lignes au journal), `config/smithsonian-v2-passe1.json`, journal `tests/journal.log`, en-têtes `tests/raw/`.
- S3 `metadata/edan/index.txt` : **200**, aucun en-tête de limite (`server: AmazonS3`).
- `api.si.edu/openaccess/api/v1.0/stats` **sans clé** : **403** JSON `API_KEY_MISSING` (« No api_key was supplied. Get one at https://api.si.edu:443 »), en-têtes sans `X-RateLimit-*` ; `x-api-umbrella-request-id` (passerelle api.data.gov). La sonde l'a classé 403 anti-bot et a arrêté l'hôte : `search` et `terms` n'ont pas été lancés. Ce 403 est un refus faute de clé, **pas un quota** ni un blocage de notre client.
- Aucun 429.

## Web (étape f)

Quatre recherches (14/11/2026). **institution** : conditions d'usage (Wayback), rien sur les limites. **présentations** : billet de lancement 2020 (Wayback) : API « hosted on data.gov », aucune limite. **utilisateurs** et **tickets** : aucun résultat ; un article tiers lu (dev.to) dit seulement « The Smithsonian requires a free API key from api.data.gov ».

## Conclusion

Le Smithsonian ne publie aucun quota. Le quota applicable vient de la plateforme api.data.gov (1 000 requêtes/heure par clé, DEMO_KEY 30/h et 50/jour par IP, en-têtes `X-RateLimit-*` sur chaque réponse, 429 au dépassement) : **documenté par la plateforme, non vérifié** pour le Smithsonian car aucune clé n'a été utilisée. Accès sans clé : refus 403 `API_KEY_MISSING`. Données en vrac : S3 public sans limite écrite. Contact : `openaccess@si.edu`. Confiance moyenne. Étape g : `config/crash-s3-index.json`.
