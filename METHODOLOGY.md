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
