# Biblioteca Apostolica Vaticana (DigiVatLib) — `vatican`

- **Statut** : en cours (doc partiellement lue ; 3 requêtes de sonde faites, toutes 200 ; pas de test d'image)
- **Pays** : Cité du Vatican
- **Point d'entrée testé** : `https://digi.vatlib.it/` (accueil), `https://digi.vatlib.it/iiif/MSS_Vat.lat.683/manifest.json`, `https://digi.vatlib.it/iiif/MSS_Vat.ebr.75/manifest.json`
- **Vérifié le** : 2026-11-13 (sonde à 21:08:03–21:08:33 UTC ; documentation consultée le même jour)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

Aucune page d'API ou de documentation IIIF officielle de DigiVatLib n'a été trouvée ni lue. Les pages officielles consultées ont été lues par l'outil de recherche ; deux pages ont renvoyé une erreur de certificat TLS (« unable to verify the first certificate ») à l'outil WebFetch, donc elles n'ont pas été lues.

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://digi.vatlib.it/ (accueil, lu par WebFetch : résumé par un petit modèle) | 2026-11-13 | Aucun quota, limite ni restriction d'usage automatisé annoncé. Pied de page : « The contents of this site are protected by copyright. » et « Neither the text nor the images may be reproduced, in any form, without the authorisation of the Vatican Library ». La mention vise la reproduction, pas l'usage automatisé. |
| https://www.vatlib.it/en/information-readers/fotoriproduzione-uso-professionale.html (« Photographic reproductions for Professional Use ») | 2026-11-13 — **non lue** : erreur de certificat TLS à WebFetch | Connue seulement par un extrait de résultat de recherche (non lu brut) : « Under no circumstances will downloading of the images be allowed. » et publication soumise à accord écrit de la bibliothèque. À relire depuis un navigateur. |
| https://spotlight.vatlib.it/… (projet Polonsky, source de l'exemple `MSS_Vat.ebr.75`) | 2026-11-13 — **non lue** : erreur de certificat TLS | Rien lu. |
| https://www.vatlib.it/… (politique, conditions générales) | non trouvée | — |
| https://www.frh-europe.org/digivatlib-the-vaticans-digital-library/ (article secondaire) | résultat de recherche seulement | Mentionne l'adoption de l'IIIF ; aucune limite. |

Conclusion documentaire : aucune limite chiffrée (quota, fenêtre, débit) trouvée. L'interdiction de téléchargement (extrait de résultat de recherche) concerne les images, pas les quotas d'API.

## 2. Recherche élargie

- Termes cherchés : « DigiVatLib Biblioteca Apostolica Vaticana IIIF manifest API documentation » ; « digi.vatlib.it iiif manifest json … MSS_Vat.lat » ; « Vatican Library DigiVatLib terms of use reuse images API rate limit » ; « "digi.vatlib.it/iiif" manifest ».
- Sources examinées :
  - Fil IIIF-Discuss « forbidden response from Vatican » (20 septembre 2016) : https://groups.google.com/g/iiif-discuss/c/Fc1epNUG1N0 (lu via WebFetch, résumé). Le manifeste officiel `http://digi.vatlib.it/iiif/MSS_Vat.lat.683/manifest.json` y est cité ; un manifeste personnalisé créé la veille recevait des HTTP 403 sur les images. Causes avancées : Referer, ids d'images changeant d'un jour à l'autre (spéculation d'Andrew Hankinson, non confirmée). Ancien (2016) ; aucune réponse officielle lue.
  - Article jlis.it et article digitalia.cultura.gov.it : résultats de recherche seulement, non lus.
  - Une page de conditions d'un autre site (Bibliotheca Laureshamensis, BAV) : HTTP 404, non lue.
  - Un article de 2025 (cité par un résultat de recherche) affirme que digi.vatlib.it tourne désormais sur IIIF 3.0 : non vérifié ; nos manifestes annoncent IIIF Presentation 2 (voir § 3).
- Résultat : aucun quota ni rate limit publié trouvé. La doc technique officielle n'a pas été trouvée. Les URL de manifestes viennent de sources secondaires (fil 2016, résultat de recherche), pas d'une page officielle ; elles sont donc testées en « source tierce ».

## 3. Tests d'appel (voir `tests/vatican.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:08:03 | https://digi.vatlib.it/ | GET | 200 | aucun | HTML de l'accueil | premier appel |
| 2 | 21:08:16 | https://digi.vatlib.it/iiif/MSS_Vat.lat.683/manifest.json | GET | 200 | aucun | JSON, `@context` IIIF Presentation 2 (`http://iiif.io/api/presentation/2/context.json`), `@type` sc:Manifest | 13 s |
| 3 | 21:08:33 | https://digi.vatlib.it/iiif/MSS_Vat.ebr.75/manifest.json | GET | 200 | aucun | JSON, même contexte Presentation 2 | 17 s |

- Non testé : `info.json` d'image (`digi.vatlib.it/iiifimage/…`) — l'identifiant d'image doit venir du manifeste, et la sonde ne conserve que 200 octets de corps ; on ne devine pas l'URL.
- Non testé : recherche / métadonnées. Les catalogues `opac.vatlib.it` (pages HTML, sans API documentée) et `www.mss.vatlib.it/arch_guii/console` n'ont pas été sondés : pas d'endpoint documenté trouvé.
- Budget utilisé : 3 requêtes sur 15.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non (aucune limite trouvée dans les pages lues ; deux pages officielles non lues à cause d'une erreur TLS).
- Limite **observée** (429 ou en-tête de quota reçu) : non (3 requêtes, aucun 429, aucun en-tête de limite).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : non, aucune requête n° 1 à 3. Le 403 de 2016 (images) concerne un autre contexte et n'a pas été reproduit (pas d'image testée).
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucun en-tête de limite sur les 3 réponses).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : erreur TLS (« unable to verify the first certificate ») à WebFetch sur vatlib.it et spotlight.vatlib.it : problème de certificat côté outil, pas un refus de l'institution.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : pas de politique de quota publiée dans les pages lues. Les images ne doivent pas être téléchargées ni republiées sans accord (extrait de recherche sur vatlib.it, non lu brut ; mention de droits sur digi.vatlib.it).
- Hypothèses (étiquetées comme telles) :
  - H1 : l'institution ne publie pas de quota pour ses manifestes, et s'appuie sur les règles de reproduction (non vérifié).
  - H2 : le 403 de 2016 venait d'un contrôle de Referer ou d'URL renouvelées (spéculation citée dans le fil 2016 ; non vérifié, non reproduit).

## 6. Confiance et pistes restantes

- Niveau de confiance : faible (doc officielle non lue, pas d'endpoint officiel identifié, manifestes testés = sources tierces).
- Ce qui reste à vérifier, et comment :
  1. Relire https://www.vatlib.it/en/information-readers/fotoriproduzione-uso-professionale.html et les conditions de digi.vatlib.it depuis un navigateur (erreur TLS à l'outil).
  2. Demander par écrit à la Biblioteca Apostolica Vaticana (contatto del servizio digitalizzazione / ufficio fotoriproduzione) : endpoints IIIF officiels, version IIIF (2 ou 3), limite de débit tolérée, et l'emplacement des `info.json`.
  3. Plus tard, avec un identifiant d'image lu depuis le manifeste dans un navigateur : un `info.json` et une vignette, espacés, pour voir si un 403 de type 2016 réapparaît.

## 5 bis. Recherche ciblée des quotas (2026-11-13)

a) **Endpoint de statut de quota** : non trouvé — termes cherchés : « DigiVatLib Vatican Library IIIF API rate limit quota contact digitalizzazione », « Vatican Library digi.vatlib.it IIIF manifest API status endpoint headers rate limit github ». Source tierce (PR Antonio-Faure/mnemosyne#40, https://github.com/Antonio-Faure/mnemosyne/pull/40, consultée via résultat de recherche, 2026-11-13) : l'hôte « has no enumerable IIIF Collection and no JSON search endpoint » ; aucun endpoint de statut évoqué. Source non officielle.

b) **En-têtes de limite documentés** : non trouvé — aucun en-tête de limite dans les résultats ni dans les 3 réponses reçues (tests/vatican.log).

c) **Clé d'API ou compte** : non trouvé — la même PR décrit le descripteur comme « keyless » (source tierce). Aucune clé ni compte officiel mentionné.

d) **Contact officiel pour demander un quota** : non trouvé — aucun contact de service de numérisation confirmé dans les résultats. La page officielle « Photographic reproductions for Professional Use » (https://www.vatlib.it/en/information-readers/fotoriproduzione-uso-professionale.html) n'a pas pu être relue : erreur de certificat TLS à WebFetch (2026-11-13). Seul un extrait de résultat de recherche existe : « Under no circumstances will downloading of the images be allowed. » (non lu en entier). Un contact par écrit reste à établir depuis un navigateur.

Conclusion : moyen d'interroger le quota : **non**. Aucun endpoint, en-tête ni compte documenté ; aucune sonde ciblée lancée (pas de `scripts/config/vatican-quota.json`).
