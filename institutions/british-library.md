# British Library — `british-library`

- **Statut** : **incomplète** (corrigé le 2026-11-13 : la doc IIIF / API de la BL n'a pas été lue ; le 403 vient aussi d'un curl depuis la machine de veille, pas seulement de l'outil de lecture — voir § 3)
- **Pays** : Royaume-Uni
- **Point d'entrée testé** : `https://iiif.bl.uk/` (point d'entrée supposé dans `institutions.csv`) ; manifeste de repli `https://api.bl.uk/metadata/iiif/ark:/81055/vdc_000000035B1A/manifest.json` (cité dans une source tierce, nom DNS non résolu)
- **Vérifié le** : 2026-11-13 (≈ 20:33 UTC)
- **Vérifié par** : agent de veille (session Claude, branche claude/veille-iiif-quotas)

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://www.bl.uk/terms-and-conditions (lien « Terms and conditions » depuis bl.uk) | 2026-11-13 | Page renvoyant 404 à l'outil de lecture : **page inaccessible**, pas de texte lu. |
| https://www.bl.uk/help/terms-of-use | 2026-11-13 | Pas de texte sur API, IIIF, quota, fair use ni accès automatisé. Seule phrase trouvée (pied de page) : « All text is © British Library Board and is available under a CC-BY Licence except where otherwise stated. » |
| https://iiif.bl.uk/ | 2026-11-13 | **403 Forbidden** à la lecture (aucun corps récupéré). Aucun texte de conditions lu. |
| https://www.bl.uk/terms/imaging-services (via recherche, non ouverte) | 2026-11-13 | Extrait cité par un résultat de recherche : « you must not copy or reproduce material supplied through our Imaging Services unless you have our written permission ». Concerne les commandes de reproduction, pas l'API publique (à confirmer). |
| https://github.com/britishlibrary (organisation GitHub) | 2026-11-13 | Aucune mention de quota ni de limite (10 dépôts visibles sur 57). Dépôts IIIF visibles : `TremendousIIIF` (serveur d'images IIIF en C#) et `UniversalViewer-old` (visionneuse archivée). |
| https://bl.uk/research/digitised-manuscripts (via recherche) | 2026-11-13 | Extrait cité par un résultat : 1 000 manuscrits numérisés remis en ligne après une cyberattaque d'octobre 2023 ; « view only and there is no download option » ; liste de plus de 2 000 documents (mise à jour juin 2025). Pas de chiffre de débit. |

Résultat doc officielle : **aucune limite chiffrée trouvée dans les pages lues**. La doc IIIF / API de la BL elle-même n'a **pas été lue** (403 sur iiif.bl.uk, page conditions en 404) : ce résultat ne permet pas de conclure qu'il n'existe aucune limite.

## 2. Recherche élargie

- Termes cherchés : « British Library IIIF API documentation terms of use rate limit » ; « iiif.bl.uk British Library IIIF manifest collections terms » ; « British Library IIIF "api.bl.uk" manifest digitised manuscripts » ; « "iiif.bl.uk" rate limit OR throttling OR "fair use" British Library image server ».
- Sources examinées : résultats de recherche web ; Wayback Machine (historique `ia_find_snapshots` mode history sur iiif.bl.uk) ; GitHub britishlibrary (page de l'organisation, pas les dépôts en détail) ; pages bl.uk (ci-dessus). Source tierce vue (non vérifiée) : guide de formation `training.iiif.io/annotations/basics/finding_bl.html` (indique que les manifestes BL sont sur `api.bl.uk`).
- Résultat : **rien de publié** sur un quota ou un débit pour `iiif.bl.uk`. Aucun ticket GitHub, forum ou article trouvé qui cite une limite. Les seules limites chiffrées trouvées concernent d'autres institutions britanniques (National Archives, legislation.gov.uk), **pas la BL**.
- Wayback (iiif.bl.uk, historique) : captures de 2024-09, 2025-02, 2025-03, 2026-08-02 et 2026-10-11. **La capture du 2026-08-02 a le statut 403** ; les autres sont des 308 ou des « warc/revisit ». Donnée observée, pas une explication.

## 3. Tests d'appel (voir `tests/british-library.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 2026-11-13 ≈ 20:3x | `https://iiif.bl.uk/` (via l'outil de lecture web, pas un appel direct de l'agent) | GET | **403 Forbidden** | aucun en-tête lu | corps non récupéré | — |
| 2 | 2026-11-13 20:33:22 | `https://api.bl.uk/metadata/iiif/…/manifest.json` (manifeste cité par source tierce) | GET (curl, UA honnête) | **échec : résolution DNS impossible** | — | — | — |
| 3 | 2026-11-13 20:33:27 | même URL, après pause de 5 s | GET (curl, UA honnête) | **échec : résolution DNS impossible** (`Could not resolve host: api.bl.uk`) | — | — | 5 s |

Autres lectures (non comptées comme tests d'appel, mais faites) : `https://www.bl.uk/help/terms-of-use` (200, texte lu), `https://www.bl.uk/terms-and-conditions` (404), `https://github.com/britishlibrary` (lecture de page). Aucun appel `info.json` ni manifeste n'a pu être réalisé.

**Arrêt des tests** : le 403 sur `iiif.bl.uk` est traité comme un signal d'arrêt (règle de prudence). Aucun autre appel n'a été fait vers `iiif.bl.uk`. Le manifeste `api.bl.uk` n'est pas résolu, donc aucune réponse n'a pu être observée sur ce point d'accès. Aucun manifeste réel ni `info.json` n'a donc été testé.

## 4. Conclusion sur les limites

- L'API annonce-t-elle ses limites dans la réponse ? **non observé** (aucune réponse exploitable : 403 sur iiif.bl.uk, DNS impossible sur api.bl.uk).
- Mécanisme observé (429 + Retry-After, en-têtes X-RateLimit, rien) : **rien à observer** ; seul le 403 sur iiif.bl.uk est consigné.
- Valeurs trouvées (quota, fenêtre) : **aucune**.
- Blocages rencontrés : 403 sur `https://iiif.bl.uk/` (lecture via outil web ; également présent dans la capture Wayback du 2026-08-02) ; `api.bl.uk` non résolu (deux tentatives) ; page `terms-and-conditions` en 404.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) :
  - Rien d'annoncé sur un quota ou un débit pour `iiif.bl.uk` dans les pages bl.uk lues ni dans les recherches.
  - Les manuscrits numérisés sont « view only and there is no download option » (bl.uk/research/digitised-manuscripts, via recherche) ; une cyberattaque d'octobre 2023 a coupé l'accès, puis une partie a été remise en ligne.
  - Le 403 sur iiif.bl.uk apparaît aussi dans la capture Wayback du 2026-08-02.
- Hypothèses (étiquetées comme telles) :
  - *Hypothèse* : la BL ne publie pas de quota parce que son service IIIF n'est pas traité comme une API à contrat (pas de clé, pas de politique écrite) ; les conditions générales ne couvrent que le texte (CC-BY).
  - *Hypothèse* : le 403 sur iiif.bl.uk vient d'un blocage des clients automatisés (pare-feu ou contrôle de bots), et non d'un quota annoncé. Non vérifiable depuis cette session.
  - *Hypothèse* : le service a été restreint après la cyberattaque de 2023, ce qui expliquerait le manque de documentation publique récente.

## 6. Confiance et pistes restantes

- Niveau de confiance : **faible** (pages clés inaccessibles : iiif.bl.uk en 403, `terms-and-conditions` en 404, `api.bl.uk` non résolu).
- Ce qui reste à vérifier, et comment :
  - Lire la page « Terms and conditions » de la BL et la doc IIIF du service, depuis une session navigateur ordinaire (non automatisée), ou demander à `permissions@bl.uk` / au service numérique de la BL s'il existe une limite de débit ou une politique d'accès automatisé.
  - Refaire le test d'un `info.json` et d'un manifeste quand le service répond, avec la pause de 5 s et l'arrêt sur 403/429.
  - Confirmer quel hôte de manifeste est en service actuel (`api.bl.uk` non résolu ; le site de la BL cite d'autres hôtes, à vérifier).
  - Ne pas reprendre sans l'accord de l'opérateur de la veille si le 403 persiste (règle d'arrêt).
