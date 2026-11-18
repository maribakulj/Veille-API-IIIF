# Passe AC — accès IIIF dans le code DRI et manifeste statique Northwestern (18 novembre 2026)

## Méthode et limites

Sources principales : **code officiel versionné** du Digital Repository of Ireland (DRI), commit immuable [`7f793a938a4be4d2f387bb92e66c17c2507e59ee`](https://github.com/Digital-Repository-of-Ireland/dri-app/commit/7f793a938a4be4d2f387bb92e66c17c2507e59ee) de la branche `develop` du **10/11/2026**, et **documentation publique de Clover (Northwestern University Libraries)**, capturée dans des copies datées du 18/11/2026. L'analyse porte sur de vrais contenus récupérés, **mais il ne s'agit pas de la lecture des URL originales bloquées** `https://repository.dri.ie/api-docs` ou `https://iiif.dc.library.northwestern.edu/iiif/3/e814609e-ddfd-4427-b4cf-1a70d6e49129/info.json`. Les deux restent non démontrées. Pas d'identification, de contournement WAF ou de test de débit.

## DRI : chemins, contrôle d'accès et signification des paramètres d'authentification

Fichiers du projet réellement lus (les URL ci-dessous renvoient **à la version du commit** et non à une branche mouvante) :

- [`config/routes.rb`](https://github.com/Digital-Repository-of-Ireland/dri-app/blob/7f793a938a4be4d2f387bb92e66c17c2507e59ee/config/routes.rb) : manifeste `/iiif/:id/manifest`, collection `/iiif/collection/:id`, séquence `/iiif/:id/sequence`, serveur Riiif sous `/images`, moteurs Rswag UI/API montés à `/api-docs`.
- [`config/initializers/rswag-ui.rb`](https://github.com/Digital-Repository-of-Ireland/dri-app/blob/7f793a938a4be4d2f387bb92e66c17c2507e59ee/config/initializers/rswag-ui.rb) : le document de spécification attendu est **`/api-docs/v1/swagger.json`**. [`config/initializers/rswag-api.rb`](https://github.com/Digital-Repository-of-Ireland/dri-app/blob/7f793a938a4be4d2f387bb92e66c17c2507e59ee/config/initializers/rswag-api.rb) : fichiers Swagger générés depuis `Rails.root/swagger`. **Le véritable fichier déployé n'a pas été extrait**, et ne doit pas être substitué par `spec/fixtures/swagger.json`, simple jeu de test avec une route de signets.
- [`spec/swagger_helper.rb`](https://github.com/Digital-Repository-of-Ireland/dri-app/blob/7f793a938a4be4d2f387bb92e66c17c2507e59ee/spec/swagger_helper.rb) : API **Swagger 2.0 / V1**, définitions de paramètres `user_token` et `user_email` en query string. Leur existence dans le schéma **n'implique pas** l'authentification obligatoire pour tous les manifestes.
- [`spec/api/iiif_spec.rb`](https://github.com/Digital-Repository-of-Ireland/dri-app/blob/7f793a938a4be4d2f387bb92e66c17c2507e59ee/spec/api/iiif_spec.rb) : **test d'un manifeste public publié avec `user_token = nil` et `user_email = nil`** sous réponse `200`; la même suite vérifie `401` pour l'accès non autorisé et `404` pour un identifiant inexistant.
- [`app/controllers/iiif_controller.rb`](https://github.com/Digital-Repository-of-Ireland/dri-app/blob/7f793a938a4be4d2f387bb92e66c17c2507e59ee/app/controllers/iiif_controller.rb) : contrôle des permissions sur le document avant renvoi des manifestes et CORS `Access-Control-Allow-Origin: *` ajouté sur ces réponses ; **ce code n'est pas une capture d'en-tête de production**.
- [`app/services/riiif_authorization_service.rb`](https://github.com/Digital-Repository-of-Ireland/dri-app/blob/7f793a938a4be4d2f387bb92e66c17c2507e59ee/app/services/riiif_authorization_service.rb) : pour une image rattachée à un objet, les autorisations sont fondées sur le caractère publié et les droits publics. Les contrôles sur l'information d'image et son affichage sont distingués par la méthode.
- [`app/controllers/concerns/dri/iiif_viewable.rb`](https://github.com/Digital-Repository-of-Ireland/dri-app/blob/7f793a938a4be4d2f387bb92e66c17c2507e59ee/app/controllers/concerns/dri/iiif_viewable.rb) : construction des manifestes Presentation **v2** (`sc:Manifest`, `sc:Collection`, `sc:Sequence`) et services Image **v2 level2** à partir des notices/objets et fichiers Solr.

**Conclusion DRI :** code de **gestion d'accès explicite**, ouvert pour les exemples de manifestes publics, authentification nécessaire pour certains contenus. Le refus Cloudflare 403 de `repository.dri.ie/api-docs` vu depuis un autre client ne démontre pas un quota. **Aucun seuil numérique de débit ni en-tête de quota n'a été vérifié dans les sources analysées**. Le commit du `develop` daté du 10/11/2026 **n'est pas une preuve que ce même commit est déployé en production** ; aucun test de débit ou d'endpoint privé n'a été exécuté.

## Northwestern : véritables documents JSON de démonstration, mais pas preuve de production

Documentation de l'équipe [Clover IIIF, *Mocks*](https://clover.iiif.library.northwestern.edu/docs/mocks) et [*Default viewer*](https://clover.iiif.library.northwestern.edu/docs/viewer/default), lues comme pages publiques en novembre 2026. Trois **manifestes statiques complets** issus de cette documentation ont été obtenus et parsés :

| URL de démonstration | Type | Contenu |
| --- | --- | --- |
| https://clover.iiif.library.northwestern.edu/mocks/tagging/manifest.json | IIIF Presentation **3**, `Manifest` | **15 982 caractères**, **1 canevas**, annotations `tagging`, renvoi à l'image réelle sur `iiif.dc.library.northwestern.edu/iiif/3/bcb98b9f-4c44-4fd0-bfa9-673fb904a2b1` |
| https://clover.iiif.library.northwestern.edu/mocks/paged/manifest.json | IIIF Presentation **3**, `Manifest` | **141 002 caractères**, **31 canevas**, catalogue de vélos 1896 ; annoté et enrichi pour démonstration |
| https://clover.iiif.library.northwestern.edu/mocks/navplace/manifest.json | IIIF Presentation **3**, `Manifest` | **12 421 caractères**, **1 canevas**, `navPlace` ajouté pour démonstration |

**Fichier de preuve conservé dans le dépôt** : [`institutions/northwestern-university-libraries/sources/lectures-2026-11-18/clover-tagging-manifest-static.json`](institutions/northwestern-university-libraries/sources/lectures-2026-11-18/clover-tagging-manifest-static.json). Ce contenu est un **mock enrichi par l'équipe Clover**, non le corps canonique d'un endpoint `api.dc...` ou `iiif.dc...`. La documentation précise que certaines représentations ont été recopiées depuis l'API en octobre 2026 puis **modifiées** : métadonnées, annotations, identifiants et démonstrations ne sont donc pas forcément la sortie brute des services de collection.

Deux tentatives ponctuelles supplémentaires sur les **vrais services Image** référencés dans les mocks, `https://iiif.dc.library.northwestern.edu/iiif/3/bcb98b9f-4c44-4fd0-bfa9-673fb904a2b1/info.json` et `https://iiif.dc.library.northwestern.edu/iiif/3/1ece48b0-8a49-491d-9f3f-90dc8bcca1ac/info.json`, ont encore rendu **`fetch_error` avec indication HTTP 200 mais sans corps JSON**. L'URL originale de l'audit `.../e814609e-ddfd-4427-b4cf-1a70d6e49129/info.json` reste elle aussi non extraite.

**Conclusion Northwestern :** démonstration documentée de Presentation 3/annotations et de références à un Image API réel, mais **aucune validation de réponse `info.json` brute**, et aucun nouveau quota chiffré. Le seuil de thumbnail 300 px de l'API REST déjà documenté est **une dimension d'image**, pas une fréquence HTTP.

## Prochaine intervention prioritaire

L'inventaire des **98 URL sans contenu original** ne doit **pas** baisser du seul fait de ces alternatives. Cette passe enrichit les données de **deux institutions** et augmente les observations supplémentaires, mais ne ferme pas les URL d'API protégées. Le meilleur complément reste une requête HTTP autorisée depuis un réseau institutionnel ou une demande explicite sur les quotas pour les cas où un seuil est réellement indispensable, en particulier les API Image et Swagger sous protection. Les PDF partiellement lus restent distincts.
