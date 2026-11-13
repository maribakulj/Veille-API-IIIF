---
id: GLAM-013
institution: National Library of Norway (NB)
pays: Norvège
statut: NON TROUVÉ APRÈS RECHERCHE (documentation IIIF officielle api.nb.no non lisible)
classe: non trouvé après recherche
statut_quota: NON TROUVÉ APRÈS RECHERCHE (documentation IIIF officielle api.nb.no non lisible) ; Documentation IIIF officielle non accessible dans cette session ; aucune preuve d'absence de limite
debit_iiif: 'Aucun débit, quota ni limite de requêtes trouvé. La documentation officielle de l''API (api.nb.no) n''a pas pu être lue : l''outil de lecture a refusé l''URL (hors liste autorisée). Pages nb.no lues : la page Swagger de l''API Image (www.nb.no/services/image/swagger/api-doc.html) n''expose aucun endpoint décrit dans le texte lu et ne mentionne aucune limite ; la page DH-lab et la page de documentation dhlab ne mentionnent aucune limite (l''API DH-lab renvoie vers api.nb.no/dhlab/, sans règle chiffrée lue). Aucune page officielle IIIF sur les limites n''a été trouvée.'
iiif_image: 'Non documentée – endpoint cité seulement par un tutoriel tiers : nb.no/services/image/resolver/URN…/info.json (aucune doc officielle NB trouvée)'
iiif_presentation: 'Non documentée – manifest cité seulement par un tutoriel tiers : api.nb.no/catalog/v1/iiif/{id}/manifest'
lacunes: Aucune page officielle NB sur les limites de l’API ou du résolveur IIIF.
methode: 'WebSearch « Nasjonalbiblioteket API begrensning per minutt IIIF » : rien d''officiel ; WebSearch « IIIF API dokumentasjon bildeservice » restreint à nb.no : pages DH-lab, Swagger image, pas de limite ; WebFetch swagger image : aucune limite, aucun endpoint IIIF décrit ; WebFetch api.nb.no : refusé (hors liste autorisée) ; WebFetch dh-lab et digital-tekstanalyse : aucune limite ; WebSearch api.nb.no catalog v1 swagger : rien d''officiel lisible'
verifie_le: '2026-11-13'
sources:
- url: https://www.nb.no/dh-lab/digital-tekstanalyse/
  note: '(lue : aucune limite ; seule API décrite : DH-lab, non IIIF)'
  surveiller: true
- url: https://www.nb.no/services/image/swagger/api-doc.html
  note: '(lue : pas de texte d''endpoint IIIF, pas de limite)'
  surveiller: true
- url: https://digitalpreservation.no/docs/dps/api/
  note: (API de préservation, authentification par jeton, sans chiffre)
  surveiller: true
- url: https://oembed.org/providers/nasjonalbiblioteket
  note: (endpoint oEmbed api.nb.no/catalog/v1/oembed, sans limite)
  surveiller: true
- url: https://github.com/Antonio-Faure/mnemosyne/pull/49
  note: '(tiers, non officiel : décrit l''API catalogue comme « keyless », sans chiffre)'
  surveiller: true
---

# National Library of Norway (NB)

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (documentation IIIF officielle api.nb.no non lisible)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Nasjonalbiblioteket API begrensning per minutt IIIF » : rien d'officiel
- WebSearch « IIIF API dokumentasjon bildeservice » restreint à nb.no : pages DH-lab, Swagger image, pas de limite
- WebFetch swagger image : aucune limite, aucun endpoint IIIF décrit
- WebFetch api.nb.no : refusé (hors liste autorisée)
- WebFetch dh-lab et digital-tekstanalyse : aucune limite
- WebSearch api.nb.no catalog v1 swagger : rien d'officiel lisible
