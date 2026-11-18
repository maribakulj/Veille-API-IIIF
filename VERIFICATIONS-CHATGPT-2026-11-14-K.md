# Rattrapage documentaire K — 14 novembre 2026

## Périmètre
Dossiers **GLAM-070 à GLAM-084** : Digital Repository of Ireland (DRI), Digital UCD, KU Leuven, Utrecht, Radboud, Jena, NDL Japon, Kyoto, Waseda, Keio, National Palace Museum Taiwan, e-Museum NICH, State Library Victoria, Qatar Digital Library, Cultural Japan.

**Méthode** : lecture des `a_verifier_manuellement` et `limites_documentees` du commit `c6bc71173f861502bd96d438f4489328ccf81b9e`, puis recherche et lecture de documents publics par moteur web / code source GitHub. Aucun contournement de WAF ni mesure HTTP sur l'IP de l'institution. Les indications « accessibles » désignent la récupération de texte documentaire via l'outil web.

## 070. Digital Repository of Ireland

**Nouvelle preuve de premier rang dans le code officiel :**
- `https://github.com/Digital-Repository-of-Ireland/dri-documentation/blob/main/developer-guide/01-api-doc.rst` (dépôt mis à jour en mars 2026) pointe vers `https://repository.dri.ie/api-docs` mais ne reproduit pas la spécification ; l'hôte reste bloqué.
- `https://github.com/Digital-Repository-of-Ireland/dri-app/blob/main/config/initializers/rswag-ui.rb` définit la **source de Swagger réelle** : `/api-docs/v1/swagger.json` (« API V1 Docs ») via rswag. **URL déduite directement du code, pas devinée** ; endpoint public **non exécuté** dans cette passe.
- `https://github.com/Digital-Repository-of-Ireland/dri-app/blob/main/spec/api/iiif_spec.rb` documente **`GET /iiif/{id}/manifest`** et des réponses **200, 401, 404**. Le test officiel contient un cas explicite de **manifeste publié accessible sans authentification** (`user_token=nil`) et de **manifeste non publié accessible avec authentification**.
- `https://github.com/Digital-Repository-of-Ireland/dri-app/blob/main/spec/swagger_helper.rb` : l'API utilise, pour certaines routes sécurisées, `user_token` et `user_email` en paramètres query (ne pas les ajouter aux URL de manifestes publics).
- Aucun seuil de débit chiffré n'a été trouvé **dans ces trois fichiers**. Le fait que les spécifications testent 200/401/404 sans 429 **n'exclut pas une protection WAF**.
- **Conclusion** : le schéma de manifeste, l'emplacement Swagger et la différence public/privé peuvent être considérés **documentés** ; `repository.dri.ie/api-docs`, `robots.txt`, `dri.ie/standards-adoption` demeurent **bloqués**.

## 071. University College Dublin — Digital UCD

La page `www.ucd.ie/library/` avait déjà été récupérée au rapport B. Le problème TLS de `digital.ucd.ie` depuis la sonde n'est pas résolu par la lecture du portail. En particulier le maximum de **2 000 pixels** annoncé par l'ancienne aide est une **limite d'image téléchargeable** et **pas un débit**. `robots.txt` actuel non lu.

## 072. KU Leuven / LIBIS / Teneo

- **Pages officielles actuelles retrouvées** : `https://bib.kuleuven.be/english/libis/libis`, `https://bib.kuleuven.be/english/collections-access-borrowing/collection-policy/digitale-preservatie-en-langetermijnbewaring`, `https://bib.kuleuven.be/english/libis/heron`. Elles décrivent Teneo comme stockage durable/visualisation IIIF et l'association avec Mirador, Universal Viewer ; mais **aucun quota req/min**.
- **Documentation de support officielle** : `https://libis.helpdocsite.com/informatie/technische-andere-informatie-home` précise les comptes **Alma** et le contact **LIBISnet helpdesk** ; **ces comptes internes Alma ne doivent pas être assimilés à une authentification IIIF**.
- **Ancien schéma du Resolver corroboré** dans le manuel technique tiers `https://kennisbank.meemoo.be/toolbox/handboek-persistente-uris` (interviews LIBIS 2016–2017), ex. `resolver.libis.be/IE157176/list`, `/metadata`, `/FL157178/stream`. Une autre présentation de formation « Toegang tot digitale objecten » mentionne `/representation`, `/thumbnail`, `/stream`, et `/manifest`. Ce sont des **schémas historiques**, pas des ressources testées en direct.
- `https://resolver.libis.be/IE978853/manifest` n'est **pas accessible** à l'outil web ; les anciens tests de la sonde sur `libis.be` restent à revalider ; ne pas transformer le schéma théorique en preuve de disponibilité.
- **Résultat** : lacune de documentation générale sur Teneo/LIBIS comblée, mais les **quatre endpoints de la liste manuelle et tous les quotas spécifiques IIIF restent ouverts**.

## 073. Utrecht University Library

Le dossier signale que le `robots.txt` de `objects.library.uu.nl` **interdit précisément /manifest, /iiif_manifest, /fcgi-bin/iipsrv.fcgi**. La présence d'une page d'aide IIIF ne constitue pas une autorisation de crawler ces routes. **Reste un contact institutionnel** pour permissions, modalités de moissonnage et plafonds. La valeur existante `Aucune limite de débit publiée = aucune` ne doit **jamais** être interprétée comme une API illimitée.

## 074. Radboud University Library

`https://repository.ubn.ru.nl/rest/` et `/rest/communities` non établis en production (404 dans la sonde). L'interface OAI et le service ContentDM sont distincts. **Reste une confirmation institutionnelle ou une documentation d'API réelle**, pas une requête répétée sur une route spéculative.

## 075. Thüringer Universitäts- und Landesbibliothek Jena

Manifeste `https://zs.thulb.uni-jena.de/api/iiif/presentation/v2/jportal_derivate_00401748/manifest` : le dossier rapporte **500 sur un seul identifiant**. Cela n'établit ni une panne générale ni un quota. **Essai de manifeste alternatif légitime** requis avant conclusion ; ne pas faire de rafales.

## 076. National Diet Library — Japan

- Documentation officielle **actuelle lisible** `https://ndlsearch.ndl.go.jp/en/help/api` : Search (SRU, OpenSearch, OpenURL), Harvest (OAI-PMH) et Thumbnail comme **familles distinctes**.
- **Inscription requise dans certains cas** : certaines entreprises/usages commerciaux et Thumbnail ; à l'inverse les particuliers et organismes non lucratifs pour usage non commercial de métadonnées n'ont pas toujours besoin d'une demande. L'institution invite les usages **continus** à se signaler par formulaire pour rester informés des évolutions.
- **Concurrence limitée** et possibilité de blocage d'IP lors de sollicitations continues trop importantes ; **pas de req/min chiffrées dans la page**. Le dossier contient les contraintes de pagination de la spécification PDF datée du **25 septembre 2026** (500 résultats Search, OAI 200 notices/resumptionToken) : ce ne sont pas des quotas de débit.
- Le manifeste IIIF de `www.dl.ndl.go.jp` et l'OAI `ndlsearch.ndl.go.jp/api/oaipmh?verb=Identify` demeurent non testés après l'arrêt 429 de la sonde initiale : ne pas insister ni les classer comme 429 observés sur ces routes.

## 077. Kyoto University — Rare Materials

Le lien `https://rmda.kulib.kyoto-u.ac.jp/en/reuse` avait déjà été lu et la restriction **2 000 pixels** s'applique à certains JPEG téléchargés, pas au nombre d'appels/min. Il reste une demande d'information **institutionnelle** sur l'usage massif de IIIF ; pas une page à « débloquer ».

## 078. Waseda University — Kotenseki

- Deux pages officielles publiques **récupérées en lecture web** : `https://www.wul.waseda.ac.jp/kotenseki/ga_IIIF/about_iiif_en.html` (explication des manifestes, boutons Universal Viewer et lien JSON) et **ancienne lacune manuelle résolue** `https://www.wul.waseda.ac.jp/kotenseki/ga_IIIF/guide_UV_en.html` (**How to Use Universal Viewer**), désormais lue et non 503 dans ce client.
- La page `https://www.wul.waseda.ac.jp/kotenseki/index_en.html` précise que réutiliser les images dans des publications, pages web ou émissions exige une autorisation préalable : **restriction de droits**, non quota.
- La **notice ciblée** `https://www.wul.waseda.ac.jp/kotenseki/html/ho04/ho04_02555/index.html` retourne toujours **503** à l'outil web ; l'URL exacte du manifeste de ce document reste donc non récupérée.
- `https://www.waseda.jp/robots.txt` n'est pas récupérable via cet outil ; **ouvert**.

## 079. Keio University

Le PDF `https://iiif.lib.keio.ac.jp/ANT/Japan/1/pdf/Japan_1.pdf` n'a pas été téléchargé car volumineux et soumis aux conditions de reproduction ; aucun nouveau plafond établi. La visionneuse URL `uv.php` reste à contrôler depuis un navigateur autorisé, sans contourner les restrictions.

## 080. National Palace Museum — Taiwan

`https://digitalarchive.npm.gov.tw/opendata/Json/NPMIIIF.pdf` a encore **expiré** lors de la tentative du lecteur web. **Le PDF n'a pas été lu**. Le `info.json` de `iiifod.npm.gov.tw`, le PDF du Presidential Hackathon et le formulaire restent en attente. Aucune nouvelle politique chiffrée n'est établie, même si la documentation de collections mentionne une Open API.

## 081. e-Museum / NICH — Japon

- `https://emuseum.nich.go.jp/terms?locale=en` ne fournit pas de page de conditions distincte au lecteur web.
- **Les conditions officielles complètes figurent bien sur** `https://emuseum.nich.go.jp/about?langId=en&webView=0`, rubrique **Terms of Use**, et sont **lisibles**. Réutilisation des images au-delà des exceptions permises par le droit d'auteur soumise à l'autorisation de l'institution détentrice. Cette source est un **remplaçant documentaire fiable pour la page /terms manquante** ; **pas de quota API chiffré**.
- `https://colbase.nich.go.jp/` est une interface SPA ; sa documentation API éventuelle n'a pas été établie ici. **Reste ouvert**.

## 082. State Library Victoria

- **Source institutionnelle de premier rang** `https://lab.slv.vic.gov.au/resources/using-iiif-to-work-with-the-librarys-digitised-collections` décrit **le manifeste exact** `https://rosetta.slv.vic.gov.au/delivery/iiif/presentation/2.1/IE145082/manifest`, son JSON IIIF Presentation 2 et sa relation aux images.
- **Autre tutoriel officiel** `https://slvlab-prod.coolify.slv.vic.gov.au/experiments/my-place-tim-sherratt/exploring-slv-urls` explique la construction d'URL avec l'identifiant IE tiré du visualiseur ou du MARC `956$e`, avec exemple `IE24074939`.
- **La racine de l'Image API `https://rosetta.slv.vic.gov.au/iiif/2` est lisible** dans le lecteur web, indique **Cantaloupe**, Image **2.x**, et liens vers Image **1.x** et **3.x**. C'est une preuve de documentation de service, **pas** que `/info.json` répond via cette IP.
- Malgré ces sources, le manifeste `IE145082` et `rosetta.slv.vic.gov.au/robots.txt` restent non récupérables : blocage Cloudflare. **Ne pas traiter l'hôte complet comme éteint** simplement parce que les routes de manifeste sont filtrées. Les limites techniques restent inconnues.

## 083. Qatar Digital Library

`https://www.qdl.qa/en/copyright-and-ethical-terms-reuse`, `https://qdl.qa/node/372`, `https://www.qdl.qa/en/iiif/81055/vdc_100023807156.0x000001/manifest` restent inaccessibles à l'outil web. **Aucun contournement ni quota vérifié**. Le seuil d'image de 1 200 pixels dans le dossier concerne la **taille maximale**, et non un débit.

## 084. Cultural Japan

`https://app.cultural.jp/iiif-collection/collection.json` reste non récupérable via le lecteur web. Les mentions `robots.txt` sur `cultural.jp` sont spécifiques à cet hôte et ne prouvent pas un quota de `app.cultural.jp`. **Ouvert**.

## Suites d'intégration
1. **DRI** : ajouter le chemin `/api-docs/v1/swagger.json` et le manifeste `GET /iiif/{id}/manifest` comme **documentation technique déduite du code officiel**, non comme endpoints testés ; distinguer objets publiés et privés.
2. **Waseda** : **déplacer le guide Universal Viewer parmi les pages lues** ; conserver la notice 503.
3. **SLV** : distinguer root Image Server public lisible et routes de manifestes filtrées ; documenter Image API 3.x comme **page de service disponible**, sans préjuger des capacités des ressources.
4. **e-Museum** : remplacer la fausse piste `/terms` par la vraie section `/about?langId=en&webView=0`.
5. **KU Leuven** : garder les sous-systèmes Alma, Limo, Teneo/Resolver et IIIF séparés, y compris dans les graphiques.
6. **NDL** : conserver les règles d'inscription et de concurrence, ne pas convertir pagination ou 429 de SRU en quotas IIIF.
7. Tous les items bloqués gardent un statut explicite et ne sont pas cochés.

Sources de preuves mentionnées directement dans chaque ligne ; les fichiers canoniques et le benchmark n'ont pas été modifiés durant cette phase de collecte.
