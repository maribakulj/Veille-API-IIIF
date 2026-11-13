---
id: GLAM-016
institution: Ghent University Library (UGent)
pays: Belgique
statut: NON TROUVÉ APRÈS RECHERCHE (documentation officielle lib.ugent.be non lisible)
classe: non trouvé après recherche
statut_quota: NON TROUVÉ APRÈS RECHERCHE (documentation officielle lib.ugent.be non lisible) ; Documentation officielle non accessible dans cette session ; aucune preuve d'absence de limite
debit_iiif: 'Aucun débit, quota ni limite de requêtes trouvé. La page officielle du catalogue (lib.ugent.be/catalog), citée par un répertoire d''APIs tiers, n''a pas pu être lue : URL refusée par l''outil (hors liste autorisée). Sources lues : un document municipal de 2020 indique que l''implémentation IIIF de l''UGent suit Image API 2.1.1 (niveau 1) et Presentation API 2.1.1, sans limite ; la page de l''IIIF Consortium (2021) n''en mentionne pas. Aucun chiffre publié n''a été trouvé.'
iiif_image: Non vérifié sur doc officielle (présence IIIF attestée par source tierce meemoo)
iiif_presentation: Non vérifié
lacunes: Doc UGent à atteindre par recherche directe ; aucune trouvée à ce stade.
methode: 'WebSearch « lib.ugent.be IIIF presentation API documentation rate limit » : rien d''officiel ; WebFetch lib.ugent.be/catalog : refusé (hors liste autorisée) ; WebSearch néerlandais « documentatie API gebruiksvoorwaarden » : document municipal et pages tierces, aucune limite'
verifie_le: '2026-11-13'
sources:
- url: https://lib.ugent.be/catalog
  note: (cité par un répertoire tiers ; non lu, refusé)
  surveiller: false
- url: https://raadpleegomgeving.stad.gent/document/6229e033d197995af400738a
  note: '(document municipal 2020 : Image API 2.1.1 niveau 1 ; sans limite)'
  surveiller: true
- url: https://iiif.io/news/2021/07/14/ghent-joins-consortium
  note: (adhésion au consortium, sans chiffre)
  surveiller: true
- url: https://apis.io/providers/ghent/
  note: '(répertoire tiers : déclare des « Rate Limits » sans les lire ; non officiel)'
  surveiller: true
---

# Ghent University Library (UGent)

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (documentation officielle lib.ugent.be non lisible)

## Notes

Le classeur attribue à UGent une « API bibliographique 10 000 notices/export » : cette API est distincte de la bibliothèque IIIF

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « lib.ugent.be IIIF presentation API documentation rate limit » : rien d'officiel
- WebFetch lib.ugent.be/catalog : refusé (hors liste autorisée)
- WebSearch néerlandais « documentatie API gebruiksvoorwaarden » : document municipal et pages tierces, aucune limite
