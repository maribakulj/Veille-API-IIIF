# Recontrôle ciblé des sources Wellcome, National Gallery, NLS et Édimbourg — 14/11/2026

Ce fichier **complète** `VERIFICATIONS-CHATGPT-2026-11-14-C.md` et `-D.md`. Les résultats ci-dessous sont des **lectures web sourcées** ; ils n'attestent ni les en-têtes de la sonde `scripts/probe.py`, ni une politique technique générale, ni des plafonds non écrits. Aucune requête de dépassement.

## Wellcome Collection (GLAM-008) : deux articles d'origine désormais lus

1. `https://stacks.wellcomecollection.org/crawlers-floods-and-fleets-a-year-of-keeping-our-digital-collections-open-10af777199c4`, Robert Kenny, **16 octobre 2026**, consulté en texte intégral dans l'outil web le 14/11/2026. La section « Bulk harvesters and the IIIF API » explique l'instauration de **budgets de requêtes par minute par moissonneur ou réseau**, sans seuil numérique publié, et d'une **limite distincte par adresse pour les images plein format**. L'objectif déclaré est de **garder l'API IIIF exploitable par des scripts**, sans défis JS qui casseraient les visualiseurs tiers. Le billet mentionne le passage de ~9 millions à 17–20 millions de requêtes IIIF quotidiennes au cours d'un épisode de trafic automatisé : **ces volumes de trafic NE SONT PAS les quotas autorisés**. Cela recoupe mais renforce la preuve Wayback dans le `data.json` original.
2. `https://stacks.wellcomecollection.org/ten-years-and-counting-wellcome-collection-and-iiif-9015cdcdefd8`, Jonathan Cates, **9 octobre 2026**, consulté en texte intégral. Confirme IIIF Presentation **v2 et v3**, et `iiif-builder`, ainsi que le recours à **IIIF Authorization 2.0** et à des manifestes exploitables par des visualiseurs tiers. Donne **361 783 manifestes** (volumétrie, pas quota). Aucune limite chiffrée de débit dans l'article.
3. `https://data.wellcomecollection.org/robots.txt` : **toujours non consultable** depuis l'outil web le 14/11. Conserver comme vérification technique séparée.

**Statut : les deux lignes Medium dans `a_verifier_manuellement` sont désormais `DOCUMENT LU DIRECTEMENT` ; le contrôle du robots.txt demeure `OUVERT`.** Ne pas effacer les anciens 403 du journal de la sonde.

## National Gallery London (GLAM-009) : manifeste IIIF 3 authentique identifié

- Ancienne documentation `https://research.ng-london.org.uk/ss-iiif/end-points` : **404 confirmé** par l'outil web.
- `https://research.ng-london.org.uk/iiif-projects/` : site officiel « IIIF Collection Explorer » du Scientific Department, consultable.
- **Nouvelle preuve forte** : `https://research.ng-london.org.uk/iiif-projects/json/building-the-picture.json` a été **lu comme JSON** : `@context = http://iiif.io/api/presentation/3/context.json`, `type=Manifest`, `label=Building the Picture: Architecture in Italian Renaissance Painting`, `provider=The National Gallery`. Les Canvas contiennent des services IIIF Image API v2 `https://research.ng-london.org.uk/iiif-int/pics/pyrByDate/.../N-1033-00-000125-PYR.tif`.
- L'API d'images **générale** annoncée est distincte : `https://www.nationalgallery.org.uk/documentation/ngacuk/collection-images` documente `https://data.ng.ac.uk/iiif/3/{image PID}/{region}/{size}/{rotation}/default.jpg` et précise que le **déploiement global Presentation est en cours**. La disponibilité d'un exemple Presentation v3 du projet scientifique n'implique pas que toutes les collections soient déjà migrées.
- Aucune limite chiffrée de **req/min** annoncée dans ces pages. L'ancien lien `ss-iiif/end-points` doit être classé `404 / documentation alternative identifiée` plutôt que `aucune source IIIF`, sans inventer un rate limit.

## National Library of Scotland (GLAM-006) : différence de millésime de la déclaration IA

- Source officielle `https://www.nls.uk/about-us/plans-and-policies/corporate-documents/` (page mise à jour **6 octobre 2026**) : contient le lien vers **AI Statement, août 2026, trois pages** : `https://www.nls.uk/media/np3pf2pv/national-library-of-scotland-ai-statement-august-2026.docx`.
- **Document août 2026 NON lu** : l'outil web refuse son format DOCX et le conteneur n'a pas pu résoudre le domaine pour le téléchargement. Ne pas prétendre avoir vérifié les clauses de la version 2026.
- `https://www.cenl.org/national-library-of-scotland-ai-statement/` reproduit le texte d'une **version de 2024**, révisée le 24 mai 2024. Elle indique le double objectif d'ouvrir les collections et de protéger certaines données sensibles contre l'accès automatisé. **Source pertinente de contexte, pas substitution probante au document 2026**.
- `https://maps.nls.uk/projects/api/` est inaccessible à l'outil web (robots) ; le fournisseur cartographique `https://docs.maptiler.com/guides/maps-apis/maps-platform/nls-historical-maps-api-historical-maps-of-great-britain-for-use-in-mashups/` explique un palier de **100 000 requêtes de tuiles mensuelles** pour certains utilisateurs non commerciaux ; cette valeur est **hors IIIF**.

## Edinburgh (GLAM-005) : éviter la généralisation des conditions de réutilisation

- Nouvelle source officielle lue : `https://library.ed.ac.uk/heritage-collections/using-the-collections/digitisation/image-licensing` (publiée le 21 août 2024 ; encore en ligne lors de cette vérification). La bibliothèque affirme une stratégie **Open by Default** pour ses images et un régime de réutilisation libre avec attribution pour les images sous **CC BY** ; les droits sur l'œuvre source et les règles pour certains contenus restent variables.
- **Conflit à qualifier** : le dossier source `institutions/edinburgh-art/data.json` qualifie la page `https://collections.ed.ac.uk/art/licensing` de « autorisation préalable pour toute utilisation des images ». Il faut distinguer **périmètre du portail Art** et **politique institutionnelle de licences**. Ne pas écraser la citation antérieure sans dater et résoudre les différences.
- **Incohérence de statut à vérifier** : `institutions/edinburgh-art/fiche.md` affirme g (crash test) déjà effectué le 14/11 ; `data.json.statut_audit` dit encore « g à faire ». Vérifier physiquement `tests/crash/edinburgh-art.log` et `CONSIGNE-ET-SUIVI.md` avant tout changement du suivi.

## Actions restant ouvertes

- **T1** : logs/robots/en-têtes HTTP exacts sur les hôtes Wellcome data, Gallery et Cambridge via une sonde non contournante (cette lecture web ne les fournit pas).
- **T2** : obtenir le texte **2026** de la déclaration IA NLS (pas la republication CENL 2024).
- **T3** : arbitrer le périmètre de licence d'Edinburgh et la cohérence de l'étape g.
- **T4** : intégrer ces distinctions dans `data.json` et le classeur **dans une passe locale validée**, sans réécrire silencieusement la source de vérité ni casser la régénération Excel.

## Contrôle du statut g d'Édimbourg : décalage **confirmé dans les fichiers**

Vérification du 14/11/2026 via le connecteur GitHub des **preuves originales** sur la branche source :

- `institutions/edinburgh-art/CONSIGNE-ET-SUIVI.md`, section `### g) Crash test progressif` : case `[x] Fait`, avec références aux deux fichiers de preuve.
- `institutions/edinburgh-art/tests/crash/edinburgh-art.log` : quatre paliers (6, 10, 50, 200 req/min), de 06:55:58 à 07:07:42 UTC ; à 200 req/min, **599 réponses HTTP 200 et une requête sans code** sur 600. Le libellé « aucun blocage » du journal doit rester une observation bornée à ces essais, **pas une affirmation d'absence de quota**.
- `institutions/edinburgh-art/tests/crash/edinburgh-art-manifeste-record-112492.json` : confirme les chiffres de la sonde, mais pas l'absence de protection au-delà du test.
- `institutions/edinburgh-art/data.json` : champ `statut_audit` encore « audit a–f complet ; g à faire » ; **statut en retard par rapport à la checklist et aux logs**.

**Décision d'intégration recommandée** : corriger le `statut_audit` sur la source canonique en citant ces preuves, puis régénérer le benchmark par le pipeline ; ne pas relancer le test g, qui risquerait d'ajouter du trafic sans information nouvelle.
