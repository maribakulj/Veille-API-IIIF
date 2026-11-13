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

## Tests (3 passes, configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `iiif.europeana.eu/presentation/90402/SK_A_3262/manifest` (exemple de la FAQ) | **200** ; ses images sont chez un CDN tiers (non testé) |
| 2 | `…/presentation/9200396/BibliographicResource_3000118436165/manifest` | **200**, 137 ko |
| 3 | `iiif.europeana.eu/image/…/info.json` et dérivé `!200,200` | **200** ×2 |

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`. **Non testées** : APIs Search et Record (une clé est exigée par la doc ; non demandée).

**Incident de la sonde** : la première tentative de la passe 3 a échoué avant l'envoi (caractère accentué dans l'URL, erreur d'encodage de ma sonde, corrigée). Aucune requête n'est partie vers Europeana.

## Web

- Le chiffre « 120 requêtes toutes les 10 secondes » relevé par l'ancienne passe sur un forum est **introuvable** : non retenu.
- Aucune annonce d'Europeana sur des robots, des clés bloquées ou l'IA trouvée.
- Profils d'API tiers (apis.io, public-api.org) : « limites non documentées » ; sans valeur officielle.

## Conclusion

- **Limite documentée chiffrée** : aucune. **Règle écrite** : usage équitable, limites par type de requête fixées par Europeana, réduction des clés personnelles jusqu'en avril 2026, blocage ou révocation de clé.
- **Limite observée** : aucune sur l'IIIF (sans clé). **En-têtes** : aucun.
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne (documentation partiellement masquée aux utilisateurs anonymes ; clés non testées).
