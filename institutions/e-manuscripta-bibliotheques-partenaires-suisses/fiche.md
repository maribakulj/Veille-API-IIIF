# e-manuscripta — plateforme des manuscrits des bibliothèques et archives suisses (`e-manuscripta-bibliotheques-partenaires-suisses`)

- **Classeur** : GLAM-020 · Suisse · **Audit v2 le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Exploitation** : Visual Library Server (Semantics), hébergé par l'ETH Zürich (« Powered by ETH Library »), partenaires dont la Zentralbibliothek Zürich et l'Universitätsbibliothek Basel.
- **Hôtes** : `www.e-manuscripta.ch` (site, OAI-PMH, IIIF, téléchargements), `sru2.visual-library.de` (SRU).

## Sources
- **Doc officielle des interfaces** : page « Schnittstellen und Datenabzug » (`/wiki/apiinfo`), lue dans la Wayback (capture 2025-03-07) car le site sert aujourd'hui un défi JavaScript (« Verifying your browser ») : OAI-PMH (paquets de 10 notices), PDF, RIS, IIIF. **Aucun quota, aucune limite de débit chiffrée.** Mise en garde : les notices METS de très gros titres peuvent dépasser le délai. Extraits : `sources/wayback/e-manuscripta-extraits-wayback.md`.
- **Conditions d'utilisation** (`/wiki/termsOfUse`, Wayback 2025-03-08) : licences par document (domaine public, CC BY-SA 4.0, droits restreints) ; « Systematic copying of files onto other servers is permitted only with the prior consent in writing of the portal's administrative office or the holding institution(s) ». Contact : adresse générique du portail.
- **robots.txt de www.e-manuscripta.ch** (lu en direct, 89 octets) : `User-agent: *` `Disallow: /` ; seuls Bingbot et Googlebot sont autorisés. Stable depuis février 2025 (Wayback). Consigne C12 : le Disallow n'arrête plus l'audit.
- **Data map de la Zentralbibliothek Zürich** (`data.zb.uzh.ch`, partenaire) : URL et exemples pour OAI, IIIF (Image 2.1, Presentation 2.0), SRU ; sets OAI ; hOCR/ALTO/HTML des textes transcrits ; aucun quota non plus (`sources/a1`, `a2`, `a4`).
- robots.txt des autres hôtes : `sru2.visual-library.de` 404 (tout autorisé), `data.zb.uzh.ch` 404, `www.zb.uzh.ch` 200 (GPTBot exclu de /recherche, `*` autorisé), `opendata.swiss` 200. Fiche opendata.swiss : licence CC BY-SA 4.0, jeu daté de 2017.

## Tests (2 passes, 16 requêtes en tout, configurations committées avant lancement, pauses 6 s)
| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | OAI `Identify`, `ListSets`, `ListMetadataFormats`, `GetRecord` (oai_dc, id 3071845), `ListIdentifiers` (set emanuszuz, une semaine) | **200** ×5 |
| 1 | IIIF manifeste v20 (3192957), `info.json` v21, dérivé `full/304` (3192960) | **200** ×3 |
| 1 | RIS (1384091), ALTO (1831288) | **200** ×2 |
| 1 | SRU `sru2.visual-library.de/emanus_alma_uzb` (exemple de la doc) | **200** |
| 2 | OAI `ListRecords` étroit (10 notices), `ListSets` avec resumptionToken | **200** ×2 |
| 2 | PDF (HEAD), hOCR, collection IIIF `v21/collection/top` | **200** ×3 |

Aucun 429, aucun 403, aucun en-tête `Retry-After`/`X-RateLimit-*`/`RateLimit-*`. En-têtes présents : `server: VLS/2603`, `vl-node`, `set-cookie: session_id`. Les API (OAI, IIIF, téléchargements) répondent donc au client de la sonde, alors que les pages HTML du site (accueil, wiki) sont derrière un défi JavaScript (observé par `fetch_doc`, non contourné). Non lancés : METS (volume), Z39.50 (hors HTTP).

## Web (4 catégories)
- Institution : pages officielles ci-dessus (Wayback) ; ZB Zürich « Les plateformes e-rara et e-manuscripta » (Visual Library, hébergé par l'ETH, interfaces OAI, IIIF, textes, Z39.50).
- Utilisateurs : recherche « e-manuscripta.ch OAI harvest timeout blocked 429 OR 503 … » : **aucun résultat** propre à e-manuscripta (seulement des cas génériques d'autres entrepôts OAI).
- Tickets : recherche GitHub/outils (e-manuscripta, e-rara, manifeste IIIF) : **aucun ticket** trouvé ; seul un outil tiers (iiif-dl, iiifdownloader) cite e-rara, sans limite (résumé de moteur, non vérifié).
- Présentations : billet de l'Universitätsbibliothek Basel du 2022-09-08 (refonte du site, IIIF, Mirador, export RIS), lu en entier : ni OAI, ni quota, ni bots.

## Conclusion
Limite chiffrée : **aucune**. Règles écrites : copie systématique sur d'autres serveurs soumise à accord écrit ; `robots.txt` `Disallow: /` pour tous les robots sauf Bingbot et Googlebot ; paquets OAI de 10 notices ; délais possibles sur les gros METS. Les API répondent en 200 sans en-tête de limite. Confiance : moyenne (pages de doc actuelles illisibles derrière le défi ; copies de 2025). Si Marcel peut ouvrir `/wiki/apiinfo` et `/wiki/termsOfUse` dans un navigateur, comparer à ces copies.
