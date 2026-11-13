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
