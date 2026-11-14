# Rattrapage P : lecture des URL originales signalées manuelles (14 novembre 2026)

**Objectif :** non pas relire les rapports A–O, mais extraire le **contenu des URL d'origine**, et noter séparément l'accessibilité HTTP depuis les autres lecteurs. Aucune mesure de taux, aucun test de saturation, aucune session authentifiée ni contournement d'anti-bot. La source ci-dessous est l'extracteur public de pages, avec sa date `acquired_at` ; cette date peut être celle d'un cache et **ne vaut pas réponse HTTP live**. Contrôle complémentaire par un second lecteur web sur cinq URL critiques : 404 sur l'ancien *Simple IIIF Discovery*, 503 sur la notice Waseda, et erreurs de lecture sur les URL robots Leyde, info.json Michigan et manifeste NDL.

## Résultats : GLAM-009 à GLAM-032 (19 URL du champ `a_verifier_manuellement`)

| Institution | URL d'origine | Contenu réellement récupéré | Date d'acquisition | Limite et suite |
|---|---|---|---|---|
| National Gallery London | https://research.ng-london.org.uk/ss-iiif/end-points | **Intégralité du document**, 12 530 caractères : *Simple IIIF Discovery*, format `?search=&limit=&from=`, script PHP de référence. `limit` plafonné à **100 résultats**, défaut **25** : **pas un quota de requêtes/minute**. | 2026-02-03 | L'autre lecteur confirme **404** sur l'URL actuelle ; copie historique documentée, service actuel non validé |
| National Library of Norway | https://www.nb.no/services/search/v2/ | Seulement page **301 Moved Permanently**, sans cible de redirection dans le contenu extrait. | 2026-11-04 | **Documentation non lue**, chercher cible actuelle et doc `api.nb.no` |
| Leiden | https://www.library.universiteitleiden.nl/robots.txt | **Fichier texte complet (2 811 caractères)** ; `User-agent: *`, nombreux `Disallow` de pages de recherche et d'index, pas de `Crawl-delay` dans le texte examiné. | 2026-11-14 | Ce site principal n'est **pas** `iiif.universiteitleiden.nl` ; le second lecteur échoue à récupérer les règles de ce dernier |
| Leiden | https://iiif.universiteitleiden.nl/robots.txt | Aucun contenu ; erreur de lecture **404** dans l'extracteur. | 2026-11-14 | Contrôle du fichier robots **toujours ouvert**, ne pas inférer absence de règles ou de quota |
| Biblissima | https://query.biblissima.fr/ | **Interface QLever SPARQL** récupérée (1 676 caractères), édition de requêtes et téléchargement CSV/TSV ; pas de résultats d'exécution SPARQL. | 2026-09-14 | L'ancienne sonde signalait 401 ; **cette copie ne prouve pas l'accès actuel au backend** |
| e-codices | https://www.e-codices.unifr.ch/en/about/contact | **Contenu de la page de contact** retrouvé ; pour les droits d'images, renvoi à chaque institution détentrice. | 2026-11-07 | **Ce n'est pas une page illisible** ; les limites non publiées sont une **question institutionnelle** |
| MDZ | https://www.digitale-sammlungen.de/en/contact | Contenu de la page de contact disponible, renvoi au service de reproduction. | 2026-11-07 | Classer contact/demande humaine, pas blocage documentaire |
| Göttingen | https://www.sub.uni-goettingen.de/digitale-bibliothek/digitale-werkzeuge/iiif-bei-der-sub-goettingen/ | Seulement page générale « Digital Humanities » suite à restructuration. | 2026-10-29 | **Pas la documentation IIIF d'origine** ; source thématique alternative à distinguer |
| Göttingen | https://www.sub.uni-goettingen.de/wir-ueber-uns/portrait/digital-policies-grundsaetze-fuer-die-digitalen-angebote-der-sub-goettingen/digitaler-zugang/ | Page d'accueil de SUB, pas l'ancien texte de Digitaler Zugang. | 2026-11-14 | Politique actuelle de substitution déjà identifiée au rapport E |
| Heidelberg | https://digi.ub.uni-heidelberg.de/diglit/Cimelia1975 | **Notice d'ouvrage récupérée**, avec liens explicites vers METS et manifestes **IIIF 2.1 et 3.0** (`/diglit/iiif/Cimelia1975/manifest` et `/diglit/iiif3/Cimelia1975/manifest`). | 2026-07-18 | Deux URL de manifestes légitimes, mais serveur sous défi Anubis au premier lecteur |
| Heidelberg | https://digi.ub.uni-heidelberg.de/diglit/rss?set=handschriften | **Texte des entrées RSS réellement extrait** (métadonnées d'octobre 2026). | 2026-11-14 | Le flux est lisible via l'extracteur, sans preuve d'en-têtes HTTP depuis la sonde |
| Heidelberg | https://pro.europeana.eu/page/the-universitaetsbibliothek-heidelberg-case-study | Page de l'étude de cas `Designing extensive EDM records` récupérée, intégration de IIIF et amélioration de métadonnées EDM. | 2026-08-13 | Aucun rate limit établi |
| Heidelberg | https://digi.ub.uni-heidelberg.de/en/bpd/projekt/nutzungsbedingungen.html | Conditions d'images Bibliotheca Palatina récupérées, dont la mention Public Domain Mark. | 2026-10-07 | Droit de réutilisation ≠ plafond de débit |
| ÖNB | https://labs.onb.ac.at/gitlab/labs-team/how-to-oenb-api | **Page de projet GitLab récupérée**, titre, dépôt, date de création du 19 octobre 2026, lien `/-/blob/main/README.md` ; **README lui-même pas lu**. | 2026-10-27 | Récupérer README brut ou archive via GitLab |
| ÖNB | https://labs.onb.ac.at/en/datasets/ | **Contenu intégral du catalogue de datasets** (~5 246 caractères). Exemples : **18 569 manifestes IIIF** Pamphlets, **4 782** Austria In Aerial Views, **21 903** Lavater. | 2026-11-03 | Tailles de collections ≠ quotas de débit ; exemples utiles pour établir accès par jeux de données |
| ÖNB | https://api.onb.ac.at/ | **Documentation API complète récupérée** : Presentation v3, Image v3, Search v2 (v1 dépréciée), endpoints REST v1 ALTO/TXT/preview/thumbnail. Contact `api@onb.ac.at`. | 2026-11-01 | Ne prouve pas les réponses HTTP des manifestes ; aucun plafond chiffré dans cette documentation |
| Smithsonian | https://www.si.edu/openaccess/devtools | **Contenu technique récupéré**, Open Access via api.data.gov, nécessité d'obtenir une clé et références EDAN. | 2026-11-13 | Les limites générales api.data.gov sont **distinctes** de quotas Smithsonian par endpoint |
| Smithsonian | https://www.si.edu/openaccess | **Page générale Open Access récupérée**, collections et outils développeurs. | 2026-11-11 | Page informative, pas contrat de quota |
| Smithsonian | https://api.data.gov/signup/ | **Formulaire d'inscription accessible en lecture**, mais aucune inscription effectuée. | 2026-11-11 | Classer `INTERVENTION_REQUISE` pour clé, pas page inaccessible |

## Résultats : GLAM-040 à GLAM-084 (20 URL du champ initial)

| Institution | URL originale | Contenu obtenu et interprétation | Date acquise |
|---|---|---|---|
| Michigan | https://quod.lib.umich.edu/ | **Contenu du répertoire Digital Collections**. L'ancien blocage 403 de la sonde ne prouve pas une suppression du site. | 2026-10-06 |
| Michigan | https://quod.lib.umich.edu/b/bhl/x-bl004079/bl004079 | **Notice complète récupérée** de « UM Carillon. Adding new bells / BL004079 », avec lien IIIF manifest **`https://quod.lib.umich.edu/cgi/i/image/api/manifest/bhl:BL004079`**. | 2026-11-14 |
| Michigan | https://quod.lib.umich.edu/cgi/i/image/api/image/bhl:BL004079:BL004079/info.json | **JSON d'Image API 2 réellement extrait** : `@context` Image 2, image **7092 × 4800**, tuiles **256**, facteurs **1,2,4,8,16,32**, profil `level2.json`. | 2026-11-14 |
| Duke | https://repository.duke.edu/dc | Page Duke Digital Collections récupérée. | 2026-09-25 |
| UCLA | https://www.library.ucla.edu/about/policies/ucla-library-copyright-policies/ | Politique de copyright lue, mais ne documente pas un quota IIIF. | 2026-09-13 |
| UCLA | https://digital.library.ucla.edu/catalog | Contenu du catalogue récupéré. | 2026-10-27 |
| Northwestern | https://dc.library.northwestern.edu/ | Site des collections récupéré, mais le texte inclut la fenêtre de cookies ; il ne démontre **pas** que les API spécifiques sont accessibles. | 2026-11-05 |
| Northwestern | https://iiif.dc.library.northwestern.edu/iiif/3/e814609e-ddfd-4427-b4cf-1a70d6e49129/info.json | **Erreur d'extraction sans contenu**, signal HTTP 200 isolé : **ne pas qualifier JSON lu**. | 2026-11-14 |
| Northwestern | https://www.library.northwestern.edu/libraries-collections/digital-collections/index.html | **Ancienne route 301**, lien vers `/libraries-collections/digital-collections/`, dont la version actuelle reste à vérifier. | 2025-10-24 |
| Leeds | https://explore.library.leeds.ac.uk/special-collections-explore/372687 | Contenu partiel de la notice, lien de manifeste officiel déjà extrait dans le rapport J ; la présente extraction ne le restitue pas. | 2026-11-01 |
| Leicester | https://le.ac.uk/robots.txt | **Fichier robots.txt complet**, `User-agent: *` avec exclusions de recherche ; règles dédiées OAI-AdsBot/OAI-SearchBot, sans `Crawl-delay` dans la version lue. | 2026-11-14 |
| National Diet Library | https://dl.ndl.go.jp/ja/terms | **Page correspondant désormais à un bandeau de cookies et à un lien `/sitepolicy`**, pas les conditions recherchées. | 2026-11-14 |
| National Diet Library | https://www.dl.ndl.go.jp/api/iiif/2542679/manifest.json | **JSON IIIF Presentation 2 complet** (35 568 caractères), objet `承安五節繪`, source PDM, `sc:Canvas`, services Image 2 de profil level 1. | 2026-11-14 |
| National Diet Library | https://ndlsearch.ndl.go.jp/api/oaipmh?verb=Identify | **Réponse OAI Identify extraite**, base `https://ndlsearch.ndl.go.jp/api/oaipmh`, protocole 2.0, dates et granularité. | 2026-11-14 |
| Waseda | https://www.wul.waseda.ac.jp/kotenseki/html/ho04/ho04_02555/index.html | **Notice complète récupérée**, manuscrit `玉篇` (Gyokuhen), lien exact `https://iiif.archive.waseda.jp/iiif/manifest/ktnsk/ho04_02555/manifest.json`. **Un autre lecteur obtient encore 503** sur cette notice. | 2026-07-18 |
| Waseda | https://www.waseda.jp/robots.txt | 403 chez l'extracteur, **non lu**. | 2026-11-14 |
| Digital Commonwealth / BPL | https://www.bpl.org/digitization/faq/ | **FAQ complète récupérée**, questions de participation, numérisation et contributions ; pas un document de quotas IIIF. | 2026-10-30 |
| Digital Commonwealth | https://www.digitalcommonwealth.org/search/opensearch.xml | **Page de défi Anubis récupérée**, **pas de XML OpenSearch**. | 2026-11-14 |
| Qatar Digital Library | https://iiif.qdl.qa/robots.txt | **403 sans contenu**, règles robots non lues. | 2026-11-14 |
| Qatar Digital Library | https://www.qdl.qa/en/copyright-and-ethical-terms-reuse | **Erreur 520**, conditions non lues. | 2026-11-14 |

## Conclusions opérationnelles

1. Les textes originaux du **PPOC**, de **Simple IIIF Discovery**, de **Leyde robots**, de **Michigan IIIF Image 2**, des **manifestes NDL** et de la **notice Waseda** permettent de **réduire les lectures manuelles** sans prétendre à une validation HTTP depuis la sonde.
2. Les **limites de résultats** `limit=100` du script NG, les tailles d'images, les droits PDM, le nombre de manifestes d'un dataset et les plafonds de service d'api.data.gov ne sont **jamais** des plafonds IIIF automatiquement transférables.
3. Les URLs refusées (Northwestern JSON non extrait, Anubis Digital Commonwealth, Qatar 403/520, Waseda robots) restent dans le registre avec motif exact.
4. Les trois manifestes documentés par les notices **Michigan**, **Waseda** et **Heidelberg** sont des URLs **légitimes**, mais leur accessibilité HTTP live et les en-têtes de débit restent à examiner par un client autorisé. La page QLever Biblissima récupérée est une **interface datée**, pas une session prouvée auprès du backend.
5. **Différencier** `lecture_documentaire` (copie indexée, potentiellement ancienne) de `verification_http` (sonde), et conserver les URL de redirection / substitution comme des résultats distincts.

Cette reprise est une passe documentaire ciblée, pas un test des étapes a–g. Aucun blocage n'a été contourné.

## Complément : vérification des URL de manifestes *découvertes dans les notices*

Les trois URL ci-dessous sont **des liens documentés dans les notices originales**; elles n'ont pas été inventées par construction d'identifiants. Les extraits ont été récupérés par l'extracteur public; leurs dates d'acquisition ne garantissent pas la réponse de la sonde depuis une autre IP.

- **Michigan** : `https://quod.lib.umich.edu/cgi/i/image/api/manifest/bhl:BL004079` : **contenu JSON IIIF Presentation extrait**, avec annotation d'image, service Image 2 et toile 7 092 × 4 800. Acquis le **2026-11-14**. L'extracteur peut présenter des fragments et non l'intégralité du JSON; **ne pas qualifier de récupération intégrale** sans téléchargement intégral.
- **Heidelberg v2** : `https://digi.ub.uni-heidelberg.de/diglit/iiif/Cimelia1975/manifest` : extrait du JSON IIIF Presentation **v2**, `sc:Manifest`, lien aux pages de l'ouvrage ; acquis le **2026-11-14**.
- **Heidelberg v3** : `https://digi.ub.uni-heidelberg.de/diglit/iiif3/Cimelia1975/manifest` : extrait du JSON IIIF Presentation **v3**, `ImageService3` et `items` ; acquis le **2026-07-17**.
- **Waseda** : `https://iiif.archive.waseda.jp/iiif/manifest/ktnsk/ho04_02555/manifest.json` : **connexion échouée**, même si le lien exact est retrouvé dans la notice originale datée du 18 juillet.
- **Norvège** : le service officiel remplaçant la documentation précédente est documenté dans l'OpenAPI `https://api.nb.no/catalog/v1/items/api-docs` (OAS 3.1, JSON récupéré du 04/11) ; ce service **Catalog Search API** n'établit pas que l'ancien `/services/search/v2/` a migré à l'identique, ni que les conditions IIIF sont identiques.
- **Göttingen** : la nouvelle page `https://www.sub.uni-goettingen.de/ueber-uns/ordnungen-und-leitlinien/digital-policies` est identifiée, mais l'extraction texte reste incomplète ; **ne pas annoncer la politique intégralement lue**.
- **NDL Japon** : la nouvelle page de conditions `https://dl.ndl.go.jp/sitepolicy` fournit réellement une politique d'usage du site. Une traduction complète et les exceptions propres à IIIF demandent une vérification distincte; la page `/ja/terms` n'est plus la source correcte.

**Distinction décisive :** l'extraction de JSON / mise en évidence des champs prouve un document lisible par un outil; elle ne prouve ni l'absence de WAF sur l'IP de la sonde, ni les en-têtes `RateLimit`, ni une capacité de moissonnage.
