---
id: GLAM-051
institution: University of British Columbia – Open Collections
pays: Canada
statut: 'PARTIEL : règle sans chiffre (limitation sans clé documentée, sans nombre ; aucun débit IIIF chiffré trouvé ; doc complète open.library.ubc.ca/docs non lue : notice de blocage)'
classe: règle sans chiffre
statut_quota: 'PARTIEL : règle sans chiffre ; clé API valable pour les trois API, dont l''API IIIF selon la doc ; aucun nombre publié'
debit_iiif: 'Aucun débit IIIF chiffré trouvé. Règle officielle sans nombre : la documentation indique que les utilisateurs non inscrits sont limités en nombre de requêtes, et que la clé obtenue par courriel vaut pour les trois API, dont l''API IIIF (extrait de recherche de bchistory.library.ubc.ca/docs). L''hôte API indique aussi que les requêtes sans clé sont limitées, sans nombre (oc-index.library.ubc.ca/search/help, lue). Chiffre voisin, non IIIF : le widget de recherche avancée annonce 10 requêtes par minute sans clé (extrait de recherche, redirection refusée) ; ce n''est pas une limite de l''API IIIF et elle n''est pas retenue comme débit IIIF. Chiffres de tiers non officiels (API Evangelist : 10 requêtes par minute par IP sans clé, 200 avec clé) : non confirmés, non retenus. Le paramètre limit=10 des exemples REST est une pagination, non un débit. Relecture du 13/11/2026 : open.library.ubc.ca/docs renvoie une notice de blocage ; le dépôt GitHub de documentation et l''introduction UBC Research Commons, lus cette fois, ne donnent aucun chiffre.'
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
- aucun chiffre de débit pour l'API IIIF dans les pages officielles lues
- 'documentation complète non lue : open.library.ubc.ca/docs renvoie une notice de blocage anti-bot (relecture du 13/11/2026), non contournée'
- 'hub ubc-library.github.io lu : aucun chiffre, il renvoie vers open.library.ubc.ca/docs (bloquée) et vers le dépôt GitHub (lu sans chiffre le 13/11/2026)'
- 'dépôt GitHub de documentation lu le 13/11/2026 : aucun chiffre de débit'
- 'introduction UBC Research Commons lue le 13/11/2026 : aucun chiffre (page d''initiation aux API)'
- 'redirection bchistory.library.ubc.ca/docs vers open.library.ubc.ca/collections/bch : non suivie (cible déjà refusée par l''outil)'
- 'chiffres 10 par minute et 200 par minute : tiers, non confirmés par une source officielle'
methode: 'WebSearch portée à l''institution (résultats non reconsultés) : documentation API officielle repérée, limitation sans nombre ; Passe 2 (2026-11-13) : 1 WebSearch (extrait de la documentation API) ; redirection vers open.library.ubc.ca refusée par l’outil. ; Passe 2 (2026-11-13) : 1 WebFetch lu (oc-index.library.ubc.ca/search/help) ; hub ubc-library.github.io lu (aucun chiffre, liens vers la doc) ; 2 WebSearch supplémentaires (extraits officiels bchistory et wiki UBC) ; redirections bchistory vers open.library.ubc.ca refusées et non suivies ; open.library.ubc.ca/docs, github.com/ubc-library/docs-open-collections-api et ubc-library-rc.github.io refusés par l''outil, non contournés ; verdict passé de NON TROUVÉ à PARTIEL car une règle officielle existe sans chiffre ; relecture du 13/11/2026 (une tentative par URL) : open.library.ubc.ca/docs renvoie une notice de blocage ; github.com/ubc-library/docs-open-collections-api et ubc-library-rc.github.io/intro-api lus, sans chiffre ; bchistory.library.ubc.ca/docs redirigée (301) vers open.library.ubc.ca/collections/bch, non suivie ; aucun chiffre IIIF retenu, verdict PARTIEL maintenu.'
verifie_le: '2026-11-13'
sources:
- url: https://bchistory.library.ubc.ca/docs
  note: '(extrait lu : limitation non chiffrée ; relecture du 13/11/2026 : redirection 301 vers open.library.ubc.ca/collections/bch, non suivie)'
  surveiller: true
- url: https://open.library.ubc.ca/collections/bch
  note: 'Redirection de la documentation API refusée par l’outil (hors liste d’autorisation) : non lue'
  surveiller: false
- url: https://ubc-library.github.io
  note: '(lu : hub de documentation, aucun chiffre ; liens vers la doc API)'
  surveiller: true
- url: https://oc-index.library.ubc.ca/search/help
  note: '(lu : clé recommandée pour les requêtes ; limite sans clé non chiffrée)'
  surveiller: true
- url: https://wiki.ubc.ca/Library:Open_Collections
  note: '(extrait de recherche : inscription par courriel pour obtenir une clé ; aucun débit)'
  surveiller: true
- url: https://open.library.ubc.ca/docs
  note: 'Relecture du 13/11/2026 : notice de blocage anti-bot (« activité inhabituelle ») à la place de la documentation ; non contournée'
  surveiller: false
- url: https://github.com/ubc-library/docs-open-collections-api
  note: '(lu le 13/11/2026 : documentation du dépôt, aucun chiffre de débit ; refusée lors de la passe 2)'
  surveiller: true
- url: https://bchistory.library.ubc.ca/search/advanced
  note: 'Redirigée vers open.library.ubc.ca (refusée) : extrait de recherche seulement ; widget, non API'
  surveiller: false
- url: https://ubc-library-rc.github.io/intro-api
  note: '(lu le 13/11/2026 : page d''initiation aux API, aucun chiffre de débit ; refusée lors de la passe 2)'
  surveiller: true
---

# University of British Columbia – Open Collections

**Verdict** : PARTIEL, RÈGLE SANS CHIFFRE (limitation non chiffrée pour les utilisateurs non inscrits ; aucun débit IIIF trouvé après relecture du 13/11/2026)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch portée à l'institution (résultats non reconsultés) : documentation API officielle repérée, limitation sans nombre

## Passe 2 (2026-11-13)
- WebSearch : extrait de la page API Documentation (bchistory) : clé requise pour les trois API ; aucun chiffre de débit.
- Wiki UBC : inscription par courriel pour obtenir une clé ; aucun débit précisé.
- La redirection vers open.library.ubc.ca n’a pas été suivie : URL refusée par l’outil.
- Recherche du débit de l'API IIIF : aucun chiffre sur les pages officielles lues.
- Hub ubc-library.github.io lu : aucun chiffre ; renvoie vers open.library.ubc.ca/docs et vers le dépôt GitHub, tous deux refusés par l'outil.
- Widget de recherche avancée : 10 requêtes par minute sans clé (extrait de recherche, hors API IIIF).
- Verdict passé de NON TROUVÉ à PARTIEL : règle officielle documentée, sans nombre.
- Relecture du 13/11/2026 (une tentative par URL) : open.library.ubc.ca/docs renvoie une notice de blocage anti-bot, sans documentation ; non contournée.
- Dépôt github.com/ubc-library/docs-open-collections-api lu : aucun chiffre ni mention de débit IIIF.
- Introduction ubc-library-rc.github.io/intro-api lue : aucun chiffre ; page d'initiation aux API.
- bchistory.library.ubc.ca/docs : redirection 301 vers open.library.ubc.ca/collections/bch, non suivie (cible déjà refusée).
- Conclusion : aucun chiffre de débit IIIF publié trouvé ; verdict PARTIEL maintenu.
