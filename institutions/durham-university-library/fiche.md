# Durham University Library — `durham-university-library`

- **Statut** : audit méthode v2 complet à l'exception de l'étape g (crash test, à la fin ; configuration prête : `config/crash-info-json.json`)
- **Hôtes** : `iiif.durham.ac.uk` (IIIF, Apache), `libguides.durham.ac.uk` (guide), `n2t.durham.ac.uk` puis `reed.dur.ac.uk` (METS), `collections.durham.ac.uk` (Omeka S), `www.durham.ac.uk` (**403 CloudFront**)
- **Vérifié le** : 2026-11-14 (UTC)

## Sources
| Source | Preuve |
|---|---|
| Guide « Digitised Collections Online » (IIIF, Mirador, partage et réemploi, takedown) | `sources/doc/raw/02.html`, `sources/guide/` |
| robots.txt de `iiif.durham.ac.uk` : **« User-agent: * / Disallow: / »** (même contenu en 2025 via Wayback) | `sources/doc/raw/03.html`, `sources/wayback/iiif-durham-robots.md` |
| robots.txt de libguides, collections (404), n2t (404), reed, durhampriory | `sources/doc/`, `sources/collections/`, `sources/guide/`, `sources/reed/` |
| `www.durham.ac.uk/robots.txt` : **403** en direct ; lu via Wayback (+ Publishing Images, PSI) | `sources/doc/raw/05.html`, `sources/wayback/` |
| Billet du projet Priory, wiki Samvera | `sources/doc/raw/06.html`, `07.html` |

Aucune page ne publie de quota, de limite de débit ni de politique de moissonnage. Le guide dit : « We currently implement version 2 of the image and presentation apis for images only. »

## Tests
Cinq passes (`config/durham-passe1…5`), journal `tests/journal.log`, en-têtes `tests/raw/`. Le Disallow / de robots.txt est journalisé à chaque requête ; les tests sont lancés avec l'accord de Marcel (C12).
- Manifeste d'exemple du wiki Samvera (`/manifests/dul/clb/clb1-94.json`) : **404** (réponse réelle).
- Index de collection (41 724 o, 93 sous-collections), sous-collection Sudan Archive (16 407 o) : 200.
- `info.json` et vignette de l'Image API : 200. Manifeste d'objet `/manifests/trifle/32150/…/manifest` (4 306 o) : 200. Visionneuse `mview.html` et `jalava/` : 200.
- METS : `n2t.durham.ac.uk` → 302 vers `reed.dur.ac.uk` → 302 https → 200.
- **Aucun en-tête de limite**, aucun 429 (20 requêtes, hors lectures de robots.txt).
- Non testés : Discover (Primo, pas d'API documentée), `www.durham.ac.uk` (403 CloudFront : refus d'accès à notre client, pas un quota).

## Web
- institution : guide (v2 image et presentation), politique PSI via Wayback (réemploi facilité, rien sur le débit).
- utilisateurs : aucun résultat (résumé de moteur, non vérifié).
- tickets : aucun résultat.
- presentations : billet du projet Priory (IIIF « as open and usable as possible »), rien sur les quotas.

## Conclusion
Pas de quota publié, aucun mécanisme de limitation observé. Seule règle écrite : `Disallow: /` dans le robots.txt de l'hôte IIIF, alors que la doc invite au réemploi des images en IIIF : contradiction non expliquée par Durham (pourquoi pas publié : hypothèse, robots.txt par défaut du serveur Apache ; non confirmé). À contacter : main.library@durham.ac.uk. Le site `www.durham.ac.uk` est derrière CloudFront (403) : URL à vérifier à la main.

## Crash test (étape g)

Crash test fait le 2026-11-14 : info-json-iiif-durham sur iiif.durham.ac.uk : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/durham-university-library.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
