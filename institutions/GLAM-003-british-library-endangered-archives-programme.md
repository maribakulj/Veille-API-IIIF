---
id: GLAM-003
institution: British Library – Endangered Archives Programme
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE (restrictions d’accès qualitatives seulement)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil de requêtes ni quota sur les pages lues ; pas de clé d’API mentionnée'
debit_iiif: 'Aucun seuil de débit IIIF publié sur les pages lues. Les restrictions relevées sont qualitatives : diffusion surtout par la Universal Viewer du site, téléchargement JPEG seulement lorsque les détenteurs d’archives l’ont accepté, et refus annoncé pour les volumes importants d’images haute résolution, sans seuil chiffré. Ce ne sont pas des débits.'
iiif_image: Universal Viewer et IIIF pour afficher les images ; version non précisée
iiif_presentation: Manifestes par icône IIIF ou /manifest sur les pages archive-file ; version non précisée
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: Téléchargement image unitaire depuis les manifestes ; pas de bulk décrit
robots_waf: NON PRÉSENT SUR CETTE PAGE
droits: Conditions d'accès ayants droit non lues
strategie: Accès réseau limité des chercheurs reconnu par l'EAP ; outils de partage pour améliorer l'accès
methode: 'WebFetch eap.bl.uk/tools : aucune limite ; WebSearch « British Library EAP IIIF API rate limit » : pages tierces seulement (archives, Gravitee) ; WebSearch « bl.uk IIIF API terms of use bulk download » : bl.uk/terms/imaging-services (tarifs, pas de limite) ; node/3936 (pas de chiffre) ; Passe 2 (2026-11-13) : 1 WebSearch, 2 WebFetch (tools ; reuse-collections-and-takedown-policy). Aucun lien de documentation API EAP sur ces pages.'
verifie_le: '2026-11-13'
sources:
- url: https://eap.bl.uk/tools
  note: ''
  surveiller: true
- url: https://eap.bl.uk/node/3936
  note: '(Reuse of Collections and Takedown Policy : pas de chiffre)'
  surveiller: true
- url: https://eap.bl.uk/reuse-collections-and-takedown-policy
  note: 'Politique de réutilisation : restrictions qualitatives, aucun chiffre ; IIIF et API non mentionnés'
  surveiller: true
---

# British Library – Endangered Archives Programme

**Verdict** : DOC LUE, AUCUN CHIFFRE

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebFetch eap.bl.uk/tools : aucune limite
- WebSearch « British Library EAP IIIF API rate limit » : pages tierces seulement (archives, Gravitee)
- WebSearch « bl.uk IIIF API terms of use bulk download » : bl.uk/terms/imaging-services (tarifs, pas de limite) ; node/3936 (pas de chiffre)

## Passe 2 (2026-11-13)
- WebFetch eap.bl.uk/tools : aucun chiffre ni clé ; liens vers des outils tiers et vers la politique de réutilisation ; aucune documentation API EAP.
- WebFetch reuse-collections-and-takedown-policy : aucun chiffre ; diffusion par la Universal Viewer ; pas de mention d’IIIF, d’API ni d’authentification.
- Pour une limite technique sur la Universal Viewer ou les points IIIF, la page renvoie vers l’équipe EAP ; non contactée.
