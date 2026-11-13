---
id: GLAM-004
institution: Cambridge University Library – CUDL
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE (IIIF déclaré en cours de mise en œuvre)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucune API décrite comme disponible sur les pages lues ; aucun chiffre publié'
debit_iiif: 'Aucun seuil publié. La page d’aide indique que l’IIIF est en cours de mise en œuvre et que les données sont surtout en METS, MODS et TEI ; aucune API n’y est décrite comme disponible. Les conditions d’utilisation interdisent l’extraction systématique de parties substantielles du contenu, sauf licence ou autorisation : c’est une règle d’usage, non un débit. Contradiction à reconfirmer avec la page about (voir traces).'
iiif_image: 'NON IMPLÉMENTÉ à date : « We are currently working on implementing the IIIF technology » (page /help)'
iiif_presentation: Non implémenté à date (même source)
acces: Services API publics ; une route Darwin requiert un jeton (dépôt cudl-services) ; ne se généralise pas à IIIF
moissonnage: Bulk « prévu, non disponible à ce stade » ; données METS/MODS/TEI ; PDF complets envisagés
robots_waf: NON PRÉSENT SUR CETTE PAGE
droits: Licence NON PRÉSENT SUR CETTE PAGE
strategie: Mise en œuvre IIIF en cours ; route IIIF du service cudl-services déclarée « not currently in use »
conflits:
- 'lib.cam.ac.uk/node/54662 évoque « près de 250 000 images disponibles via IIIF » : date et périmètre non vérifiés, à arbitrer'
lacunes:
- date de la page lib.cam.ac.uk
- statut IIIF réel en production
methode: 'WebSearch « Cambridge Digital Library CUDL IIIF API documentation usage limits » : pas de doc API officielle ; WebSearch « cudl IIIF rate limit requests per minute terms » : rien d’officiel ; WebFetch cudl.lib.cam.ac.uk/terms : aucun chiffre ; Passe 2 (2026-11-13) : 2 WebSearch (dont une restreinte à cudl.lib.cam.ac.uk), 2 WebFetch (terms ; help).'
verifie_le: '2026-11-13'
sources:
- url: https://cudl.lib.cam.ac.uk/terms
  note: ''
  surveiller: true
- url: https://www.lib.cam.ac.uk/research/digital-humanities/case-studies/dynamic-digital-library-iiif-scoping-project
  note: (projet IIIF, sans chiffre)
  surveiller: true
- url: https://cudl.lib.cam.ac.uk/help/
  note: 'Aide : aucun chiffre ; IIIF en cours de mise en œuvre ; données en METS, MODS, TEI ; APIs demandées aux utilisateurs, non engagées'
  surveiller: true
- url: https://cudl.lib.cam.ac.uk/about/
  note: 'Extrait de recherche seulement, page non ouverte : mentionne un accès aux contenus via des API comme IIIF ; contredit la page help'
  surveiller: true
---

# Cambridge University Library – CUDL

**Verdict** : DOC LUE, AUCUN CHIFFRE (règle d’extraction systématique interdite, sans seuil)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Cambridge Digital Library CUDL IIIF API documentation usage limits » : pas de doc API officielle
- WebSearch « cudl IIIF rate limit requests per minute terms » : rien d’officiel
- WebFetch cudl.lib.cam.ac.uk/terms : aucun chiffre

## Passe 2 (2026-11-13)
- WebFetch terms : aucun chiffre, clé ni documentation API ; restriction d’accès possible à tout ou partie du site ; extraction systématique interdite sans licence.
- WebFetch help : aucun chiffre ; IIIF déclaré en cours de mise en œuvre ; téléchargement de livres entiers en PDF à l’étude, sans échéance.
- Contradiction à reconfirmer : l’extrait de la page about dit que les contenus sont accessibles par des API comme IIIF, alors que la page help dit le contraire. Des pages de visualisation affichent des liens de manifeste IIIF (extraits de recherche). Verdict inchangé faute de chiffre ; à trancher par lecture complète de la page about et d’un manifeste.
