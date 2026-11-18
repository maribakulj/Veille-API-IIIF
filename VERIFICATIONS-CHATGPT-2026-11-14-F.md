# Rattrapage documentaire F — 14 novembre 2026

Périmètre de cette passe : **Smithsonian, Harvard, Harvard Art Museums, Yale Center for British Art**, dans la série GLAM-032 à GLAM-039. Source des questions : dossiers `institutions/*/data.json` au commit `c6bc71173f861502bd96d438f4489328ccf81b9e`. Les vérifications **ne sont pas des tests HTTP d'en-têtes ni des dépassements de quotas**.

## Smithsonian Institution (GLAM-032)

**URL manuelles du dossier :**
- `https://www.si.edu/openaccess/devtools` : le **texte officiel actuel est récupérable par l'index web** (source indexée il y a quatre semaines) ; page « Open Access Developer Tools », décrit la publication de JSON sur GitHub **mise à jour chaque semaine**, l'API Open Access accessible via **api.data.gov** et EDAN. Il ne publie **pas** de plafond Smithsonian spécifique de débit. **Attention** : la lecture directe peut être 404 ou filtrée selon le client ; la récupération indexée n'est pas une preuve HTTP live. Source : https://www.si.edu/openaccess/devtools.
- `https://www.si.edu/openaccess` : page officielle consultable via l'outil web, présentant l'Open Access, sa FAQ, ses outils développeurs et sa politique de réutilisation, sans valeur numérique de quota dans la page. Source : https://www.si.edu/openaccess.
- `https://api.data.gov/signup/` : **inscription nécessaire** pour obtenir une clé propre. Elle est une action utilisateur, pas une lecture de documentation ou un test de limite ; ne pas créer de compte ni envoyer un formulaire pour « clôturer » une vérification.
- La **FAQ officielle** https://www.si.edu/openaccess/faq explique que les objets Open Access peuvent avoir un **manifeste IIIF JSON** et que les métadonnées sont accessibles à la fois via l'API et par dépôts JSON GitHub ; la distinction droits CC0 vs droits tiers et marques Smithsonian ne concerne pas un débit d'API.
- Le module institutionnel https://github.com/Smithsonian/smithsonian-openaccess/blob/main/README.md exige expressément un `api_key` de `api.data.gov` pour les appels de ses méthodes `si_openaccess.search`, `content`, `metrics_stats`. Ce dépôt ne prouve pas pour autant un quota différent de la plateforme de clés.

**Politique vérifiée au niveau de l'infrastructure api.data.gov :**
- https://api.data.gov/docs/developer-manual/ : limite par défaut **1 000 requêtes/heure par clé**, DEMO_KEY **30 requêtes/heure et 50/jour par IP**, réponses attendues `X-RateLimit-Limit`, `X-RateLimit-Remaining`, code `429` en cas de dépassement.
- https://api.data.gov/docs/agency-manual/ : l'agence peut modifier les limites par **service**, **utilisateur**, voire **famille d'URLs** (et introduire des plafonds à plus courte durée). **Ces chiffres ne sont donc pas un quota Smithsonian démontré.** Les reproduire dans le benchmark uniquement avec `périmètre=api.data.gov / défaut`, `applicabilité Smithsonian=à confirmer`.
- Réponse non vérifiée ici : en-têtes réels d'une requête Smithsonian avec une clé valide et plafond éventuellement personnalisé ; action `CLÉ / UTILISATEUR REQUISE`, pas défaut d'une page publique.

## Harvard Art Museums (GLAM-034)

**Ticket `https://github.com/harvardartmuseums/api-docs/issues/29` : statut confirmé OPEN au 14 novembre 2026.**
- Créé **28 avril 2026**, dernier commentaire du **29 avril 2026**.
- Le demandeur rapporte : `api.harvardartmuseums.org` renvoie HTTP 200, `nrs.harvard.edu` redirige en **303** vers `ids.lib.harvard.edu`, lequel peut renvoyer **429 dès la première image**, même à environ **une image/10 s** et sous le plafond annoncé de **2 500 appels/jour** de l'API de métadonnées. Localisation du client rapportée : infrastructure AWS Tokyo.
- Réponse de **Jeff Steward**, membre du projet : problème observé chez plusieurs utilisateurs à travers le monde ; pas de solution annoncée à cette date ; l'équipe du musée **ne gère pas** le système `ids.lib.harvard.edu`, ne peut pas y débloquer une IP ; pas d'option de téléchargement massif de ses images CC0 actuellement. Source : https://github.com/harvardartmuseums/api-docs/issues/29#issuecomment-4343669728.
- **Conséquence : un 429 constaté à la première requête au CDN peut traduire une restriction d'IP/d'accès et non une consommation réelle du quota du service de métadonnées.** Ne pas propager le plafond 2 500/jour à l'hôte d'images ; ne pas affirmer que le ticket est résolu.
- Documentation publique officielle : https://github.com/harvardartmuseums/api-docs/blob/master/README.md :
  - API REST de métadonnées **requiert apikey** ;
  - Image API IIIF **v2.1** via `baseimageurl` / `primaryimageurl` et redirection NRS ;
  - Presentation API **distincte**, ex. `https://iiif.harvardartmuseums.org/manifests/object/299843`.
  - L'absence de clé pour le service d'images ne signifie pas immunité aux limitations CDN.
- `https://harvardartmuseums.org/article/1035` (« The HAM API at 10 », 2023) reste en **404/bloqué** dans l'outil web ; une mention de l'article sur le portfolio du responsable ne remplace pas la lecture de l'original. **Ouvert**.
- Le formulaire Google de clé reste sous authentification/action de compte ; aucune demande envoyée.

## Harvard Library (GLAM-033)
- `https://harvardwiki.atlassian.net/wiki/spaces/LibraryStaffDoc/pages/43287734/LibraryCloud+APIs` est une source officielle pour la limite LibraryCloud déjà enregistrée dans le dossier. Ne pas extrapoler ce plafond à `viewer.lib.harvard.edu`, à MPS ou à Harvard Art Museums : au moins trois plateformes distinctes.
- Les contraintes AWS WAF et `mps.lib.harvard.edu/robots.txt` ne sont pas résolues par cette passe.

## Yale Center for British Art (GLAM-036)
- `https://britishart.yale.edu/open-data-and-data-services-terms-use` a été **relu** dans sa version indexée il y a trois semaines. Il exige un `User-Agent` décrivant le logiciel, le contact email et l'URL pour les clients automatisés. Le Center peut limiter ou bloquer l'usage **excessif à sa discrétion**, sans publier de seuil de requêtes/minute.
- Point juridique important : une **URL de ressource image présente dans les données ne vaut pas, à elle seule, autorisation de télécharger ou réutiliser cette image**. Les données ouvertes et les fichiers média font l'objet de conditions distinctes.
- Ancien hôte `collection.britishart.yale.edu` et le wiki JS `yaleits.atlassian.net` restent sans preuve technique actuelle. Les conditions de la YCBA ne sont pas automatiquement celles des différentes plateformes Yale.

## Ce qui reste
- Confirmer les **limites configurées réellement par le Smithsonian** via un compte autorisé ou réponse de l'institution, et, séparément, les éventuels quotas des **manifestes IIIF non servis par api.data.gov**.
- Vérifier les URLs d'images et de manifestes Harvard de façon polie et séparée sur une infrastructure contrôlée, **sans reproduire volontairement un blocage 429**.
- Recherche historique de l'article « The HAM API at 10 » si une copie intégrale est disponible légalement.
- Approfondir Yale LUX (API liée, JS SPA, wiki) et garder séparées les familles IIIF Image, Presentation et Linked Art.
