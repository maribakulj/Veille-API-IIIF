---
id: GLAM-016
institution: Ghent University Library (UGent)
pays: Belgique
statut: 'NON TROUVÉ APRÈS RECHERCHE (IIIF) : aucune documentation IIIF ni chiffre trouvés sur les pages officielles'
classe: non trouvé après recherche
statut_quota: 'NON TROUVÉ APRÈS RECHERCHE : aucun seuil ni quota IIIF trouvé ; exports de catalogue libres (MARC XML, quotidiens)'
debit_iiif: Aucun débit IIIF trouvé. Les pages officielles trouvées traitent des exports de catalogue en MARC XML, quotidiens et sans limite chiffrée, et de l’API Biblio pour les publications de l’université (REST, hors IIIF, non lue). Une absence de chiffre ne signifie pas absence de limite.
iiif_image: Non vérifié sur doc officielle (présence IIIF attestée par source tierce meemoo)
iiif_presentation: Non vérifié
lacunes:
- aucune documentation IIIF officielle trouvée
- lib.ugent.be/catalog refusé en passe 1
- API Biblio non lue
methode: 'WebSearch « lib.ugent.be IIIF presentation API documentation rate limit » : rien d''officiel ; WebFetch lib.ugent.be/catalog : refusé (hors liste autorisée) ; WebSearch néerlandais « documentatie API gebruiksvoorwaarden » : document municipal et pages tierces, aucune limite ; Passe 2 (2026-11-13) : 1 WebSearch restreinte à ugent.be (résultats : bibliothèque, exports de données ; aucune documentation IIIF).'
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

## Passe 2 (2026-11-13)
- WebSearch ugent.be : aucune documentation IIIF ni chiffre ; pages de bibliothèque, données ouvertes et dépôts sans rapport avec un débit IIIF.
- Extrait lib.ugent.be (données ouvertes) : exports MARC XML quotidiens ; ce ne sont pas des API IIIF.
- API Biblio (publications, REST) : documentation signalée par extrait, non lue ; même si elle était chiffrée, elle ne serait pas un débit IIIF.
- Les pages iiif.io et apis.io citées en passe 1 : la seconde est un agrégateur tiers, non retenue.
