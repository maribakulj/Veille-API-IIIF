# University College Dublin Libraries – Digital UCD (`university-college-dublin-digital-ucd`)

- **Classeur** : GLAM-071 · Irlande · audit v2 du 2026-11-14 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `digital.ucd.ie` (site temporaire), `iiif.ucd.ie` et `data.ucd.ie` (ancienne plateforme, services cités par la doc archivée), `www.ucd.ie` (site de la bibliothèque).

## Sources
- **Situation actuelle** (`sources/a1`, `sources/a2`) : la plateforme d'origine a été retirée (« we identified a system vulnerability and took the difficult decision to retire the ageing infrastructure », about.html). Le site actuel est un « temporary access website » statique construit avec CollectionBuilder-CSV : 5 objets de collection, exports `metadata.json/csv`, `facets.json`, `subjects.*`, `timelinejs.json`. Une nouvelle plateforme est annoncée pour 2026. Contact : digital.library@ucd.ie. Documents : Rights, Access and Re-use Policy, User Guide to Reuse, Ethical Cataloguing Guidelines (PDF, `sources/a2`, texte extrait avec pdftotext en `*.pdf.txt`) : aucune mention de quota, d'API, de moissonnage ni de robots.
- **robots.txt** : `digital.ucd.ie/robots.txt` = 404 (aucune règle) ; `iiif.ucd.ie` : DNS inexistant ; `data.ucd.ie` : délai dépassé ; `www.ucd.ie/robots.txt` : 403 CloudFront « Request blocked » à la sonde, lu via Wayback (capture du 2025-10-01 : Disallow limités à /webteam/, /webtest*/ etc., pas de Crawl-delay, rien sur /library/).
- **Ancienne plateforme via Wayback** (`sources/wayback/ucd-ancienne-plateforme.md`) : page « Services » (capture du 2024-12-04) : API IIIF Image 2.0 (`iiif.ucd.ie/loris/...`), IIIF Presentation 2.0 / OpenSearch / Linked Data (`data.ucd.ie/api/...`), unAPI, vues `.json`, API géospatiale, API quantitative. Aucune phrase sur un quota ; seule limite : image téléchargeable au plus 2000 px de large (pas un débit). Conditions d'usage : « solely for the purposes of research and education », métadonnées CC BY-SA 4.0. Accueil du 2024-12-31 : « back working after a period of disruption ».
- `www.ucd.ie` : arrêté après le 403 (registre partagé, 24 h) ; page /library/ listée à vérifier à la main.

## Tests (2 passes ; 15 + 5 requêtes)
- **Passe 1** (configuration `ucd-v2-passe1.json`) : toutes les URL https de `digital.ucd.ie` : `SSLCertVerificationError` en Python (chaîne incomplète : curl, lui, obtient 200 ; sources/a1, a2, a4). `iiif.ucd.ie` : erreur DNS (hôte disparu). `data.ucd.ie` (manifeste, info.json, collection, OpenSearch, VoID) : 5 délais dépassés (30 s) : service éteint. `digital.ucd.ie/api/unAPI` et `/view/ivrla.31285.json` : **404**.
- **Passe 2** (HEAD en http, sans suivre de redirection) : accueil **200** (Apache), `/assets/data/metadata.json`, `/c0097/`, `/items/ucdlib_001.html` : 404 en http (le serveur http ne sert pas les mêmes fichiers que https). Aucun en-tête de limite (`X-RateLimit-*`, `Retry-After`) à aucun moment, aucun 429.
- Les fichiers `metadata.json` (2 257 o) et `facets.json` (642 o) lus par `fetch_doc.sh` : 200.
- Limite de l'outil : la sonde ne peut pas désactiver la vérification TLS ; les en-têtes des réponses https ne sont donc pas relevés.

## Web
- Institution : aucune politique de quota, de bots ni de moissonnage trouvée (page IIIF de guides.iiif.io : seulement la marche à suivre pour copier le lien de manifeste ; apis.io : seul l'export de métadonnées statique, « Rate Limit Signal: derived », valeur dérivée sans source).
- Utilisateurs : aucune plainte 429/503 trouvée (recherche : une).
- Tickets et présentations : refaits le 2026-11-14 par WebSearch (2 recherches). Tickets : aucun ticket GitHub mentionnant digital.ucd.ie (résumé de moteur, non vérifié ; la recherche interne de GitHub déjà lue donnait le même résultat). Présentations : slideshare « IIIF & Beyond » (ne parle ni de débit ni de robots) ; billet DRI sur l'atelier IIIF et liste des publications UCD signalés par le moteur, non lus (DRI en 403).

## Conclusion
Aucun quota ni limite de débit publiés, avant comme après la refonte. Le site actuel est statique (pas d'API) ; les API IIIF/OpenSearch/Linked Data de l'ancienne plateforme sont inaccessibles (DNS, délais, 404). À refaire quand la nouvelle plateforme (annoncée pour 2026) sera en ligne. Confiance : moyenne.
