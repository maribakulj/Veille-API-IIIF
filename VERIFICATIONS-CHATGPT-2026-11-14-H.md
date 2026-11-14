# Rattrapage documentaire H — 14 novembre 2026

Étape : **GLAM-041 à GLAM-049**, principalement Northwestern, Duke, UCLA, Princeton et National Gallery of Art. Les `a_verifier_manuellement` et `limites_documentees` des dossiers ont été rapprochés des sources officielles accessibles. Pas de tests d'en-têtes ni de requêtes de charge.

## Northwestern University Libraries (GLAM-045) : API officielle et code source

L'ancienne entrée `https://www.library.northwestern.edu/libraries-collections/digital-collections/index.html` peut être complétée par **deux sources officielles actuelles** :
- Documentation API : https://api.dc.library.northwestern.edu/ (redirige vers https://api.dc.library.northwestern.edu/docs/v2/index.html).
- Code source maintenu par la bibliothèque : https://github.com/nulib/dc-api-v2 (README et spécification `docs/docs/spec/openapi.yaml`). Dépôt poussé au **12 novembre 2026** d'après la métadonnée GitHub consultée.

L'API documente les familles `/works`, `/collections`, `/file-sets` ainsi que des représentations IIIF. Le README détaille :
- `GET /works/[WORK_ID]?as=iiif` : **manifeste IIIF** d'un Work ;
- `GET /works/[WORK_ID]/search?as=iiif&q=[QUERY]` : recherche dans les transcriptions, **IIIF Content Search 2.0**, renvoie une `AnnotationPage` ;
- `GET /file-sets/[FILE_SET_ID]/search?as=iiif&q=[QUERY]` : recherche dans les annotations d'un Canvas ;
- `/oai` documenté dans l'OpenAPI, avec `resumptionToken` pour le moissonnage.
Les URL locales `https://USER_PREFIX.dev.rdc.library.northwestern.edu:3002/...` dans le README sont des **exemples de développement**, et non des points d'accès publics à réutiliser. Elles ne doivent pas devenir des endpoints d'audit.

**Piège de quotas** : le dépôt `nulib/dc-api-v2` possède aussi un sous-module `chat/` avec `rate_limiter.py` et des réponses 429 (fichier `chat/src/handlers.py`). **Ce mécanisme concerne l'API conversationnelle de chat**, pas une preuve de quota de l'API principale `/works`, IIIF, Search ou OAI. Aucun plafond chiffré de l'API principale n'a été vérifié lors de cette passe.

**Restent ouverts** : `https://dc.library.northwestern.edu/` (403 CloudFront par la sonde), le `info.json` `https://iiif.dc.library.northwestern.edu/iiif/3/e814609e-ddfd-4427-b4cf-1a70d6e49129/info.json` (non testé après 403), les en-têtes et la politique de débit sur les hôtes de production. La nouvelle doc prouve les endpoints et la politique de pagination/représentation, pas l'accès technique depuis un client précis.

## Duke University Libraries (GLAM-044) : confirmation du dispositif Anubis

La FAQ institutionnelle https://library.duke.edu/using/off-campus/impact-of-bots a été lue le 14/11. Elle confirme :
- Déploiement d'**Anubis (preuve de travail côté navigateur)** dès **juin 2025** pour répondre aux sollicitations excessives et parfois trompeuses des bots, notamment sur le Duke Digital Repository ;
- Pour le crawling autorisé, recommandé **au moins 10 secondes de délai** entre les requêtes, et respect des `Disallow` ;
- Restriction des **téléchargements automatisés systématiques de matériels de bibliothèque** ; certains catalogues contiennent des données sous licence ;
- **500 Mo sur 30 minutes** : seuil de blocage temporaire des comptes sur les **ressources proxifiées sous licence**, et **non une limite IIIF**. L'interface publique Duke Digital Repository ne doit pas hériter de ce chiffre.

Il faut conserver le `200 + page de défi Anubis` comme **blocage applicatif**, pas comme API répondant 200 avec un manifeste valide ; ne pas tenter de contourner le mécanisme.

Le PDF du pilote Anubis incomplet `https://dukespace.lib.duke.edu/server/api/core/bitstreams/816ef134-55cf-49f6-9a8b-1e8a2324b1ff/content` n'a pas été lu intégralement lors de cette passe. Le téléchargement interrompu antérieur ne doit pas être effacé.

## UCLA Library Digital Collections (GLAM-046) : URL de politique résolue

- `https://www.library.ucla.edu/about/policies/ucla-library-copyright-policies/` : **page institutionnelle officielle récupérée et lue**, offrant des liens sur les ressources électroniques sous licence, les réserves, les copies d'archives, les documents inédits, etc.
- https://www.library.ucla.edu/about/policies/lsc-duplication-use-licensing-policy/ : politique spécifique aux **Special Collections** ; le fait de fournir un fichier numérique ne vaut pas autorisation générale de réutiliser l'œuvre, et les droits tiers doivent être respectés.
- https://www.library.ucla.edu/about/policies/library-special-collections-digitization-policy/ : politique de numérisation et publication de collections, sans plafond de requêtes IIIF dans cette page.
Aucune de ces pages ne donne de seuil de débit pour `digital.library.ucla.edu` ; ne pas les présenter comme restrictions de quota. Le possible défi Anubis sur `/catalog` n'a pas été reproduit techniquement ici.

## Princeton University Art Museum (GLAM-042)
- L'API de métadonnées est explicitement documentée dans https://github.com/Princeton-University-Art-Museum/puam-api-docs/blob/main/README.md sous `https://data.artmuseum.princeton.edu` ; **pas d'authentification actuellement exigée** selon ce README, susceptible de changement. Docs relatives à Objects, Makers, Packages et Search.
- Le README propose également des archives **JSON complètes et statiques** des collections, mises à jour chaque semaine, pour les usages en visualisation et ML **ne nécessitant pas d'appels dynamiques** (fichiers `objects.zip`, `makers.zip`, `packages.zip`). C'est un mode de collecte plus adapté qu'un moissonnage agressif de l'API, mais **ce n'est pas une règle de rate limiting**.
- Les pages de conditions et robots `artmuseum.princeton.edu`, ainsi que `media.artmuseum.princeton.edu/robots.txt`, **restent non vérifiées** en direct.

## GLAM-041, 043, 047, 048, 049
- Princeton University Library : conditions d'accès et d'images difficiles à lire sur les hôtes Cloudflare ; ne pas attribuer au musée les règles de la bibliothèque, et réciproquement.
- Cornell : pages `digital.library.cornell.edu` toujours en 403 ; droits de reproduction documentaire à ne pas confondre avec quota.
- Art Institute Chicago : déjà traité dans le rapport B (API de métadonnées anonyme 60/min ; IIIF Image hôte séparé).
- Getty : ses données ouvertes et ses images n'ont pas nécessairement la même licence ; `media.getty.edu/robots.txt` en 503 et ID Management API restent ouverts.
- National Gallery of Art : pages `www.nga.gov` en défi ; `api.nga.gov/robots.txt` décrit des règles robots, pas un quota de débit API. Le manifeste `https://www.nga.gov/api/v1/iiif/presentation/manifest.json?cultObj:id=26` n'a pas été testé ici.

## À intégrer avec contrôle de qualité
- Northwestern : enrichir l'inventaire des familles **Content Search v2** et **OAI-PMH**, conserver quota **inconnu**, et ne pas extrapoler le limiter du sous-projet `chat/`.
- Duke : classifier **10 s = recommandation politesse crawler** ; **500 Mo/30 min = seuil proxy e-resources**, **pas IIIF** ; défendre l'absence de contournement Anubis.
- UCLA : marquer la lecture documentaire de l'ancienne URL `copyright-policies` comme résolue, sans prétendre mesurer les 429.
- Princeton : proposer les JSON hebdomadaires statiques comme alternative de récolte, non comme valeur de quota.
