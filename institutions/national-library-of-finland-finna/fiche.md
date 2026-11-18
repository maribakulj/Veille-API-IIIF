# Finna — Bibliothèque nationale de Finlande (`national-library-of-finland-finna`)

- **Hôtes** : `api.finna.fi`, `www.finna.fi`, wiki `www.kiwi.fi` (tous **403** pour notre sonde ; lecture par Wayback uniquement).
- **Vérifié le** : 2026-11-13, par Sonnet 5.5. Suivi : `CONSIGNE-ET-SUIVI.md`. Extraits : `sources/wayback/finna-extraits-wayback.md`.

## Ce que disent les sources
- **`api.finna.fi/robots.txt`** (Wayback, 31/05/2025) : `User-agent: *` / `Disallow: /` → **les robots sont exclus de l'API**.
- **`finna.fi/robots.txt`** (Wayback, 02/05/2026) : `Crawl-delay: 1`, `/SearchApi/` et `/*/api/` interdits, robots d'IA (ClaudeBot, GPTBot…) bloqués.
- **Conditions d'usage de l'API** : aucune inscription, mais « may, however, choose to introduce registrations […] to avoid excessive server load » ; métadonnées CC0 ; ressources liées sous leurs propres conditions ; **aucun chiffre de débit**.
- Documentation Swagger (principale) : **non lue** (403, pas de copie).

## Tests
Passe 1 (2026-11-14, 1 requête) : `GET api.finna.fi/api/v1/search?lookfor=test&limit=1` → **403** défi Cloudflare (`cf-mitigated: challenge`) : arrêt sur l'hôte, non contourné. (Le `Disallow: /` du robots.txt ne dispense plus de tester, consigne C12.) La spécification OpenAPI (Wayback 2025-08-10, `sources/wayback/finna-openapi-et-kiwi-robots.md`) donne `limit` max 100 et `resumptionToken`, aucune limite de débit.

## Web
Recherches : aucune politique de débit publiée ; le paquet R `finna` met 5 s par défaut (réglage client, non officiel) ; wiki tiers : `limit` 0–100, 100 000 résultats max (non vérifié à l'original).

## Conclusion
Limite chiffrée : aucune trouvée (seul `Crawl-delay: 1` sur le site). Règle écrite : API exclue aux robots par robots.txt ; inscription possible en cas de charge. Confiance : faible à moyenne. **Données Finna : à revoir si Marcel obtient un accès humain à la doc Swagger.**

## Rattrapage documentaire — passe X (15 novembre 2026)

Deux pages **originales** du suivi manuel ont été réellement récupérées : l'index `Finna API Documentation In English` (3 848 caractères, copie 05/11/2026) et `viewpage.action?pageId=75202667` (38 323 caractères, copie 15/11/2026). Les **conditions officielles de Finna**, relues intégralement (6 895 caractères, mise à jour affichée 25/10/2024), confirment qu'aucune inscription n'est requise pour l'**API REST de métadonnées**, mais qu'une restriction peut être introduite en cas de surcharge. **CC0 ne s'étend pas automatiquement aux images liées.** L'OpenAPI REST actuelle v11.0.3 existe à `/api/v1/?openapi` ; l'ancien `/v1?swagger` demeure 403. Les règles robots et les quotas Image IIIF sont des questions distinctes. Voir [`VERIFICATIONS-CHATGPT-2026-11-15-X-DOCUMENTS-ORIGINAUX.md`](../../VERIFICATIONS-CHATGPT-2026-11-15-X-DOCUMENTS-ORIGINAUX.md).
