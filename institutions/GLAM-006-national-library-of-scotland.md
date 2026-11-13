---
id: GLAM-006
institution: National Library of Scotland
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE IIIF (quota de tuiles hors IIIF publié)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE IIIF ; quota de tuiles hors IIIF : 100 000 requêtes par mois au palier gratuit non commercial (extrait de recherche)'
debit_iiif: Aucun seuil de débit IIIF publié sur la page de contact lue ni sur l’aide de la visionneuse (extrait). Les cartes zoomables ont des points IIIF Presentation et un info.json accessible par « Show IIIF ». Le chiffre de 100 000 requêtes par mois concerne les tuiles de l’API Historic Maps (service MapTiler), non l’IIIF.
iiif_image: Image IIIF présente (carte NLS, extrait Digirati) ; version non précisée
iiif_presentation: Manifestes sur view.nls.uk/manifest/... ; version non précisée
acces: Non relevé
moissonnage: 'Data Foundry : corpus téléchargeables (MARCXML, Dublin Core, cartes, texte) ; licences par jeu de données'
droits: Licences par jeu de données (Data Foundry)
lacunes:
- page projects/api non ouverte (erreur côté site)
- licence 2016 (PDF) non lue
- robots.txt non lu
methode: 'WebSearch « NLS IIIF API rate limit requests per minute » : rien d’officiel ; WebSearch « digital.nls.uk terms of use download images API » : pages NLS sans limite ; WebFetch digital.nls.uk/gallery : refusé (URL non autorisée) ; à reprendre ; WebSearch « National Library of Scotland IIIF requests terms of use limit » : politiques NLS sans chiffre ; galerie toujours non lisible ; Passe 2 (2026-11-13) : 2 WebSearch (domaine nls.uk), 2 WebFetch (projects/api : erreur côté site ; enquiries : lu).'
verifie_le: '2026-11-13'
sources:
- url: https://www.nls.uk/media/bhbn3m5l/2016-metadata-digital-licencing-policy.pdf
  note: '(politique de licence 2016, extrait : pas de chiffre)'
  surveiller: true
- url: https://www.infodocket.com/2018/07/04/iiifs-universal-viewer-launches-on-national-library-of-scotland-digital-gallery-more-than-730000-images-available/
  note: '(reprise d''un communiqué NLS de 2018 : lancement, pas de limite)'
  surveiller: true
- url: https://guides.iiif.io/guides/digital.nls.uk/
  note: (guide tiers, mis à jour le 2 avril 2024, sans chiffre visible)
  surveiller: true
- url: https://maps.nls.uk/enquiries
  note: 'Contact et copies : aucun chiffre IIIF ni clé ; pas d’API mentionnée ; téléchargements payants sans quota'
  surveiller: true
- url: https://maps.nls.uk/projects/api/
  note: 'Extrait de recherche seulement : page non ouverte (erreur côté site) ; palier gratuit de 100 000 requêtes de tuiles par mois, hors IIIF'
  surveiller: true
- url: https://maps.nls.uk/view/help/
  note: 'Extrait de recherche seulement : Show IIIF donne l’info.json ; aucune limite'
  surveiller: true
---

# National Library of Scotland

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (aucune doc officielle de quota ; galerie non lisible)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « NLS IIIF API rate limit requests per minute » : rien d’officiel
- WebSearch « digital.nls.uk terms of use download images API » : pages NLS sans limite
- WebFetch digital.nls.uk/gallery : refusé (URL non autorisée) ; à reprendre
- WebSearch « National Library of Scotland IIIF requests terms of use limit » : politiques NLS sans chiffre ; galerie toujours non lisible

## Passe 2 (2026-11-13)
- WebFetch maps.nls.uk/enquiries : aucun chiffre IIIF ni clé ; téléchargements payants par commande, sans quota ; pas de limite sur les captures d’écran ni les PDF.
- WebFetch maps.nls.uk/projects/api/ : erreur côté site, page non lue. L’extrait de recherche mentionne le palier gratuit de 100 000 requêtes de tuiles par mois.
- Extrait maps.nls.uk/view/help : Show IIIF donne l’URI de base de l’Image API ou l’info.json ; aucune limite décrite.
- Le quota de tuiles relève de l’API Historic Maps (MapTiler, depuis 2022), non de l’IIIF : ne pas le traiter comme un débit IIIF.
- Date de la page projects/api incertaine : l’extrait indique une ancienneté très élevée, alors que le texte décrit le passage à MapTiler en 2022.
