---
id: GLAM-082
institution: State Library Victoria
pays: Australie
statut: DOC LUE, AUCUN CHIFFRE (tutoriel IIIF officiel lu ; accès anonyme suggéré mais non confirmé)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni throttling ; clé non précisée'
debit_iiif: Aucun chiffre de limite de requêtes, de débit ni de quota sur le tutoriel IIIF de la bibliothèque. Les nombres présents (taille d’un PDF, dimensions d’une image de 7 000 × 5 257 px, « centaines de milliers » d’images) ne sont pas des limites d’accès. Le code d’exemple appelle manifestes et images sans identifiants, ce qui suggère un accès anonyme, sans que la page le confirme. Le service d’images déclare Image API 2, niveau 1. Les conditions d’utilisation liées ne sont pas lues.
iiif_image: Serveur IIIF d'images ; URL d'image construites à partir d'un identifiant Handle (tutoriel SLV LAB, avril 2025) ; version non précisée
iiif_presentation: 'Manifestes Presentation 2.1 : rosetta.slv.vic.gov.au/delivery/iiif/presentation/2.1/{id}/manifest (tutoriel SLV LAB, avril 2025)'
api_recherche: NON PRÉSENT SUR CETTE PAGE
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: Mention « This work is out of copyright » dans les manifestes d'exemple ; ressources du LAB en accès libre
strategie: IIIF comme mode de livraison de toutes les images numérisées ; URL de manifeste non exposées dans l'interface, constructibles
lacunes:
- conditions d’utilisation liées (rosetta.slv.vic.gov.au) non lues
- clé ou accès anonyme non confirmés
- aucune documentation SLV propre à l’API
methode: 'WebSearch « State Library Victoria IIIF API rate limit terms » : tutoriel SLV sans seuil ; limites d''autres institutions écartées ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (tutoriel IIIF).'
verifie_le: '2026-11-13'
sources:
- url: https://slvlab-prod.coolify.slv.vic.gov.au/resources/using-iiif-to-work-with-the-librarys-digitised-collections
  note: '(tutoriel SLV LAB, extrait : pas de chiffre)'
  surveiller: true
---

# State Library Victoria

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (aucune doc officielle de quota)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « State Library Victoria IIIF API rate limit terms » : tutoriel SLV sans seuil ; limites d'autres institutions écartées

## Passe 2 (2026-11-13)
- WebFetch tutoriel IIIF : aucun seuil ni quota ; accès anonyme suggéré par le code d’exemple, non confirmé ; conditions liées non lues.
