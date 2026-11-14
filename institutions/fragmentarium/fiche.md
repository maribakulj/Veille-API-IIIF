# Fragmentarium (`fragmentarium`)

- **Classeur de référence** : GLAM-023 · **Pays** : Suisse (Université de Fribourg, issu d'e-codices)
- **Hôte** : `fragmentarium.ms` (manifestes IIIF Presentation 2, images IIIF Image 2 via Loris, pages web)
- **Vérifié le** : 2026-11-14, par Sonnet 5.5
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Sources

- Conditions d'utilisation (`/pages/terms`) : usage non commercial des images libre, restrictions possibles par institution ; métadonnées sous CC BY. **Aucune règle de débit ni de robots.**
- Digital Laboratory (`/pages/about/digital-laboratory`) : « Fragmentarium offers free access to all of its services. » ; IIIF Image API (serveur Loris) et IIIF Presentation API. Aucune URL d'API ni quota donnés.
- `robots.txt` (48 octets, lu en entier) : `Disallow: /cms/` et `/auth/` ; pas de `Crawl-delay`.
- Autres pages lues : privacy, impressum, past-and-present, partners, contact (aucune règle de débit). `/case_studies` : 404.
- Pas de clé, pas d'endpoint de statut, pas d'en-têtes de limite documentés. Contact : `fragmentarium@unifr.ch`.
- Dossiers de preuves : `sources/a`, `sources/b` (SHA-256 et textes).

## Tests (1 passe, 5 requêtes, pauses 6 s, configuration committée avant lancement)

| Endpoint | Résultat |
|---|---|
| manifeste `metadata/iiif/F-ioqy/manifest.json` (identifiant du lien public du site) | **200** |
| collection `metadata/iiif/collection/C-a4xj.json` (champ `within` du manifeste) | **200** |
| `loris/F-ioqy/page_5.jp2/info.json` | **200** |
| dérivé `full/200,/0/default.jpg` | **200** |
| page `overview/F-ioqy` (seeAlso) | **200** |

Aucun 429. Aucun en-tête de limite (en-têtes bruts : Apache/2.4.62, `cache-control: max-age=2393857, public`, `access-control-allow-origin: *`). La recherche (`/search`) n'est pas testée : interface web sans API documentée.

## Web

Quatre catégories couvertes (voir `data.json`) : aucune plainte (429/503/blocage), aucun ticket GitHub, article de l'université et guide IIIF.io sans limite. Résumés de moteur marqués « non vérifié ».

## Conclusion

- **Limite chiffrée** : aucune. **Règle écrite** : droits d'usage des images, `robots.txt` limité à `/cms/` et `/auth/`.
- **Limite observée** : aucune (5 requêtes réussies). **Moyen d'interroger le quota** : aucun.
- **Pourquoi non publié** (hypothèse) : service académique gratuit, petit, sans mécanisme de limitation visible. Confiance : moyenne.
- Crash test (g) : préparé (`config/crash-info-json.json`), à lancer à la fin.
