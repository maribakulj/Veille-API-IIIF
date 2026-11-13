---
id: GLAM-013
institution: National Library of Norway (NB)
pays: Norvège
statut: 'NON TROUVÉ APRÈS RECHERCHE (IIIF) : seule une API de vignettes, sans chiffre, est décrite'
classe: non trouvé après recherche
statut_quota: 'NON TROUVÉ APRÈS RECHERCHE : aucun seuil ni quota publié sur les pages lues ; clé d’API non précisée'
debit_iiif: Aucun débit IIIF trouvé. La page Swagger d’une API de vignettes (NB Image API 1.0.0) n’a livré que son titre à l’ouverture ; l’extrait de recherche la décrit sans chiffre ni clé. L’API de texte (api.nb.no) a été refusée par l’outil en passe 1 et n’a pas été réessayée. Une absence de chiffre ne signifie pas absence de limite.
iiif_image: 'Non documentée – endpoint cité seulement par un tutoriel tiers : nb.no/services/image/resolver/URN…/info.json (aucune doc officielle NB trouvée)'
iiif_presentation: 'Non documentée – manifest cité seulement par un tutoriel tiers : api.nb.no/catalog/v1/iiif/{id}/manifest'
lacunes:
- 'Swagger : contenu non lisible par l’outil'
- API de texte api.nb.no refusée en passe 1
- documentation IIIF nationale non trouvée
methode: 'WebSearch « Nasjonalbiblioteket API begrensning per minutt IIIF » : rien d''officiel ; WebSearch « IIIF API dokumentasjon bildeservice » restreint à nb.no : pages DH-lab, Swagger image, pas de limite ; WebFetch swagger image : aucune limite, aucun endpoint IIIF décrit ; WebFetch api.nb.no : refusé (hors liste autorisée) ; WebFetch dh-lab et digital-tekstanalyse : aucune limite ; WebSearch api.nb.no catalog v1 swagger : rien d''officiel lisible ; Passe 2 (2026-11-13) : 2 WebSearch (dont une restreinte à nb.no), 1 WebFetch (Swagger : titre seulement).'
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
- url: https://www.nb.no/forskning/digital-humaniora/
  note: 'Extrait de recherche : IIIF en cours pour tous les contenus numériques ; aucun chiffre'
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

## Passe 2 (2026-11-13)
- WebFetch Swagger : titre seulement ; l’extrait de recherche donne l’URL de base www.nb.no/services/image/resolver, une licence Creative Commons Public Domain et un contact développeur.
- Extrait nb.no « Digital humaniora » : IIIF en cours pour l’ensemble des contenus numériques ; API de texte NB Digital mentionnée, sans chiffre.
- Extrait nb.no « Hvem har tilgang » : accès par niveaux (libre, en bibliothèque, sous conditions) ; ce ne sont pas des débits.
- À reprendre avec une lecture complète de la documentation, non accessible à l’outil à cette passe.
