---
id: GLAM-044
institution: Duke University Libraries
pays: États-Unis
statut: PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement)
classe: pas de débit IIIF chiffré
statut_quota: PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement) ; Page officielle lue en extrait ; documentation IIIF de Duke non trouvée
debit_iiif: 'Aucune limite IIIF ni quota d''API n''est publié par Duke. La seule valeur chiffrée relevée est une recommandation de politesse pour les robots, sur la page officielle « impact of bots » de la bibliothèque : espacer les requêtes d''un délai d''au moins 10 secondes (crawl delay), même lorsque robots.txt ne le précise pas. Ce n''est ni un quota ni une règle d''API, mais une limite voisine, à signaler comme telle.'
iiif_image: NON VÉRIFIÉ sur doc officielle
iiif_presentation: Manifestes IIIF récupérés par l'API avec cache (merge request GitLab du dépôt public DDR de Duke) ; version non précisée
acces: NON PRÉSENT dans les sources lues
moissonnage: NON PRÉSENT dans les sources lues
robots_waf: NON PRÉSENT dans les sources lues
bots_ia: NON PRÉSENT dans les sources lues
droits: NON PRÉSENT dans les sources lues
strategie: Le dépôt public DDR interroge l'API pour les manifestes et retombe sur un fichier IIIF statique en cas d'erreur (merge request GitLab)
lacunes: 'Doc API Duke (classeur : api-catalog.oit.duke.edu) à rechercher par nom exact.'
methode: 'WebSearch « Duke University Libraries digital collections IIIF API rate limit terms » : recommandation de crawl repérée, pas de quota IIIF'
verifie_le: '2026-11-13'
sources:
- url: https://library.duke.edu/using/off-campus/impact-of-bots
  note: '(extrait lu : délai de crawl recommandé de 10 secondes)'
  surveiller: true
- url: https://repository.duke.edu/
  note: '(extrait : dépôt numérique, sans chiffre)'
  surveiller: true
---

# Duke University Libraries

**Verdict** : PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Duke University Libraries digital collections IIIF API rate limit terms » : recommandation de crawl repérée, pas de quota IIIF
