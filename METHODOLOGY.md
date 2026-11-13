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
