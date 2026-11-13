---
id: GLAM-011
institution: Europeana
pays: Pays-Bas / UE
statut: PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement) + CONFLIT entre pages officielles
classe: pas de débit IIIF chiffré
statut_quota: 'PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement) + CONFLIT entre pages officielles ; '
debit_iiif: 'Politique d’usage équitable : « reasonable limit », sans chiffre ; blocage possible de la clé. La FAQ officielle dit pouvoir interroger les API « as often as you like without any throttling » ; le même site dit l’inverse ailleurs (limite raisonnable possible). Un message officiel de l’équipe API (groupe Google) cite 120 requêtes par 10 secondes pour les « requêtes externes » : il vise l’API miniatures, pas IIIF. L’API IIIF ne demande pas de clé.'
iiif_image: Image API servie par les fournisseurs quand ils la proposent (non servie par Europeana elle-même)
iiif_presentation: 'Documentée – Presentation 2.1 et 3 : iiif.europeana.eu/presentation/{id}/manifest (manifests générés depuis EDM) ; Content Search v1'
api_recherche: Content Search v1 (doc IIIF Europeana)
change_discovery: Non relevé
acces: 'Pas de clé API pour l''API IIIF : « You don''t need an API key for this API! » (doc Europeana, extrait relu le 13/11/2026)'
moissonnage: 'Accès libre gratuit à toutes les APIs (FAQ Europeana) ; Search API : 100 résultats par réponse (classeur)'
droits: Droits des fournisseurs ; accès au manifeste n'implique pas accès aux images sources
strategie: 'Agrégateur : manifestes IIIF générés depuis EDM pour l''ensemble des fournisseurs'
lacunes:
- limite chiffrée Search API non relue sur page officielle
- politique WAF
methode: 'WebSearch « Europeana Search API Record API rate limit requests per second » : CGU, politique, groupe de discussion ; WebSearch « Europeana IIIF API usage limits » : FAQ et doc IIIF ; WebFetch politique d’usage équitable : aucun chiffre'
verifie_le: '2026-11-13'
sources:
- url: https://europeana.atlassian.net/wiki/spaces/EF/pages/2704146433
  note: (politique d’usage équitable, sans chiffre)
  surveiller: true
- url: https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417/API+FAQ
  note: (« query our APIs as often as you like without any throttling »)
  surveiller: true
- url: https://europeana.atlassian.net/wiki/spaces/EF/pages/1627914244/IIIF+APIs+Documentation
  note: (pas de clé pour l’IIIF)
  surveiller: true
- url: https://groups.google.com/g/europeanaAPI/c/dnjJBzWaQQU
  note: '(forum de l’équipe API : 120 req/10 s, API miniatures, non IIIF)'
  surveiller: true
---

# Europeana

**Verdict** : PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement) + CONFLIT entre pages officielles

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Europeana Search API Record API rate limit requests per second » : CGU, politique, groupe de discussion
- WebSearch « Europeana IIIF API usage limits » : FAQ et doc IIIF
- WebFetch politique d’usage équitable : aucun chiffre
