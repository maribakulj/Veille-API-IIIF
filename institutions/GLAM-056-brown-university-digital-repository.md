---
id: GLAM-056
institution: Brown University Digital Repository
pays: États-Unis
statut: NON TROUVÉ APRÈS RECHERCHE (page de politique bloquée par une vérification humaine)
classe: non trouvé après recherche
statut_quota: 'NON TROUVÉ APRÈS RECHERCHE : la page de politique n’a pas livré son contenu ; aucun chiffre trouvé'
debit_iiif: 'Aucun débit IIIF trouvé. La page de politique du dépôt ne renvoie qu’un écran de vérification humaine, sans contenu. La documentation d’API (studio/api-docs) avait été refusée par l’outil en passe 1 : non réessayée. Le verdict « doc lue » de la passe 1 est retiré tant que ces pages ne sont pas lisibles.'
iiif_image: Passerelle IIIF utilisant Loris pour l'Image API (blog Brown, résumé de recherche) ; version non précisée
iiif_presentation: Manifestes générés par la passerelle (blog Brown) ; version non précisée
api_recherche: 'API REST/recherche citée par apis.io (tertiaire) ; le blog Brown indique que l''API de recherche n''est pas encore implémentée : contradiction non résolue'
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: NON PRÉSENT SUR CETTE PAGE
strategie: Passerelle IIIF (Loris + manifestes générés) ; API de recherche annoncée mais non confirmée
lacunes:
- studio/policies bloquée par une vérification humaine
- studio/api-docs refusée en passe 1
- à relire avec un navigateur, sans contournement
methode: 'Passe 1 : doc officielle lue ; WebSearch « Brown University Digital Repository IIIF API terms rate limit » : agrégateur écarté, passerelle IIIF et politique lues en extrait ; Passe 2 (2026-11-13) : 1 WebFetch (policies : écran de vérification, aucun contenu).'
verifie_le: '2026-11-13'
sources:
- url: https://repository.library.brown.edu/studio/api-docs/
  note: '(passe 1 : aucun chiffre)'
  surveiller: true
- url: https://library.brown.edu/create/digitaltechnologies/?p=185
  note: '(extrait : passerelle IIIF et manifestes, pas de chiffre)'
  surveiller: true
- url: https://repository.library.brown.edu/studio/policies
  note: '(extrait : limite de 4 Go pour l''envoi, hors API)'
  surveiller: true
---

# Brown University Digital Repository

**Verdict** : DOC LUE, AUCUN CHIFFRE (passe 1 ; extrait de cette passe sans chiffre)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- Passe 1 : doc officielle lue
- WebSearch « Brown University Digital Repository IIIF API terms rate limit » : agrégateur écarté, passerelle IIIF et politique lues en extrait

## Passe 2 (2026-11-13)
- WebFetch studio/policies : écran de vérification humaine ; aucun seuil ni clé ; lien vers un formulaire de contact.
- Le verdict de passe 1 (« doc lue ») est retiré : contenu non lu. Ne pas contourner la vérification.
