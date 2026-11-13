---
id: GLAM-024
institution: Bayerische Staatsbibliothek / MDZ
pays: Allemagne
statut: PARTIEL (règle annoncée, chiffre absent)
classe: règle sans chiffre
statut_quota: PARTIEL (règle annoncée, chiffre absent) ; Règle annoncée sur page officielle lue ; chiffre absent
debit_iiif: 'Page officielle (interfaces des collections numériques, version anglaise) : « Please note that there is a limit to the number of requests that can be made to the Image API per 24 hours. » Même règle pour les téléchargements OCR : « a limit to the number of OCR downloads that can be made per 24 hours ». La Presentation API est dite « unlimited ». Aucun nombre n''est donné pour la limite de 24 heures ; aucune limite par minute ou seconde n''est mentionnée.'
iiif_image: Image API v2 (api.digitale-sammlungen.de/iiif/image/v2/{image_id}/…) ; spécification citée 2.1
iiif_presentation: Presentation API v2 (api.digitale-sammlungen.de/iiif/presentation/v2/{object_id}/manifest) ; spécification citée 2.1
api_recherche: NON PRÉSENT SUR CETTE PAGE
acces: 'NON PRÉSENT SUR CETTE PAGE (en-tête Access-Control-Allow-Origin: * mentionné)'
moissonnage: Dépôt conforme à OAI-PMH ; téléchargement en masse NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: Aucune licence nommée ; « Commercial use may be excluded. » ; renvoi à la déclaration de droits de chaque objet
lacunes:
- chiffre du plafond 24 h (Image et OCR)
- date de mise à jour de la page
- politique robots et bots IA
methode: 'WebSearch « BSB IIIF image API rate limit » : page officielle MDZ avec règle de 24 heures ; WebFetch digitale-sammlungen.de/en/interfaces : règle de 24 heures, aucun nombre ; WebSearch « Image API Anfragen pro 24 Stunden Limit Zahl » : aucune valeur trouvée sur les pages officielles'
verifie_le: '2026-11-13'
sources:
- url: https://www.digitale-sammlungen.de/en/interfaces
  note: '(lue : règle de 24 heures, sans nombre)'
  surveiller: true
- url: https://api.digitale-sammlungen.de/iiif/image/v2/
  note: (endpoint d'exemple cité par la page officielle, non interrogé)
  surveiller: true
---

# Bayerische Staatsbibliothek / MDZ

**Verdict** : PARTIEL (règle annoncée, chiffre absent)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « BSB IIIF image API rate limit » : page officielle MDZ avec règle de 24 heures
- WebFetch digitale-sammlungen.de/en/interfaces : règle de 24 heures, aucun nombre
- WebSearch « Image API Anfragen pro 24 Stunden Limit Zahl » : aucune valeur trouvée sur les pages officielles
