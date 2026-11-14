# National Library of Scotland (`national-library-of-scotland`)

- **Classeur de référence** : GLAM-006 · **Pays** : Royaume-Uni (Écosse)
- **Hôtes** : `view.nls.uk` (manifestes, collections), `dg-view.nls.uk` (images, Cantaloupe), `map-view.nls.uk` (images de cartes), `deriv.nls.uk` ; sites `digital.nls.uk` et `maps.nls.uk` (**CAPTCHA**)
- **Vérifié le** : 2026-11-13, par Sonnet 5.5
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **Moissonnage IIIF — document officiel du NLS** (demande CoreTrustSeal, PDF lu et haché) : « All of the web services support web crawling and harvesting for direct access from search engines. » et « IIIF volumes are harvestable via a top-level collections-based json file that provides access to all IIIF manifests (https://view.nls.uk/collections/top.json) ».
- **Quota chiffré, hors IIIF** : l'API des couches de cartes géoréférencées est servie par MapTiler Cloud : « There is a 'free' tier for all non-commercial subscribers using 100,000 tile requests per month or less. » (copie Wayback 2025-11-14). Ne concerne pas le service IIIF.
- **Copyright** (copie Wayback 2025-12-03) : réutilisation encouragée sous CC-BY, avec attribution ; aucune règle de débit ni sur les robots.
- **robots.txt** : `view.nls.uk` bloque des robots d'IA nommés (dont ClaudeBot, anthropic-ai, GPTBot, CCBot) et rien pour `*` ; `deriv.nls.uk` : `*` : `Disallow: /dcn6/` ; `dg-view.nls.uk` : pas de route (404) ; `data.nls.uk` : lu.
- **Déclaration IA du NLS** (data.nls.uk) : la politique doit guider « how we […] allow our data to be used by others » ; le détail est dans un document Word non lu.
- **Aucun** en-tête de limite, clé, ni endpoint de statut documenté pour l'IIIF.

## Accès aux pages

`digital.nls.uk` et `maps.nls.uk` renvoient une page **« Human Verification »** (CAPTCHA, statut 405) à notre client. Je ne la contourne pas. Pages lues dans la Wayback Machine (voir `sources/wayback/`). La FAQ `maps.nls.uk/help/` et la page de conditions de `digital.nls.uk` n'ont pas de copie archivée récente : **non lues**.

## Tests (5 passes, configurations committées avant chaque lancement)

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | `view.nls.uk/collections/top.json` (documenté par le NLS) | **200**, 47 collections |
| 2 | `view.nls.uk/collections/1208/2191/120821910.json` | **200**, 688 ko, 4 142 manifests |
| 3 | `view.nls.uk/manifest/1204/4314/120443143/manifest.json` | **200**, 44 ko, IIIF Presentation 2 |
| 4 | `dg-view.nls.uk/iiif/2/…/info.json` et dérivé `full/!200,200/0/default.jpg` | **200** ×2 |
| 5 | `map-view.nls.uk/iiif/1/19619%2F196194600/info.json` (identifiant d'un ticket public) | **200** |

Aucun 429. Aucun en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`. Non testés : `digital.nls.uk` et `maps.nls.uk` (CAPTCHA, hôte arrêté par la règle de la méthode).

| 6 (14/11) | `data.nls.uk/wp-json/wp/v2/pages/60` (REST WordPress annoncé par la page d'accueil, non documenté comme API) | **200**, GET seul (`allow: GET`), aucun en-tête de limite |

Recherches web du 14/11 : aucune page du NLS sur les robots ni sur d'autres points de moissonnage que `top.json` (résumés de moteur, non vérifiés).

## Web

- **Un utilisateur** (ticket `dezoomify-rs` n° 92, décembre 2020, `map-view.nls.uk`) rapporte qu'un tuilage « plein format » reçoit un **403** : « The requested pixel area exceeds the maximum threshold set in the configuration. » Ancien, d'un particulier, **non vérifié par nous** (nous n'avons pas demandé de grande image).
- Presse et sources secondaires : usage du site des cartes (5 000 utilisateurs par jour en 2022, source tierce) ; aucune plainte ni politique de moissonnage ou de bots trouvée.

## Conclusion

- **Limite documentée chiffrée sur l'IIIF** : non. **Limite observée** : non (9 requêtes réussies).
- **Politique officielle** : moissonnage IIIF explicitement prévu via `top.json` ; robots d'IA nommés bloqués ; CAPTCHA sur les sites de pages.
- **Quota chiffré hors IIIF** : 100 000 tuiles par mois (MapTiler, gratuit non commercial).
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne à élevée pour l'IIIF.
