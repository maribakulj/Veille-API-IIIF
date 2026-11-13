# The National Gallery, Londres (`national-gallery-london`)

- **Classeur de référence** : GLAM-009 · **Pays** : Royaume-Uni
- **Hôtes** : `data.ng.ac.uk` (service IIIF Image 3 actuel), `media.ng-london.org.uk` (serveur IIIF historique « Beta »), `data.ng-london.org.uk` (API historique), `www.nationalgallery.org.uk` (site)
- **Vérifié le** : 2026-11-13, par Sonnet 5.5
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **« Collection image APIs »** : la Galerie « is in the process of implementing a full IIIF service » (Image et Presentation) ; en attendant : `https://data.ng.ac.uk/iiif/3/{image PID}/{region}/{size}/{rotation}/default.jpg`, exemple `…/0M1F-000B-0000-0000/full/max/0/default.jpg` (NG35, Titien).
- **Serveur historique** : « Legacy National Gallery - Beta IIIF Sever », images en CC BY-NC-ND 4.0 ; exemples de manifestes et d'images publiés sur sa page d'accueil.
- **Conditions d'utilisation du site** : interdit, entre autres, de « creating a database that includes material downloaded or obtained from the Website without written permission from the Gallery » ; usage personnel non commercial ; certaines images en CC BY-NC-ND 4.0, les faits clés en CC0. Une mention de « robot (or bot) » ne vise que la vente de billets.
- **`robots.txt`** : `www.nationalgallery.org.uk` : `*` sans interdiction notable (`/custom/popups`, `/external`) ; `Googlebot-Image` : `/server.iip` ; `research.ng-london.org.uk` : `/fcgi-bin/` ; les hôtes IIIF n'ont pas de `robots.txt` (404).
- **Aucun** quota, en-tête de limite, clé ni endpoint de statut.

## Tests (3 passes, configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `data.ng.ac.uk/iiif/3/0M1F-…/info.json` et dérivé `!200,200` | **200** ×2 |
| 2 | `media.ng-london.org.uk/iiif/…` : manifeste, `info.json`, dérivé 512 px | **200** ×3 |
| 3 | exemple de la doc `…/full/max/0/default.jpg` | **200**, JPEG de **800 × 730** pixels |

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`.

**Observation par mesure** : l'image « maximale » de l'exemple fait 800 × 730 pixels. Aucun texte officiel ne le dit ; un projet tiers l'avait déjà signalé (« at most about 800 px »).

## Web

- Page « Collection image APIs » et serveur historique : le service IIIF complet (Presentation) est annoncé mais non terminé.
- Un projet tiers (PR `jsa-art-tools` n° 6) indique que la collection de Londres s'interroge par un point d'accès Elasticsearch de `data.ng.ac.uk` : non vérifié (adresse masquée dans la doc).
- Aucune plainte, aucune politique de bots ni de débit trouvée pour les services de la Galerie.

## Conclusion

- **Limite documentée chiffrée** : non. **Limite observée** : non (6 requêtes réussies, aucun en-tête).
- **Règle contractuelle** : pas de base de données constituée à partir du site sans autorisation écrite.
- **Plafond de taille mesuré** : 800 × 730 px pour `full/max` (non documenté).
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne.
