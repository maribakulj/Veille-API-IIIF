---
id: GLAM-014
institution: National Library of Finland – Finna
pays: Finlande
statut: DOC LUE, AUCUN CHIFFRE (api.finna.fi libre, IIIF non mentionné)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni clé d’API sur la page lue ; accès gratuit déclaré'
debit_iiif: 'Aucun seuil de débit publié. La page présente l’interface api.finna.fi comme gratuite ; les photos et autres documents liés peuvent avoir des restrictions de droits, non détaillées. Les conditions interdisent les méthodes automatisées pour les fonctions qui exigent une connexion : règle d’usage, non un débit. IIIF non mentionné.'
iiif_image: Non vérifié sur doc officielle
acces: Clé API personnelle requise pour le script de téléchargement d'images (annonce, mise en service automne 2025)
moissonnage: Script Node.js de téléchargement d'images en masse via clé API, conçu pour éviter le limiteur de débit (rapport WP 3.2, 04/06/2025)
lacunes:
- documentation technique de api.finna.fi non trouvée sur les pages du domaine
- droits des documents liés non détaillés
methode: 'WebSearch « Finna API documentation rate limit requests api.finna.fi » : rien d''officiel chiffré ; WebSearch « Finna IIIF image API kansalliskirjasto usage limits terms » : projet IIIF et téléchargeur, sans chiffre ; WebFetch kiwi.fi documentation Finna : refusé (hors liste autorisée) ; WebSearch « Finna API Documentation In English kiwi » : résultats tiers uniquement ; WebFetch GitHub NatLibFi/Finna-API-image-file-downloader : refusé (hors liste autorisée) ; Passe 2 (2026-11-13) : 1 WebFetch (moreabout_finna), 1 WebSearch restreinte à finna.fi (conditions : extrait).'
verifie_le: '2026-11-13'
sources:
- url: https://finna.fi/Content/moreabout_finna?lng=en-gb
  note: (service gratuit, sans chiffre)
  surveiller: true
- url: https://www.kielipankki.fi/?p=33141
  note: '(projet officiel : téléchargeur d''images, clé d''API requise, sans seuil)'
  surveiller: true
- url: https://iiif.io/news/2025/04/07/Finland/
  note: (annonce IIIF de la Bibliothèque nationale, sans chiffre)
  surveiller: true
- url: https://www.finna.fi/Content/terms?lng=en-gb
  note: 'Extrait de recherche : automates interdits pour les fonctions avec connexion ; restriction d’accès sans seuil'
  surveiller: true
---

# National Library of Finland – Finna

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (documentation API officielle non lisible)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Finna API documentation rate limit requests api.finna.fi » : rien d'officiel chiffré
- WebSearch « Finna IIIF image API kansalliskirjasto usage limits terms » : projet IIIF et téléchargeur, sans chiffre
- WebFetch kiwi.fi documentation Finna : refusé (hors liste autorisée)
- WebSearch « Finna API Documentation In English kiwi » : résultats tiers uniquement
- WebFetch GitHub NatLibFi/Finna-API-image-file-downloader : refusé (hors liste autorisée)

## Passe 2 (2026-11-13)
- WebFetch moreabout_finna : aucun chiffre ; api.finna.fi décrite comme gratuite ; pas de clé mentionnée ; IIIF non mentionné ; aucun lien de documentation API.
- Extrait finna.fi/Content/terms : interdiction des automates pour les fonctions avec connexion ; droit de restreindre l’accès, sans seuil chiffré.
- Documentation technique de l’API non trouvée sur les pages du domaine : à rechercher à la prochaine passe.
