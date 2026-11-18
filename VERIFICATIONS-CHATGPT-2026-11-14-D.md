# Rattrapage documentaire D — 14 novembre 2026

Cette passe poursuit l'examen des dossiers **GLAM-009 à GLAM-023**. Elle distingue « URL antérieure non lue », « source officielle pertinente retrouvée » et « réponse technique de sonde non établie ». Source primaire des tâches : `institutions/<slug>/data.json` à la branche `claude/veille-iiif-quotas`, commit `c6bc71173f861502bd96d438f4489328ccf81b9e`.

## GLAM-009 : National Gallery (Londres)
- **L'ancienne URL** `https://research.ng-london.org.uk/ss-iiif/end-points` **renvoie bien 404** depuis l'outil web : il n'est pas légitime de l'indiquer « quota non publié » sans rechercher son contexte.
- Il existe **deux surfaces distinctes** :
  - L'**explorateur IIIF de projets de recherche** à `https://research.ng-london.org.uk/iiif-projects/` ; documentation de cette interface : Collections IIIF et Manifests, groupes de ressources, affichage dans Mirador. Cette page n'est pas un contrat d'API de recherche et n'annonce pas de quota.
  - La **documentation institutionnelle actuelle « Collection image APIs »** `https://www.nationalgallery.org.uk/documentation/ngacuk/collection-images` (lue le 14/11) dit que le service complet IIIF Image + Presentation est **en cours d'implémentation** dans son DAM ; un service Image API reste disponible en attendant à `https://data.ng.ac.uk/iiif/3/{image PID}/{region}/{size}/{rotation}/default.jpg` avec un exemple explicitement documenté. **Aucun plafond req/min n'est trouvé dans la page** ; cela n'implique pas l'absence de limite technique.
- Le contexte de l'ancienne interface est corroboré par le dépôt du projet `https://github.com/jpadfield/iiif-discovery`, dont le README évoque les Simple IIIF Discovery End-points. **Ne pas confondre** ces exemples de recherche expérimentale avec les conditions institutionnelles du domaine `data.ng.ac.uk`.
- **Résultat** : l'absence de lecture de l'ancienne route ne doit pas laisser croire qu'aucune documentation IIIF n'existe. La documentation de référence actuelle peut être reliée à la fiche ; les quotas techniques restent **non déterminés**.

## GLAM-013 : National Library of Norway
- `https://www.nb.no/services/search/v2/` demeure **inaccessible** à l'outil web. Les deux anciens timeouts sont documentés par le dossier.
- **OpenAPI officielle alternative accessible** : `https://api.nb.no/catalog/v1/items/api-docs` (OAS 3.1, page actuelle consultée 14/11), avec `GET /catalog/v1/items`, `GET /catalog/v1/search`, `GET /catalog/v1/aggregations`, `GET /catalog/v1/musicsearch`. Son interface lisible est `https://api.nb.no/` (Swagger UI).
- Les réponses documentées incluent 400, 401, 404, 500 ; l'absence de 429 dans la spécification **n'établit pas** qu'aucune limitation de débit existe. Ne pas inférer qu'il s'agit d'une redirection de l'ancienne Search v2 sans preuve de migration.
- **Résultat** : documentation de recherche **récupérée via une nouvelle API officielle**, ancien endpoint non vérifié, quota toujours non chiffré pour cette famille.

## GLAM-015 : Leiden University Libraries
- Deux robots.txt identiques apparaissent **en double** dans `a_verifier_manuellement` : `https://www.library.universiteitleiden.nl/robots.txt` est cité deux fois. Cette duplication devrait être corrigée à l'intégration.
- Les deux URLs robots `https://www.library.universiteitleiden.nl/robots.txt` et `https://iiif.universiteitleiden.nl/robots.txt` **restent illisibles** à l'outil web. Ne pas extrapoler le Crawl-delay 10 secondes du sous-domaine `digitalcollections.universiteitleiden.nl` à l'Image API.
- La page institutionnelle `https://www.library.universiteitleiden.nl/` est **consultable** et pointe vers les Digital Collections. Ce fait ne remplace pas les versions robots ni les en-têtes IIIF.
- **Résultat** : aucune nouvelle preuve de débit ; dédoublonnage documentaire nécessaire ; contrôles techniques toujours ouverts.

## GLAM-014 : National Library of Finland — Finna
- Suite aux vérifications des rapports antérieurs, les URL de spécification `https://api.finna.fi/v1?swagger` et `https://api.finna.fi/api/v1/?openapi` n'ont pas fait l'objet d'une nouvelle récupération directe dans cette passe. Les déclarations du portail Kiwi **ne sont pas** une preuve des en-têtes ou du fonctionnement de l'hôte API. Statut **ouvert**.

## GLAM-017 : Biblissima+
- `https://query.biblissima.fr/` reste à considérer comme une ressource **sous accès contrôlé (401)** d'après les essais du dépôt. `https://doc.biblissima.fr/api/sparql/` décrit l'accès sur demande. **Ne pas transformer une clé ou demande d'accès en quota supposé de SPARQL**. Pour l'API de réconciliation, le paramètre `limit` est un nombre de résultats et **pas** une limite de requêtes/minute.

## GLAM-018 : e-codices
- L'item `https://www.e-codices.unifr.ch/en/about/contact` figure parmi les « pages manuelles » **bien qu'il ait déjà été lu** ; la seule action reste une **prise de contact** pour une éventuelle politique non publiée. Déplacer cet item en catégorie « réponse institutionnelle requise », plutôt que « page illisible ».

## GLAM-021 : EPFL Plume
- **Erreur d'inférence potentielle dans `data.json`** : le champ `limites_documentees` donne la valeur **« aucune »** pour une ligne « Crawl-delay / limite de débit » parce que le `robots.txt` ne contient pas de `Crawl-delay` et interdit seulement `/admin/` et `/login`. **Une absence de `Crawl-delay` ne démontre en aucun cas une absence de limitation applicative de débit.** Scinder en deux assertions : `robots.txt : aucun Crawl-delay déclaré` (si vérifié) ; `rate limits HTTP : non documentés / non établis` sauf autre source.
- Risque de classement erroné « illimité » dans le benchmark à vérifier en priorité. **Pas de nouveau test réseau réalisé**.

## GLAM-016, 019, 020, 022, 023
- Les autres dossiers (Ghent sans URL manuelle, e-rara/e-manuscripta documentés en première passe, Hedera/Bodmer Lab documenté seulement par archive ou index, Fragmentarium sans URL manuelle) ne sont **pas revalidés techniquement** par ce rapport. Les précédentes preuves restent à confronter.

## Vérifications nécessaires pour conclure
- National Gallery : déterminer le statut actuel du service expérimental `ss-iiif`, sans le confondre avec `data.ng.ac.uk`, et relever les conditions/quotas d'Image API séparément des projets de recherche.
- Norway : identifier si l'ancienne Search v2 est dépréciée via preuve officielle ; ne pas classer « remplaçant officiel » sans avis de migration.
- Leiden : robots.txt des deux hôtes et élimination du doublon.
- EPFL : corriger la notion « aucun rate limit » tirée du seul robots.txt.
