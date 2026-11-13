# Bodleian Libraries (Digital Bodleian) — `bodleian`

- **Statut** : audit méthode v2 complet à l'exception de l'étape g (crash test, après l'audit de toutes les institutions)
- **Pays** : Royaume-Uni (GLAM-002 du classeur de référence)
- **Hôtes** : `digital.bodleian.ox.ac.uk` (site, API de données), `iiif.bodleian.ox.ac.uk` (IIIF)
- **Vérifié le** : 2026-11-13 (UTC), par Sonnet 5.5, passe v2
- **Passe précédente** (Haiku, ancienne méthode) : archivée dans l'historique Git

## a) Documentation lue

| Page | Fichier de preuve | Lecture |
|---|---|---|
| `digital.bodleian.ox.ac.uk/developer/`, `/developer/iiif/`, `/developer/data/`, `/terms/`, `/faq/` | `sources/bodleian/` (`SHA256SUMS`, `FETCH.log`, `text/`) | texte extrait en entier, lu |
| `digital.bodleian.ox.ac.uk/robots.txt` | `sources/bodleian/suite/` | 200 |
| `iiif.bodleian.ox.ac.uk/robots.txt` | `sources/bodleian/suite/` | **400** (« Bad request ») |
| Billet du blog, 2026-10-01 | `sources/bodleian/blog-ia/` | lu en entier |
| Politique IA des Bodleian Libraries (PDF) | `sources/bodleian/poster/bodleian-ai-policy.pdf` | texte extrait, 2 277 mots, lu |
| Poster LIBER 2025 (PDF image) | `sources/bodleian/poster/liber2025.pdf` | **lu visuellement** (pas de couche texte) |

## b) Endpoints tirés de la doc

Manifestes (`/iiif/manifest/{uuid}.json`), canvases, annotations, images (`/iiif/image/{id}/info.json`, `{region}/{size}/{rotation}/{quality}.{format}`), collections (`/iiif/collection/top|all|{id}`), flux d'activité (`/iiif/activity/*`), racine (`/` → 303 vers `/info.json`). API de données : `/search`, `/collections/<nom>/`, `/partners/<nom>/`, `/objects/{id}`. **`/account/*` exige une authentification (401)** : non testé.

## c) Configuration

`scripts/config/bodleian.json` (12 entrées), écrite avant la passe v2.

## d) Quota dans la doc

- **Aucun quota chiffré.** Aucun nom d'en-tête de limite. Aucune clé (hors `/account`).
- Doc IIIF : « You are welcome to harvest our manifests for the purposes of indexing or making our content available in aggregator services. However, if are expecting to harvest a significant number of manifests, we would ask that you get in touch with us and let us know. »
- Conditions : section « Prohibited use » : interdiction de l'**usage commercial** des images (CC BY-NC 4.0, plafond de 3 000 exemplaires pour les publications académiques). Ce n'est pas une règle de débit.
- Politique IA : « we may apply technical, contractual or other measures to manage these risks while preserving legitimate research and educational use of collections » (portant sur « AI-enabled web crawling »).
- `robots.txt` du site : `User-agent: *`, `Disallow` sur `/register/*`, `/logout/`, `/password/`, `/build/`, `/derivatives/` ; **pas de `Crawl-delay`**.
- Contact pour un moissonnage important : `digital-bodleian@bodleian.ox.ac.uk` (page `developer/iiif`).

## e) Tests (passe v2)

12 requêtes, 2026-11-13 22:03:18 → 22:04:09 UTC, pauses ≥ 6 s, UA du projet : `tests/bodleian.log` (session du 22:03:18Z), en-têtes bruts dans `tests/raw/bodleian/`. **Aucun 403, aucun 429, aucun en-tête `Retry-After` / `X-RateLimit-*` / `RateLimit-*`.** Les 301 et 303 ne sont pas suivis.

## f) Ce que disent les gens et l'institution sur le web

| Source | Date | Étiquette | Contenu (texte exact) |
|---|---|---|---|
| Poster LIBER 2025, « Open scholarship vs AI », Bodleian Libraries (3 auteures) — `sources/bodleian/poster/liber2025.pdf` | 2025-07 | **institution** | « Our websites are grinding to a halt » ; « Web scraping is bringing our websites to a crawl » ; « Companies & scrapers are ignoring robots.txt » ; « How do we limit bots without losing human users? ». Le poster dit « our websites » et « our repositories », sans nommer Digital Bodleian. |
| Billet du blog Digital and Scholarly Resources, 2026-10-01 — `sources/bodleian/blog-ia/` | 2026-10-01 | **institution** | « avoiding the unrestricted, unannounced harvesting that has caused problems for the repository in the past. (This includes AI bots that ignore normal usage limits.) » ; « Because the Bodleian Libraries chose to have this conversation rather than simply blocking large-scale access outright… ». **Portée : le dépôt ORA (Oxford Research Archive)**, pas Digital Bodleian. |
| Politique IA des Bodleian Libraries (PDF) — `sources/bodleian/poster/bodleian-ai-policy.pdf` | 2026 (Michaelmas) | **institution** | Voir d) : mesures « technical, contractual or other measures » envisagées contre le crawling par IA. |
| Fil iiif-discuss « Crawler Etiquette – a request » (`groups.google.com/g/iiif-discuss/c/Z3GVdj6s61w`) | 2017-11-13 | **institution (message de l'équipe Digital Bodleian)**, ancien | Extraits (outil de lecture, lecture limitée à de courts extraits) : demande d'un contact dans le User-Agent ; « even a 500ms delay between requests would help moderate traffic » ; préférence pour un blocage temporaire ; « We would like to avoid automated throttling of our connections if at all possible ». Une réponse invite à respecter `Crawl-Delay`, 429 et `Retry-After` (aucune valeur). Message non relu en entier. |

## g) Crash test

À faire après l'audit de toutes les institutions (METHODOLOGY.md, étape g). Plafond : **200 req/min** si la limite est annoncée illimitée ou absente (c'est le cas ici). Précaution : la Bodleian dit explicitement ne pas vouloir de throttling automatique et préférer un blocage temporaire.

## Conclusion

- **Limite documentée chiffrée** : non.
- **Limite observée** : non (aucun 429, aucun en-tête).
- **403 anti-bot** : non.
- **Règle explicite** : prévenir avant un moissonnage important de manifestes.
- **Contexte** : la Bodleian déclare publiquement subir un scraping qui dégrade ses sites et ignore `robots.txt`, et envisage des mesures techniques. Ce n'est pas un quota publié, mais un risque de blocage ou de limitation future non annoncée.
- **Moyen d'interroger le quota** : aucun (ni endpoint, ni en-tête, ni compte).
- **Confiance** : moyenne à élevée pour l'absence de quota publié (pages lues en entier, 12 requêtes) ; faible pour l'absence de limite réelle côté serveur.
