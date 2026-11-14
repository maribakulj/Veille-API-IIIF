# University of St Andrews Library (University Collections) — `university-of-st-andrews-library`

- **Statut** : audit méthode v2 complet à l'exception de l'étape g (crash test, à la fin ; configuration prête : `config/crash-info-json.json`)
- **Hôtes** : `collections.st-andrews.ac.uk` (base Collections, manifestes et Image API, Cantaloupe), `www.st-andrews.ac.uk`, `exhibit.st-andrews.ac.uk` (Exhibit), `eprints.st-andrews.ac.uk` (DNS introuvable)
- **Vérifié le** : 2026-11-14 (UTC)

## Sources
| Source | Preuve |
|---|---|
| robots.txt de `collections.st-andrews.ac.uk` : **« User-agent: * / Disallow: / »** ; de `www` : **Crawl-delay 10** | `sources/doc/raw/01.html`, `03.html` |
| Pages `/collections/about` et aide « Find and research materials » : la page live renvoie l'accueil des collections ; texte lu via Wayback | `sources/doc/`, `sources/wayback/collections-about.md` |
| Digitisation service, terms and conditions (Wayback) | `sources/wayback/` |
| Doc Exhibit, robots.txt Exhibit et blog des musées, définition de service « Digital reproductions » | `sources/exhibit/` |
| `eprints.st-andrews.ac.uk` : DNS introuvable | `sources/eprints/FETCH.log` |

Aucune page ne publie de quota ni de politique de moissonnage. La page « About » dit : « To re-use any of our records/images in other IIIF tools, copy the "IIIF Manifest" link found on the record pages ».

## Tests
Deux passes (`config/standrews-passe1-manifeste.json`, `passe2-images`), pause 10 s (Crawl-delay de www), journal `tests/journal.log`, en-têtes `tests/raw/`. Le `Disallow: /` est journalisé ; tests lancés avec l'accord de Marcel (C12).
- Manifeste `/77713/manifest` (6 790 o, IIIF Presentation 2) : 200. Notice de la base : 200.
- `info.json` `/iiif/2/56718~56718/` et vignette (HEAD) : 200 ; en-tête `x-powered-by: Cantaloupe/4.1.4`.
- **Aucun en-tête de limite**, aucun 429 (4 requêtes, hors robots.txt).
- Non testés : recherche (annoncée en panne, sans API documentée) et Exhibit (pas d'API de données).

## Web
- institution : « About » (Wayback), service de numérisation : réemploi IIIF encouragé, rien sur le débit.
- utilisateurs, tickets, presentations : aucun résultat (résumé de moteur, non vérifié) ; le billet « A guide to Exhibit » renvoie 410.

## Conclusion
Pas de quota publié, aucun mécanisme de limitation observé (sur 4 requêtes seulement). Seules règles écrites : `Disallow: /` sur l'hôte des collections et `Crawl-delay: 10` sur `www` ; elles contredisent l'invitation à réemployer les manifestes (pourquoi pas publié : hypothèse, robots.txt de protection contre les robots IA ; non confirmé). À contacter : unicolls@st-andrews.ac.uk.
