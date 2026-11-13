---
id: GLAM-010
institution: Victoria and Albert Museum
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE (pages développeurs et conditions lues ; guide v2 non ouvert)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni clé d’API sur la page développeurs et les conditions lues'
debit_iiif: Aucun seuil de débit publié sur la page développeurs, qui renvoie à la norme IIIF Image API pour l’image, ni sur la page des conditions. La section 9 citée par la page développeurs est absente de la page conditions lue ; les conditions d’API renvoient à une autre page, non lue.
iiif_image: IIIF Image (dérivés selon objet, recommandation 768 / 2 500 px selon classeur)
iiif_presentation: Non confirmé
droits: Données et images disponibles pour réutilisation (developers.vam.ac.uk)
lacunes:
- page images (IIIF) redirigée vers http non suivie
- guide v2 redirigé vers http non suivi
- conditions d’API (page va-websites-terms-conditions) non lues
methode: 'WebFetch developers.vam.ac.uk : renvoie à la section 9, aucun chiffre lu ; WebFetch conditions V&A : résumé qui attribue le chiffre à la V&A (2 appels, même résultat) ; WebSearch : le texte exact n’apparaît que dans les pages de The National Archives ; Erreur évitée : premier résumé mal attribué, retiré ; WebSearch « Victoria and Albert Museum API rate limit requests per second » : aucune page V&A ; revendeur tiers écarté ; Passe 2 (2026-11-13) : 4 WebFetch : developers.vam.ac.uk (lu) ; terms-of-use (lu) ; images et guide v2 (redirection 302 vers http non suivie). Chiffre de passe 1 réattribué à The National Archives, non au V&A.'
verifie_le: '2026-11-13'
sources:
- url: https://developers.vam.ac.uk/
  note: (renvoie à la section 9 des conditions, sans chiffre lu)
  surveiller: true
- url: https://www.nationalarchives.gov.uk/terms-and-conditions/discovery-for-developers-about-the-application-programming-interface-api/
  note: '(texte TNA, autre institution : ne compte pas pour la V&A)'
  surveiller: true
- url: https://www.vam.ac.uk/articles/terms-of-use
  note: 'Conditions : aucun chiffre ; section 9 absente ; conditions d’API renvoyées ailleurs'
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

## Passe 2 (2026-11-13)
- WebFetch developers.vam.ac.uk : aucun chiffre ; pas de clé mentionnée ; IIIF Image API renvoyée vers la norme ; liens vers la documentation images et l’API Reference.
- WebFetch vam.ac.uk terms-of-use : aucun chiffre ; cinq sections, sans section 9 ; les conditions d’API renvoient vers une page de conditions des sites non lue.
- WebFetch developers.vam.ac.uk/images et /guide/v2/ : redirection 302 vers une adresse http:// ; non suivie, à relire en https.
- Le chiffre de passe 1 (3 000 par jour) provient du texte de The National Archives : il reste écarté pour le V&A.
