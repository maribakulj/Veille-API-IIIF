---
id: GLAM-056
institution: Brown University Digital Repository
pays: États-Unis
statut: DOC LUE, AUCUN CHIFFRE (passe 1 ; extrait de cette passe sans chiffre)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE (passe 1 ; extrait de cette passe sans chiffre) ; Passe 1 : doc officielle lue ; passe 2 : extraits de la page passerelle IIIF et de la politique, sans chiffre d''API'
debit_iiif: 'La documentation officielle de la BDR (repository.library.brown.edu/studio/api-docs) avait été lue en passe 1 : ni chiffre ni règle d''accès API. Cette passe n''a remonté qu''un agrégateur tiers mentionnant une « limite de débit documentée » sans valeur, écarté. Le service IIIF de la BDR passe par une passerelle d''authentification (Loris pour l''image, manifestes générés), sans seuil publié dans les extraits lus. Les conditions de dépôt indiquent une limite de 4 Go par utilisateur pour l''envoi de collections personnelles : ce n''est pas une limite d''API.'
iiif_image: Passerelle IIIF utilisant Loris pour l'Image API (blog Brown, résumé de recherche) ; version non précisée
iiif_presentation: Manifestes générés par la passerelle (blog Brown) ; version non précisée
api_recherche: 'API REST/recherche citée par apis.io (tertiaire) ; le blog Brown indique que l''API de recherche n''est pas encore implémentée : contradiction non résolue'
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: NON PRÉSENT SUR CETTE PAGE
strategie: Passerelle IIIF (Loris + manifestes générés) ; API de recherche annoncée mais non confirmée
lacunes: Vérifier les limites Brown dans la doc officielle studio/api-docs, non lue à ce stade.
methode: 'Passe 1 : doc officielle lue ; WebSearch « Brown University Digital Repository IIIF API terms rate limit » : agrégateur écarté, passerelle IIIF et politique lues en extrait'
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
