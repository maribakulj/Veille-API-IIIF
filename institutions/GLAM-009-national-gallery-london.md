---
id: GLAM-009
institution: National Gallery London
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE (service IIIF en cours de mise en œuvre)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni clé d’API sur les pages lues (aide, images, licences, API Elasticsearch)'
debit_iiif: Aucun seuil de débit publié sur les pages lues. Pour les images, la page indique le motif d’URL IIIF sur data.ng.ac.uk et que le service complet est encore en cours de mise en œuvre. Pour les données, l’API Elasticsearch publique n’annonce ni plafond de résultats ni limite de requêtes ; la clé ou la connexion n’y sont pas précisées. Les licences (CC0 pour les données structurées, CC BY 4.0 pour les textes, CC BY-NC-ND 4.0 pour les images) sont des règles d’usage, non des débits.
iiif_image: Mention « Image v3 documentée » dans le classeur ; non confirmé par les extraits lus
iiif_presentation: Manifestes IIIF via data.ng-london.org.uk (NG Beta API, ex-IIIF Presentation) ; version non confirmée
acces: Clé ou connexion non précisées sur l’API Elasticsearch ni sur les pages lues
moissonnage: Données structurées liées (Beta API)
droits: « information made available for re-use through our API under our terms and conditions » (page documentation/ngacuk)
conflits:
- 'Classeur : « serveur IIIF historique retiré » — non vérifié sur page officielle lue'
lacunes:
- conditions générales de réutilisation (texte intégral) non lues ; page licences lue
- pages d’identifiants pérennes et de formats interopérables non lues
- Beta API (data.ng-london.org.uk) non lue
methode: 'WebSearch « National Gallery London open access images API IIIF terms rate limit » : page d’aide officielle trouvée ; WebFetch page d’aide des API : aucun chiffre ; Passe 2 (2026-11-13) : 1 WebSearch, 4 WebFetch (aide ; collection-images ; licences ; API Elasticsearch).'
verifie_le: '2026-11-13'
sources:
- url: https://nationalgallery.org.uk/documentation/ngacuk/help
  note: ''
  surveiller: true
- url: https://research.ng-london.org.uk/projects/
  note: (contact Picture Library pour usage d’images, sans chiffre)
  surveiller: true
- url: https://www.nationalgallery.org.uk/documentation/ngacuk/collection-images
  note: 'Images : aucun chiffre ; motif d’URL IIIF ; service complet en cours ; licences renvoyées ailleurs'
  surveiller: true
- url: https://www.nationalgallery.org.uk/documentation/ngacuk/licences
  note: 'Licences : aucun chiffre ; CC0 pour les données, CC BY 4.0 pour les textes, CC BY-NC-ND 4.0 pour les images'
  surveiller: true
- url: https://www.nationalgallery.org.uk/documentation/ngacuk/collection-data/elasticsearch-api
  note: 'API Elasticsearch : aucun plafond ni limite de requêtes ; size 0 seulement dans un exemple ; clé non précisée'
  surveiller: true
---

# National Gallery London

**Verdict** : DOC LUE, AUCUN CHIFFRE

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « National Gallery London open access images API IIIF terms rate limit » : page d’aide officielle trouvée
- WebFetch page d’aide des API : aucun chiffre

## Passe 2 (2026-11-13)
- WebFetch ngacuk/help : aucun chiffre ; liens vers les pages de données, d’images et de licences ; pas de clé mentionnée.
- WebFetch collection-images : aucun chiffre ; motif d’URL IIIF sur data.ng.ac.uk ; la page dit que le service IIIF complet est en cours ; contact par courriel suggéré pour les limites.
- WebFetch licences : aucun chiffre ; pas d’autorisation ni de notification requise, mais une demande de courriel pour décrire l’usage des données.
- WebFetch collection-data/elasticsearch-api : aucun plafond publié ; requête en GET sur data.ng.ac.uk/es/public/_search ; clé ou connexion non précisées ; contact par courriel suggéré pour les limites.
- Non lu : les pages d’identifiants pérennes et de formats interopérables, liées depuis l’aide, ne sont pas ouvertes à cette passe.
