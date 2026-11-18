# Actions humaines prioritaires après vérification des URL IIIF

État le **15 novembre 2026**. Ce document **ne réclame pas de relire les 260 anciennes URL**. La source de vérité est la file produite en CI : `data/triage-interventions-humaines.csv` (artefact du workflow `rattrapage-inventaire-manuel`).

## Ce qu'exigerait explicitement une décision ou un compte

| Priorité | Service | Démarche, **non réalisée** | Nécessaire pour le benchmark IIIF ? |
|---|---|---|---|
| 1, si besoin de quota précis | Biblioteca Nacional de Portugal | Écrire à `bndigital@bnportugal.gov.pt`, demander conditions de scripts sur manifestes et `info.json`, limites publiques sans compte, modalités de demande d'un accès chercheur/institutionnel | **Éventuellement**, car la réponse n'est pas déductible de `robots.txt` |
| 2, si API Harvard nécessaire | Harvard Art Museums | Formulaire de clé API `https://docs.google.com/forms/d/1Fe1H4nOhFkrLpaeBpLAnSrIMYvcAxnYWm0IU9a6IkFA/viewform` ; **aucune clé demandée** | **Conditionnel**, ne prouve ni n'accorde les accès IIIF de Harvard Library |
| 2, si NPM Image API indispensable | National Palace Museum (Taïwan) | Formulaire institutionnel `https://contactus.npm.gov.tw/Web/case-apply.jsp?l=1&TArea=1`, identité + captcha, demande de règles IIIF et d'accès non commercial institutionnel | **Conditionnel**, guide PDF IIIF déjà lu et UID de manifestes déjà retrouvés |
| Hors IIIF | Internet Archive Tasks API | Requiert un compte et clé pour `/services/tasks.php`, **ne pas solliciter** pour établir des limites IIIF | **Non**, sauf projet spécifique utilisant l'API Tasks |
| Hors contact public | Yale Library interne | `web.library.yale.edu/lit/servicecatalog/164929` renvoie vers connexion SSO institutionnelle | **Non**, utiliser d'abord les documents publics OAI/IIIF de Yale déjà récupérés |

**Aucun courriel, formulaire, clé, authentification, test de charge ou contournement de CAPTCHA n'a été envoyé ou réalisé.** Les sollicitations doivent être justifiées par une question précise restée sans réponse dans la documentation officielle.

## Points techniques à traiter indépendamment, sans demander de lecture manuelle générale

| Priorité | Institution | Document technique toujours non lu | Alternative déjà lue / étape suivante |
|---|---|---|---|
| Haute | Cultural Japan | `app.cultural.jp/iiif-collection/collection.json` | IIIF Discovery in Japan a **une collection distincte** de 30 sous-collections, pas remplacement du JSON de Cultural Japan |
| Haute | Northwestern | `iiif.dc.library.northwestern.edu/iiif/3/.../info.json` | OpenAPI 3.1 / v2 officielle de 19 463 caractères retrouvée ; exemple REST `?as=iiif` à distinguer de l'Image API |
| Document obtenu, accès live à préciser | National Palace Museum | **Vrai `info.json` original enregistré** dans le dépôt le 18/11 (Image 2, 3055×2291, tuiles 512) | Ancien timeout toujours documenté ; aucun quota mesuré. Demande institutionnelle conditionnelle seulement si nécessaire |
| Haute | Villanova | `digital.library.villanova.edu/Item/vudl:92879/Manifest` | Domaine du catalogue et notice fournisseur récupérés ; l'exemple ciblé reste 403 |
| Moyenne | DRI | `repository.dri.ie/api-docs` (seul Swagger UI) | Routes Rswag et `iiif/:id/manifest` prouvées dans le code officiel ; récupérer le document OpenAPI de l'application |
| Moyenne | Folger | `digitalcollections.folger.edu/` | Défi humain sur le catalogue ; historique de la plateforme IIIF documenté, demander accès officiel si nécessaire |
| Document obtenu, accès live à préciser | Qatar Digital Library | Manifeste original JSON Presentation 2 lu en copie datée du 23/10 | HTTP live de la sonde non garanti, mais **aucune lecture humaine du manifeste à refaire** |
| Moyenne | Cambridge | Anciennes routes `cudl.link/v1/metadata/` et `/transcription` | Nouveau manifeste `cudl.lib.cam.ac.uk/iiif/MS-ADD-03996` réellement extrait, README CUDL Services disponible |

Le `robots.txt` d'un domaine n'est pas un contrat de quotas ; un `403` ne signifie pas qu'il faut contourner le filtrage, et une licence ne fixe pas de débit. Les documents personnels, les collections sous droits et les traitements de masse appellent des vérifications supplémentaires, indépendantes de la simple lecture de page.

## Où voir la totalité des cas sans refaire le travail

- Workflow CI : `.github/workflows/rattrapage-documentaire.yml`, **13 puis 16 tests** suivant les commits.
- Fichier généré : `data/triage-interventions-humaines.csv` **dans l'artefact** `rattrapage-inventaire-manuel` de la dernière CI ; **non versionné** pour éviter un fichier de sortie périmé.
- Résumé généré : `data/resume-triage-interventions.json`.
- Générateur : `scripts/triage_interventions.py` ; le CSV se recalcule après chaque nouvelle lecture, sans solliciter les APIs externes.

**Statut** : une entrée `CONTENU_NON_DEMONTRE_PAR_REPRISE_O` signifie *absence de preuve de contenu dans le registre*, pas preuve d'indisponibilité publique. Les actions humaines sont suggérées **seulement si l'information est nécessaire**.

## Mise à jour du 15 novembre : pages débloquées et actions à ne plus demander

Le statut initial « Art Institute of Chicago : `info.json` à lire » **n'est plus à jour**. La passe W a extrait le **JSON complet original** (IIIF Image 2, 6 679 × 4 577 pixels, 931 caractères) dans une copie datée du 15/11. Le **403 Cloudflare depuis la sonde** reste une question distincte pour une utilisation réelle. Le lecteur humain n'a **pas** à rouvrir cette page simplement pour en connaître la structure. Voir [rapport W](VERIFICATIONS-CHATGPT-2026-11-15-W-IIIF-IMAGES.md).

Autres tâches de lecture retirables de la file active : la documentation Finna anglaise (les deux URL historiques désormais lues), la page Contact Us de National Gallery of Art et l'étude de cas UK National Archives (rapport [X](VERIFICATIONS-CHATGPT-2026-11-15-X-DOCUMENTS-ORIGINAUX.md)) ; le **texte des 26 diapositives Yale LUX** (rapport [Y](VERIFICATIONS-CHATGPT-2026-11-15-Y-PDF-IIIF.md)). L'URL `iiif.archivelab.org` de l'Internet Archive est **historique**, officiellement remplacée par `iiif.archive.org`, où un `info.json` correspondant au même objet a été récupéré ; ne pas exiger de rendre l'ancien service de laboratoire opérationnel.

Pour Cardiff, **25 diapositives sur 29** ont été inspectées visuellement. **Quatre restent inaccessibles** (20, 23, 24, 28) ; cela demeure une lecture partielle, pas une page « complète ».

**Chiffres vérifiés par [CI #43748080199](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43748080199)** : **157 / 260 URL** avec contenu documentaire obtenu, **103 / 260** sans contenu démontré. Dans ce résidu, **80** ne demandent pas d'action humaine par défaut, **18** demanderaient une intervention conditionnelle et **5** correspondent à des demandes/contact/compte explicites. Les trois demandes institutionnelles et deux accès sous compte décrits plus haut restent **facultatifs**, sans formulaire ni message transmis.

**Liste active téléchargeable :** ouvrir l'artefact `rattrapage-inventaire-manuel` de la [dernière CI documentaire](https://github.com/maribakulj/Veille-API-IIIF/actions/runs/43748080199), puis `data/triage-interventions-humaines.csv`. Les numéros historiques des anciennes sections de ce document ne sont pas la métrique courante.


## Mise à jour du 18 novembre 2026

La CI documentaire confirme **162 URL originales avec contenu effectivement retrouvé** (11 lectures web, 151 copies indexées) sur 260 URL historiques, et **98 dont le contenu reste non démontré**. Les 98 se partagent en **77 cas sans lecture humaine requise par défaut, 16 interventions conditionnelles et 5 demandes/accès explicites**. Les cinq n'impliquent **pas** cinq courriels à envoyer : les deux contrôles de compte sont périphériques au besoin IIIF.

Le `info.json` original du National Palace Museum a été **extrait en JSON complet et sauvegardé** dans [la source du dépôt](institutions/national-palace-museum-taiwan/sources/lectures-2026-11-18/info-K1F000001N000000000PAA-indexed.json), mais son accessibilité HTTP depuis la sonde demeure non établie. L'Art Institute et Qatar étaient déjà satisfaits pour la **lecture du document**, non pour la disponibilité technique. Rapports [AA](VERIFICATIONS-CHATGPT-2026-11-18-AA-NPM-EUROPEANA-CARDIFF.md) et [AB](VERIFICATIONS-CHATGPT-2026-11-18-AB-HARVARD-KB-CULTURALJAPAN.md).

Le PDF Cardiff IGELU est passé de **25/29 à 28/29 diapositives inspectées visuellement**, sans pouvoir lire la page 24. Les endpoints Cultural Japan Collection, Northwestern Image, Villanova, DRI Swagger et plusieurs autres restent sans corps exploitable. Aucun formulaire envoyé, aucune authentification ni contournement de WAF effectué.
