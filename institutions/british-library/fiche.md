# British Library — `british-library` (audit v2, 2026-11-14)

- **Statut** : étapes a à f faites ; g (crash test) non lancée, configuration prête (`config/crash-bl-digirati.json`).
- **Hôtes** : `bl.digirati.io` (manifestes et images IIIF, actif) ; `iiif.bl.uk` (visionneuse, 403 IIS) ; `api.bl.uk` (DNS KO) ; `www.bl.uk` (doc).

## Sources
- `https://www.bl.uk/terms` (passe2/raw/01.html) : art. 10.4 « Readers shall not systematically or programmatically download or print any Eresource. » ; conditions du site, art. 3 : interdiction « to create a database (electronic or otherwise) that includes material downloaded or otherwise obtained from the Website except where expressly permitted ... or otherwise permitted in writing ». Aucun chiffre de débit.
- `https://www.bl.uk/services/collection-metadata-services` (passe2/raw/02.html) : Z39.50 authentifié ; contact metadata@bl.uk ; pas d'API HTTP documentée.
- `https://www.bl.uk/collection/digitised-manuscripts-archives` (passe3/raw/01.html) : liens `https://iiif.bl.uk/uv/#?manifest=https://bl.digirati.io/iiif/ark:/81055/...` : ce sont les URL d'API tirées de la doc ; aucun mot sur quotas.
- Politique « open metadata » (passe3/raw/02.html) : CC0 par défaut, pas de limite de débit.
- GitHub `britishlibrary/TremendousIIIF` (passe1/raw/08.html) : serveur d'images, « currently used in production », aucune limite écrite.
- robots.txt : www.bl.uk `Allow: /` ; iiif.bl.uk 404 ; bl.digirati.io 404 ; blogs.bl.uk `Allow: /` ; api.bl.uk DNS. Pas de Crawl-delay ni Request-rate.
- `https://www.bl.uk/help/terms-of-use` et `/help/how-to-reuse-images-of-unpublished-manuscripts` : renvoient désormais la page Research générique (passe1/raw/02.html est un 404 IIS pour la page collection ; passe5/raw/01.html contenu générique). `https://www.bl.uk/research/digitised-manuscripts` : idem (passe1/raw/05.html).
- Wayback : `sources/wayback/iiif-bl-uk.md` (aucune capture 200 de iiif.bl.uk).

## Tests (tests/journal.log, 8 requêtes sondes sur 2 passes + robots/fetch_doc)
Passe 1 (`config/bl-digirati-manifestes.json`) : 2 manifestes 200 (~0,85 et ~1,1 Mo, server AmazonS3, CloudFront), racine bl.digirati.io HEAD 404. Passe 2 (`config/bl-digirati-images.json`) : info.json v2, v3, thumbs 200 ; image 200x200 200 ; HEAD manifeste 200. Aucun en-tête RateLimit-*, X-RateLimit-* ni Retry-After ; `access-control-allow-origin: *`, `cache-control: public, max-age=86400` sur info.json. `iiif.bl.uk` : 403 IIS (fetch_doc, passe1/FETCH.log) : arrêté, non retesté ; la sonde n'a pas été lancée vers lui. `api.bl.uk` : non résolu.

## Web (4 catégories, 4 recherches)
- institution : aucune page de politique API/IIIF de la BL trouvée par le moteur ; seules les conditions générales ci-dessus et la politique open metadata (CC0).
- utilisateurs : aucune plainte BL (résumé de moteur, non vérifié) ; résultat voisin Vatican (hors sujet).
- tickets : aucun ticket sur `bl.digirati.io` / `iiif.bl.uk` / `api.bl.uk` (iiif-dl ne gère pas IIIF 3.0, résumé de moteur, non vérifié).
- présentations : ateliers training.iiif.io (lus) : exemples `api.bl.uk/metadata/iiif/...`, aucune limite ; une collection (livres Google) « do not currently allow sharing ».
- Contexte (résumé de moteur, non vérifié) : cyberattaque d'octobre 2023 ayant coupé les services dont IIIF.

## Conclusion
Aucune limite de débit publiée ni observée sur les 8 requêtes. Seules des interdictions textuelles de moissonnage systématique existent (conditions de bl.uk), sans chiffre, sans mécanisme technique documenté. Confiance moyenne : iiif.bl.uk non lisible (403), page de réutilisation des images absente. Hypothèse : l'infrastructure (CloudFront) peut appliquer des règles non annoncées ; non vérifiée.
