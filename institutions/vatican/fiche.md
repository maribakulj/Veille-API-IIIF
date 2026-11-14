# Biblioteca Apostolica Vaticana (DigiVatLib) — `vatican`

- **Statut** : audit v2 a–f complet ; g (crash test) à faire en fin de boucle
- **Vérifié le** : 2026-11-14 · **Vérifié par** : agent de veille (Claude Sonnet 5.5, lot E)
- L'ancienne fiche (passe Haiku du 2026-11-13) est remplacée ; sa session de sonde, lancée avant le commit de sa configuration, est archivée verbatim dans `tests/archive/` et rejouée.

## 1. Sources (documentation lue)
Fichiers : `sources/a1`, `sources/a2`, `sources/a3` (HTML brut, texte extrait, SHA256SUMS).
- `digi.vatlib.it/about` et `/` : DigiVatLib « is based on the International Image Interoperability Framework (IIIF) technology » ; aucune limite, aucun quota, aucune règle d'usage automatisé. Pied de page : « Neither the text nor the images may be reproduced, in any form, without the authorisation of the Vatican Library ».
- `digi.vatlib.it/robots.txt` : `Disallow: /search, /*/search, /*/index-search, /*/detail/*, /about, /news` ; `Crawl-delay: 10` (tous), Bingbot 30, SemrushBot exclu.
- `www.vatlib.it/.../fotoriproduzione-uso-professionale.html` (lue en entier, plus d'erreur TLS avec fetch_doc) : clauses de licence de reproduction ; art. 9 « Under no circumstances will downloading of the images be allowed. » : concerne les sites web des licenciés qui publient des reproductions, pas l'API de DigiVatLib.
- `vaticanlibrary.va/it/disclaimer.html`, `privacy-policy.html` : pas de règle de débit ni de moissonnage.
- Contact : `bav@vatlib.it` (page Contacts and offices).
- robots.txt par hôte : digi.vatlib.it (ci-dessus) ; spotlight.vatlib.it `Crawl-delay: 10`, Disallow sur les recherches de catalogue ; opac.vatlib.it `Allow: /$` + `Disallow: /*` ; www.vatlib.it, www.mss.vatlib.it, www.vaticanlibrary.va : 404 (tout autorisé).
- Recherche de quota (d) dans chaque page : pas d'endpoint de statut, pas d'en-tête de limite documenté, pas de clé ni de compte donnant un quota, contact général seulement.

## 2. Tests (voir `tests/journal.log`, `tests/raw/`)
Passe 1 (`vatican-v2-passe1.json`, 10 requêtes dont 4 robots.txt) : accueil, manifestes MSS_Vat.lat.683 (446 ko, IIIF Presentation 2) et MSS_Vat.ebr.75, accueil OPAC, console mss : tous 200 ; spotlight.vatlib.it : erreur de certificat (robots et accueil, aucun contournement).
Passe 2 (`vatican-v2-passe2-images.json`, 5 requêtes) : `info.json` (IIIF Image 2 level2), dérivé 200 px, vignette, notice `/mss/detail/` (Disallow de robots.txt, lancée avec l'accord de Marcel, C12) : tous 200.
Aucun 429, aucun en-tête `Retry-After`/`X-RateLimit-*`/`RateLimit-*` ; serveur Apache, `Cache-Control: no-cache`, cookie de session JSESSIONID, `Access-Control-Allow-Origin: *`.

## 3. Web (f)
Voir `sources/web/recherches-web-2026-11-14.md` : fil iiif-discuss 2016 (403 sur images d'un manifeste recopié, causes spéculatives) ; article de Paola Manoni (BAV), DigItalia 2-2020 (aucune limite) ; billet tiers Paris Bible 2022 ; aucun ticket d'outil tiers trouvé.

## 4. Conclusion
- Limite documentée : aucune de débit ; seule consigne chiffrée : `Crawl-delay: 10` (robots.txt).
- Limite observée : non (15 requêtes, aucun 429).
- L'API n'annonce pas ses limites dans ses réponses.
- Pourquoi non publié : non trouvé ; hypothèse (étiquetée) : l'institution s'appuie sur les règles de reproduction plutôt que sur une politique d'API.
- Confiance : moyenne. À vérifier à la main : spotlight.vatlib.it (TLS), digitavaticana.org (timeout), photographic-laboratory ; écrire à `bav@vatlib.it` pour une limite non publiée.
- Crash test (g) : configuration `config/crash-info-json.json` prête ; attention, le Crawl-delay de 10 s est inférieur au palier de 200 req/min : à signaler à Marcel.
