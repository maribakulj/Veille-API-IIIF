---
id: GLAM-023
institution: Fragmentarium
pays: Suisse
statut: DOC LUE, AUCUN CHIFFRE (conditions lues ; IIIF présent seulement en mots-clés)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota ; usage non commercial déclaré gratuit'
debit_iiif: 'Aucun seuil de débit publié sur la page des conditions. L’usage non commercial des images est déclaré gratuit, certains propriétaires imposant leurs restrictions document par document. Le terme IIIF n’apparaît que dans les mots-clés : aucun endpoint IIIF ni condition IIIF n’est décrit. Les métadonnées, hors descriptions de fragments, sont sous licence Creative Commons Attribution.'
iiif_image: 'Image API niveau 2 : profil http://iiif.io/api/image/2/level2.json dans les manifestes'
iiif_presentation: 'Presentation API v2 : contexte http://iiif.io/api/presentation/2/context.json dans les manifestes'
acces: NON VÉRIFIÉ
moissonnage: 'Manifestes par fragment : fragmentarium.ms/metadata/iiif/{id}/manifest.json ; collections IIIF citées'
robots_waf: NON VÉRIFIÉ
droits: NON VÉRIFIÉ
strategie: Images servies par Loris sur fragmentarium.ms ; certains canevas pointent vers e-rara.ch et e-codices.unifr.ch (images hébergées ailleurs)
lacunes:
- endpoints IIIF non décrits sur la page lue
- 'accès en masse : contact fragmentarium@unifr.ch, non contacté'
methode: 'WebSearch « Fragmentarium IIIF API limits rate documentation » : guide communautaire et conditions officielles ; Conditions d''utilisation de Fragmentarium : aucune limite (extrait lu via résultat de recherche) ; Passe 2 (2026-11-13) : 1 WebFetch (conditions).'
verifie_le: '2026-11-13'
sources:
- url: https://fragmentarium.ms/pages/terms
  note: '(lue : aucun chiffre)'
  surveiller: true
- url: https://iiif.io/guides/guides/fragmentarium.ms/
  note: (guide communautaire, non officiel, sans chiffre lu)
  surveiller: true
---

# Fragmentarium

**Verdict** : DOC LUE, AUCUN CHIFFRE (conditions d'utilisation lues)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Fragmentarium IIIF API limits rate documentation » : guide communautaire et conditions officielles
- Conditions d'utilisation de Fragmentarium : aucune limite (extrait lu via résultat de recherche)

## Passe 2 (2026-11-13)
- WebFetch pages/terms : aucun seuil de requêtes, quota, téléchargement ni moissonnage ; pas d’API mentionnée ; clé non précisée.
- Accès en masse : contact fragmentarium@unifr.ch indiqué ; non contacté.
