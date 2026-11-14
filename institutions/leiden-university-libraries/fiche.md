# Leiden University Libraries (`leiden-university-libraries`)

- **Classeur** : GLAM-015 · Pays-Bas · **Vérifié le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Chaîne d'hôtes réellement servie** : `digitalcollections.universiteitleiden.nl` (301) → `iiif-endpoint.universiteitleiden.nl` (302) → `catalogue.leidenuniv.nl` (Primo, manifeste IIIF 3) → images sur `eu-img02.ext.exlibrisgroup.com` (Ex Libris, IIIF Image 2 niveau 2).

## Sources
- `digitalcollections…/robots.txt` : **`Crawl-delay: 10`** ; Disallow sur des chemins Drupal (`/admin/`, `/search/`, `/user/`…), pas sur `/iiif_manifest/`.
- `catalogue.leidenuniv.nl/robots.txt` : `Crawl-delay: 10` ; Disallow `/primaws`, `/discovery/search`, `/nde/search` ; GPTBot, Applebot, Yandex bloqués.
- `iiif-endpoint…/robots.txt` : 404 (autorisé). `eu-img02…/robots.txt` : 403 « Missing Authentication Token » (route absente d'une passerelle AWS, pas un anti-bot).
- Page « Terms of use » (reproductions, collections spéciales) : licence indiquée dans chaque notice ; images non protégées réutilisables en CC-BY ; **aucune règle d'API, aucun quota**. L'identifiant d'exemple `item:1520785` vient d'une page publique de Biblissima (tiers).
- Aucune documentation d'API ni de page de conditions d'usage IIIF trouvée sur les domaines de Leiden.

## Tests (4 passes, configs committées avant lancement, pauses de 10 s)
| Passe | Requête | Résultat |
|---|---|---|
| 1 | manifeste `digitalcollections…/iiif_manifest/item:1520785/manifest` | 301 vers iiif-endpoint |
| 2 | idem sur `iiif-endpoint…` | 302 vers Primo |
| 3 | manifeste Primo `iiifVersion=3` | **200**, 1,9 Mo, 729 canevas, `rights` = Public Domain Mark |
| 4 | `info.json` et dérivé 200 px sur Ex Libris | **200** ×2 (5 300 octets) |

Aucun 429, aucun en-tête de limite (en-têtes `x-amzn-*`, `x-cache`, CloudFront seulement).

## Web
Aucune politique de débit ou de bots propre à Leiden. Un ticket tiers (mnemosyne#4) rapporte un site HTML derrière un défi anti-bot (non observé : page d'accueil en 200 pour nous). Aucun test de masse : la limite éventuelle est celle d'Ex Libris/CloudFront, non publiée.

## Conclusion
Limite chiffrée : seulement `Crawl-delay: 10` (robots.txt). Pas de limite observée. Confiance : moyenne. Crash test (g) : plafond 200/min mais **prudence : la limite éventuelle appartient à Ex Libris**, donc une décision de Marcel est utile avant.

## Rattrapage du 2026-11-14
- Doc IIIF de Leiden (`lab.library.universiteitleiden.nl/iiif-docs`, 7 pages) lue : Image API 2.1 (base `/iiif/2`) et Presentation API 2.1 (`/manifests`), conditions d'usage = brouillon sans règle de débit. `robots.txt` : lab 404, `library.` 200 (pas de Crawl-delay), `www.library.` et `iiif.universiteitleiden.nl` : connexion coupée par le serveur (non contourné).
- Passe 5 : `lab…/manifests` 301 puis 200, `manifests/collection.json` **200**, aucun en-tête de limite, aucun 429. `iiif.universiteitleiden.nl/iiif/2` non testé (connexion coupée, arrêt de l'hôte) : à vérifier depuis un navigateur.
