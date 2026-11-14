# Rattrapage documentaire M — 14 novembre 2026

## Compléments ciblés GLAM-080 et GLAM-084
Contexte : `PLAN-RATTRAPAGE-CHATGPT.md`, `VERIFICATIONS-CHATGPT-2026-11-14-K.md` et champ `a_verifier_manuellement` de `data.json` au commit `c6bc71173f861502bd96d438f4489328ccf81b9e`. Lecture documentaire via les pages publiques, **pas mesure HTTP depuis la sonde Python**.

### Cultural Japan (GLAM-084) : URL de collection IIIF corroborée par le site officiel

**L'URL problématique du dossier** est `https://app.cultural.jp/iiif-collection/collection.json` (403/access denied pour le client précédent).

La page d'accueil officielle `https://cultural.jp/en` :
- affiche explicitement **« IIIF Collection »** dans le menu *Usage* et fournit un lien externe de visualisation pointant vers un lecteur IIIF de Kanzaki avec le paramètre URL **exact** `https://app.cultural.jp/iiif-collection/collection.json`. L'hôte Kanzaki n'est **pas** présenté comme l'hébergeur de la collection.
- affiche un lien **« For Developers »** vers `https://api.cultural.jp/`, redirigé vers `https://api.cultural.jp/spec` : page avec le titre **Cultural Japan Search API**, mais sans texte lisible par notre lecteur HTML. La seule présence de cette documentation ne constitue pas une observation de clé, authentification ou quota.
- affiche un lien distinct vers un **« RDF Store »** `ld.cultural.jp`, et un outil « IIIF Collection ».
- source consultée 14 novembre 2026 (document indexé environ 3 semaines auparavant).

La page officielle `https://cultural.jp/en/policy` énonce que le service agrège et republie des métadonnées et images en utilisant IIIF, RDF et API, **et renvoie systématiquement aux conditions des bases contributrices** pour la réutilisation. Elle avertit que des URLs et contenus peuvent changer, sans indiquer un plafond en requêtes/minute.

La description technique émanant du créateur `https://tech.ldas.jp/en/projects/cultural-japan/` confirme une plateforme agrégeant des métadonnées de musées/bibliothèques japonaises et internationales, mises en RDF et accessibles via un **endpoint SPARQL** et une **API développeur**, avec moteur de recherche Elasticsearch. C'est une **description opérateur/développeur**, non un test de disponibilité des endpoints. Les trois familles doivent être distinguées : **IIIF Collection, API de recherche, triplestore SPARQL**.

**Conclusion documentée :** `app.cultural.jp/iiif-collection/collection.json` **est bien une URL référencée officiellement par le producteur** ; le JSON n'a pas été lu (outil de lecture 400 lors du passage par le lien externe et refus du domaine direct antérieur), le schéma de Collection et les droits effectifs des contenus doivent encore être contrôlés. **Aucune valeur de quota n'est démontrée.**

Sources :
- https://cultural.jp/en
- https://cultural.jp/en/policy
- https://api.cultural.jp/spec
- https://tech.ldas.jp/en/projects/cultural-japan/

### National Palace Museum, Taiwan (GLAM-080) : droits et granularité de téléchargement

La page **officielle d'une notice de collection** `https://digitalarchive.npm.gov.tw/Collection/Detail/25449?dep=U` est lisible. Elle affiche :
- **boutons « Copier le lien IIIF » et « Ouvrir IIIF »**, confirmant un lien IIIF au niveau des objets sans obliger à reconstituer un ARK/identifiant ;
- images **1 mégapixel sous CC0** (réutilisation sans attribution) ;
- images **6 mégapixels sous CC BY 4.0** (attribution requise), et consultation IIIF annoncée pour les 6 MP ;
- la déclaration du portail indique environ **410 000 images** offertes sous les deux catégories de résolution (nombre global du portail, pas volume de l'objet).

Ces droits/résolutions ne sont **ni un seuil de débit IIIF, ni une preuve de la capacité du serveur d'images à satisfaire des URLs arbitraires**. En particulier le `info.json` `https://iiifod.npm.gov.tw/iiif/2/K1F%2FK1F000001N000000000PAA/info.json` du dossier reste non validé en direct.

Le lien « Qu'est-ce que IIIF ? » depuis cette même notice mène au **PDF officiel** `https://digitalarchive.npm.gov.tw/Json/NPMIIIF.pdf` qui a encore dépassé le délai de lecture. Son contenu n'a **pas** été inspecté ni résumé. L'ancien chemin `/opendata/Json/NPMIIIF.pdf` reste également non lu.

La racine `https://iiifod.npm.gov.tw/iiif/2` a parfois été indexée avec le message générique du serveur Cantaloupe et la mention Image API 2.x ; dans cette reprise le lecteur direct retourne **403**, ce qui interdit de conclure que le service est aujourd'hui accessible au client.

Source primaire :
- https://digitalarchive.npm.gov.tw/Collection/Detail/25449?dep=U
- https://digitalarchive.npm.gov.tw/Json/NPMIIIF.pdf (lien constaté, PDF non lu)

## À intégrer plus tard dans les fiches et le benchmark

- **Cultural Japan** : indiquer la preuve **forte de référencement institutionnel de l'URL de collection**. Maintenir `accès au JSON: non confirmé`, `quota IIIF: non documenté`, et séparer API Search, SPARQL et IIIF Collection.
- **Taiwan NPM** : ajouter les niveaux **1 MP CC0** et **6 MP CC BY 4.0** en rubrique « licences / tailles d'images » ; **ne pas** décrire ces tailles comme `RateLimit`.
- Les deux cas exigent encore une **validation technique du manifeste / info.json** depuis un environnement conforme aux règles d'accès. Aucun contournement ni test en rafale ici.
