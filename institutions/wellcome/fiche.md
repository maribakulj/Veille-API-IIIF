# Wellcome Collection (`wellcome`)

- **Classeur de référence** : GLAM-008 · **Pays** : Royaume-Uni
- **Hôtes** : `api.wellcomecollection.org` (API Catalogue), `iiif.wellcomecollection.org` (IIIF, **Crawl-delay 30 s**), `data.wellcomecollection.org` (instantanés), `wellcomecollection.org`, `developers.wellcomecollection.org`
- **Vérifié le** : 2026-11-13, par Sonnet 5.5 (reprise complète de la passe de Haiku)
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que Wellcome publie sur les limites et les robots

- **`robots.txt` de `iiif.wellcomecollection.org`** (lu en entier) : `User-agent: *`, `Disallow:` vide (tout autorisé), **`Crawl-delay: 30`**, **`Request-rate: 1/30s`**. C'est une limite de débit écrite : **une requête toutes les 30 secondes**. (Le fichier commence par un BOM invisible, qui a mis ma sonde en défaut : voir « Incidents ».)
- **Ticket GitHub `platform#6741`** (dépôt de Wellcome, 2026-10-05, fermé) : règles WAF de l'hôte IIIF. « One curl address hitting `/search/` and `/text/` at up to 26 a second: **held to 300 per address in five minutes**. » ; d'autres sources sont « rate limited » ou bloquées (valeurs non publiées). Le trafic de `/image/` a grimpé de 2,3 à 6 millions de requêtes par jour.
- **Ticket `platform#6843`** (2026-11-02) : blocage de rafales de robots et d'un « botnet de prévisualisation » ; les règles basées sur le débit sont à court d'emplacements (« the ACL has used all 10 »).
- **RFC `docs#161`** (brouillon ouvert, 2026-07-30) : « **Considerate, rate-limited, self-identifying bot traffic is welcome. Evasive, high traffic, inconsiderate bot traffic is not; if we deem it inconsiderate, we will attempt to block it.** » Réponses envisagées : `429 Too Many Requests` avec `Retry-After`, blocage au bord. Les seuils sont « deliberately not in this public document ».
- **Blog « Crawlers, floods and fleets »** (2026-10-16, lu en entier) : « we set budgets: a fixed number of requests a minute for a given harvester or network » ; limite par adresse sur les images plein format ; « a bulk user who tells us who they are gets the benefit of the doubt » ; pour tout le catalogue : « the daily snapshot rather than the API […] say who you are in your user agent, read robots.txt, spread your requests over time ».
- **Doc développeurs** : API Catalogue et IIIF « no sign up or authentication required » ; « if you require a full harvest of the catalogue, you should use the daily snapshot instead of the API » (`works.json.gz`, 1,5 Go).
- **`wellcomecollection.org/robots.txt`** : `*` autorisé sauf `/account` ; robots d'IA bloqués (ClaudeBot, anthropic-ai, GPTBot, Bytespider…).

## Tests (8 passes, configurations committées avant chaque lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | API Catalogue `works?pageSize=1` et `…&availabilities=online` | **200** |
| 1 | `data.wellcomecollection.org/…/works.json.gz` et `images.json.gz` (HEAD) | **200** |
| 2 | `works/a222zvge?include=items` | **200** |
| 3 | `iiif…/presentation/v2/b18659135` et `/v3/…` | **200** (672 ko pour le v2) |
| 4 | `iiif…/image/b18659135_0001.jp2/info.json` | **401** (matériel restreint) ; dérivé `!200,200` : **200** |
| 5 | `iiif…/presentation/v3/b18035723` (œuvre ouverte) | **200** |
| 6 | `iiif…/image/b18035723_0001.JP2/info.json` et dérivé | **200** ×2 |
| 7 | `api…/catalogue/v2/images?pageSize=1` et `concepts?pageSize=1` (référence `developers…/api/catalogue`, lue en entier, aucune mention de limite) | **200** ×2 |
| 8 | `api…/catalogue/v2/images/a22a42f2` et `concepts/a2233f9d` (identifiants de la passe 7) | **200** ×2 |

Rattrapage : `robots.txt` de developers.wellcomecollection.org (404, tout autorisé) et de stacks.wellcomecollection.org (Medium, 200) lus ; référence `/api/catalogue` téléchargée (`sources/v4`).

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`.

## Incidents (à lire)

1. **Passe 3** : deux requêtes IIIF sont parties à **6 s** d'intervalle au lieu de 30 s, parce que ma sonde ne lisait pas le `Crawl-delay` du fichier (BOM). Corrigé ; les passes 4 à 6 respectent 30 s (mesuré dans le journal).
2. **Passe de Haiku** (ancienne méthode) : 4 requêtes IIIF à 6 s d'écart, contraires au même `Crawl-delay`. Elles ne sont pas comptées dans cette passe.
3. Le `info.json` de l'œuvre `b18659135` répond 401 : accès restreint (Wellcome : « restricted material may be made available online to authenticated users »). Pas un blocage.

## Conclusion

- **Limites documentées chiffrées** : `Crawl-delay` 30 s et `Request-rate` 1/30 s sur l'hôte IIIF ; 300 requêtes par adresse en 5 minutes sur `/search/` et `/text/` (WAF) ; instantané quotidien pour un moissonnage complet.
- **Politique envers les robots** : explicite (s'identifier, lire `robots.txt`, espacer, utiliser l'instantané) ; robots d'IA bloqués.
- **Limite observée** : aucune (aucun 429, aucun en-tête).
- **Moyen d'interroger le quota** : aucun (le 429 avec `Retry-After` est envisagé, pas observé).
- **Confiance** : élevée pour la politique, moyenne pour les seuils réels.
