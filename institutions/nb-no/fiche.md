# Nasjonalbiblioteket — Bibliothèque nationale de Norvège (`nb-no`)

- **Classeur de référence** : GLAM-013 · **Pays** : Norvège
- **Hôtes** : `api.nb.no` (API Catalogue et manifestes IIIF), `www.nb.no` (site et résolveur d'images, **Crawl-delay 4 s**)
- **Vérifié le** : 2026-11-13, par Sonnet 5.5 (reprise complète de la passe de Haiku)
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **OpenAPI** (`api.nb.no/catalog/v1/items/api-docs`, 8 chemins : `search`, `musicsearch`, `items`, `items/{id}`, `items/searchafter`, `aggregations`, `relatedItems`, `contentfragments`) : les réponses déclarées sont 400, 401, 404, 500 ; **aucun 429, aucun en-tête de limite, aucune mention de débit**. Aucun chemin IIIF n'y figure.
- **`www.nb.no/robots.txt`** : `User-agent: *`, `Allow: /`, `Disallow` sur `/cgi-bin/wa`, `/archives/`, `/sok/`, `/baser/`, `/emigrasjon/`, `/gallerinor/`, `/idtjeneste/`, `/test/`, et **`Crawl-delay: 4`**. `api.nb.no` n'a pas de `robots.txt` (404).
- **IIIF** : non documenté dans l'OpenAPI ; **les réponses de l'API annoncent elles-mêmes** les liens `_links.presentation` (`…/catalog/v1/iiif/{id}/manifest`) et un résolveur d'images sur `www.nb.no/services/image/resolver/`.
- **Pages du laboratoire DH-lab** et fiche `data.norge.no` : l'API `api.nb.no/dhlab` est décrite ; l'accès « may still require registration and an API key request » (métadonnée du catalogue de données, non une règle de l'API). Contact : `dh-lab@nb.no`.
- **Aucune page de conditions d'usage de l'API** n'a été trouvée sur `nb.no` (seule la politique de confidentialité). L'ancienne page `www.nb.no/services/search/v2/` n'a pas répondu en 30 s : **non lue**.

## Tests (2 passes, configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `api.nb.no/catalog/v1/items?q=Ibsen&size=1`, `search`, `aggregations` | **200** ×3 |
| 2 | `api.nb.no/catalog/v1/iiif/{id}/manifest` (lien annoncé par l'API) | **200**, 71 ko |
| 2 | `www.nb.no/services/image/resolver/URN:NBN:…/info.json` et vignette 64 px | **200** ×2 ; pauses de 6 s au-delà du `Crawl-delay` de 4 s |

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`. Non testés : `musicsearch`, `searchafter`, `relatedItems`, `contentfragments` (paramètres non documentés par un exemple ; pas de devinette), l'API `dhlab`.

## Web

- Tickets de projets tiers (`mnemosyne#49`, `bindery#2979`) : API publique sans clé ; un connecteur s'impose lui-même 1 requête par seconde ; **aucune limite publiée par le NB**. Non officiel.
- Aucune plainte, aucune politique de bots ni de débit du NB trouvée.

## Conclusion

- **Limite documentée chiffrée** : `Crawl-delay: 4` sur `www.nb.no` uniquement (pas sur l'API).
- **Limite observée** : aucune (5 requêtes de données réussies). **En-têtes** : aucun.
- **Politique d'usage de l'API** : introuvable.
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne.

Rattrapage (2026-11-14) : session initiale archivée puis rejouée ; ancienne API de recherche www.nb.no/services/search/v2/ : timeout de 30 s à nouveau ; robots.txt de data.norge.no (Crawl-delay 1, Disallow /api/) et nationallibraryofnorway.github.io (404) lus.
