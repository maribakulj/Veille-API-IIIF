# Herzog August Bibliothek Wolfenbüttel — `hab` (audit v2, a à f)

- **Statut** : audit v2 complet a à f ; g (crash test) préparé, non lancé (`config/crash-iiif-info-json.json`).
- **Pays** : Allemagne · **Audit** : 2026-11-14 · **Verdict quota** : aucun quota ni limite de débit publié ; aucun en-tête de limite observé.

## Sources (étape a, d)
Pages lues en entier (copie + SHA-256 dans `sources/*/SHA256SUMS`, texte dans `sources/*/text/`) :
- `sources/doc1/` : page IIIF de la HAB (blog du 18/12/2019, quatre API IIIF présentées sans URL ni limite ; PURL `?link=167`), Nutzungshinweise (licences : images en domaine public, données structurelles sans droits, le reste CC BY-SA ; aucune règle de débit ni d'usage automatisé ; contact auskunft@hab.de), copyright.html (marquée « Veraltet »), accueil diglib.hab.de (« Über eine OAI-Schnittstelle werden bibliographische und fallweise strukturelle Metadaten zum Harvesten zur Verfügung gestellt »), site manuscrits hab.bodleian.ox.ac.uk. La page standards-dokumentation renvoie 404.
- `sources/doc2/` : `/js/digitized.json` appelé par le JS du site (script.prd.js), version allemande de la page IIIF, Garantieerklärung (PDF `?link=033`), pages hab.de Digitale Bibliothek et reproductions : rien sur quotas ni bots.
- robots.txt (`sources/robots/`, `robots2/`, `portraits/`, `doc2/01.html`) : diglib.hab.de Disallow sur des répertoires techniques (/wdb/, /download.php, /rules/…), pas de Crawl-delay ; www.hab.de Disallow /wp-admin/ ; oai.hab.de, hab.bodleian.ox.ac.uk, iiif.hab.de, portraits.hab.de : 404 ; iiif.bodleian.ox.ac.uk : 400 ; image.hab.de : 403 (voir blocages).
- d) Endpoint de statut de quota, en-tête de limite documenté, clé ou compte donnant un quota : aucun dans toutes ces pages. Contact : auskunft@hab.de.

## Tests (étape e ; journal `tests/journal.log`, en-têtes `tests/raw/`)
Quatre passes, configurations committées avant lancement (`config/hab-passe1…4`). L'ancienne session du 13/11 (configuration committée après son lancement) est archivée verbatim dans `tests/archive/`.

| Passe | Endpoint | Résultat |
|---|---|---|
| 1 | hab.bodleian.ox.ac.uk/js/digitized.json (518 ko, liste des URI de manifestes) | 200 |
| 1 | oai.hab.de Identify et ListMetadataFormats | 200 |
| 1 | diglib.hab.de/sitemap.xml (HEAD) | 200 |
| 2 | iiif.hab.de manifeste (Presentation 2, 635 ko) et vignette Image | 200 |
| 2 | iiif.hab.de/…/manifest | 303 vers /manifest.json (même hôte), puis 200 |
| 2 | iiif.bodleian.ox.ac.uk manifeste | 200 |
| 3 | info.json iiif.hab.de et iiif.bodleian.ox.ac.uk | 200 |
| 4 | portraits.hab.de/werk/9043/iiif (Presentation 3) | 200 |

Aucun 429, aucun en-tête `Retry-After`/`RateLimit-*`. Les URL IIIF ne viennent pas d'une page de doc HAB : elles sont lues dans `digitized.json` (champs `uri`, `thumbnail_uri`) et dans les manifestes. IIIF Authentication et Content Search : annoncées sans URL, non testées.

## Blocages
`image.hab.de/robots.txt` : 403 Forbidden Apache générique (2026-11-14T03:19:55Z), hôte arrêté et non testé (hôte des images des portraits). Wayback : toutes les captures 2024-2026 sont des 404 (`sources/wayback/image-hab-de-robots.md`). Nature du 403 non déterminée.

## Web (étape f, 4 recherches, 2026-11-14)
- institution : pas de politique de bots ou moissonnage trouvée en dehors des pages déjà lues ; page IIIF HAB relue dans l'original.
- utilisateurs : aucun résultat sur la HAB (requête « iiif.hab.de 429 OR 503 OR blocked OR "rate limit" HAB Wolfenbüttel manifest download problem ») ; les résultats concernaient d'autres institutions (résumé de moteur, non vérifié).
- tickets : aucun résultat (requête « github issue "iiif.hab.de" OR "diglib.hab.de" manifest harvester OR crawler OR importer ») ; mets2iiif (subhh) lié à un projet HAB/Bodleian, sans ticket de quota (résumé de moteur).
- presentations : D. Maus, « Von METS zu Manifest » (Kitodo, 22/01/2021), PDF lu dans l'original (`sources/tiers/`) ; aucune mention de quota. Découverte de portraits.hab.de (HAB) par la recherche.

## Conclusion
Aucune limite documentée, aucune observée sur une vingtaine de requêtes réparties sur 7 hôtes (oai.hab.de, diglib.hab.de, hab.bodleian.ox.ac.uk, iiif.hab.de, iiif.bodleian.ox.ac.uk, portraits.hab.de). Hypothèse non vérifiée : l'absence de règle chiffrée traduit une absence de politique plutôt qu'une absence de limite ; le 403 d'image.hab.de reste à élucider auprès de auskunft@hab.de.
