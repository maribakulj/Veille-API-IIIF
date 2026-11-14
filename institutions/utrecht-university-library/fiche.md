# Utrecht University Library — Special Collections (`utrecht-university-library`)

- **Classeur** : GLAM-073 · Pays-Bas · Audit v2 du 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `objects.library.uu.nl` (lecteur Mirador, manifestes IIIF, serveur d'images IIPImage), `ubu-objects.sites.uu.nl` (site WordPress des manuels), `www.uu.nl` (pages Special Collections). `bc.library.uu.nl` (cité par un tiers) : DNS introuvable.

## Sources (étape a)
- Manuel Mirador (PDF néerlandais, 2025) : IIIF et Mirador, aucune limite de débit (`sources/doc/text/02-pdf.txt`). La version anglaise `Using-the-new-viewer-Mirador.pdf` renvoie 404 (`sources/doc/FETCH.log`).
- Page « About IIIF » d'un objet (`sources/doc2/text/03.txt`) : manifestes Presentation v2 `https://objects.library.uu.nl/manifest/iiif/v2/<id>` et v3 `.../v3/<id>`, info.json d'image `.../fcgi-bin/iipsrv.fcgi?IIIF=<chemin>/info.json`, v3 par négociation de contenu ; liens de téléchargement `/download/<id>/pdf` et `/fulltext`.
- Page des manuels : questions à `library.functioneelbeheer@uu.nl` ; manuel : `ubu.fb.digitalisering@uu.nl` ; Special Collections : `library.specialcollections@uu.nl`. Aucune page de conditions d'usage de l'API, aucun quota, aucun en-tête de limite documenté.
- Actualités uu.nl (incunables, manifeste du Réseau du patrimoine numérique) : IIIF cité, « unlimited access to its collections » comme intention, sans chiffre.
- **robots.txt** : `objects.library.uu.nl` interdit `/anno`, `/manifest`, `/iiif_manifest`, `/fcgi-bin/iipsrv.fcgi` (tous agents) ; pas de `Crawl-delay`. `www.uu.nl` : règles Drupal classiques, sans `Crawl-delay`. `ubu-objects.sites.uu.nl` : `Disallow: /wp-admin/`. `iipimage.sourceforge.io` : 404 (tout autorisé). `bc.library.uu.nl` : DNS introuvable. Ces interdictions visent précisément les endpoints IIIF : on les a testés avec l'autorisation de Marcel (C12).

## Tests (2 passes, configs committées avant lancement, pauses 6 s, 10 requêtes)
- Passe 1 : manifeste v2 **200** (487 ko), manifeste v3 **200**, `fulltext` HEAD **200**, `pdf` HEAD **200** (739 Mo annoncés, aucun corps téléchargé), `reader/.../metadata` **200** ; image `info.json` et dérivé 150 px de l'exemple de la page « About IIIF » : **404** (identifiant sans point avant `jp2` : l'exemple de la doc est faux).
- Passe 2 (URL lues dans le manifeste) : `info.json` **200** (serveur `iipsrv/1.3`), dérivé 150 px **200**, `/iiif_manifest/image:...` **404**.
- Aucun 429, aucun 403, aucun en-tête `Retry-After` ni `X-RateLimit-*`. Seul en-tête de cache observé : `x-fastcgi-cache` (nginx).
- Au cours de l'étape a, la page `reader/object-list` (liste complète des titres) pesait 9,8 Mo.

## Web (étape f)
- Institution : recherche politique d'usage et robots : rien de plus que les pages lues.
- Utilisateurs : aucune plainte 429/503/blocage trouvée ; fil iiif-discuss de juin 2023 : un manifeste v3 d'Utrecht (hôte de développement) ne se charge pas dans Mirador car `sc:Manifest` y figure à la place de `Manifest` (corrigé par l'utilisateur côté client ; pas un quota).
- Présentations : le guide Mirador et la dépêche de l'incunable (900 incunables prévus d'ici 2027) ; un billet IIPImage sur Utrecht existe mais n'a pas été lu.
- Tickets : recherche non exécutée (quota de recherches web de la session épuisé), à refaire.

## Conclusion
Limite chiffrée : aucune publiée ni observée. Les endpoints IIIF sont interdits par robots.txt mais répondent 200 sans en-tête de limite. Confiance : moyenne (peu de volume testé). Contact pour le volume : `ubu.fb.digitalisering@uu.nl`.
