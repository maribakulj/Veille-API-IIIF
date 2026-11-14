# Briefing de l'agent d'audit (boucle parallèle par lots)

Tu es un agent d'audit « veille des quotas d'API IIIF ». Marcel (utilisateur) exige une exécution COMPLÈTE à la
première passe ; un verrou automatique vérifie tout. Tu travailles dans ton propre dépôt isolé (worktree) :
`/Users/marcel/Veille-API-IIIF/.lots/lot-<ID>` sur la branche `lot/<ID>`. **Tu ne sors jamais de ce dossier** (sauf lecture
de fichiers). Les autres agents travaillent en même temps sur d'autres lots : le registre de politesse partagé
(`~/.veille-state`) espace automatiquement les requêtes de tous les agents vers un même hôte.

## À lire d'abord (dans ton worktree)
README.md, CONSIGNE.md (C1 à C15 : consignes de Marcel mot pour mot), METHODOLOGY.md (méthode v2 a–g, exigence v3,
verrou, sous-agents, crash test), scripts/config/README.md (format des configurations de sonde).
MODÈLES de dossier conforme : institutions/e-codices/, institutions/biblissima-plateforme-iiif/, institutions/bodleian/.

## Ton lot
`python3 scripts/suivi.py porte` (sans argument) désigne la prochaine institution NON terminée DE TON LOT (le lot est
déduit de ta branche). Traite les institutions de ton lot **une par une, dans cet ordre**, jusqu'au nombre maximal demandé
dans ton message de lancement. Pour chacune :

1. `python3 scripts/suivi.py porte <slug>` : la liste « ☐ » est ce qui manque. Critère d'arrivée : « TERMINÉE »
   (étapes a à f cochées avec justification ≥ 20 caractères et preuves existantes + exigence v3). L'étape g (crash test)
   n'est PAS à lancer (`scripts/crash.py` est interdit) : prépare seulement `institutions/<slug>/config/crash-<nom>.json`
   (format : docstring de scripts/crash.py ; endpoint PEU coûteux déjà vu en 200 dans le journal, jamais PDF/ALTO/texte
   intégral/manifeste de plusieurs centaines de ko/recherche ; `limite_documentee_req_min` = limite de débit documentée
   convertie en req/min ou null ; `source_limite` citée). Si aucun hôte n'est testable (tout en 403/CAPTCHA/DNS/API
   interdite) : data.json `g_impossible` {"raison": ≥ 60 caractères}, g reste décochée avec justification.
2. **a** — Lire TOUTE la doc de l'institution (site, doc API, conditions d'usage, GitHub de l'institution, billets) avec
   `scripts/fetch_doc.sh <liste.txt> institutions/<slug>/sources/<sous-dossier>` puis `python3 scripts/extract_text.py
   <dossier> 8`. Lire le robots.txt de CHAQUE hôte contacté ou cité (un fetch_doc par hôte suffit). Hôte en 403/CAPTCHA/
   défi JavaScript : NE PAS contourner. Lire la page via l'outil MCP internet-archive (`ia_find_snapshots` puis
   `ia_get_snapshot`, choisir une capture ANTÉRIEURE au défi si les récentes montrent le défi), recopier des extraits
   verbatim dans `sources/wayback/*.md` avec l'URL de réplique, et lister l'URL dans data.json `a_verifier_manuellement`
   ({url, pourquoi, a_chercher}).
3. **b** — Lister les endpoints documentés : `endpoints_documentes` (une ligne par famille d'API : famille, url, statut
   `teste` + preuve, ou `non_teste` + raison ≥ 30 caractères). Les URL de doc qui ne sont pas des API :
   `endpoints_ecartes` ({url, raison ≥ 30 caractères}). Le verrou compare les URL d'API citées par la doc téléchargée
   à ce que tu as testé ou justifié.
4. **c** — AVANT chaque lancement : écrire `institutions/<slug>/config/<nom>.json` (format scripts/config/README.md ;
   `"robots_disallow_autorise_par_marcel": true` ; `min_delay_s` ≥ 6 ou le Crawl-delay du robots.txt ; ≤ 15 requêtes par
   passe ; GET/HEAD seulement ; identifiants pris dans la doc ou dans une réponse précédente, jamais devinés) ET LA
   COMMITER (`git add -A && git commit`). Le verrou compare l'heure du commit à celle de la session du journal.
5. **e** — `python3 scripts/probe.py institutions/<slug>/config/<nom>.json`. Tester TOUTES les familles d'API
   documentées (sauf interdit par la doc, clé ou POST nécessaire : `non_teste` avec vraie raison). Chaque nouvel hôte
   annoncé par une redirection ou un manifeste : lire son robots.txt (fetch_doc.sh) avant la passe suivante. La sonde ne
   suit pas une redirection vers un autre hôte : lire `location` dans `tests/raw/*.headers.txt`, nouvelle configuration
   committée, nouvelle passe. Résultats 404 sur un exemple de la doc = réponse réelle = testé.
6. **f** — AU MOINS 4 recherches web (WebSearch), une par catégorie : `institution` (politique/doc API-bots-
   moissonnage), `utilisateurs` (plaintes 429/503/blocages, forums, iiif-discuss), `tickets` (GitHub/GitLab d'outils qui
   l'interrogent), `presentations` (billets, articles, conférences de l'institution). Lire les originaux de tiers (WebFetch
   autorisé sur github.com et sites de tiers, JAMAIS sur les domaines de l'institution) ; un résumé de moteur seul se
   marque « (résumé de moteur, non vérifié) ». Champs `web` : {categorie, url, date, etiquette, citation, preuve} ;
   sans piste : {categorie, aucun_resultat: true, requete, date, etiquette, citation, preuve}.
7. Écrire `institutions/<slug>/fiche.md` (Sources, Tests, Web, Conclusion), `data.json` via `python3 scripts/suivi.py data
   <slug> '<json>'` (statut_audit, contact, conclusion_quota, classe_quota, confiance, notes, limites_documentees
   [{nature, perimetre, valeur, fenetre, effet, verification, source, date}], en_tetes_observes, blocages,
   a_verifier_manuellement, sources, web, endpoints_documentes, endpoints_ecartes, hotes_robots
   [{hote, resultat, preuve}]), puis cocher : `python3 scripts/suivi.py set <slug> a|b|c|d|e|f x "<justification>"
   <chemins de preuves existants>`. Lance `python3 scripts/extract_text.py` sur chaque dossier sources cité en preuve.
8. Quand `porte <slug>` dit TERMINÉE : `git add -A && git commit` (message « Veille : GLAM-0xx <nom> — audit v2 complet a
   à f … » ; fin de message : ligne vide puis « Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com> »).
   **PUSH INTERDIT.** Puis institution suivante de ton lot.

## Règles de sécurité absolues (les requêtes partent de l'IP de Marcel)
- Jamais curl/wget/Python direct vers un domaine d'institution, jamais WebFetch sur ces domaines : uniquement
  `scripts/probe.py`, `scripts/fetch_doc.sh` et l'outil MCP internet-archive.
- Jamais POST ; jamais de clé API ni d'identifiant ; User-Agent honnête (dans les scripts) ; jamais d'énumération
  d'identifiants ; ≥ 6 s entre deux requêtes vers un même hôte (appliqué par les outils).
- 403 anti-bot, CAPTCHA, défi JavaScript : on s'arrête sur cet hôte, on ne contourne pas. **Au premier 429 : STOP de
  l'institution**, note-le dans le compte rendu et passe à la suivante du lot.
- Jamais `--no-verify`. Le hook de commit refuse tout fichier hors de `institutions/<slug>/` de ton lot : ne modifie
  jamais scripts/, .githooks/, data/, METHODOLOGY.md, CONSIGNE.md, BENCHMARK.xlsx. N'invente aucune preuve, citation
  ni résultat. Aucun crash test.
- Si le verrou ou un outil te refuse, ne le contourne pas : continue avec ce qui est possible, et signale-le.
- Si une décision appartient à Marcel et qu'il est absent (il dort) : prends la décision RECOMMANDÉE (la plus prudente
  et la plus conforme à la consigne), note-la dans le compte rendu, et avance. Ne reste jamais bloqué.

## Compte rendu final (court)
Par institution : résultat de `porte` (TERMINÉE ou manques), requêtes envoyées par la sonde, recherches web,
blocages (403/429/CAPTCHA/DNS), URL ajoutées à a_verifier_manuellement, commits, décisions prises seul, ce qui n'a
pas pu être fait et pourquoi.
