# Passe Y — étude des PDF de présentation plutôt que seul lien vers ceux-ci

Date : 15 novembre 2026. Deux documents étaient classés **lecture PDF partielle** dans la file du rattrapage. La lecture porte sur **leur contenu** ; il ne s'agit pas d'endpoints de quotas ni d'une autorisation de moissonner.

## 1. Yale LUX : texte des 26 diapositives lu, figures clés contrôlées

**URL originale de la file** : https://www.cni.org/wp-content/uploads/2022/12/LUX-CNI-Susan-Rob-Rob-Sanderson.pdf

Document CNI Fall Forum du **12 décembre 2022**, par Robert Sanderson et Susan Gibbons, **26 pages**.

- **Texte du PDF extrait et parcouru intégralement**, couvrant les pages 1–26, avec **369 lignes repérées par page** dans le lecteur.
- **Captures visuelles vérifiées** : diapositives 11, 15, 20, 26 ; de précédentes vérifications avaient contrôlé les diapositives 1 et 19. **Les autres images n'ont pas fait l'objet d'un examen visuel détaillé**, même si leur contenu textuel est extrait. Les pages de démonstration peuvent donc conserver une composante visuelle non documentée.
- Architecture présentée : **LOUD (Linked Open Usable Data)**, **JSON-LD**, **Linked Art**, **IIIF**, modèles **FAIR** et **SHARED**.
- **IIIF Change Discovery** est explicitement cité dans les principes SHARED à la diapositive **15** (index zéro 14), afin d'améliorer la possibilité de moissonner les changements.
- Les diapos 16–18 distinguent équipes/projet, architecture JSON-LD et recherche multi-modale ; diapos 19–23 traitent des graphes, de la réconciliation d'entités, des divergences entre domaines patrimoniaux et du coût de maintenance.
- Les diapos finales 23–26 exposent les incertitudes sur l'adoption, les coûts partagés et la **documentation technique partageable**.
- Aucun seuil `requests/min`, `429` chiffré, exigence de clé ni barème d'authentification n'est inscrit dans le **texte intégral extrait des 26 pages**. Il faut cependant **éviter d'attribuer à 2026** les états de projet d'un document de **2022**.

**Classement : `PDF_TEXTE_INTEGRAL_LU_VISUELS_PARTIELS`**, satisfait la recherche documentaire textuelle sans prétendre à une lecture détaillée de chaque capture.

## 2. Cardiff, Alma Digital / IIIF : 25 diapositives examinées visuellement, quatre encore indisponibles

**URL originale de la file** : https://igelu.org/wp-content/uploads/2022/10/Unlocking-your-collections-with-Alma-Digital-and-IIIF.pdf

Présentation d'Alison Harvey, Cardiff University, **29 pages**. Le lecteur n'extrait que **17 lignes** : elle est **largement constituée d'images et captures**, il serait erroné de qualifier les 29 diapositives de « lues par extraction PDF ».

**Pages effectivement examinées visuellement :** 1–19, 21–22, 25–27 et 29 (numérotation humaine), soit **25 / 29**. Certaines montrent le catalogue Alma, ses collections numérisées, des fiches Edward Thomas, Priscilla Scott-Ellis et l'intégration d'**Universal Viewer** avec métadonnées/provenance et conditions d'attribution CC BY 4.0. D'autres affichent des exemples de présentation, d'archives visuelles, de recherche et d'intégration de Mirador/Universal Viewer.

**Pages manquantes : 20, 23, 24 et 28 (numérotation humaine ; index PDF 19, 22, 23, 27)**, car le lecteur d'images a renvoyé des timeouts à deux tentatives pour ces pages. Le PDF distant ne s'est pas laissé télécharger par la voie alternative. **Le statut reste `PDF_PARTIEL_25_SUR_29`**, sans promotion au statut « intégralement lu ». On ne peut pas conclure à l'absence certaine de quota sur les quatre pages non examinées, même si les diapositives vues sont centrées sur l'usage et les projets.

### Conclusion méthodologique

- **Yale** : texte des 26 pages vraiment lu, avec figures représentatives examinées, mais pas audit iconographique exhaustif.
- **Cardiff** : inspection visuelle substantielle 25 / 29, **4 diapositives encore absentes**. Ne pas déléguer indistinctement la totalité de la présentation à une personne : documenter les pages précises qui manquent.
- Ni un modèle de données JSON-LD, ni l'usage d'Universal Viewer, ni une licence ouverte ne suffisent pour déduire des quotas de requêtes IIIF.
