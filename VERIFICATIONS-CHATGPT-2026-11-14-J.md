# Rattrapage documentaire J — 14 novembre 2026

## Périmètre
Reprise des dossiers **GLAM-058 à GLAM-069** (Huntington, Digital Commonwealth, David Rumsey, Blavatnik, Leventhal, Durham, Cardiff, Lancaster, Leeds, Leicester, St Andrews, Parliamentary Archives). L'état de départ est `institutions/*/data.json` dans la branche `claude/veille-iiif-quotas`. Les rapports B et I traitaient déjà une partie des institutions ; ce document ajoute **les observations effectivement nouvelles**. Consultation via moteur/lecteur web, **pas une requête HTTP de la sonde Python**, sans contournement des défis.

| Institution / URL à vérifier | Observation | Statut |
|---|---|---|
| **GLAM-059 Digital Commonwealth**, https://www.digitalcommonwealth.org/for_institutions | Retour **404** par le lecteur web (ancienne page introuvable). La page officielle actuelle https://www.digitalcommonwealth.org/institutions présente la liste des contributeurs mais **pas** les procédures techniques d'inscription. La page https://www.digitalcommonwealth.org/api est lisible et documente OAI-PMH, JSON, IIIF Image **2.0**, Presentation **2.0**. | **SOURCE ALTERNATIVE TROUVÉE** pour les API ; ancienne page `for_institutions` déplacée ou retirée, ne pas l'inférer comme alias HTTP. |
| Digital Commonwealth, https://www.digitalcommonwealth.org/privacy | **Page originale lue**, explique cookies, données de navigation et statistiques agrégées ; aucune condition d'extraction automatisée ou quota API dans ce document. | **LECTURE DOCUMENTAIRE CLOSE**, sans conclure « aucune limite ». |
| Digital Commonwealth, https://www.digitalcommonwealth.org/search/opensearch.xml | Renvoie **page Anubis “Sorry, we can't verify your browser!”** dans l'outil web, pas un XML OpenSearch. | **BLOCAGE TECHNIQUE OUVERT** ; ne pas confondre réponse HTML de défi et descripteur API valide. |
| Digital Commonwealth / BPL, https://www.bpl.org/digitization/faq/ | Renvoie **vérification de navigateur avec JavaScript**, pas la FAQ. | **BLOCAGE DOCUMENTAIRE OUVERT**. |
| **GLAM-066 Leeds**, https://explore.library.leeds.ac.uk/special-collections-explore/372687 | **Notice complète récupérée** dans l'outil web (titre : *[Horae Beatae Mariae Virginis]*, cote **BC MS 5**, 1440–1460) ; **lien de manifeste exact fourni dans le HTML** : `https://iiif.library.leeds.ac.uk/presentation/cc/q8qkdfmm`. Cette URL est donnée par la bibliothèque, **non devinée**. La notice indique un régime de droits particuliers (œuvre orpheline selon la bibliothèque) ; ne pas déduire « libre de tout droit » du seul âge du manuscrit. | **LACUNE DOCUMENTAIRE DE L'URL IIIF RÉSOLUE** ; manifeste/en-têtes **non testés**. |
| **GLAM-067 Leicester**, https://le.ac.uk/library/about/policies | **Page de politiques officielle lue**. Le lien mène à https://le.ac.uk/library/about/policies/special-collections-online-takedown-policy (texte intégral de la politique de retrait lu) et à https://le.ac.uk/library/about/policies/archives-access (politique d'accès aux Archives and Special Collections, approuvée **19 juin 2024**). | **LACUNE DOCUMENTAIRE RÉSOLUE**, aucune limite IIIF chiffrée dans ces documents. |
| Leicester, https://le.ac.uk/robots.txt | **Fichier texte lu** dans le lecteur web, indexation récente (~2 semaines). `User-agent: *` exclut certaines routes de recherche du **site principal** ; ne mentionne ni `Crawl-delay` ni `Disallow: /iiif` dans les 25 lignes de la version récupérée. `OAI-AdsBot` et `OAI-SearchBot` ont `Allow: /` spécifique. | **LECTURE DU ROBOTS.TXT DOCUMENTÉE**, mais les règles de **`leicester.contentdm.oclc.org`** et des autres hôtes demeurent **indépendantes**. Ne pas en déduire un quota illimité. |
| **GLAM-068 St Andrews**, https://www.st-andrews.ac.uk/terms/ | **Page actuelle lue dans son intégralité** (210 lignes). Elle encadre l'accès, le copyright, l'accès aux services, les RSS ; **aucun chiffre de débit IIIF publié** dans ce texte. | **LACUNE “suite de la page non lue” RÉSOLUE** ; pas de preuve sur les conditions spécifiques à l'hôte `collections.st-andrews.ac.uk`. |
| St Andrews, documentation complémentaire | https://www.st-andrews.ac.uk/library/about/librariesandmuseums/servicedefinitions/digital-reproductions/ et https://www.st-andrews.ac.uk/library/about/librariesandmuseums/servicedefinitions/research-with-unicolls/ décrivent le traitement institutionnel des **demandes de reproduction et de recherche à grande échelle**, avec convention/protocole selon la demande. La section `5.7.1` du règlement universitaire https://www.st-andrews.ac.uk/policy/libraries-and-museums/library-regulations-policy.pdf proscrit le téléchargement systématique des **e-resources sous licence** : ne pas l'appliquer indistinctement aux collections libres de droits hébergées sous IIIF. | **CADRE D'ACCÈS COMPLÉTÉ**, le PDF `eprints.../IIF resources.pdf` reste non vérifié, et les deux anciennes URL de catalogue redirigées ne sont pas une documentation IIIF retrouvée. |
| **GLAM-063 Durham** | https://www.durham.ac.uk/departments/library/about-us/policies/ toujours en 403 dans l'outil web ; robots actuel non lu ; `iiif.durham.ac.uk/robots.txt` du dépôt interdit `/`. | **OUVERT**, pas de contournement. |
| **GLAM-064 Cardiff** | Déjà traité dans rapport A. Aucune donnée supplémentaire sur `robots.txt` actuelle ni sur les limites IIIF distinctes d'Alma. | **RESTE TECHNIQUE**. |
| **GLAM-065 Lancaster** | L'item manuel porte sur le `robots.txt` de **Cambridge CUDL**, donc d'un **autre établissement**. Il faut éviter de compter ce blocage tiers comme une lacune propre à la plateforme Lancaster. | **RECLASSER CROSS-REFERENCE**, sans effacer l'historique. |
| **GLAM-058 Huntington** | L'ancienne page `/terms-and-conditions-use-photographs` et `researchguides/.../imagingservices` ont été traitées dans le rapport B ; cette passe n'apporte pas de mesure d'API. | **TECHNIQUE RESTE OUVERT**. |
| **GLAM-060 David Rumsey** et **GLAM-061 Blavatnik** | Aucun item `a_verifier_manuellement` dans le dossier de départ. Le `Crawl-Delay: 500` de Rumsey est une **règle robots par hôte**, pas un débit HTTP mesuré. | **PAS DE MANUEL À CLOTURER** ; audit g encore à faire. |
| **GLAM-062 Leventhal** | `www.digitalcommonwealth.org/copyright` était déjà lue ; l'absence de politique chiffrée dans cette page est une **question à l'institution**, pas une page illisible. `www.leventhalmap.org/robots.txt` renvoie 404 d'après dossier, un autre hôte `collections.leventhalmap.org` impose 15 s. | **RECLASSER : contact / robots hôte distinct**. |
| **GLAM-069 Parliamentary Archives** | Pas de preuve récente pour les hôtes Cloudflare. Les éventuels quotas des API parlementaires de `developer.parliament.uk` ne doivent pas être extrapolés aux archives CALM. | **OUVERT**. |

### Liens de preuve
- https://www.digitalcommonwealth.org/api
- https://www.digitalcommonwealth.org/institutions
- https://www.digitalcommonwealth.org/privacy
- https://www.digitalcommonwealth.org/search/opensearch.xml
- https://explore.library.leeds.ac.uk/special-collections-explore/372687
- https://le.ac.uk/library/about/policies
- https://le.ac.uk/library/about/policies/special-collections-online-takedown-policy
- https://le.ac.uk/library/about/policies/archives-access
- https://le.ac.uk/robots.txt
- https://www.st-andrews.ac.uk/terms/
- https://www.st-andrews.ac.uk/library/about/librariesandmuseums/servicedefinitions/digital-reproductions/
- https://www.st-andrews.ac.uk/library/about/librariesandmuseums/servicedefinitions/research-with-unicolls/

**Critère de clôture :** seule la lecture documentaire des lignes explicitement marquées est clôturée. Les quotas non chiffrés et les tests g, les versions actuelles de robots.txt sur hôtes protégés et les endpoints non visités ne le sont pas.
