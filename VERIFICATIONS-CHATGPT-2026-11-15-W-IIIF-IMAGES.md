# Passe W (15/11/2026) : une URL IIIF Image originale débloquée

## Art Institute of Chicago : vrai `info.json` de la file manuelle

**URL exacte dans `a_verifier_manuellement` :**
`https://www.artic.edu/iiif/2/b3974542-b9b4-7568-fc4b-966738f61d78/info.json`

**Résultat nouveau :** une extraction publique datée **2026-11-15** a fourni un **JSON IIIF Image API 2 intégral (931 caractères)**. Il a été **parsé comme JSON**, pas simplement cité par une notice ni confondu avec une page de défi Cloudflare. Propriétés lues :
- `@context=http://iiif.io/api/image/2/context.json`
- `@id=https://www.artic.edu/iiif/2/b3974542-b9b4-7568-fc4b-966738f61d78`
- dimensions : **6 679 × 4 577 px**
- tuiles **256 px**, facteurs de réduction **1, 2, 4, 8, 16, 32, 64**
- profil **`http://iiif.io/api/image/2/level2.json`**
- objet `profile[1]` énumérant des fonctions techniques et `maxArea=30 569 783` : **surface maximale d'image**, pas limite de requêtes.

**Prudence :** sur le navigateur / lecteur direct, la même URL peut renvoyer **403 Cloudflare**. Une copie récupérée par un extracteur n'est pas un test HTTP de notre client avec relevé des en-têtes et ne prouve pas une disponibilité universelle. Une extraction plus ancienne sur cet endpoint avait même rendu uniquement une redirection 301 autoréférente (2026-07-05). Les constats successifs ne doivent **pas être écrasés**.

**Sources institutionnelles et retours des utilisateurs :**
- Documentation officielle <https://api.artic.edu/docs/#iiif-image-api> : API REST sur `api.artic.edu`, images IIIF sur **`www.artic.edu/iiif/2`** ; `image_id` doit être récupéré via les métadonnées plutôt que deviné, recommandations de tailles (dont 843 px).
- <https://api.artic.edu/docs/#scraping-images> : téléchargement d'images un par un et environ une seconde de délai entre les téléchargements ; simple recommandation de courtoisie, **pas** un plafond Image IIIF à 60 req/min.
- <https://github.com/art-institute-of-chicago/api-data/issues/9> (2026) : problème public « IIIF image host ... returns HTTP 403 Cloudflare challenge for non-browser clients ».
- <https://github.com/art-institute-of-chicago/data-aggregator/issues/151> (signalement du 05/12/2025) : retour d'utilisateur sur `cf-mitigated: challenge`, restriction CORS et réponse 403.
- <https://github.com/lovasoa/dezoomify/issues/929> (2026) : autre symptôme d'échec dans un proxy et lecture possible dans des clients spécifiques.

**Conclusion :** une des **18 routes techniques P1** a désormais son **contenu documentaire original**, sans que soit démontré l'accès live par la sonde. Les **60 req/min officiels concernent la REST metadata API**, non ce serveur IIIF Image ; la recommandation d'1 image/seconde n'est pas une observation de quota appliqué. La fiche AIC connaissait déjà les quotas et les recommandations d'usage, ce qui est nouveau ici est **le JSON exact** et la corroboration des refus 403 tiers.

## National Palace Museum : serveur Image documenté, image ciblée toujours en échec

- Page publique <https://iiifod.npm.gov.tw/iiif/2> : serveur Cantaloupe annonçant Image API **2.x**, exemples `/iiif/2/{identifier}/info.json` et `/full/full/0/default.jpg`, et autres routes v1/v3. Cette page est **retrouvée par l'index public**, sans lecture live par la sonde.
- L'URL initiale `https://iiifod.npm.gov.tw/iiif/2/K1F%2FK1F000001N000000000PAA/info.json` a de nouveau échoué par **timeout**, comme une autre URL de test publiée sur le même hôte. **Pas de JSON extrait**, pas de 429/403 observé sur cette requête. Ne pas convertir un timeout en preuve d'absence de quotas.

## Vérifications de contrôle négatives

- **Northwestern Image** : `https://iiif.dc.library.northwestern.edu/iiif/3/e814609e-ddfd-4427-b4cf-1a70d6e49129/info.json` : `fetch_error` avec signal HTTP 200 sans corps, **pas de JSON**. OpenAPI 3.1 du REST du fournisseur déjà obtenue en V.
- **Cultural Japan** : `https://app.cultural.jp/iiif-collection/collection.json` : `fetch_error` avec signal HTTP 200 sans corps ; le jeu tiers IIIF Discovery in Japan n'est pas le même document.
- **Villanova** : `/Item/vudl:92879/Manifest` et l'exemple `/Collection/vudl:3/IIIF` renvoient 403 au lecteur ; aucune tentative de contourner la protection.
- **Jena** : l'exemple `/api/iiif/presentation/v2/jportal_derivate_00401748/manifest` restitue le front de protection `mod_repudiator`, **pas** le JSON.
- **Bologna Historica** : `/oai` et `/oai?verb=Identify` renvoient 400 avec cet extracteur ; ne pas affirmer que le protocole OAI est définitivement en panne ni qu'il retourne un quota.
- **Digital Commonwealth** : `/search/opensearch.xml` restitue la page de vérification humaine, non le XML.
- **Yale** : `/catalog/opensearch.xml` n'a fourni qu'un résumé d'en-tête de service, non le document XML.
- **National Gallery of Art** : le manifeste d'exemple `?cultObj:id=26` et variante avec caractère encodé répondent 403 ; aucune donnée récupérée.

**Méthode :** consultations ponctuelles de documentation et de ressources publiques, aucun essai massif ni injection de cookies, sessions, comptes ou solveurs CAPTCHA. Des mises à jour des données canoniques et du classeur sont à effectuer **ensemble** après réconciliation des sources.
