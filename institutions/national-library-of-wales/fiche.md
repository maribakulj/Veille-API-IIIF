# National Library of Wales (`national-library-of-wales`)

- **Classeur de référence** : GLAM-007 · **Pays** : Royaume-Uni (Pays de Galles)
- **Hôtes** : `iiif.llyfrgell.cymru` (manifestes et images, **nouvel hôte officiel**), `damsssl.llgc.org.uk` et `dams.llgc.org.uk` (anciens, redirigent vers le nouveau), `discover.library.wales` (catalogue), `viewer.library.wales`, `www.library.wales` (403 anti-bot)
- **Vérifié le** : 2026-11-13, par Sonnet 5.5
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **Limite de taille d'image** — page « NLW Image servers » (formation IIIF 2025 rédigée avec le personnel du NLW, « may be out of date ») : « **Images are limited to 1200 by 1200** » ; « Image limiting […] allows the server to enforce a limit for downloading the full image. It doesn't stop users from zooming into an image and its always possible to stich together the tiles ». **Confirmé par notre mesure** : une requête `full/full` renvoie un JPEG de **1200 × 1200** pixels.
- **`discover.library.wales/robots.txt`** (catalogue) : pour `*` : `Disallow` sur `/primaws`, `/discovery/search`, `/nde/search`, **`Crawl-delay: 10`** ; GPTBot, YouBot, DuckDuckBot et d'autres sont bloqués.
- **Wiki de développement du NLW** (page du 2017-04-11) : « we needed to implement caching on the indexing server to reduce stress on the IIIF server » (cache gzip de 12 Go) ; la recherche IIIF « cuts off at 100 results » ; HTTP 401 pour les images dont le NLW ne détient pas les droits.
- **Copyright** (copie Wayback 2026-10-09) : information du secteur public réutilisable (règlement britannique de 2015) ; métadonnées en CC0 ; pas de règle de débit.
- **Aucun** quota, en-tête de limite, clé ni endpoint de statut documenté.

## Accès aux pages

`www.library.wales` renvoie 403 (anti-bot) : pages lues dans la Wayback. Le PDF « Access to Collection Items Policy » n'est pas lisible : **non lu**. `viewer.library.wales/robots.txt` n'est pas un `robots.txt` (c'est la page de l'application).

## Tests (3 passes, configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `iiif.llyfrgell.cymru/manifests/2.0/6086535/manifest.json` | **200** |
| 1 | `damsssl.llgc.org.uk/iiif/…` (4 URL de la page d'atelier) et `dams.llgc.org.uk/…/fonds.json` | **302** vers `iiif.llyfrgell.cymru` |
| 2 | `iiif.llyfrgell.cymru/manifests/2.0/4389767/manifest.json` | **200**, 265 ko, domaine public |
| 2 | presse (issue, collection) et fonds d'archives, anciens identifiants | **404** (non retrouvés à la nouvelle adresse) |
| 3 | `…/iiif/4389768/info.json`, dérivé `!200,200`, `full/full` | **200** ×3 ; le plein format mesure **1200 × 1200** |
| 3 | `damsssl.llgc.org.uk/iiif/2.0/image/4527505/info.json` | **302** (ancien hôte) |

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`.

## Web

- Un développeur tiers (PR `mnemosyne` n° 25) note que l'hôte n'expose **ni collection agrégée ni endpoint de recherche** et que les journaux de presse n'ont pas de manifeste public : cohérent avec nos 404. Non officiel.
- Présentation du NLW de 2016 (200 000 manifestes, 1,1 million d'images de presse) et page de presse de 2017 (adhésion au consortium IIIF) : aucune politique de débit.
- Aucune plainte, aucune règle de moissonnage ni de bots publiée par le NLW sur ses hôtes IIIF.

## Conclusion

- **Limite documentée chiffrée** : taille d'image 1200 × 1200 (confirmée) ; `Crawl-delay: 10` sur le catalogue.
- **Limite de débit observée** : non (aucun en-tête, aucun 429 sur 11 requêtes réussies).
- **Moyen d'interroger le quota** : aucun.
- **À noter** : le NLW a **déplacé son IIIF** vers `iiif.llyfrgell.cymru` ; les adresses de la page d'atelier (2025) redirigent, et certains identifiants de presse et d'archives ne suivent plus.
- **Confiance** : moyenne.

Rattrapage (2026-11-14) : `www.library.wales/robots.txt` lu via Wayback (capture 2024-05-01) : aucun Disallow, Crawl-delay 5 ; `viewer.library.wales/robots.txt` reconfirmé comme page d'application (pas de robots.txt).
