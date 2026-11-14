# Europeana (`europeana`)

- **Classeur de référence** : GLAM-011 · **Pays** : Union européenne (Pays-Bas)
- **Hôtes** : `iiif.europeana.eu` (IIIF, **sans clé**), `api.europeana.eu` (APIs Search, Record… : **clé requise**), `www.europeana.eu`, `pro.europeana.eu` (403 pour la sonde)
- **Vérifié le** : 2026-11-13, par Sonnet 5.5 (reprise complète de la passe de Haiku)
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **Politique d'usage équitable** (base de connaissances, mise à jour du 2024-09-05, lue en entier) : « Use of the API must be limited to a reasonable number of concurrent requests to an API, together with an appropriate wait period […] Europeana may specify a limit per type of request and/or across all Europeana APIs, to which you will be required to adhere. » ; en cas d'erreur de limite, « you must reduce the number of concurrent requests » ; « The failure to comply with this policy may result in your access key be temporarily blocked or even revoked. » ; pour des métadonnées en masse : jeux de données FTP/HTTP ou **OAI-PMH**. Contact : `api@europeana.eu`.
- **« Accessing the APIs »** : « The rate limits for personal keys have been progressively reduced until April 2026 » ; les clés de projet ont des limites « significantly higher » ; « If abuse of an API key is detected, Europeana Foundation may impose additional usage limits or suspend or revoke access ». **Aucun chiffre publié.**
- **Conditions d'utilisation** : « Europeana may limit the number of requests the User may send and receive through the Europeana API. »
- **IIIF** (« IIIF APIs Documentation ») : « **You don't need an API key for this API!** » ; manifestes à `https://iiif.europeana.eu/presentation/{DATASET_ID}/{LOCAL_ID}/manifest` (« IIIF Manifests at Europeana »).
- **FAQ de l'API** (page plus ancienne) : « You can query our APIs as often as you like without any throttling or limiting. » — **contredit** la politique d'usage équitable et la réduction des limites des clés personnelles ; à ne pas retenir.
- **`robots.txt`** : `iiif.europeana.eu` : `User-agent: *` et `Disallow:` vide (tout autorisé) ; `www.europeana.eu` : `Disallow: /api/*`, `/iiif/*`, `/*/iiif/*` (ces chemins du site web) ; `api.europeana.eu` : page de l'application, pas un `robots.txt`.
- **Réserve** : la base de connaissances précise « You're viewing this with anonymous access, so some content might be blocked » : la doc lue peut être partielle.

## Tests (5 passes, configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `iiif.europeana.eu/presentation/90402/SK_A_3262/manifest` (exemple de la FAQ) | **200** ; ses images sont chez un CDN tiers (non testé) |
| 2 | `…/presentation/9200396/BibliographicResource_3000118436165/manifest` | **200**, 137 ko |
| 3 | `iiif.europeana.eu/image/…/info.json` et dérivé `!200,200` | **200** ×2 |

| 4 | `…/annopage/0090019?lang=fr` (page d'annotations plein texte, URL du manifeste) | **200** |
| 4 | `…/presentation/9200396/BibliographicResource_3000118436165/search?q=paris` (Content Search, un item) | **200** |
| 4 | `api.europeana.eu/fulltext/search.json?query=fulltext:paris&profile=minimal` | **401** `invalid_apikey` (clé exigée, malgré « You don't need an API key » de la doc IIIF ; ce n'est pas un quota) |
| 5 | `api.europeana.eu/fulltext/9200396/…/0090019` (ressource plein texte, URL de l'annopage) | **200** |

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`. **Non testées** : APIs Search et Record (une clé est exigée par la doc ; non demandée).

**Incident de la sonde** : la première tentative de la passe 3 a échoué avant l'envoi (caractère accentué dans l'URL, erreur d'encodage de ma sonde, corrigée). Aucune requête n'est partie vers Europeana.

## Web

- **Correction (passe 5)** : le chiffre « 120 requêtes par 10 secondes » est **retrouvé** : liste europeanaAPI, 12/07/2024, équipe Europeana : « The current set rate limit for external requests is set at a maximum of 120 requests per 10 seconds » (page lue) ; même fil : « we temporarily rate-limited the IP address of this user » (API des vignettes). Non reprise dans la doc officielle lue, non observée par nos tests.
- Tickets : github.com/europeana/rd-europeana-python-api/issues, 9 tickets ouverts, aucun sur les limites (titres lus).
- Politique/IA : recherche sans annonce propre à Europeana ; un papier Open Future (déc. 2025, non lu : PDF illisible par l'outil) traite des bots en général.
- Aucune annonce d'Europeana sur des robots, des clés bloquées ou l'IA trouvée.
- Profils d'API tiers (apis.io, public-api.org) : « limites non documentées » ; sans valeur officielle.

## Conclusion

- **Limite documentée chiffrée** : aucune. **Règle écrite** : usage équitable, limites par type de requête fixées par Europeana, réduction des clés personnelles jusqu'en avril 2026, blocage ou révocation de clé.
- **Limite observée** : aucune sur l'IIIF (sans clé). **En-têtes** : aucun.
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne (documentation partiellement masquée aux utilisateurs anonymes ; clés non testées).

## Passes 4-5 (lot D) : pages pro.europeana.eu
`pro.europeana.eu/page/api-libraries-and-plugins` et `/project/iiif-europeana-working-group` : 403 anti-bot pour `fetch_doc.sh` le 2026-11-14 (non contourné) ; lues sur répliques Wayback (`sources/wayback/pro-europeana.md`) : aucune limite chiffrée, ni API. robots.txt de pro (Wayback 2025-05-07) : `Disallow: /admin/` pour `*`. robots.txt de europeana.atlassian.net lu : Crawl-delay 1. Remarque : `fetch_doc.sh` a envoyé la 2e requête vers pro après un premier 403 (outil, pas de décision).
