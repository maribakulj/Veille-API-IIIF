# Blavatnik Archive — `blavatnik-archive`

- **Statut** : audit v2 a à f ; g préparée (configuration crash, à lancer par le coordinateur)
- **Pays** : États-Unis (GLAM-061) · **Hôtes** : `www.blavatnikarchive.org` (site, derrière Cloudflare), `iiiflb.blavatnikarchive.org` (IIIF Image API 3, Cantaloupe 5.0.7)
- **Vérifié le** : 2026-11-14 (UTC)

## Sources

- `www.blavatnikarchive.org/robots.txt` (200) : `User-agent: *`, `Content-Signal: search=yes,ai-train=no,use=reference`, `Allow: /` ; liste de robots d'entraînement d'IA en `Disallow: /` (ClaudeBot, GPTBot, CCBot…) ; notre User-Agent n'est pas visé ; pas de Crawl-delay. Preuve : `sources/doc/raw/01.html`.
- `iiiflb.blavatnikarchive.org/robots.txt` : 404 (erreur Cantaloupe « No route for path »), tout autorisé. `sources/doc2/raw/04.html`.
- Pages du site lues : `/collections`, `/more/about`, `/more/contact`, `/more/programs`, `/collection/periodicals`. **Aucune page de documentation d'API, de conditions d'usage ni de politique de débit.** Contact pour usage : formulaire « For research, usage or other requests » (`sources/doc2/text/02.txt`).
- Guide IIIF du consortium (`guides.iiif.io/guides/blavatnikarchive.org/`) : renvoie seulement à `/collections` (`sources/doc/text/03.txt`).
- Les pages portent le message d'interface « This record has a IIIF manifest » ; l'URL du manifeste n'apparaît nulle part dans les pages lues.

## Tests (passe 1, 3 requêtes de test + robots.txt)

`config/passe1.json` (committée avant), identifiants pris dans la page de collection lue. 5 requêtes au total (dont 2 robots.txt), 2026-11-14 02:37:41 → 02:38:11Z : page d'item `/item/24496` 200 ; `info.json` IIIF 3 (profil level2, 200) ; dérivé `full/^!200,200/0/default.jpg` 200. **Aucun 403, aucun 429, aucun en-tête de limite** (`tests/raw/`).

## Web

Officielle : aucune politique d'API/bots trouvée hors robots.txt. Présentations, tickets, utilisateurs : aucun résultat (moteur, non vérifié).

## Conclusion

- **Limite documentée** : aucune. **Limite observée** : non (3 requêtes).
- **Règle** : robots.txt interdit l'entraînement d'IA (signal `ai-train=no`).
- **Étape g** : configuration `config/crash-image-info.json` prête ; non lancée (interdit à l'agent). Site derrière Cloudflare, `iiiflb` sans réseau détecté dans les en-têtes (nginx).

## Crash test (étape g)

Crash test fait le 2026-11-14 : crash-image-info sur iiiflb.blavatnikarchive.org : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/blavatnik-archive.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
