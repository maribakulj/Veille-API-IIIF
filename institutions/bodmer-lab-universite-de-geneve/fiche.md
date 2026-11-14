# Bodmer Lab – Université de Genève (`bodmer-lab-universite-de-geneve`)

- **Classeur** : GLAM-022 · Suisse · **Vérifié le** 2026-11-14 par Sonnet 5.5 (lot D) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Chaîne d'hôtes** : `bodmerlab.unige.ch` (site Concrete5, manifeste IIIF 2 annoncé par la page Mirador) → `iiif.hedera.unige.ch` (hedera, UNIGE : manifestes et IIIF Image 2 niveau 2).

## Sources
- `bodmerlab.unige.ch` (accueil, À propos, Réalisations, Images, notice, page Mirador) : sources/a, a2, a3. Pas de page de documentation d'API ni de conditions d'usage d'API ; mention « Sauf indication contraire, les contenus de ce site sont publiés sous une licence Creative commons CC-BY-NC, 4.0. »
- `fondationbodmer.ch` (recherche, reproductions, CGV) : sources/a, a4, a6 ; images en accès libre : « the copyrights in force remain the same » et crédit demandé.
- `robots.txt` lus : bodmerlab (16 Disallow techniques, pas de Crawl-delay), fondationbodmer (**Crawl-delay 10**), hedera.unige.ch (**Crawl-delay 40**, Disallow /dataset), iiif.hedera.unige.ch (**401**), www.unige.ch (défi JavaScript ; réplique Wayback : Crawl-delay 5).
- `www.unige.ch` e-Research (hedera, What is IIIF) : défi JavaScript F5/TSPD, non contourné ; lus sur Wayback (`sources/wayback/unige-ch.md`).

## Tests (2 passes, configurations committées avant lancement, pause 10 s)
| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | manifeste `bodmerlab.unige.ch/fr/constellations/autographes/manifest/1072205386` | **200**, 238 ko lus |
| 2 | manifeste `iiif.hedera.unige.ch/iiif/manifests/bodmerlab/IIIFManifest_1072205386.json` (HEAD) | **200** |
| 2 | `…/iiif/2/bodmerlab/1072205386/1072205386_002.jpg/info.json` | **200** |
| 2 | dérivé `full/pct:2/0/default.jpg` | **200** |

Aucun 429, aucun en-tête `Retry-After`, `X-RateLimit-*` ni `RateLimit-*`. Non testés : image pleine taille de l'exemple UNIGE (autre projet), SPARQL et collections hedera (URL absentes des sources).

## Web (4 catégories)
- Institution : conditions de reproduction de la Fondation (lues). Présentations : UNIGE e-Research (Wayback lu). Utilisateurs, tickets : aucun résultat visant Bodmer Lab ; le guide IIIF (guides.iiif.io) indique le bouton Mirador pour trouver le manifeste.

## Incident d'outil
`fetch_doc.sh` a envoyé 3 requêtes de suite à `www.unige.ch` malgré un défi JavaScript dès la première (l'outil n'arrête pas un hôte défié). Pas de contournement ; Wayback utilisé.

## Conclusion
- **Limite documentée chiffrée** : aucune. Seuls les Crawl-delay (10 s Fondation, 40 s hedera.unige.ch, 5 s unige.ch) ; licence CC BY-NC 4.0 et crédit demandé.
- **Limite observée** : aucune. **En-têtes** : aucun. **Moyen d'interroger le quota** : aucun.
- **Crash test (g)** : configuration `config/crash-iiif-hedera-info.json` préparée, non lancée (hôte UNIGE sans réseau protégé détecté à vérifier par crash.py).
- **Confiance** : moyenne (pas de documentation d'API ; e-Research lu via Wayback).

## Crash test (étape g)

Crash test fait le 2026-11-14 : hedera-info-json sur iiif.hedera.unige.ch : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/bodmer-lab-universite-de-geneve.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
