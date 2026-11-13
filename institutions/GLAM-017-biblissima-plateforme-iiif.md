---
id: GLAM-017
institution: Biblissima+ (plateforme IIIF)
pays: France
statut: DOC LUE, AUCUN CHIFFRE (pages de documentation lues ; docs Nakala et Gallica non lues)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur les pages de documentation lues ; clé d’API non précisée'
debit_iiif: 'Aucun seuil de débit IIIF publié sur les pages lues (vademecum et API Présentation). Le vademecum exige HTTPS et CORS sur les manifestes et info.json, et recommande Change Discovery : ce sont des exigences techniques, non des débits. Les images épigraphiques restent hébergées sur Nakala, dont les limites relèvent d’une documentation non lue. Les sources Gallica et ARCA ne sont pas couvertes.'
iiif_image: Image API référencée par le portail (IIIF360, documentation Biblissima)
iiif_presentation: Presentation API ; version 3 « à venir » (présentation de 2018 ; à actualiser)
droits: 'Agrégateur : manifestes fournis par établissements ; droits par établissement'
strategie: Portail national interopérable ; service IIIF360 d'accompagnement ; comptage des consultations IIIF prévu
lacunes:
- documentation Nakala et Huma-Num non lue
- 'Gallica : limites du service source non couvertes'
- iiif.biblissima.fr/collections refusé en passe 2
methode: 'WebSearch « Biblissima+ plateforme IIIF documentation API image limites requêtes » : présentations, aucun chiffre ; WebSearch « doc.biblissima.fr IIIF images limite requêtes serveur » : présentations de 2019 à 2025, aucun chiffre ; WebFetch doc.biblissima.fr/iiif/introduction-iiif : refusé (hors liste autorisée) ; Passe 2 (2026-11-13) : 1 WebSearch restreinte à biblissima.fr, 2 WebFetch lus (vademecum ; api-presentation), 1 WebFetch refusé (iiif.biblissima.fr/collections, non contourné).'
verifie_le: '2026-11-13'
sources:
- url: https://doc.biblissima.fr/iiif/introduction-iiif/
  note: (citée par le Ministère de la Culture et EMF ; refusée par l'outil)
  surveiller: false
- url: https://iiif.biblissima.fr/collections/
  note: (collections IIIF de manuscrits, page non lue)
  surveiller: false
- url: https://francearchives.gouv.fr/fr/article/705250527
  note: (article FranceArchives cité par la présentation, non lu)
  surveiller: false
- url: https://doc.biblissima.fr/vademecum-biblissima/
  note: 'Vademecum : aucun chiffre ; HTTPS et CORS exigés ; Change Discovery Level 1 recommandé ; clé non précisée'
  surveiller: true
- url: https://doc.biblissima.fr/api/api-presentation/
  note: 'API Présentation : aucun chiffre ; manifestes générés sans plafond annoncé ; images épigraphiques sur Nakala'
  surveiller: true
---

# Biblissima+ (plateforme IIIF)

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (documentation officielle doc.biblissima.fr non lisible)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Biblissima+ plateforme IIIF documentation API image limites requêtes » : présentations, aucun chiffre
- WebSearch « doc.biblissima.fr IIIF images limite requêtes serveur » : présentations de 2019 à 2025, aucun chiffre
- WebFetch doc.biblissima.fr/iiif/introduction-iiif : refusé (hors liste autorisée)

## Passe 2 (2026-11-13)
- WebFetch vademecum-biblissima : aucun chiffre ; HTTPS et CORS exigés sur manifestes et info.json ; Change Discovery Level 1 recommandé ; contact de l’équipe.
- WebFetch api/api-presentation : aucun chiffre ni clé ; manifestes par descripteur, par recherche iconographique et par inscriptions ; images épigraphiques servies par Nakala.
- WebFetch iiif.biblissima.fr/collections/ : refusé par l’outil (hors liste autorisée) en passe 2 ; non contourné.
- Gallica, source de nombreux manifestes : les limites de son propre service ne sont pas couvertes ici ; à traiter avec la fiche BnF.
