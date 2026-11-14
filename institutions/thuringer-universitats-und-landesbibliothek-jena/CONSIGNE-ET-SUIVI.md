# Thüringer Universitäts- und Landesbibliothek – Jena — consigne et suivi

- **Dossier** : `institutions/thuringer-universitats-und-landesbibliothek-jena/`  ·  **Classeur de référence** : GLAM-075  ·  **Pays** : Allemagne
- **Statut d'institution** : active
- **Dernière mise à jour du suivi** : (à renseigner à chaque modification)

## Suivi par étape (à cocher, avec justification et preuves)

### a) Documentation lue en entier
> Toutes les pages de doc liées à l'API (développeurs, interfaces, conditions, FAQ, aide, mentions légales, robots.txt), téléchargées avec `scripts/fetch_doc.sh` (URL, date, SHA-256), lues en entier (`scripts/extract_text.py`).

- [ ] **Pas fait**
  - **Justification** : Pas encore traitée : l'audit suit l'ordre du classeur de référence (une institution à la fois).
  - **Preuves** : 

### b) Endpoints tirés de la doc
> Liste des endpoints citée par la doc (URL, exemples). Jamais devinée. Une interdiction ou une impossibilité écrite dans la doc justifie de renoncer (citer la phrase).

- [ ] **Pas fait**
  - **Justification** : Pas encore traitée : l'audit suit l'ordre du classeur de référence (une institution à la fois).
  - **Preuves** : 

### c) Configuration écrite AVANT les tests
> `config/<nom>.json` pilote `scripts/probe.py`, committée avant le lancement. Un endpoint absent de la doc mais non interdit se teste avec un script poli (identifiants issus de pages publiques ou d'exemples de la doc, pas de devinette).

- [ ] **Pas fait**
  - **Justification** : Pas encore traitée : l'audit suit l'ordre du classeur de référence (une institution à la fois).
  - **Preuves** : 

### d) Quota cherché dans la doc
> Pour chaque page lue : endpoint de statut, en-têtes de limite documentés, clé ou compte donnant un quota, contact pour un volume plus élevé. Chaque réponse cite sa source.

- [ ] **Pas fait**
  - **Justification** : Pas encore traitée : l'audit suit l'ordre du classeur de référence (une institution à la fois).
  - **Preuves** : 

### e) Test systématique de chaque endpoint
> Chaque endpoint documenté est testé (budget 15 requêtes par passe, pause ≥ 6 s, GET/HEAD, UA du projet). Redirections du même hôte suivies. Un 403 arrête son hôte, un 429 arrête l'institution. Seules les interdictions écrites dans la doc dispensent de tester.

- [ ] **Pas fait**
  - **Justification** : Pas encore traitée : l'audit suit l'ordre du classeur de référence (une institution à la fois).
  - **Preuves** : 

### f) Ce que disent les gens sur le web
> Plaintes, discussions, présentations de l'institution, politique envers les API et les bots, blogs, GitHub, forums, listes de diffusion. Sources étiquetées (officielle / institution / utilisateur / tiers), lues, citées.

- [ ] **Pas fait**
  - **Justification** : Pas encore traitée : l'audit suit l'ordre du classeur de référence (une institution à la fois).
  - **Preuves** : 

### g) Crash test progressif
> Seulement après l'audit complet (a à f) de toutes les institutions et avec l'accord de Marcel : paliers jusqu'à 2 × la limite documentée, ou 200 req/min si illimité ou sans limite documentée. Arrêt au premier 429/403/CAPTCHA.

- [ ] **Pas fait**
  - **Justification** : Pas encore traitée : l'audit suit l'ordre du classeur de référence (une institution à la fois).
  - **Preuves** : 

### Contrôles transversaux
- Budget : 15 requêtes par passe · pauses ≥ 6 s · GET/HEAD seulement · UA du projet · aucun contournement. Ces contrôles sont calculés depuis le journal (voir « Contrôles automatiques »).

<!-- AUTO:DEBUT -->
## Contrôles automatiques (calculés depuis `tests/journal.log`)
- Requêtes enregistrées : **3** (sessions de sonde : 1, maximum par session : 3)
- Plus courte pause vers un même hôte : **10 s** (règle : ≥ 6 s)
- Méthodes utilisées : GET (règle : GET/HEAD seulement)
- Anomalies : aucune
<!-- AUTO:FIN -->

## Consigne intégrale

<!-- CONSIGNE:DEBUT -->
# Consigne intégrale de Marcel (source unique)

Ce fichier est recopié tel quel dans le fichier `CONSIGNE-ET-SUIVI.md` de **chaque** dossier d'institution
(par `scripts/suivi.py sync`). Il contient d'abord les consignes de Marcel, mot pour mot et dans l'ordre
où elles ont été données, puis la méthode (`METHODOLOGY.md`) qui les applique.
Les consignes plus récentes l'emportent sur les plus anciennes quand elles se contredisent
(par exemple : plus de sous-agents).

## 1. Consignes de Marcel (verbatim, 2026-11-13)

**C1 — mission initiale**
> je veux que tu travaille ici sur le repo veille IIIF API sur mon github, tu mettra à jour ta branche sur github à chaque nouveau commit. Je veux que tu reprennes le travail en vérifiant toutes les institutions une par une, tu dois chercher toute la doc, toutes les infos pour chacune à fond en cherchant partout, site, code, github, articles, etc. Si tu ne trouve rien sur les quotas, la doc sur les rates limit ou tout autre élément de doc tu dois trouver pourquoi ils ne la publient pas. Je veux aussi que tu testes une par une chaque API depuis ici de manière très prudente pour essayer de voir si elles annoncent les rate limit avec des appels qui suivent la doc, si l'API les annonce quand on les appelle, etc. Je veux que tu lance une boucle et des sous agents haiku pour aller plus vite et tu dois continuer la boucle jusqu'à ce que chaque institution ait été vérifiée intégralement. Pour ça chaque agent et sous agent doit tester une par une à fond

*(Remplacée par C9 : plus de sous-agents, tout est fait en direct, une institution à la fois.)*

**C2 — traçabilité**
> il faut que tout soit vérifiable et documenté et puisse être refait

**C3 — étape f) (web)**
> ou tu dois rechercher sur le net si des gens parlent de quotas, s'en plaignent, etc, s'il y a des présentations qui en parlent venant de l'institution, s'ils parlent de leur politique vis à vis des API, des bots, etc, tout ce qui est relatif à l'usage des api dans cette institution sur le web

**C4 — recherche exhaustive**
> je ne veux pas que tu t'arrêtes là, tu dois scanner tout le site de la bayerische pour trouver et tu dois chercher sur internet s'il y a des gens qui en parlent

**C5 — crash test (étape g)**
> une sorte de crash test pour voir jusqu'ou on peut aller, progressivement
> avant de se faire bloquer (sans abuser non plus et lancer 1000 requetes/min), on fixe un seuil à 200/min, notamment pour voir si quand c'est illimité ça l'est vraiment, evidemment on ne fait ça qu'une fois que toute l'appli a été bien testée et le dossie prêt pour éviter de se faire bannir avant d'avoir finit l'audit de l'institution
> *(précisé ensuite : plafond « 2 × la limite documentée » si une limite est documentée ; 200 req/min si annoncé illimité ou sans limite documentée)*

**C6 — périmètre et ordre**
> je veux les 84 dans l'ordre, avec la méthode complète, une par une
> saute Gallica, Gallica c'est moi donc pas besoin

**C7 — reprise après audit de Haiku**
> je veux que tu regarde tout ce qu'a fait Haiku et que tu vérifie s'il a bien suivi les consignes, si non, tu recommence et tu refait en suivant la méthode, il faut que ce soit un par un en suivant toute la méthode de bout en bout

**C8 — couverture des tests**
> pour chaque institution tout doit être testé systématiquement, toutes les consignes doivent être suivies, si par contre dans la doc on te dit que c'est interdit ou pas possible tu laisse tomber, mais si ce n'est pas écrit tu teste avec un script adapté en suivant la doc ou s'il n'y en a pas en faisant des scripts polis

**C9 — qualité et méthode de travail**
> t'es sûr que toutes les données pertinentes y figureront et que le classeur est bien fait en suivant la consigne ?
> tout doit être carré et sourcé
> ton idée de base était pas mieux ? *(→ deux plafonds pour le crash test)*
> pose toi et réflechis à la meilleur méthode pour ma consiggne *(→ une institution à la fois, pas de sous-agents, méthode v2)*

**C10 — le classeur Excel**
> je veux qu'il y en ai un dans le repo qui se mette à jour automatiquement avec toutes les infos rajoutées au fur et à mesure, je veux un fichier propre, avec des graphiques pertinents, toutes les infos pertinentes, etc

**C11 — dossiers et suivi (cette consigne)**
> je veux que tu crée un dossier par institution, dans chaque dossier il doit y avoir un fichier md avec toute l'intégralité de la consigne et à chaque étape tu dois cocher si ça a été fait avec justification
> et evidemment tout le travail doit être fait pour chaque institution dans le dossier correspondant, sans casser la ci du fichier excel qui doit se mettre à jour automatiquement

## 2. Règles de fonctionnement qui en découlent

- Tout le travail d'une institution se fait **dans son dossier** `institutions/<slug>/` : fiche, sources, tests, configurations, données.
- Chaque étape a) à g) est **cochée ou non, avec une justification et des preuves** dans `CONSIGNE-ET-SUIVI.md`. Une case cochée sans justification ou sans preuve existante bloque le commit (`scripts/suivi.py validate`).
- Le classeur `BENCHMARK.xlsx` est régénéré à chaque commit à partir des dossiers d'institutions.
- Si la doc dit qu'un test est interdit ou impossible : on y renonce, en citant la phrase. Si ce n'est pas écrit : on teste, avec un script adapté à la doc, ou à défaut avec un script poli (pause ≥ 6 s, User-Agent honnête, GET/HEAD, budget de 15 requêtes par passe, aucune énumération ni devinette d'identifiants : les identifiants viennent de pages publiques ou d'exemples de la doc).
- Aucun contournement : pas de faux User-Agent, pas de changement d'IP, pas de compte d'autrui.
- Les décisions de Marcel s'appliquent par institution : **BnF Gallica écartée**, **BnF OpenAPI abandonnée**.

**C12 — robots.txt (Marcel, 14/11/2026, mot pour mot)** : « quand le robot.txt interdit les robots, pourquoi tu t'arrêtes ? t'es pas un bot vu que t'es piloté directement par moi ici non ? »
→ Un `Disallow` de robots.txt n'arrête plus l'audit : on teste quand même, avec l'option `"robots_disallow_autorise_par_marcel": true` (le Disallow est journalisé). Restent obligatoires : Crawl-delay et pauses ≥ 6 s, budget ≤ 15 requêtes par passe, GET/HEAD seulement, User-Agent honnête, **aucun contournement de 403 / CAPTCHA**, aucun identifiant deviné. Remplace la phrase de C8 sur les interdictions, pour robots.txt seulement (une interdiction écrite dans des conditions d'utilisation reste respectée).

**C13 — pages illisibles : documenter, Marcel vérifie à la main (Marcel, 14/11/2026, mot pour mot)** : « non laisse tomber, je préfère juste que tu me le documente et j'irais voir moi même un par un, il me faudra un nouveau doc avec toutes les urls à vérifier manuellement pour chaque institutions, ça peut être par exemple un nouvel onglet du tableur excel »
→ Annule l'idée d'utiliser Chrome pour les 403. Chaque URL que la sonde ne peut pas lire (403, CAPTCHA, délai, TLS…) est listée dans `data.json`, champ `a_verifier_manuellement` (`url`, `pourquoi`, `a_chercher`), et apparaît dans l'onglet « À vérifier à la main » de `BENCHMARK.xlsx` (régénéré à chaque commit).

**C14 — décisions de Marcel du 14/11/2026 (mots pour mot)**
- « je veux que le verrou concerne tout ce qui a été coché et doit être aussi justifié, toutes les consignes de tout ce que tu dois faire pour chaque institution »
- « ben oui t'as mon accord vu que je te l'ai demandé !!! » (crash test g) ; « et oui ça doit être fait institution par institution sinon verrou »
- « 1 oui ok, 2 pourquoi ? 3 refais ces sessions » ; puis « je veux bien les exclure, mais comment être sûr que tu ne vas pas en profiter pour en exclure des légitimes ? »
- « une fois que toutes les précautions auront été prises, tu pourras continuer la boucle avec des sous agents qui respectent bien la méthodologie, tu me confirmes que le verrou fonctionnera pour les sous agents ? »
→ Appliqué : (1) verrou par étape cochée (a à g) et ordre strict ; (2) exclusion des pages de doc du contrôle de couverture **mécanique** (code 200 + HTML, sinon jamais) et listée dans l'onglet « Doc exclue » ; (3) sessions non conformes archivées dans `tests/archive/` puis rejouées ; (4) étape g obligatoire pour qu'une institution soit « terminée » ; (5) `probe.py`, `crash.py` et `fetch_doc.sh` refusent de se lancer si une institution antérieure n'est pas terminée.

**C15 — crash tests à la fin (Marcel, 14/11/2026, mot pour mot)** : « je préfère qu'on fasse tous les crash tests à la fin un par un » ; et avant : « oui mais il faut que ça s'adapte aux prochains » (plafond par type de réseau, voir METHODOLOGY).
→ L'étape g n'autorise ni ne bloque plus l'institution suivante ; elle reste obligatoire pour la clôture finale (`suivi.py fin` donne le plan). Les crash tests se font à la fin, un par un, avec `scripts/crash.py` (politique adaptative par réseau, 30 min entre réseaux protégés).

---

# Méthode (METHODOLOGY.md, recopiée)

# Méthode de la veille — quotas et rate limits des API IIIF

Objectif : pour chaque institution de `institutions.csv`, savoir (1) ce que la
documentation publique dit des quotas et limites de débit, (2) si l'API annonce
ses limites quand on l'appelle normalement, (3) si la réponse est absente, et
pourquoi quand elle l'est.

## Règles de prudence (non négociables)

- **Lecture seule** : uniquement `GET` (et `HEAD` si utile). Aucun POST, aucune
  écriture, aucun formulaire.
- **Endpoints publics documentés** uniquement. Pas de devinette de chemins
  hors doc, pas de parcours d'identifiants (brute force, énumération).
- **Pause ≥ 5 s** entre deux requêtes vers un même hôte (≥ 10 s pour
  gallica.bnf.fr et openapi*.bnf.fr, qui ont déjà coupé des connexions après une
  rafale).
- **Budget ≤ 15 requêtes par institution** pour les tests d'appel. La recherche
  documentaire (web) n'est pas comptée.
- **Arrêt immédiat** sur 429, 503, 403 répété, connexion coupée ou captcha :
  on consigne le code, les en-têtes (`Retry-After`, `X-RateLimit-*`,
  `RateLimit-*`, `nextAccessTime`…) et on n'insiste pas.
- **Pas de contournement** : on n'usurpe pas d'User-Agent de navigateur pour
  passer un blocage, on ne fait pas tourner d'IP, on n'utilise pas de compte qui
  n'est pas celui du projet. Un blocage est une donnée à consigner.
- **User-Agent honnête** : `VeilleAPIIIF/0.1 (veille documentaire; github.com/maribakulj/Veille-API-IIIF)`.
- **Aucune donnée personnelle** ni identifiant ne doit apparaître dans les
  fichiers du dépôt. Les réponses sont résumées (en-têtes + statut + 200 octets
  de corps au maximum), jamais recopiées en entier.

## Distinguer quatre choses (à écrire séparément dans chaque fiche)

- **Documenté** : la doc officielle annonce une limite, avec URL, date et citation exacte.
- **Observé** : une réponse 429 (ou un en-tête `Retry-After`, `X-RateLimit-*`, `RateLimit-*`) a été reçue lors de nos appels. Seul ce cas établit un mécanisme de limitation.
- **Accès refusé à ce client (403 anti-bot)** : 403 ou page de défi (Cloudflare « Just a moment », IIS 403) reçu dès la 1re ou la 2e requête. Ce n'est **pas** un quota : c'est un refus d'accès à notre client. Ne jamais l'écrire comme « limite de débit ».
- **Non vérifié** : tout le reste. Une limite documentée mais jamais observée reste « documentée, non vérifiée ».

Un 403 ne se contourne pas (pas de changement d'User-Agent vers un navigateur, pas de changement d'IP). On consigne, on arrête pour cet hôte, et on note ce qui devrait être refait autrement (navigateur de l'utilisateur, demande écrite à l'institution).

## Déroulé pour une institution

1. **Documentation** : chercher la doc officielle de l'API (site de
   l'institution, portail développeurs, GitHub, wiki, page « terms of use »,
   « fair use », « usage policy », « conditions d'utilisation »). Pour chaque
   source, noter l'URL, la date de consultation et la phrase exacte qui parle de
   quota / limite / débit / fréquence, ou son absence.
2. **Recherche élargie** si la doc officielle est vide ou muette : articles,
   billets de blog, issues GitHub, forums (IIIF Slack/Discourse, listes),
   archives Wayback (`ia_find_snapshots`). Noter les termes cherchés.
3. **Tests** (≤ 15 requêtes) : manifeste, image info.json, une requête de
   recherche si documentée, puis un petit nombre d'appels répétés espacés pour
   voir si des en-têtes de quota apparaissent. Consigner pour chaque appel :
   horodatage UTC, URL, statut, en-têtes pertinents, taille, délai depuis
   l'appel précédent.
4. **Pourquoi pas publié ?** Si aucun quota n'est annoncé nulle part : chercher
   une explication (politique de l'institution, mention d'une « fair use » sans
   chiffre, API en beta, débit « raisonnable » non chiffré, politique de
   l'hébergeur…). Distinguer ce qui est **trouvé** (avec source) de ce qui est
   **supposé** (étiqueté « hypothèse »).
5. **Fiche** : remplir `TEMPLATE.md` dans `institutions/<slug>.md`.

## Format des fichiers

- `institutions/<slug>.md` : une fiche par institution (gabarit `TEMPLATE.md`).
- `tests/<slug>.log` : journal brut des requêtes (horodatage, URL, statut,
  en-têtes pertinents), une ligne par requête.
- `REPORT.md` : tableau de synthèse, mis à jour à la fin de chaque lot.

## Statut d'une institution

- `à faire` → `en cours` → `vérifiée` (fiche complète, tests faits ou arrêtés
  pour une raison écrite) → `synthétisée` (ligne dans REPORT.md).
- Une institution n'est « vérifiée intégralement » que si la doc, la recherche
  élargie, les tests et la question « pourquoi pas publié ? » sont tous
  remplis.

## Méthode v2 (validée par Marcel le 2026-11-13) — checklist obligatoire

Une institution n'est « vérifiée » que si TOUTES les étapes ont leur preuve dans le dépôt.
Une étape non faite reste « non faite », et l'institution reste « incomplète ».

**Ordre et parallélisme** : une institution à la fois, dans l'ordre de `institutions.csv`.
Au plus deux agents en parallèle, sur deux institutions différentes, chacun n'écrit que
dans son propre dossier. Aucun agent n'écrit dans un journal ou une fiche qu'un autre traite.
Les journaux ne sont jamais réécrits : on ajoute, on ne remplace pas.

**a) Doc lue en entier.** Toutes les pages de doc liées à l'API (développeurs, interfaces,
conditions d'utilisation, FAQ, aide, mentions légales), lues en entier. Chaque page est
sauvegardée dans `sources/<slug>/` avec URL, date UTC et empreinte SHA-256, et la fiche
cite le fichier de preuve.

**b) Endpoints tirés de la doc.** La liste des endpoints vient de la doc (citée). Jamais devinée.

**c) Configuration écrite AVANT les tests.** `scripts/config/<slug>.json` liste les endpoints
et pilote `scripts/probe.py`. Chaque requête produit un fichier d'en-têtes bruts dans `tests/raw/<slug>/`.

**d) Recherche de quota dans la doc.** Pour chaque source lue : endpoint de statut, en-têtes
de limite documentés (nom exact), clé ou compte donnant un quota, contact pour un volume plus
élevé. Chaque réponse cite sa source.

**e) Test de chaque endpoint.** Même après un 403 sur un autre endpoint de la même institution.
Un 403 arrête son hôte, un 429 arrête l'institution et prévient Marcel. Le test de dépassement
(provoquer un 429 pour lire `Retry-After`) n'est fait qu'avec l'accord explicite de Marcel.

**f) Ce que disent les gens sur le web.** Recherche sur le net de tout ce qui concerne l'usage
des API de l'institution : plaintes ou questions sur les quotas, blocages de bots, présentations
de l'institution sur sa politique d'API, billets de blog, issues GitHub, forums, listes
de diffusion, réseaux professionnels, publications de l'institution sur ses API. Chaque
source est citée (URL, date, étiquette : officielle / présentation de l'institution /
utilisateur / tiers). Les noms de personnes privées ne sont pas reproduits.

**Vérification finale (par l'orchestrateur)** : contrôle que chaque étape a son fichier de
preuve. Sinon l'institution reste « incomplète ».

**g) Crash test progressif (jusqu'où peut-on aller).** Étape ajoutée le 2026-11-13 sur
demande de Marcel. Elle provoque volontairement des blocages depuis l'IP de Marcel : elle ne
se lance qu'après la fin de l'agent de l'institution, jamais en parallèle, et jamais sur un
hôte déjà bloqué en 403 anti-bot.

- **Plafond selon le cas** (retenu par Marcel le 2026-11-13) :
  - API à **limite documentée** : paliers jusqu'à **2 × la limite documentée**, au plus.
    Au-delà, on n'apprend rien de plus : la limite est déjà connue.
  - API **annoncée illimitée** ou **sans limite documentée** : paliers jusqu'à **200 req/min**,
    pour vérifier que l'annonce « illimité » tient vraiment.
  Le plafond ne se dépasse jamais. Il porte sur toutes les requêtes de l'IP de Marcel vers
  l'hôte, pas par agent.
- **Paliers** : on part de 1/3 de la limite documentée (ou 6 req/min sans limite documentée),
  puis on monte par paliers jusqu'au plafond du cas : 1/3, 2/3, 1×, 1,5×, 2× (limite
  documentée), ou 5×, 10×, 50×, 200 req/min (API illimitée ou sans limite documentée). Chaque palier dure au moins 3 minutes et envoie des
  requêtes régulièrement espacées (pas de rafale).
- **Ordre** : le crash test n'est lancé qu'une fois l'audit complet de l'institution terminé
  (étapes a à f, dossier prêt). Il ne doit pas risquer de bannir l'IP avant la fin de l'audit.
- **Arrêt immédiat** au premier 429, CAPTCHA ou 403 anti-bot. On consigne le palier, l'heure, les
  en-têtes complets (`Retry-After`, `X-RateLimit-*`, `RateLimit-*`) et le corps tronqué.
- **Attente** : après un blocage, on n'envoie rien vers cet hôte pendant au moins
  `Retry-After` (ou, à défaut, la durée annoncée par la doc, ou 1 h), puis on note si
  l'hôte répond à nouveau. Aucune reprise pendant le blocage (c'est la règle de la LoC :
  le compteur repart à zéro si l'on insiste).
- **Journal** : chaque palier dans `tests/crash/<slug>.log` (ajout seulement), avec le
  nombre de requêtes, la durée et le résultat. La configuration du test est committée dans
  `scripts/config/<slug>-crash.json` avant le lancement.
- **Accord** : Marcel est prévenu avant chaque institution (l'IP de son Mac sera bloquée
  pendant la durée du blocage). Pas de crash test sur MARCXML de la LoC (blocage 72 h) sans
  accord explicite à part.
- **Résultat** : une ligne dans la fiche : « seuil observé entre palier X et Y, en-tête Z »,
  ou « aucun blocage jusqu'à 2 × la limite documentée » (API limitée), ou « aucun blocage
  jusqu'à 200 req/min » (API illimitée). Un test « illimité » n'est pas une preuve
  d'illimitation au-delà de 200 req/min.

## Règles ajoutées après l'audit du 2026-11-13 (voir AUDIT-HAIKU.md)

- Le budget de 15 requêtes s'applique **par passe** d'une institution (un déroulé complet de la méthode). Les anciennes passes restent dans leurs journaux, sans être comptées.
- Aucune étape n'est marquée « non applicable » sans citer la phrase de la doc qui la justifie.
- Aucune fiche n'est marquée « vérifiée » avant que a) à f) aient chacune un fichier de preuve contrôlé.
- `data/institutions.json` n'est alimenté qu'à partir de la fiche relue de l'institution, jamais de mémoire.
- Le travail se fait une institution à la fois, sans sous-agent, dans l'ordre du classeur de référence (`data/perimetre.csv`).


## Disposition du dépôt et règle de couverture des tests (2026-11-13, consignes C8 et C11)

- **Un dossier par institution** : `institutions/<slug>/` contient tout son travail (fiche, `data.json`, `sources/`, `config/`, `tests/`) et `CONSIGNE-ET-SUIVI.md`, où **chaque étape a) à g) est cochée ou non, avec une justification et des preuves**.
- Une case cochée sans justification ou sans preuve existante bloque le commit (`scripts/suivi.py validate`, crochet pre-commit). `BENCHMARK.xlsx` est régénéré à chaque commit depuis ces dossiers.
- **Couverture des tests** : tout endpoint documenté est testé. **Seule une interdiction ou une impossibilité écrite dans la doc** (citation à l'appui) dispense de tester. Si rien n'est écrit : on teste, avec un script adapté à la doc ; si la doc n'en décrit pas, avec un script poli (pause ≥ 6 s, UA du projet, GET/HEAD, budget de 15 requêtes par passe, identifiants issus de pages publiques ou d'exemples de la doc, jamais énumérés ni devinés).
- La sonde suit une redirection du même hôte (comptée dans le budget). Plusieurs passes sont possibles : chacune a son propre budget de 15 requêtes et sa configuration committée avant lancement.

## robots.txt (ajouté le 2026-11-13, constaté sur l'EAP)

- Le `robots.txt` de chaque hôte testé est **téléchargé et lu à l'étape a)** (il fait partie de la doc : il contient des interdictions écrites).
- La sonde le lit **automatiquement** avant de tester un hôte (`respect_robots`, vrai par défaut) : jokers `*` et `$`, groupe de notre User-Agent sinon `*`, plus long motif gagnant, `Crawl-delay` respecté s'il dépasse notre pause. Un chemin interdit n'est **pas lancé** (ligne « NON LANCÉ : interdit par robots.txt » dans le journal) : c'est une interdiction écrite, qui dispense de tester (consigne C8).
- `robots.txt` indisponible (4xx) : tout est autorisé ; erreur serveur ou réseau : tout est traité comme interdit (RFC 9309). La lecture de `robots.txt` compte dans le budget de la passe.

**Incident du 2026-11-13 (Wellcome)** : le `robots.txt` de `iiif.wellcomecollection.org` commence par un BOM invisible ; la sonde ne reconnaissait alors pas `User-agent: *` et ignorait `Crawl-delay: 30`. Deux requêtes sont parties à 6 s d'écart au lieu de 30 s (passe 3 de Wellcome). Corrigé : la sonde retire le BOM et lit aussi `Request-rate`. Règle : **lire à l'étape a) le `robots.txt` de chaque hôte avec les yeux**, y compris `Crawl-delay` et `Request-rate`, en plus de la lecture par la sonde ; le résultat est consigné dans la fiche.

## Étape f — minimum exigé (décision du 14/11/2026, après remarque de Marcel)
Au moins **4 recherches web par institution**, une par catégorie : (1) politique/doc de l'institution sur API, bots, moissonnage ; (2) plaintes ou retours d'utilisateurs (429, 503, blocages, forums, listes iiif-discuss) ; (3) tickets GitHub/GitLab d'outils tiers qui l'interrogent ; (4) présentations, billets de blog ou articles de l'institution. Chaque piste utile est **lue dans l'original** quand c'est possible (résumé de moteur = indice seulement) et étiquetée (officielle / institution / utilisateur / tiers). Les catégories sans résultat sont notées « aucun résultat ».

## Exigence v3 : contrôlée par le commit (14/11/2026)
`scripts/suivi.py validate` refuse de laisser cochée l'étape f d'une institution tant que `data.json` ne contient pas : (1) `web` couvrant les 4 catégories (`institution`, `utilisateurs`, `tickets`, `presentations`) avec soit une URL lue, soit `aucun_resultat` + `requete` ; (2) `endpoints_documentes` : une ligne par famille d'API, `statut` `teste` (preuve existante) ou `non_teste` (raison ≥ 30 caractères) ; (3) `hotes_robots` : un robots.txt lu, avec preuve, pour **chaque hôte** contacté par les configurations. Les institutions faites avant cette règle sont listées dans `data/exigence_ancienne.txt` ; l'onglet « Couverture » de `BENCHMARK.xlsx` montre leurs manques (« à compléter ») ; on les retire de la liste une fois complétées.

## Verrou d'ordre et commande `porte` (14/11/2026)
- `python3 scripts/suivi.py porte [slug]` affiche ce qui manque (étapes, exigence v3, anomalies de journal) à l'institution en cours : on l'exécute **avant** de dire qu'une institution est finie. Elle indique la prochaine à traiter.
- `validate` (donc le commit) échoue si une institution est commencée (configuration, journal ou étape cochée) alors qu'une institution **antérieure dans l'ordre du classeur** n'est pas terminée. Exemptions : institutions écartées ; `data/exigence_ancienne.txt` (faites avant l'exigence v3, à rattraper) ; `data/ancien_travail_haiku.txt` (commencées par l'ancienne méthode, à refaire : on les retire de la liste quand on les reprend).

## Sous-agents (14/11/2026)
Le verrou agit : (a) **au lancement** des outils officiels (`probe.py`, `crash.py`, `fetch_doc.sh` appellent `suivi.py autorise <slug>` et refusent si une institution antérieure n'est pas terminée, étape g comprise) ; (b) **au commit** (`validate`). Il n'agit pas sur un `curl` direct : les sous-agents reçoivent l'interdiction de `curl`/WebFetch vers les domaines d'institutions, et on vérifie dans `tests/journal.log` et les diffs qu'aucune requête n'est partie hors des outils. Un sous-agent traite **une seule institution à la fois**, dans l'ordre, et doit finir par `python3 scripts/suivi.py porte <slug>` affichant « TERMINÉE ». Les sous-agents ne commitent pas ; le commit est refusé tant que `validate` n'est pas au vert.

## Crash test : politique adaptative par réseau (14/11/2026, décision de Marcel : « il faut que ça s'adapte aux prochains »)
`scripts/crash.py` applique seul, pour toute institution présente ou future :
1. **Détection** : requête initiale vers l'endpoint ; les en-têtes identifient le réseau (Cloudflare, AWS CloudFront, Akamai, Fastly, Azure Front Door, Imperva, Sucuri, DataDome, HUMAN, Kasada ; liste `VENDORS` à compléter si un nouveau apparaît).
2. **Plafond** : 200 req/min (hôte sans réseau à réputation partagée), **60 req/min** si un réseau est détecté ; dans les deux cas jamais au-delà de 2 × la limite documentée. Paliers sans limite documentée : 6, 10, 50, 200 (protégé : 6, 10, 30, 60).
3. **Un seul test protégé à la fois, 30 min entre deux** (état dans `data/crash_reseaux_proteges.json`) ; **requête témoin** avant (Cloudflare : `cdn-cgi/trace` ; CloudFront : `aws.amazon.com/robots.txt`) : si elle est défiée, abandon.
4. **Hôte partagé** : si un autre dossier a déjà testé le même hôte, le résultat est repris sans envoyer de requête (Leiden et Gand).
5. Requête de détection en 403/429/CAPTCHA ou erreur : abandon, étape g « impossible » à documenter.
6. Ordre d'exécution conseillé : hôtes sans réseau protégé d'abord, réseaux protégés en dernier.

## Boucle parallèle par lots (14/11/2026, décision de Marcel : 5 agents)
- `data/lots.json` répartit les institutions restantes en 5 lots (A à E, tourniquet par ordre du classeur). **L'ordre strict s'applique à l'intérieur d'un lot**, pas entre lots.
- Chaque agent travaille dans son worktree `.lots/lot-<ID>` (branche `lot/<ID>`), brief commun `data/BRIEF-AGENT.md`.
- **Au lancement** : `probe.py`, `crash.py` et `fetch_doc.sh` appellent `suivi.py autorise <slug>` *dans le dépôt principal* : refus si l'institution n'est pas dans le lot de l'agent, ou si une institution antérieure du même lot n'est pas terminée.
- **Au commit** : le hook (lu dans le dépôt principal, donc non modifiable par un agent) refuse tout fichier hors de `institutions/<slug>/` des institutions du lot et valide le lot ; le classeur n'est pas régénéré par les agents.
- **Politesse partagée** (`scripts/hostlock.py`, registre `~/.veille-state`) : ≥ 6 s entre deux requêtes vers un même hôte, tous agents confondus ; au plus 30 requêtes/min au total ; un crash test (verrou exclusif) suspend tout autre trafic.
- **Intégration** par le coordinateur seulement : `python3 scripts/integrer_lot.py <ID> [--push]` (périmètre, fusion sans commit, validation globale, régénération du classeur ; fusion annulée si un contrôle échoue).
- Limites connues : un `curl` direct ou une copie locale modifiée de `scripts/` par un agent n'est pas empêché techniquement ; le commit ne peut pas porter ces modifications, et l'intégration revérifie le périmètre.

## Données personnelles (14/11/2026)
Le dépôt GitHub est **public**. Aucune donnée personnelle de Marcel (adresse IP) ne doit y figurer. Les valeurs sensibles sont listées dans `~/.veille-state/secrets.txt` (hors dépôt) : le hook de commit refuse tout commit qui les ajoute ; `probe.py` et `fetch_doc.sh` les remplacent par « [IP retirée] » dans les fichiers qu'ils produisent. Certains serveurs renvoient l'IP du client dans un en-tête (ex. `x-mps-client-ip`).

## Jetons et secrets dans les pages publiques (14/11/2026)
GitHub bloque (« push protection ») tout push contenant un jeton reconnu, même s'il figure dans une page web publique téléchargée (ex. jeton Mapbox dans le JavaScript d'un site). `hostlock.redact` (utilisé par `probe.py` et `fetch_doc.sh`) remplace les motifs connus par « [jeton retiré] » ; le hook de commit refuse un commit qui en contient. Ne jamais utiliser l'URL d'autorisation de GitHub pour passer outre.
<!-- CONSIGNE:FIN -->
