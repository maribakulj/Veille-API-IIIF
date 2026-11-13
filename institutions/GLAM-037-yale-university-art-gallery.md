---
id: GLAM-037
institution: Yale University Art Gallery
pays: États-Unis
statut: NON TROUVÉ APRÈS RECHERCHE (site officiel refusé par l’outil ; seul lien IIIF listé non officiel)
classe: non trouvé après recherche
statut_quota: 'NON TROUVÉ APRÈS RECHERCHE : aucun chiffre lu ; page officielle refusée'
debit_iiif: 'Aucun débit IIIF trouvé. La page officielle artgallery.yale.edu/collections est refusée par l’outil : non contournée, marquée non surveillée. Le seul lien IIIF de la fiche est une formation tierce, non une source officielle. Aucune règle de débit n’a donc pu être lue pour ce musée.'
iiif_image: 'Image Service 2 : images.collections.yale.edu/iiif/2/yuag:{UUID} observé dans des manifestes officiels'
iiif_presentation: 'Presentation 3 : contexte http://iiif.io/api/presentation/3/context.json observé dans manifests.collections.yale.edu/yuag/obj/{id}'
acces: 'Aucune permission requise pour le domaine public : « No permission to use images of public-domain works is required. »'
moissonnage: NON PRÉSENT dans les pages lues
robots_waf: NON PRÉSENT dans les pages lues
droits: 'Images du domaine public : téléchargement immédiat via le lien « download » (page Rights and Reproductions)'
lacunes:
- page officielle des collections refusée par l’outil
- documentation IIIF ou API du musée non lue
methode: 'WebSearch « Yale University Art Gallery IIIF API rate limit terms images » : pas de chiffre ; WebSearch « Yale Peabody Museum digital collections IIIF manifests usage terms » : résultats hors galerie, à reprendre si besoin ; Passe 2 (2026-11-13) : 1 WebFetch refusé (artgallery.yale.edu/collections), non contourné.'
verifie_le: '2026-11-13'
sources:
- url: https://training.iiif.io/advanced_iiif/basics/finding_yale.html
  note: '(extrait : manifestes v2 et v3 des musées Yale, pas de limite)'
  surveiller: true
- url: https://artgallery.yale.edu/collections
  note: 'Refusée par l’outil (hors liste d’autorisation) : non lue, non surveillée'
  surveiller: false
sources_sans_url:
- Aucune page officielle de quota atteignable (recherche bornée)
---

# Yale University Art Gallery

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (aucune doc officielle de quota)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Yale University Art Gallery IIIF API rate limit terms images » : pas de chiffre
- WebSearch « Yale Peabody Museum digital collections IIIF manifests usage terms » : résultats hors galerie, à reprendre si besoin

## Passe 2 (2026-11-13)
- WebFetch artgallery.yale.edu/collections : URL hors liste d’autorisation ; non contournée.
