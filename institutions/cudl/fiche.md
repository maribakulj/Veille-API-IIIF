# Cambridge University Library — Cambridge Digital Library (`cudl`)

- **Classeur de référence** : GLAM-004 · **Pays** : Royaume-Uni
- **Hôtes** : `cudl.lib.cam.ac.uk` (site, manifestes), `images.lib.cam.ac.uk` (images), `cudl.link` (services, **non résolu en DNS**)
- **Vérifié le** : 2026-11-13, par Sonnet 5.5 (reprise complète de la passe de Haiku)
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **Page « About »** (copie Wayback 2026-10-17) : « You can also access content through application programming interfaces (APIs) such as the International Image Interoperability Framework (IIIF). » Aucune URL, aucun quota.
- **Conditions** (copie Wayback 2025-11-19) : sont interdits, sauf licence explicite, « **systematically extract and/or re-utilise substantial parts of the Content** » et « create and/or publish your own database that features substantial parts of this site ». C'est une interdiction contractuelle de réutilisation, pas une règle de débit.
- **`robots.txt`** (copie Wayback 2026-05-01) : `User-agent: *` ; `Disallow: /search`. Pas de `Crawl-delay`.
- **Page « Help »** (copie Wayback 2026-05-01) : ancienne FAQ (« We are currently working on implementing the IIIF technology… »).
- **README `cudl-services`** (GitHub, lu) : API « publicly accessible and (for the most part) requires no authentication » ; routes `/v1/metadata`, `/v1/transcription`, `/v1/translation`, `/v1/xtf/similarity`, `/v1/rdb/membership`, `/v1/darwin` (jeton), `/v1/iiif` (« not currently in use »), servies sur le domaine `cudl.link`. Aucun quota.
- **Aucun** quota, en-tête de limite, clé ni endpoint de statut documenté.

## Accès aux pages officielles

Les pages `/terms`, `/help`, `/about` et `/robots.txt` renvoient **403 CloudFront (« Request blocked »)** à notre sonde, alors que les manifestes et les images répondent 200. Je n'ai pas insisté ; les pages ont été lues dans la Wayback Machine (voir `sources/wayback/`, avec URL de réplique). Le téléchargement de ces copies par `curl` a été refusé par le système : les extraits sont recopiés à la main et vérifiables par l'URL de réplique, sans empreinte du texte complet.

## Tests (3 passes, toutes les configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `cudl.lib.cam.ac.uk/iiif/MS-ADD-03958` (manifeste, identifiant d'exemple du README) | **200**, 185 ko, IIIF Presentation 2, aucun en-tête de limite |
| 2 | `cudl.link/v1/transcription/…/MS-ADD-03958/i111` et `cudl.link/v1/metadata/` | **échec DNS** (hôte non résolu) : aucune requête HTTP partie |
| 3 | `images.lib.cam.ac.uk/iiif/MS-ADD-03958-001-00001.jp2/info.json`, `…/full/!200,200/0/default.jpg`, `…-00002.jp2/info.json` (identifiants publics tirés du manifeste) | **200** ×3, aucun en-tête de limite |

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`. Non testés : `/search` (interdit par `robots.txt`), `/v1/darwin` (jeton), les autres routes `cudl.link` (hôte non résolu).

| 4 (14/11) | `cudl.link/v1/metadata/MS-ADD-03958` (nouvel essai) | **échec DNS** à nouveau, aucune requête HTTP partie |

Robots relus le 14/11 (`sources/robots-v4`) : `cudl.lib.cam.ac.uk/robots.txt` toujours **403 CloudFront** (copie Wayback gardée), `cudl.link` DNS non résolu, `images.lib.cam.ac.uk` 404 (aucune règle). `/search` : aucune URL de requête documentée, non testé (le Disallow ne dispense plus, C12).

## Web

- Profil d'API tiers (apis.io) : donne les formes `cudl.lib.cam.ac.uk/iiif/<id>` et `images.lib.cam.ac.uk/iiif/<id>.jp2/info.json`, confirmées par nos tests ; mentionne des limites sans chiffre (non vérifié).
- **Non applicable** : les conditions de Cambridge University Press (limite de 500 PDF par heure) concernent un autre organisme ; elles ne s'appliquent pas à CUDL.
- Presse sectorielle (GovTech, GLAM-E Lab, Scholarly Kitchen) sur les robots d'IA et les collections numérisées : **rien de spécifique à CUDL**.
- Recherches du 14/11 (utilisateurs, tickets) : aucune plainte 429/403 ni ticket d'outil visant CUDL (résumés de moteur, non vérifiés).
- Aucune plainte, aucune présentation de CUDL sur sa politique de moissonnage ou de bots trouvée.

## Conclusion

- **Limite documentée chiffrée** : non. **Limite observée** : non (6 requêtes réussies sans en-tête ni 429).
- **Règle explicite** : pas d'extraction systématique de parties substantielles ni de base de données dérivée sans licence ; `/search` interdit aux robots.
- **Moyen d'interroger le quota** : aucun.
- **Contact** : `dl-feedback@lib.cam.ac.uk`.
- **Confiance** : moyenne.

## Crash test (étape g)

Crash test fait le 2026-11-14 : image-info-json sur images.lib.cam.ac.uk : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/cudl.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
