# e-codices — Bibliothèque virtuelle des manuscrits de Suisse (`e-codices`)

- **Classeur** : GLAM-018 · Suisse · **Refonte v2 le** 2026-11-14 par Sonnet 5.5 (l'ancien audit, partiel, avait manqué l'interface OAI) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `www.e-codices.unifr.ch` (site, manifestes IIIF), `e-codices.ch` (OAI), `media.e-codices.ch` (images IIIF).

## Ce que dit la doc officielle
- **Terms of Use** : pas de quota ni de limite de débit ; images libres en non commercial (par bibliothèque propriétaire) ; **interface OAI-PMH** (Dublin Core) en quatre langues : `e-codices.ch/oai/{de,en,fr,it}/oai.php?verb=Identify` ; métadonnées et aperçus « released for free use ». Aucune URL IIIF dans la doc (page « Web Application » : IIIF Image et Presentation citées sans URL).
- `robots.txt` de `www.e-codices.unifr.ch`, `e-codices.ch`, `media.e-codices.ch` : `Disallow:` vide (tout autorisé).

## Tests (3 passes, configs committées avant lancement, pauses 6 s)
OAI (`Identify` en et de, `ListMetadataFormats`, `ListSets`) : **200** ×4 · manifeste `fmb-cb-0100` (471 ko, 610 canevas) et collection `ubb` : **200** ×2 · `info.json` et dérivé 200 px sur `media.e-codices.ch` : **200** ×2. Aucun 429, aucun en-tête de limite. `ListRecords` non lancé (volume).

## Web (5 recherches, une par catégorie)
- Utilisateurs/tiers : un vérificateur de liens (SexyCodicology) enregistre des **503** et délais dépassés intermittents sur les pages de recherche e-codices (pas sur IIIF) ; des 429 y viennent d'autres bibliothèques.
- Outils tiers : crawlers (IIIF-Crawler, manuscript-dl, mnemosyne#36, sourcelibrary#1426) passent par `collection.json` puis les manifestes ; aucun ne cite de limite.
- Institution/présentations : aucun résultat sur une politique de bots ou de débit.

## Conclusion
Limite chiffrée : aucune. Règle écrite : usage non commercial libre, source à citer pour l'usage commercial. Confiance : moyenne.
