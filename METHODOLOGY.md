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
