---
id: GLAM-014
institution: National Library of Finland – Finna
pays: Finlande
statut: NON TROUVÉ APRÈS RECHERCHE (documentation API officielle non lisible)
classe: non trouvé après recherche
statut_quota: NON TROUVÉ APRÈS RECHERCHE (documentation API officielle non lisible) ; Documentation technique officielle non accessible dans cette session ; aucune preuve d'absence de limite
debit_iiif: 'Aucun débit, quota ni nombre de requêtes trouvé. La documentation officielle de l''API (kiwi.fi, api.finna.fi/Documentation) n''a pas pu être lue : URL refusée par l''outil (hors liste autorisée). Page officielle lue en résultat de recherche : le service d''API Finna est décrit comme un accès ouvert gratuit, sans chiffre. Projet officiel de téléchargement d''images (Kielipankki, dépôt NatLibFi) : le script exige une clé d''API personnelle ; aucun seuil n''est cité dans le résumé lu. Le classeur indiquait « Pas de débit IIIF chiffré » : non contredit, non confirmé.'
iiif_image: Non vérifié sur doc officielle
acces: Clé API personnelle requise pour le script de téléchargement d'images (annonce, mise en service automne 2025)
moissonnage: Script Node.js de téléchargement d'images en masse via clé API, conçu pour éviter le limiteur de débit (rapport WP 3.2, 04/06/2025)
lacunes:
- doc Finna API in English non lue
- statut de la clé API en 2026
methode: 'WebSearch « Finna API documentation rate limit requests api.finna.fi » : rien d''officiel chiffré ; WebSearch « Finna IIIF image API kansalliskirjasto usage limits terms » : projet IIIF et téléchargeur, sans chiffre ; WebFetch kiwi.fi documentation Finna : refusé (hors liste autorisée) ; WebSearch « Finna API Documentation In English kiwi » : résultats tiers uniquement ; WebFetch GitHub NatLibFi/Finna-API-image-file-downloader : refusé (hors liste autorisée)'
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
