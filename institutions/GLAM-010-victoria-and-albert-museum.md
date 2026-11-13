---
id: GLAM-010
institution: Victoria and Albert Museum
pays: Royaume-Uni
statut: NON TROUVÉ APRÈS RECHERCHE (chiffre attribué à TNA, non retenu)
classe: non trouvé après recherche
statut_quota: NON TROUVÉ APRÈS RECHERCHE (chiffre attribué à TNA, non retenu) ; Résumé de la section 9 non vérifié mot à mot ; recherche de remplacement sans source V&A chiffrée
debit_iiif: 'Le chiffre de 3 000 appels par jour à une requête par seconde, lu dans un résumé des conditions V&A, est identique à celui de The National Archives, retrouvé sur ses pages : il n''est pas retenu pour la V&A. Aucune documentation V&A chiffrée n''a été trouvée. Un revendeur tiers annonce une limite d''une requête par seconde pour une « V&A Museum API » : non retenu (service tiers).'
iiif_image: IIIF Image (dérivés selon objet, recommandation 768 / 2 500 px selon classeur)
iiif_presentation: Non confirmé
droits: Données et images disponibles pour réutilisation (developers.vam.ac.uk)
lacunes:
- guide/v2 non lu
- chiffre 3 000/j non vérifié
methode: 'WebFetch developers.vam.ac.uk : renvoie à la section 9, aucun chiffre lu ; WebFetch conditions V&A : résumé qui attribue le chiffre à la V&A (2 appels, même résultat) ; WebSearch : le texte exact n’apparaît que dans les pages de The National Archives ; Erreur évitée : premier résumé mal attribué, retiré ; WebSearch « Victoria and Albert Museum API rate limit requests per second » : aucune page V&A ; revendeur tiers écarté'
verifie_le: '2026-11-13'
sources:
- url: https://developers.vam.ac.uk/
  note: (renvoie à la section 9 des conditions, sans chiffre lu)
  surveiller: true
- url: https://www.nationalarchives.gov.uk/terms-and-conditions/discovery-for-developers-about-the-application-programming-interface-api/
  note: '(texte TNA, autre institution : ne compte pas pour la V&A)'
  surveiller: true
sources_sans_url:
- Aucune page officielle V&A de quota atteignable (recherche bornée)
---

# Victoria and Albert Museum

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (chiffre attribué à TNA, non retenu)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebFetch developers.vam.ac.uk : renvoie à la section 9, aucun chiffre lu
- WebFetch conditions V&A : résumé qui attribue le chiffre à la V&A (2 appels, même résultat)
- WebSearch : le texte exact n’apparaît que dans les pages de The National Archives
- Erreur évitée : premier résumé mal attribué, retiré
- WebSearch « Victoria and Albert Museum API rate limit requests per second » : aucune page V&A ; revendeur tiers écarté
