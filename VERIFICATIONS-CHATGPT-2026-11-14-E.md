# Rattrapage documentaire E — 14 novembre 2026

Priorité : **GLAM-024 à GLAM-031** (MDZ, Göttingen, Heidelberg, ÖNB, Vatican, Portugal, Bologna, LoC). Cette note conserve les blocages techniques et distingue le champ de la source. Les URL ont été reprises dans les `data.json` du dépôt au commit `c6bc71173f861502bd96d438f4489328ccf81b9e`.

## GLAM-024 : Bayerische Staatsbibliothek / MDZ
La documentation courante `https://www.digitale-sammlungen.de/en/interfaces` a été **lue intégralement** malgré un avertissement d'application JavaScript au début du HTML. Elle affirme distinctement :
- **Presentation API IIIF v2 : accès annoncé sans limite** ;
- **Image API v2 : nombre de requêtes limité par 24 heures, valeur non publiée** ;
- **OCR : nombre de téléchargements limité par 24 heures, valeur non publiée** ;
- exemple manifest `https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00012345/manifest` et info.json `https://api.digitale-sammlungen.de/iiif/image/v2/bsb00103155_00013/info.json`.
Ces éléments **figurent déjà** dans `data.json` : ne pas les dupliquer. La page `https://www.digitale-sammlungen.de/en/download-options` expose le service DaFo, qui exige une demande avec email/CAPTCHA pour des images haute définition et un plafond de commande par jour, **différent** du plafond de l'Image API. Le recours à `mailto:mdz@bsb-muenchen.de` relève de la **demande institutionnelle**, pas d'une page « illisible ». Le point d'accès OAI BDR en 403 reste sans nouvel essai valide.

## GLAM-025 : Göttingen State and University Library
Deux anciennes URL renvoyant vers l'accueil dans le dépôt ont de **véritables équivalents dans le nouveau site** :
1. `https://www.sub.uni-goettingen.de/digitale-bibliothek/digitale-werkzeuge/iiif-bei-der-sub-goettingen/` (ancienne) → **nouveau contenu connexe** `https://www.sub.uni-goettingen.de/forschung/forschungswerkzeuge` : sous-section `Dokumentbetrachter TIFY (IIIF)` et renvois aux dépôts compatibles IIIF. Il s'agit d'un équivalent thématique, **pas d'une redirection vérifiée**.
2. `https://www.sub.uni-goettingen.de/wir-ueber-uns/portrait/digital-policies-grundsaetze-fuer-die-digitalen-angebote-der-sub-goettingen/digitaler-zugang/` (ancienne) → **nouvelle page officielle globale** `https://www.sub.uni-goettingen.de/ueber-uns/ordnungen-und-leitlinien/digital-policies`, contenant la section `Digitaler Zugang` et `Digitale Produktion`.
La politique indique une ouverture des interfaces et la réutilisation avec aussi peu de restrictions que possible ; **elle ne documente pas de requêtes/minute**. À réconcilier avec les extraits Wayback dans le dossier et conserver les deux anciens permaliens comme historique.

## GLAM-026 : Universitätsbibliothek Heidelberg
- `https://digi.ub.uni-heidelberg.de/en/bpd/projekt/nutzungsbedingungen.html` est **maintenant lisible depuis l'outil web**. Il s'agit des **droits d'usage des images numériques de Bibliotheca Palatina** (Public Domain Mark, crédit des reproductions), **pas d'un document de rate limits**.
- `https://www.ub.uni-heidelberg.de/helios/digi/nutzung/Welcome.html` redirige à présent vers `https://www.ub.uni-heidelberg.de/helios/digi/nutzung/` ; page officielle lue, MAJ affichée au 22 juillet 2025. Elle précise la **gratuité de l'usage des numérisations** sous différents régimes de droits (PDM, CC BY-SA, InC, œuvres indisponibles).
- **Correction P0** : dans `institutions/universitatsbibliothek-heidelberg/data.json`, `limites_documentees` comporte une ligne `nature="Aucune limite de débit documentée"` dont la preuve est cette phrase sur l'absence de frais. **La source ne permet pas cette déduction**. Retirer cette preuve de la catégorie `limites_documentees` de débit, et la ranger en droits/conditions de réutilisation ; indiquer `quota de débit non établi` faute de source dédiée. L'absence de droits à payer n'est ni une absence de quota ni une absence de filtres anti-robots.
- Les pages Anubis et le flux RSS restent à vérifier techniquement ; aucun contournement.

## GLAM-027 : Österreichische Nationalbibliothek — avancée documentaire substantielle
- Le portail officiel courant `https://api.onb.ac.at/` documente **IIIF Presentation 3, Image 3, Content Search 2, Search 1 dépréciée**, ainsi que `/rest/v1/ie/{ieId}/alto/{pageNumber}`, `/txt/`, `/preview`, `/thumbnail`.
- **Désormais, un identifiant *officiel* a été retrouvé** dans les diapositives de l'ÖNB au workshop « The IIIF Services of the Austrian National Library », **7 mai 2025** (Johannes Knüchel, Christoph Steindl), https://zenodo.org/records/15369312/files/The%20IIIF%20Services%20of%20the%20Austrian%20National%20Library.pdf?download=1 :
  - **Ancien** `https://iiif.onb.ac.at/presentation/AKON/AK076_113/manifest/`
  - **Nouveau** `https://api.onb.ac.at/iiif/presentation/v3/manifest/AKON_AK076_113`
  - **Identifiant de la même ressource** `https://api.onb.ac.at/iiif/presentation/v3/manifest/10168F8E`
- **ATTENTION** : le PDF est une **source de migration publiée en 2025**, non la preuve que l'endpoint répond aujourd'hui. L'outil web ne récupère pas les deux URLs de manifestes quand elles sont ouvertes directement (ne fournit pas de headers). Le PDF a été analysé textuellement ; la fonction de capture de page du PDF a échoué avec une erreur d'encodage. Le numéro **10168F8E** ne doit pas être présenté comme « deviné ».
- La documentation SACHA `https://iiif.onb.ac.at/api/` indique des protections contre le téléchargement massif, particulièrement pour les fonds ABO, sans seuil de requêtes chiffré. Ne pas extrapoler la politique d'ABO à toutes les collections et à la nouvelle infrastructure sans confirmation.
- **Action suivante** : remplacer « aucun ieId publié / impossible de tester » par « **ieId officiel trouvé, exécution HTTP encore non vérifiée** » ; préparer un test de manifeste unique selon la procédure locale du projet, sans surcharge.

## GLAM-028 : Vatican
Aucune nouvelle preuve sur `spotlight.vatlib.it` (erreur TLS), DigiVatLib ou Photographic Laboratory dans cette passe. Les interdictions de reproduction ne sont pas à confondre avec un débit technique.

## GLAM-029 : Biblioteca Nacional de Portugal
`mailto:bndigital@bnportugal.gov.pt` est une **action de contact**, pas une page web. La redirection `https://purl.pt/32689/1/` reste à qualifier au niveau navigateur/HTTP.

## GLAM-030 : Università di Bologna — AMS Historica
`https://historica.unibo.it/oai` et `https://historica.unibo.it/server/oai/request?verb=Identify` n'ont pas été récupérés par l'outil web : **aucune nouvelle preuve de fonctionnement**. Ne pas confondre l'en-tête `x-ratelimit-limit: 500` relevé historiquement sur le *sitemap index* du service DSpace avec une limite prouvée sur la famille OAI-PMH ou IIIF ; le **périmètre de l'en-tête doit être vérifié**.

## GLAM-031 : Library of Congress
Déjà traité dans le rapport B : plafonds chiffrés documentés par famille API, sans vérification du navigateur pour `www.loc.gov/pictures/api` et sans conclusion sur les en-têtes reçus par une sonde.

## Résultats nouveaux à intégrer
1. **Deux anciennes pages Göttingen retrouvent leur équivalent officiel actuel.**
2. **La page de conditions Heidelberg, auparavant non lue, est maintenant lisible.**
3. **La catégorie de rate limit Heidelberg doit être corrigée : sa source ne parle que de gratuité de réutilisation.**
4. **Une présentation officielle de l'ÖNB donne deux URLs de manifeste et un identifiant `ieId` exploitables**, mais pas de preuve HTTP live.
5. Les quotas Image/OCR MDZ demeurent **non chiffrés** tandis que Presentation est annoncé illimité : séparation de famille déjà correctement documentée.
