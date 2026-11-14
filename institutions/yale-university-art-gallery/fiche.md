# Yale University Art Gallery (YUAG) — `yale-university-art-gallery`

- **Statut** : audit méthode v2 complet a à f ; étape g préparée (crash test à la fin, C15).
- **Pays** : États-Unis (GLAM-037)
- **Hôtes** : `artgallery.yale.edu` (site, **défi Cloudflare 403**), `manifests.collections.yale.edu`, `images.collections.yale.edu`, `media.collections.yale.edu` (API IIIF), `lux.collections.yale.edu`, `yaleits.atlassian.net` (wiki)
- **Vérifié le** : 2026-11-14 (UTC), Sonnet 5.5, lot D (dossier vide au départ)

## Sources (étapes a, d)

| Page | Preuve | Lecture |
|---|---|---|
| `artgallery.yale.edu/robots.txt` | 403 (« Just a moment... ») en direct, `sources/doc/FETCH.log` ; Wayback `sources/wayback/robots-artgallery.md` | l'hôte est arrêté (non contourné), les pages suivantes sautées ; robots.txt lu via la capture du 2026-05-01 : Disallow `/collection?*`, ~150 agents d'IA bloqués, pas de Crawl-delay |
| `/using-collection/using-images`, `/terms-and-conditions` | `sources/wayback/` (verbatim) | « anyone may use the Gallery’s open-access material without further application, authorization, or fees » ; « collection data is available in human- and machine-readable formats via its website and online systems » ; **aucune limite de débit, aucune API nommée** ; contact `yuagrights@yale.edu` (droits) |
| `guides.iiif.io/guides/artgallery.yale.edu/` | `sources/doc/` | fiche de répertoire du consortium IIIF, sans règle |
| Wiki ITS `yaleits.atlassian.net/wiki/x/…` (schémas d'URL) | `sources/doc4/` | **illisible** : 202 vide (JavaScript) ; listé à vérifier à la main |
| robots.txt des hôtes API : `manifests`, `images`, `media.collections.yale.edu`, `media.artgallery.yale.edu` tous **404** ; `lux.collections.yale.edu` 200 (Disallow `/view/results/`) | `sources/doc/`, `sources/doc2/`, `sources/doc3/` | lus avec les yeux : aucun Crawl-delay |

## Endpoints (étape b)

Aucune doc de la Gallery ne décrit les API. Les adresses viennent de pages publiques : le manifeste v3 `manifests.collections.yale.edu/yuag/obj/{id}` (id 31719 cité par des résultats de recherche publics), les services d'image (`images.collections.yale.edu/iiif/2/yuag:{uuid}`), la variante `/v2/` documentée par le guide « Finding Yale manuscripts » (training.iiif.io, lu). Détail : `data.json`.

## Tests (étape e)

3 passes, 11 requêtes de sonde robots.txt compris (2 + 6 + 2 + …, voir journal), configurations committées avant lancement (`config/yuag-passe1…3`).
- Manifeste v3 (247 ko) et v2 : **200**. `info.json` et image 150 px (Cantaloupe 4.1.9, Jetty) : **200**. Miniature `media.collections.yale.edu` : **307** vers un S3 signé d'un autre hôte (non suivi). `canvas/…` et `annopage/…` (ids du manifeste) : **404**.
- **Aucun en-tête de limite**, aucun 429, aucun 403 sur les hôtes `collections.yale.edu`.

## Web (étape f)

Quatre recherches (14/11/2026) : conditions de la Gallery (Wayback), article Yale News du 24/02/2025 sur LUX (lu : une phrase sur une API, rien sur les limites), guide IIIF « Finding Yale manuscripts » (lu : pas de limite, pas de moissonnage). **utilisateurs** et **tickets** : aucun résultat.

## Conclusion

Aucun quota publié ni observé. L'accès aux images est ouvert sans autorisation ni frais, avec attribution. Le site `artgallery.yale.edu` refuse notre client (Cloudflare) ; les API IIIF, sur d'autres hôtes, répondent normalement et sans en-tête de limite. Confiance moyenne (wiki Yale et LUX non lus). Étape g : `config/crash-image-info.json`.
