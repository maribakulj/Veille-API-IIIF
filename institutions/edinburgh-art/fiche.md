# University of Edinburgh — Art Collection (`edinburgh-art`)

- **Classeur de référence** : GLAM-005 · **Pays** : Royaume-Uni (Écosse)
- **Hôtes** : `collections.ed.ac.uk` (site, manifestes), `images.is.ed.ac.uk` (serveur d'images LUNA)
- **Vérifié le** : 2026-11-13, par Sonnet 5.5 (reprise complète : la passe de Haiku concluait à tort qu'aucun endpoint n'était documenté)
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **Page IIIF du site** : les fiches ont une icône IIIF à glisser vers un visualiseur ; la page de fiche expose le lien `…/art/record/{id}/1/manifest.json` (et les visualiseurs Mirador et UV de la bibliothèque).
- **Licence** (`/art/licensing`) : « Use of images from this site, or any derivative works, can only be made with permission in advance. Images are provided for the purposes of research, private study or review. » Contact : `HeritageCollections@ed.ac.uk`.
- **`collections.ed.ac.uk/robots.txt`** : `User-agent: *` et `Disallow:` vide (tout autorisé).
- **`images.is.ed.ac.uk/robots.txt`** (serveur LUNA, 279 lignes, lu en entier) : pour `User-agent: *`, 31 règles `Disallow` (exports, login, RSS, recherche…) et **`Crawl-Delay: 500`** — soit **une requête toutes les 500 secondes** ; `Crawl-Delay: 50` pour Googlebot. Baiduspider et Yandex sont bloqués.
- **Aucun** quota, clé, ni endpoint de statut documenté dans les pages du site.

## Tests (2 passes, configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `collections.ed.ac.uk/art/record/112492/1/manifest.json` (lien de la fiche) | **200**, IIIF Presentation 2 |
| 2 | `images.is.ed.ac.uk/luna/servlet/iiif/UoEart~…/info.json` | **200**, aucun en-tête de limite |
| 2 | `…/full/!96,96/0/default.jpg` | **200**, aucun en-tête de limite |
| 2 | `images.is.ed.ac.uk/luna/servlet/iiif/m/UoEart~…/manifest` (manifeste « related ») | **200**, **`ratelimit-limit: 5.0`**, **`ratelimit-reset: 1`** |

La passe 2 a respecté le `Crawl-Delay` : ses requêtes sont espacées de 500 s (22:36:05 → 22:44:25 → 22:52:45 → 23:01:06 UTC), ce qui a pris 25 minutes.

**Observation** : seul le manifeste LUNA renvoie des en-têtes `ratelimit-*` ; `info.json` et l'image n'en renvoient pas. L'unité de `5.0` n'est documentée nulle part (par seconde ? par fenêtre ?) ; `reset: 1` laisse penser à une seconde. Valeur à interpréter avec prudence.

## Web

- Recherches web (3) : aucune plainte ni politique de moissonnage ou de bots d'Édimbourg trouvée. Un ticket GBIF sur un serveur d'images du **Royal Botanic Garden Edinburgh** parle de robots d'IA et de scraping, mais c'est un **autre organisme** : non applicable.
- Billets du blog des bibliothèques (2016) sur la mise en ligne de l'IIIF (LUNA 7.2) : aucune règle de débit.

## Conclusion

- **Limite documentée chiffrée** : `Crawl-Delay: 500` (robots.txt de LUNA).
- **En-têtes de limite observés** : `ratelimit-limit: 5.0` et `ratelimit-reset: 1` sur le manifeste LUNA (unité non documentée).
- **403 / 429** : aucun.
- **Moyen d'interroger le quota** : aucun endpoint de statut ; les en-têtes d'une requête normale de manifeste donnent une valeur.
- **Confiance** : moyenne.

## Crash test (étape g)

Crash test fait le 2026-11-14 : manifeste-record-112492 sur collections.ed.ac.uk : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/edinburgh-art.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
