# Rattrapage S — 20 URL manuelles : Yale, Folger, Princeton, NCSU et Huntington (14/11/2026)

Nouvelle lecture des **URL d'origine** `a_verifier_manuellement`, à travers un extracteur public. Conserver la date `acquired_at` dans le registre : texte indexé ≠ réponse live de la sonde. Ne pas convertir les permissions de réutilisation, règles robots ou capacités Image API en quotas.

| Institution | URL initiale | Contenu / erreur | Date copie |
|---|---|---|---|
| NC State | https://d.lib.ncsu.edu/collections/ | **Portail Rare and Unique Digital Collections récupéré**. | 2026-07-15 |
| NC State | https://d.lib.ncsu.edu/collections/catalog/mc00227-003-ff0073-000-001_0004 | **401**, notice non récupérée. | tentative 14/11 |
| NC State | https://d.lib.ncsu.edu/robots.txt | `fetch_error` avec code 200, **pas de texte robots**. | tentative |
| NC State | https://d.lib.ncsu.edu/collections/about | **Page de réutilisation récupérée**, rappel des droits de tiers et citation. | 2026-08-27 |
| Folger | https://digitalcollections.folger.edu/ | **Page « Verifying that you're human »**, pas collections. | 2026-11-12 |
| Folger | https://catalog.folger.edu/ | Seul « Go to main content », document **non effectivement lu**. | 2026-11-12 |
| Folger | https://findingaids.folger.edu/robots.txt | `fetch_error` HTTP 200 sans contenu : fichier non lu. | tentative |
| Folger (référence externe) | https://www.vam.ac.uk/blog/digital/iiif-wordpress-and-shakespeare-too | **Billet V&A complet**, projet commun V&A/Folger de modules IIIF WordPress et Universal Viewer, historique (2019), pas règle de débit. | 2026-04-26 |
| Stanford | https://library.stanford.edu/contact-us | **Page de contact récupérée**, pas plafond. | 2026-11-07 |
| Princeton Library | https://library.princeton.edu/about/collections-use | **Copyright and Permissions Policy récupérée**, non un quota IIIF. | 2026-11-02 |
| Princeton Library | https://library.princeton.edu/about/policies/special-collections-copyright-credit-and-citation-guidelines | **Texte des règles Special Collections récupéré**, publication sans redevance d'usage par la bibliothèque, sous réserve des droits applicables. | 2026-10-19 |
| Princeton Library | https://artmuseum.princeton.edu/ | **Page d'accueil du musée récupérée**, qui contient des URL Image API v3 du sous-domaine media, mais ne documente pas ses quotas. | 2026-11-13 |
| Huntington | https://www.huntington.org/robots.txt | **robots.txt réellement extrait**, `User-Agent: *` Allow /, exclusions de /collections/search, /search, /calendar ; pas de débit. | 2026-11-14 |
| Huntington | https://www.huntington.org/digital-library | `fetch_error` HTTP 200 sans contenu, non lu. | tentative |
| Huntington | https://huntington.emuseum.com/ | **Page d'accueil collections art récupérée**, catalogue emuseum, pas documentation IIIF. | 2026-10-29 |
| Yale Art Gallery | https://artgallery.yale.edu/using-collection | **Page Using the Collection récupérée**, politiques de prêt, recherche et téléchargement d'images ouvertes. | 2026-11-09 |
| Yale LUX | https://lux.collections.yale.edu/ | **Texte d'accueil LUX récupéré** : IIIF pour images et Linked Art pour données, pas limite d'accès chiffrée. | 2026-09-13 |
| Yale Library | https://collections.library.yale.edu/catalog/16945082 | **Notice d'estampe de Hogarth récupérée**. | 2026-03-08 |
| Yale Library | https://collections.library.yale.edu/catalog/oai?verb=Identify | **Réponse OAI-PMH Identify réellement extraite**, endpoint `/catalog/oai`, protocole version 2.0. | 2026-11-14 |
| Yale Library | https://collections.library.yale.edu/iiif/2/32352934/info.json | **JSON Image API 2 réellement extrait**, dimensions **5 095 × 6 784**, tuiles de **512**, facteurs 1–64, profil `level2`. | 2026-11-14 |

### Conséquences du lot

- **Yale Digital Collections :** les URL exactes issues de la file manuelle produisent à présent une réponse OAI `Identify` exploitable et un vrai document `info.json` Image API 2 ; cela **lève une lacune documentaire**, pas une mesure de performance ni de quotas.
- **Folger :** aucun contenu de ses collections n'est extrait de l'écran de vérification ; le billet V&A prouve un historique de coopération IIIF, pas l'accès actuel au serveur Folger.
- **Huntington et Princeton :** droits de réutilisation, `robots.txt` et endpoint d'images doivent rester distincts. Un `Allow` dans robots ne signifie jamais « aucun plafond HTTP ».
- **NCSU :** refus 401 d'une notice ciblée et absence de corps `robots.txt` ne doivent pas être effacés par la lecture du portail principal.

Un test HTTP d'en-têtes, des demandes d'autorisation et une régénération complète du benchmark restent des étapes séparées. Aucun contournement ni test de charge dans ce lot.
