# Victoria and Albert Museum (`victoria-and-albert-museum`)

- **Classeur de référence** : GLAM-010 · **Pays** : Royaume-Uni
- **Hôtes** : `api.vam.ac.uk` (API Collections v2), `framemark.vam.ac.uk` (images IIIF), `iiif.vam.ac.uk` (manifestes), `developers.vam.ac.uk` (doc), `www.vam.ac.uk`
- **Vérifié le** : 2026-11-13, par Sonnet 5.5
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **Conditions des sites web du V&A, section 9 « Terms of use for V&A APIs »** (PDF juin 2024 ; identique dans la version de juin 2022, relu) :
  - « We wish to provide access to the API with as few barriers as possible. However, we **reserve the right to require the use of API keys**, or some other form of authentication in the future. »
  - Section 9.2 « Best practice » (« Although **not formally part of the terms and conditions** ») : « As a guideline, you should make **no more than 3,000 API calls per day at a rate of no more frequently than one request per second**. The V&A may choose to limit the number of API calls more formally in the future. »
  - Section 9.3 (conditions) : ne pas conserver le contenu de l'API plus de **quatre semaines** ; utiliser l'URL d'image renvoyée par l'API plutôt qu'en faire une copie ; usage non commercial personnel et éducatif, l'usage commercial passe par `vaimages@vam.ac.uk`.
- **`www.vam.ac.uk/robots.txt`** : `User-agent: *`, nombreux `Disallow` (dont `/*q=*`, `/*page=`), **`Crawl-delay: 2`**. Les hôtes `api.vam.ac.uk` et `framemark.vam.ac.uk` n'ont pas de `robots.txt` (404).
- **OpenAPI** (`api.vam.ac.uk/openapi.json`, 12 chemins) : ne déclare que les réponses 200 et 422 ; **aucun 429, aucun en-tête de limite**.
- Le guide documente les endpoints, la vignette 100×100, l'`info.json` et le manifeste `iiif.vam.ac.uk/collections/{id}/manifest.json`.

## Tests (2 passes, configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `objects/search?q=Etruria&page_size=1`, `object/O828146`, `objects/clusters/search`, `sayt/search` | **200** ×4 |
| 1 | `iiif.vam.ac.uk/collections/O9138/manifest.json` (exemple du guide) | **200**, 95 ko |
| 2 | `framemark…/2016JF9061/info.json`, vignette 100×100, `full/full` | **200** ×3 ; `full/full` mesuré **2 500 × 1 597** |

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`. Nos requêtes sont espacées de 6 s, bien au-delà de l'indicatif d'une par seconde.

## Rattrapage du 2026-11-14
- Lus : guide `welcome.html` (licence : section 9.3 des conditions), page `www.vam.ac.uk/api` (aucune URL de l'API de 2009), page `articles/terms-of-use`, billets « IIIF at the V&A » et « V&A MCP Server » (aucune limite de débit). `iiif.vam.ac.uk/robots.txt` : 404 ; hôte S3 des PDF : 403 AccessDenied (pas de robots.txt lisible).
- Passe 3 : `www.vam.ac.uk/blog/wp-json/wp/v2/posts/67662` : **200**, aucun en-tête de limite. Service MCP (`mcp.vam.ac.uk/mcp/`) non testé : protocole par POST.

## Web

- Billet de lancement de l'API (blog du V&A, lu) : décrit les nouveautés, aucune limite.
- Une recherche sur les bots et l'IA n'a trouvé **aucune publication du V&A** sur le sujet.
- Correction d'un résumé de recherche : il affirmait que la règle de 2022 était « plus souple » ; **le texte de 2022 contient les mêmes chiffres** (3 000 par jour, un par seconde).

## Conclusion

- **Limite documentée chiffrée** : 3 000 appels par jour et un appel par seconde, à titre **indicatif** (hors conditions formelles) ; `Crawl-delay: 2` sur le site.
- **Limite observée** : non. **En-têtes de limite** : aucun.
- **Réserve annoncée** : clés d'API ou limitation formelle possibles à l'avenir.
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : élevée pour la règle écrite, moyenne pour l'application réelle.
