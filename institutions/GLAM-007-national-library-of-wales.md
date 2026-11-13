---
id: GLAM-007
institution: National Library of Wales
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE (aucune documentation API actuelle trouvée)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota sur la page lue ; redevances et licences pour les reproductions'
debit_iiif: 'Aucun seuil de débit IIIF publié sur la page de référence lue. Les pages du site de la bibliothèque trouvées traitent de licences et de redevances de reproduction, non de débit. Un wiki technique ancien du LLGC signale une réponse 401 sur certaines images protégées : c’est un contrôle d’accès, non un débit.'
iiif_image: Affirmation d’un atelier IIIF non officiel (toutes les collections en IIIF) ; à confirmer sur une page de la bibliothèque
iiif_presentation: Manifestes sur damsssl.llgc.org.uk/iiif/2.0/... ; présentation v2 ; passage à la v3 évoqué sans date, source non officielle
acces: Non relevé
moissonnage: Recommandation https obligatoire pour réutilisation (atelier non officiel)
lacunes:
- page IIIF officielle de la bibliothèque non trouvée par recherche
- robots.txt non lu
- "affirmations « atelier » : source non officielle, à remplacer par une page de la bibliothèque"
methode: 'WebSearch « NLW IIIF API rate limit terms of use » : rien d’officiel ; WebSearch en gallois « cyfyngiad cyfradd » : documents sans rapport ; WebFetch gwybodaethsyllwr.llgc.org.uk : aucune limite ; Passe 2 (2026-11-13) : 2 WebSearch (domaines library.wales et llgc.org.uk), 1 WebFetch. Aucune documentation Image API ou Presentation API officielle et actuelle trouvée.'
verifie_le: '2026-11-13'
sources:
- url: https://gwybodaethsyllwr.llgc.org.uk/index.php?lang=en
  note: ''
  surveiller: true
- url: https://www.library.wales/fileadmin/docs_gwefan/new_structure/visit/things_to_do/reading_at_nlw/Terms_and_Conditions_of_Use_April_2026.pdf
  note: (conditions de lecture, sans API ; non relu en détail)
  surveiller: true
- url: https://www.library.wales/commercial-services/media/licensing
  note: 'Extrait de recherche seulement : licences et redevances pour reproductions ; pas de limite technique'
  surveiller: true
---

# National Library of Wales

**Verdict** : DOC LUE, AUCUN CHIFFRE

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « NLW IIIF API rate limit terms of use » : rien d’officiel
- WebSearch en gallois « cyfyngiad cyfradd » : documents sans rapport
- WebFetch gwybodaethsyllwr.llgc.org.uk : aucune limite

## Passe 2 (2026-11-13)
- WebFetch gwybodaethsyllwr : aucun chiffre, aucune clé mentionnée ; un modèle d’URL d’image est montré ; deux outils IIIF tiers, sans documentation.
- WebSearch (domaines NLW) : aucune documentation Image ou Presentation API actuelle trouvée.
- Wiki technique dev.llgc.org.uk (ancien) : décrit l’Image API 2.0 et une réponse 401 sur des images protégées ; non retenu comme source faute de datation.
- Licences : redevance et conditions d’accord pour certaines reproductions ; aucun seuil technique.
