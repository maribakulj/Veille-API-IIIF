# Finna — Bibliothèque nationale de Finlande (`national-library-of-finland-finna`)

- **Hôtes** : `api.finna.fi`, `www.finna.fi`, wiki `www.kiwi.fi` (tous **403** pour notre sonde ; lecture par Wayback uniquement).
- **Vérifié le** : 2026-11-13, par Sonnet 5.5. Suivi : `CONSIGNE-ET-SUIVI.md`. Extraits : `sources/wayback/finna-extraits-wayback.md`.

## Ce que disent les sources
- **`api.finna.fi/robots.txt`** (Wayback, 31/05/2025) : `User-agent: *` / `Disallow: /` → **les robots sont exclus de l'API**.
- **`finna.fi/robots.txt`** (Wayback, 02/05/2026) : `Crawl-delay: 1`, `/SearchApi/` et `/*/api/` interdits, robots d'IA (ClaudeBot, GPTBot…) bloqués.
- **Conditions d'usage de l'API** : aucune inscription, mais « may, however, choose to introduce registrations […] to avoid excessive server load » ; métadonnées CC0 ; ressources liées sous leurs propres conditions ; **aucun chiffre de débit**.
- Documentation Swagger (principale) : **non lue** (403, pas de copie).

## Tests
**Aucun envoi** : le `robots.txt` de l'hôte API exclut les robots (consigne C8 : si c'est interdit, on laisse tomber) et l'hôte bloque notre sonde (403, on ne contourne pas).

## Web
Recherches : aucune politique de débit publiée ; le paquet R `finna` met 5 s par défaut (réglage client, non officiel) ; wiki tiers : `limit` 0–100, 100 000 résultats max (non vérifié à l'original).

## Conclusion
Limite chiffrée : aucune trouvée (seul `Crawl-delay: 1` sur le site). Règle écrite : API exclue aux robots par robots.txt ; inscription possible en cas de charge. Confiance : faible à moyenne. **Données Finna : à revoir si Marcel obtient un accès humain à la doc Swagger.**
