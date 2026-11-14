# Rijksmuseum (`rijksmuseum`)

- **Classeur de référence** : GLAM-012 · **Pays** : Pays-Bas
- **Hôtes** : `data.rijksmuseum.nl` (Search, résolveur, OAI-PMH, LDES, IIIF Change Discovery), `iiif.micr.io` (IIIF Image et Presentation, Micrio), `id.rijksmuseum.nl`, `www.rijksmuseum.nl`
- **Vérifié le** : 2026-11-13, par Sonnet 5.5 (reprise complète de la passe de Haiku)
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **Aucune clé** : « No API key is needed » (Search API, OAI-PMH). Services documentés : Search (Linked Art Search), résolveur d'identifiants (Linked Art), OAI-PMH (EDM), LDES, SRU (déprécié), IIIF Change Discovery, IIIF Image, IIIF Presentation, vidages de données.
- **Aucun** quota, en-tête de limite, ni endpoint de statut. Seules limites chiffrées : « The API serves pages that contain a **maximum of one hundred ordered events** » (Change Discovery) ; résultats paginés par jeton.
- **Moissonnage** : « You can use the OAI-PMH API, the Search API or the LDES API to harvest collection data. »
- **`iiif.micr.io/robots.txt`** (lu en entier) : « As a condition of accessing this website, you agree to abide by the following content signals » ; **`Content-Signal: search=yes,ai-train=no,use=reference`** ; « express reservations of rights under Article 4 of the EU Directive 2019/790 » ; une trentaine de robots d'entraînement d'IA bloqués (ClaudeBot, GPTBot, anthropic-ai, CCBot…) ; deux groupes `*` (`Allow: /` puis `Disallow: /`) se combinent : l'accès reste autorisé (RFC 9309, `Allow` l'emporte à égalité).
- **`www.rijksmuseum.nl/robots.txt`** : `*` autorisé, sauf quelques chemins (`/en/collection/search?*`, connexion). `data.rijksmuseum.nl` : pas de `robots.txt` (404).
- **Politique d'information et de données** (en vigueur depuis le 17 juillet 2024) : 3.16 : le musée souhaite que les technologies d'IA qui utilisent ses données respectent la politique et ses valeurs, soient « transparent » ; attribution recommandée.
- L'ancienne page de conditions de l'API (domaine de préproduction Azure) renvoie 403 : **non lue** ; elle concernait l'ancienne API à clé.

## Tests (2 passes, configurations committées avant lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `data…/search/collection`, résolveur `/200107928`, OAI-PMH (`Identify`, `ListMetadataFormats`, `ListSets`, `GetRecord` EDM), LDES, IIIF Change Discovery | **200** ×8 |
| 2 | `iiif.micr.io/RFwqO/info.json`, `/manifest`, dérivé `!200,200` | **200** ×3 |
| 3 (rejeu conforme de la session archivée) | `iiif.micr.io/PJEZO` : manifeste, `info.json`, image 800 px ; manifeste `RFwqO` | **200** ×4 |


Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*` (en-têtes bruts relus). `ListRecords` n'est pas testé (très volumineux, la doc ne l'impose pas).

## Web

- Une recherche sur les bots et les limites n'a trouvé **aucune politique de débit** du Rijksmuseum ; des listings tiers disent « limites non documentées ».
- La politique de données et le `robots.txt` de Micrio sont la position officielle sur l'IA : entraînement interdit (`ai-train=no`), usage de référence.

- Recherches de la passe de rattrapage du 2026-11-14 (voir `data.json`) : aucune plainte 429 ni ticket trouvé ; ancienne politique Open Data lue via Wayback (`sources/wayback/`), sans quota ; l'ancienne page de conditions Azure n'a aucune capture Wayback (URL à vérifier à la main).

## Conclusion

- **Limite documentée chiffrée de débit** : aucune. Pagination : 100 événements par page (Change Discovery).
- **Règle écrite** : `Content-Signal` `ai-train=no`, robots d'entraînement d'IA bloqués, réservation de droits (directive européenne 2019/790).
- **Limite observée** : aucune (11 requêtes réussies, aucun en-tête). **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne à élevée.
