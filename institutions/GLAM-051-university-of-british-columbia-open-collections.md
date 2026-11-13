---
id: GLAM-051
institution: University of British Columbia – Open Collections
pays: Canada
statut: NON TROUVÉ APRÈS RECHERCHE (aucun chiffre de débit trouvé ; clé requise ; pages complètes non lues)
classe: non trouvé après recherche
statut_quota: 'NON TROUVÉ APRÈS RECHERCHE : aucun débit ni quota chiffré dans les extraits lus ; clé API requise'
debit_iiif: 'Aucun chiffre de débit IIIF trouvé. Un extrait de la documentation API d’Open Collections indique qu’une clé API est requise, valable pour les API REST, OAI-PMH et IIIF ; le wiki de la bibliothèque précise qu’une inscription par courriel est nécessaire pour l’obtenir. Le paramètre limit=10 des exemples REST est une pagination, non un débit. Un agrégateur tiers mentionne une rubrique « Rate Limits » sans contenu lisible : non retenu. La page complète n’a pas pu être lue, car la redirection vers open.library.ubc.ca est refusée par l’outil : non suivie.'
iiif_image: NON PRÉSENT SUR CETTE PAGE (page officielle lue = notice de blocage)
iiif_presentation: NON PRÉSENT SUR CETTE PAGE
api_recherche: Recherche API documentée (oc-index.library.ubc.ca/search/help) ; détails non lus
acces: 'Clés API : « Open Collections API Keys are valid for all three of our APIs » (doc officielle bchistory.library.ubc.ca/docs, extrait). Limites par clé NON PRÉSENTES dans l''extrait officiel'
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: 'Notice de blocage « requête bloquée … activité inhabituelle » sur la page officielle : anti-bot actif'
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: NON PRÉSENT SUR CETTE PAGE
strategie: Accès API limité sans clé ; seuil non publié
lacunes:
- page de documentation complète non lue (redirection refusée)
- chiffre de débit des API non trouvé
- rubrique « Rate Limits » du tiers non lisible
methode: 'WebSearch portée à l''institution (résultats non reconsultés) : documentation API officielle repérée, limitation sans nombre ; Passe 2 (2026-11-13) : 1 WebSearch (extrait de la documentation API) ; redirection vers open.library.ubc.ca refusée par l’outil.'
verifie_le: '2026-11-13'
sources:
- url: https://bchistory.library.ubc.ca/docs
  note: '(extrait lu : limitation non chiffrée)'
  surveiller: true
- url: https://open.library.ubc.ca/collections/bch
  note: 'Redirection de la documentation API refusée par l’outil (hors liste d’autorisation) : non lue'
  surveiller: false
---

# University of British Columbia – Open Collections

**Verdict** : DOC LUE, AUCUN CHIFFRE (limitation non chiffrée pour les utilisateurs non inscrits)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch portée à l'institution (résultats non reconsultés) : documentation API officielle repérée, limitation sans nombre

## Passe 2 (2026-11-13)
- WebSearch : extrait de la page API Documentation (bchistory) : clé requise pour les trois API ; aucun chiffre de débit.
- Wiki UBC : inscription par courriel pour obtenir une clé ; aucun débit précisé.
- La redirection vers open.library.ubc.ca n’a pas été suivie : URL refusée par l’outil.
