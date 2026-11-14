# Plan de rattrapage documentaire — 14 novembre 2026

## Portée et traçabilité
Branche de travail : `chatgpt/rattrapage-documentation-2026-11-14`, issue de `claude/veille-iiif-quotas` au commit `c6bc71173f861502bd96d438f4489328ccf81b9e`.
Périmètre : 93 dossiers d'institutions ; BnF Gallica et BnF OpenAPI restent écartées conformément à `CONSIGNE.md`. Cette opération porte **sur les trous documentaires et les URL `a_verifier_manuellement`**, et non sur une certification de toutes les API, ni sur le crash-test g.

Une preuve de consultation par un outil de lecture web n'est **pas** une preuve HTTP (statut, en-têtes, absence de protection anti-bot), ni une preuve de possibilité de téléchargement automatisé depuis le poste d'origine. L'absence de quota dans une page particulière ne démontre pas l'absence d'un quota global.

## Boucle déterministe par institution
1. **Inventorier** `data.json` : `a_verifier_manuellement`, sources incertaines, `non_teste`, rubriques f incomplètes, citations sans texte original, discordances `fiche.md`/`data.json`. Ne jamais considérer un `mailto:`, un GitHub déjà lu, une ancienne URL 404 ou une ressource hors périmètre comme un « blocage manuel » sans justification.
2. **Qualifier chaque URL** : (A) doc officielle en direct, (B) copie indexée/archive seulement, (C) redirection ou ressource déplacée, (D) erreur 404/410, (E) refus 401/403/CAPTCHA/défi, (F) DNS/TLS/délai, (G) authentification/contact humain requis, (H) vérification technique HTTP distincte, (I) URL informative sans action.
3. **Vérifier en priorité** les portails développeurs, conditions et pages d'aide, puis les PDF/présentations et les rapports de tiers. Lire la source et chercher explicitement `rate limit`, `requests`, `quota`, `throttle`, `429`, `Retry-After`, `API key`, `fair use`, `robots`, `crawl`, `IIIF`, et les équivalents locaux.
4. **Distinguer les familles** Image API / Presentation API / Search API / OAI / SRU / SPARQL / APIs généralistes ; une limite de l'API Search ne prouve rien sur un service IIIF.
5. **Chercher une deuxième source** si une page est muette ou incohérente : documentation versionnée, OpenAPI/Swagger, tickets publics, billets institutionnels, conférence, FAQ et archives ; conserver les contradictions documentaires.
6. **Renseigner les résultats** dans `REVÉRIFICATIONS-CHATGPT.md` (URL exacte, date, outil, source, fait observé, qualité de preuve, statut et travail résiduel). Ne pas cocher automatiquement les étapes a–g de la méthode v2/v3. Ne pas transformer une lecture web en test de la sonde. Ne pas supprimer le blocage historique dans `data.json` avant que la preuve requise par sa formulation ne soit satisfaite.
7. **Contrôle de qualité** : une ligne par URL ; historique du blocage distinct de l'état aujourd'hui ; ne jamais déduire `illimité` du silence de la documentation ; ne pas inventer d'en-tête ni de code HTTP. Si le site reste bloqué, l'item reste ouvert.
8. **Intégration** : les changements de source de vérité (`data.json`, `fiche.md`) et du classeur `BENCHMARK.xlsx` doivent être effectués ensemble par le pipeline local existant (`scripts/suivi.py` / `scripts/build_benchmark.py`) pour ne pas laisser un Excel divergent. Cette branche de recherche sépare donc les résultats documentaires de la validation et de la régénération du classeur.

## Ordre et priorités
- **P0** : contradictions sur des plafonds chiffrés, risques de mauvaise attribution entre familles d'API, conditions interdisant un usage automatisé.
- **P1** : URL d'API/de documentation inaccessibles et essentielles pour les quotas ou modalités d'authentification.
- **P2** : conditions d'utilisation, robots.txt, documents sur les bots, articles institutionnels.
- **P3** : archives anciennes, FAQ généralistes, pages informatives ou de contact.
- Reprendre **dans l'ordre GLAM-001 à GLAM-084**, puis les 9 hors périmètre, en ignorant uniquement les deux dossiers explicitement écartés.

## Politique d'accès
Lecture de sources publiques par navigateur/recherche/index sans contournement des CAPTCHA, sans usurpation de client, sans tests de charge ni rafales de requêtes. Une page visible par index n'autorise pas à conclure qu'une sonde peut y accéder, et un robots.txt permissif n'autorise pas nécessairement le moissonnage. Si une validation exige une session authentifiée, un contrat ou un contact institutionnel, l'item est classé `INTERVENTION REQUISE`.

## Critères de fin
- Chaque item `a_verifier_manuellement` initial est soit documenté avec preuve et statut, soit conservé comme blocage motivé.
- Chaque dossier bénéficie d'une synthèse des autres manques identifiés.
- Tous les constats sur des quotas séparent « officiel/documenté », « observé HTTP » et « hypothèse ».
- Les éléments que seul un navigateur authentifié, l'administration de l'institution ou une sonde contrôlée peuvent établir restent explicitement ouverts.
- Un passage final contrôle l'absence de contradictions et la cohérence du benchmark avant intégration.

**Limite de cette exécution** : la session ChatGPT ne constitue ni un worker persistant ni une sonde HTTP depuis l'IP de l'utilisateur ; les vérifications non conclues ne doivent pas être marquées comme faites.
