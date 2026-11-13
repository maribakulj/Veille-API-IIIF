---
id: GLAM-022
institution: Bodmer Lab – Université de Genève
pays: Suisse
statut: NON TROUVÉ APRÈS RECHERCHE (page Bodmer Lab refusée ; fondation lue sans chiffre ni API)
classe: non trouvé après recherche
statut_quota: 'NON TROUVÉ APRÈS RECHERCHE : aucun chiffre de débit ; page Bodmer Lab refusée par l’outil'
debit_iiif: 'Aucun débit IIIF trouvé. La page de recherche de Bodmer Lab (bodmerlab.unige.ch) est refusée par l’outil : non contournée, source marquée non surveillée. La page de la Fondation Bodmer lue ne donne aucun chiffre de limite, de quota ni de throttling, et ne mentionne ni API ni IIIF. Elle décrit un préavis de deux mois pour la consultation et des frais de publication : ce ne sont pas des limites d’usage. Le guide IIIF communautaire listé n’est pas une source officielle.'
iiif_image: NON VÉRIFIÉ sur doc officielle
iiif_presentation: NON VÉRIFIÉ sur doc officielle ; manifeste exposé via le bouton Mirador (source tierce)
acces: NON VÉRIFIÉ
moissonnage: NON VÉRIFIÉ
robots_waf: NON VÉRIFIÉ
droits: NON VÉRIFIÉ
lacunes:
- page Bodmer Lab refusée par l’outil
- documentation IIIF ou API non lue
- clé non mentionnée sur la page de la fondation
methode: 'WebSearch « Bodmer Lab Genève IIIF API conditions d''utilisation limite requêtes » : conditions de la Fondation Bodmer, guide communautaire ; WebFetch bodmerlab.unige.ch : refusé (hors liste autorisée) ; Passe 2 (2026-11-13) : 1 WebFetch refusé (bodmerlab.unige.ch), non contourné ; 1 WebFetch (www.fondationbodmer.ch/recherche).'
verifie_le: '2026-11-13'
sources:
- url: https://bodmerlab.unige.ch/fr/search?keywords=
  note: (refusée par l'outil)
  surveiller: false
- url: https://fondationbodmer.ch/recherche
  note: (conditions de reproduction de la Fondation, sans quota)
  surveiller: true
- url: https://guides.iiif.io/guides/bodmerlab.unige.ch/
  note: (guide communautaire, non officiel, sans chiffre lu)
  surveiller: true
---

# Bodmer Lab – Université de Genève

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (page officielle non lisible)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Bodmer Lab Genève IIIF API conditions d'utilisation limite requêtes » : conditions de la Fondation Bodmer, guide communautaire
- WebFetch bodmerlab.unige.ch : refusé (hors liste autorisée)

## Passe 2 (2026-11-13)
- WebFetch bodmerlab.unige.ch : URL hors liste d’autorisation ; non contournée.
- WebFetch fondationbodmer.ch/recherche : aucun chiffre ; pas d’API ni d’IIIF ; préavis de consultation non assimilé à une limite.
