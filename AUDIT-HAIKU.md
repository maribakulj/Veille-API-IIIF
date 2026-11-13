# Audit du travail fait par Haiku (2026-11-13) contre METHODOLOGY.md v2

Audit réalisé par Sonnet 5.5 le 2026-11-13, à la demande de Marcel, sur le contenu du dépôt
(fiches, journaux, sources, configurations, historique Git). Chaque constat ci-dessous vient d'un
contrôle fait sur les fichiers, pas d'un rapport d'agent.

## Verdict

**Le travail de Haiku ne suit pas la méthode v2 de bout en bout.** Les 20 institutions de la
première passe sont à refaire intégralement. Les 6 institutions de la passe v2 de Haiku sont à
compléter et à contrôler une par une. Les journaux eux-mêmes sont utilisables comme historique
(aucune pause < 6 s, GET/HEAD seulement, User-Agent honnête), mais pas comme preuve de la
méthode v2.

## Ce qui est conforme (vérifié)

- Aucune pause < 6 s entre deux requêtes vers un même hôte dans les journaux datables.
- Seulement des méthodes GET et HEAD ; aucun POST ; aucun User-Agent de navigateur.
- Aucune ligne perdue dans les journaux (historique Git contrôlé) ; l'écart signalé pour
  Harvard, Princeton et NYPL n'a rien effacé.
- Les statuts des journaux concordent avec les en-têtes bruts de `tests/raw/` (aucune divergence).
- Aucun contournement de blocage 403.

## Écarts constatés

### Écarts de méthode (sur l'ensemble)

| # | Écart | Preuve |
|---|---|---|
| 1 | **16 fiches se déclarent « vérifiée » ou « complète »** alors que la méthode v2 n'a pas été appliquée | `grep Statut institutions/*.md` |
| 2 | **Étape a) non faite** pour 20 institutions : aucune page de doc sauvegardée, aucune empreinte, lectures par résumé d'outil | `sources/` n'existe que pour 6 institutions ; 9 fiches citent « en résumé » ou « tronqué » |
| 3 | **Étape f) (web) absente ou minimale** pour les 20 institutions de la première passe | aucune section dédiée dans les fiches |
| 4 | **Configuration écrite après les tests**, pas avant, pour les 20 institutions : les `scripts/config/*.json` ont été reconstitués pour documenter des requêtes déjà faites | historique Git des configurations |
| 5 | **Adresses devinées** (interdit par l'étape b) : Wellcome `image/v2/…` (400), MDZ `/iiif/` (404, issue du CSV), KB-DK URL « reconstituées », EAP `about-eap` et `terms` (404), Édimbourg `/art/terms` (404) | fiches wellcome, kb-dk ; institutions/mdz/tests/journal.log ; institutions/eap-bl/sources, edinburgh-art |
| 6 | **Données du classeur saisies de mémoire** : `data/institutions.json` a été alimenté à partir de rapports de conversation, pas relu fiche par fiche | commit ae3b5b9 |
| 7 | **`institutions/eap-bl.md` n'existe pas** ; `institutions/edinburgh-art/fiche.md` ne contient que la section ajoutée, sans en-tête de fiche | `ls institutions/` |

### Écarts de prudence

| # | Écart | Preuve |
|---|---|---|
| 8 | **Budget de 15 requêtes dépassé** : Bodleian 25 requêtes (13 de l'agent + 12 de ma relance), MDZ 16 | journaux `institutions/bodleian/tests/journal.log`, `institutions/mdz/tests/journal.log` |
| 9 | **Test hors dépôt** : MDZ a été testé avec `mdz-nouveaux.json`, configuration non committée | fiche MDZ, section « Correction » |
| 10 | LoC : plafond de 12 requêtes de la consigne dépassé (13) | rapport de l'agent LoC |

### Écarts de processus

| # | Écart | Preuve |
|---|---|---|
| 11 | Vingt agents lancés en parallèle avec des consignes courtes ; fiches « vérifiées » sur 3 à 12 requêtes | historique de session |
| 12 | Une consigne d'agent sans institution (« TON INSTITUTION : » vide), corrigée par message | historique de session |
| 13 | Message de commit trompeur : le commit `wellcome` contenait aussi les fichiers `loc` | commit b7c2803 |
| 14 | Commit avec un JSON invalide pour Édimbourg (aucune donnée ajoutée) | commit 5c47f81 |
| 15 | Empreintes SHA-256 des agents irreproductibles (MDZ) | corrigé par `scripts/fetch_doc.sh` |
| 16 | Un fichier parasite (`sources/robots-cudl-edinburgh.txt.list`) laissé dans `sources/` | supprimé le 2026-11-13 |

## Verdict par institution

| Institution | Passe | Conforme v2 ? | Décision |
|---|---|---|---|
| bnf-gallica | v2 (Haiku) | sans objet | **écartée à la demande de Marcel** |
| bodleian | v2 (Haiku) | non : budget 25 > 15, f) partiel (blog lu en résumé) | compléter |
| eap-bl | v2 (Haiku) | non : pas de fiche, pas de configuration, f) non fait | refaire |
| cudl | v2 (Haiku) | non : a) partiel, g) bloquée | compléter |
| edinburgh-art | v2 (Haiku) | non : fiche absente, pas de configuration | refaire |
| mdz | v2 (Haiku + contrôle) | non : budget 16 > 15, test hors dépôt, f) partiel | compléter |
| loc, internet-archive, wellcome, british-library, europeana, e-codices, vatican, slub, hab, kb-nl, kb-dk, nb-no, bne, rijksmuseum, smithsonian, getty, harvard, princeton, nypl | première passe | non | **refaire intégralement** |
| bnf-openapi | abandonnée | sans objet | rester abandonnée |

## Règles ajoutées après l'audit

- **Le budget de 15 requêtes s'applique par passe** d'une institution (une passe = un déroulé complet de la méthode). Les anciennes passes restent archivées dans leurs journaux, sans être comptées.
- **Aucune étape n'est marquée « non applicable » sans citer** la phrase de la doc qui la justifie.
- **Aucune fiche n'est marquée « vérifiée »** avant que les étapes a) à f) aient chacune leur fichier de preuve et que l'orchestrateur ait contrôlé ces preuves.
- **`data/institutions.json` n'est alimenté qu'à partir de la fiche relue** de l'institution, jamais de mémoire.

## Décisions de Marcel après l'audit

- **BnF Gallica : écartée** (2026-11-13). C'est l'institution de Marcel, l'audit n'est pas nécessaire. Les sources déjà téléchargées restent dans `institutions/bnf-gallica/sources/` à titre d'historique, sans être poursuivies.
- **BnF OpenAPI : abandonnée** (2026-11-13, déjà décidé).
