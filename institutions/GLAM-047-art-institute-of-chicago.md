---
id: GLAM-047
institution: Art Institute of Chicago
pays: États-Unis
statut: PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement)
classe: pas de débit IIIF chiffré
statut_quota: PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement) ; Documentation officielle lue en extrait (accès anonyme, 60 req/min) ; service IIIF non chiffré dans la page lue
debit_iiif: 'La documentation officielle de l''API (api.artic.edu/docs, extrait lu) limite les utilisateurs anonymes à 60 requêtes par minute. Ce chiffre concerne l''API REST des œuvres ; aucun seuil distinct n''est publié pour le service d''images IIIF dans la page lue. Une source tierce mentionne une demande de politesse (une requête par seconde) : non retenue comme chiffre officiel.'
iiif_image: 'IIIF Image API : base https://www.artic.edu/iiif/2 (copie tierce de l''OpenAPI, spécification citée 2.0)'
iiif_presentation: NON VÉRIFIÉ sur doc officielle
acces: '« You may access our API without authentication. » ; en-tête AIC-User-Agent recommandé ; clé : NON PRÉSENT SUR CETTE PAGE'
moissonnage: 'Dumps de données mis à jour chaque nuit (doc officielle, extrait) ; pour le scraping : « please throttle your requests to no more than one per second »'
robots_waf: NON VÉRIFIÉ
droits: 'Données générales CC0 1.0 ; descriptions CC BY 4.0 ; images : usage recommandé pour les œuvres marquées domaine public'
lacunes: Relire api.artic.edu/docs ; vérifier si les images IIIF ont un quota propre.
methode: 'WebSearch « Art Institute of Chicago api.artic.edu docs rate limit IIIF » (domaines api.artic.edu, artic.edu, github.com) : doc officielle lue en extrait, 60 req/min ; dépôts tiers écartés pour le chiffre'
verifie_le: '2026-11-13'
sources:
- url: https://api.artic.edu/docs/
  note: '(extrait lu : 60 requêtes par minute pour les utilisateurs anonymes)'
  surveiller: true
- url: http://aggregator-data.artic.edu/docs/
  note: (même documentation, version de l'agrégateur, 60 req/min)
  surveiller: true
---

# Art Institute of Chicago

**Verdict** : PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Art Institute of Chicago api.artic.edu docs rate limit IIIF » (domaines api.artic.edu, artic.edu, github.com) : doc officielle lue en extrait, 60 req/min ; dépôts tiers écartés pour le chiffre
