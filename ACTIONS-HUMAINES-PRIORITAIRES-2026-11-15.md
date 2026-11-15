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
| Haute | Art Institute of Chicago | `www.artic.edu/iiif/2/.../info.json`, redirection/autodéfi | Guide public API et droits déjà lus ; vérifier une image IIIF par client autorisé, sans extrapoler limite REST |
| Haute | Cultural Japan | `app.cultural.jp/iiif-collection/collection.json` | IIIF Discovery in Japan a **une collection distincte** de 30 sous-collections, pas remplacement du JSON de Cultural Japan |
| Haute | Northwestern | `iiif.dc.library.northwestern.edu/iiif/3/.../info.json` | OpenAPI 3.1 / v2 officielle de 19 463 caractères retrouvée ; exemple REST `?as=iiif` à distinguer de l'Image API |
| Haute | National Palace Museum | `iiifod.npm.gov.tw/iiif/2/.../info.json` | Guide IIIF PDF 13 pages et exemples de manifestes retrouvés ; en-têtes et accès d'images non établis |
| Haute | Villanova | `digital.library.villanova.edu/Item/vudl:92879/Manifest` | Domaine du catalogue et notice fournisseur récupérés ; l'exemple ciblé reste 403 |
| Moyenne | DRI | `repository.dri.ie/api-docs` (seul Swagger UI) | Routes Rswag et `iiif/:id/manifest` prouvées dans le code officiel ; récupérer le document OpenAPI de l'application |
| Moyenne | Folger | `digitalcollections.folger.edu/` | Défi humain sur le catalogue ; historique de la plateforme IIIF documenté, demander accès officiel si nécessaire |
| Moyenne | Qatar Digital Library | Manifeste `/en/iiif/81055/.../manifest` | **Résolu pour le contenu** : vrai JSON IIIF Presentation 2 intégral (copie 23/10), mais réponse live de la sonde encore inconnue |
| Moyenne | Cambridge | Anciennes routes `cudl.link/v1/metadata/` et `/transcription` | Nouveau manifeste `cudl.lib.cam.ac.uk/iiif/MS-ADD-03996` réellement extrait, README CUDL Services disponible |

Le `robots.txt` d'un domaine n'est pas un contrat de quotas ; un `403` ne signifie pas qu'il faut contourner le filtrage, et une licence ne fixe pas de débit. Les documents personnels, les collections sous droits et les traitements de masse appellent des vérifications supplémentaires, indépendantes de la simple lecture de page.

## Où voir la totalité des cas sans refaire le travail

- Workflow CI : `.github/workflows/rattrapage-documentaire.yml`, **13 puis 16 tests** suivant les commits.
- Fichier généré : `data/triage-interventions-humaines.csv` **dans l'artefact** `rattrapage-inventaire-manuel` de la dernière CI ; **non versionné** pour éviter un fichier de sortie périmé.
- Résumé généré : `data/resume-triage-interventions.json`.
- Générateur : `scripts/triage_interventions.py` ; le CSV se recalcule après chaque nouvelle lecture, sans solliciter les APIs externes.

**Statut** : une entrée `CONTENU_NON_DEMONTRE_PAR_REPRISE_O` signifie *absence de preuve de contenu dans le registre*, pas preuve d'indisponibilité publique. Les actions humaines sont suggérées **seulement si l'information est nécessaire**.
