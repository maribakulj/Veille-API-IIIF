# University of Toronto Libraries (`university-of-toronto-libraries`)

- **Classeur** : GLAM-050 · Canada · audit v2 le 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `iiif.library.utoronto.ca` (manifestes et images IIIF), `collections.library.utoronto.ca` (site Collections U of T, notices MODS), `utlib.github.io` (doc du personnel).

## Sources
- **Doc officielle** (`sources/a/`, `a3/`, `a4/`) : FAQ « Reusing Collections U of T items with IIIF » : manifeste `https://iiif.library.utoronto.ca/presentation/PID/manifest`, collections `…/presentation/collections/PID`, liste `…/presentation/v2/collections` ; « Presentation API (v2 and v3; manifests currently default to v2) », « Image API (v2) ». Doc du personnel : « Collections U of T IIIF manifests and image URLs are published with the goal of providing access and capacity for reuse in perpetuity » ; contact digitalinitiatives@library.utoronto.ca. Plateforme maison depuis le 21/05/2024 (Islandora 7 abandonné).
- **Aucune mention de quota, de limite de débit ni de politique de robots** dans ces pages.
- `robots.txt` : `collections.library` : `Allow: /`, `Disallow: /api/` ; `iiif.library` : 302 (pas de robots.txt) ; `library.utoronto.ca` : `Disallow: /storage-request` ; `static.scholarsportal.info` : 412 ; `utlib.github.io`, `cloud.scholarsportal.info` : 404.

## Tests (2 passes, configurations committées avant lancement, pauses 6 s ; 15 requêtes, robots compris)
Manifeste v2 : **200** ; motifs sans version et `presentation/collections/PID` : **307** vers `/v2/` puis **200** ; liste des collections : 307 puis 200 ; page d'item : **200** ; `info.json` d'image (Image API 2, niveau 2, lu dans le manifeste), dérivé 80 px et notice MODS : **200**. Aucun 429, aucun en-tête `RateLimit-*`/`Retry-After` ; serveur `nginx`. Aucune limite annoncée par les en-têtes.
Non testé : manifeste Presentation v3 (doc sans URL).

## Web (4 recherches)
- Institution et utilisateurs : aucun résultat propre à iiif.library.utoronto.ca (pas de politique de bots, pas de plainte 429/403).
- Tickets : aucun ticket citant iiif.library.utoronto.ca.
- Présentations/billets de l'institution : guide de migration 2024 et historique de Collections U of T (`sources/a4/`), sans mention de limite.

## Pourquoi pas publié
Aucune limite chiffrée ; l'institution met l'accent sur la réutilisation (« capacity for reuse in perpetuity »). La plateforme est en mode maintenance à capacité réduite (doc, non chiffrée). Hypothèse (non vérifiée) : pas de limitation appliquée à ce jour.

## Conclusion
Limite chiffrée : aucune. IIIF Presentation et Image sans en-tête de limite, sans défi. Confiance : moyenne. Contact : digitalinitiatives@library.utoronto.ca. Étape g : `config/crash-image-info.json` prête.
