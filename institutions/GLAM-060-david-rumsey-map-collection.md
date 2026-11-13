---
id: GLAM-060
institution: David Rumsey Map Collection
pays: États-Unis
statut: DOC LUE, AUCUN CHIFFRE (documentation API LUNA lue ; générique, non spécifique à David Rumsey)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucune limite de requêtes ; OAuth 1.0 pour la Record Data API ; pas d’authentification montrée pour la Viewer API'
debit_iiif: 'Aucun chiffre de débit ni de quota sur la documentation API LUNA lue. Les seuls nombres sont des tailles de page par défaut (50 pour la Record Data API, 10 pour la Viewer API) : pagination, non débit. Une règle sur le paramètre fullData (réservé aux enregistrements individuels ou à un décalage inférieur à 5) restreint un usage, sans être une limite de débit. La Record Data API exige l’inscription d’une application en OAuth 1.0. Les limites IIIF propres à David Rumsey ne sont pas décrites ; la page IIIF v1 liée n’a pas été lue.'
iiif_image: 'Présence IIIF confirmée par la liste IIIF (guides.iiif.io) ; service non décrit sur une page officielle lue. Exemple tiers : davidrumsey.com/luna/servlet/iiif/{id}'
iiif_presentation: 'Manifeste : davidrumsey.com/luna/servlet/iiif/m/{id}/manifest (exemple tiers parse.bot) ; version non précisée'
api_recherche: API LUNA Viewer v1 et v2 (documentation LUNA, non IIIF) ; API de recherche IIIF non documentée sur page officielle lue
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: Métadonnées de plus de 38 000 cartes fournies à la DPLA (communiqué DPLA, 2013) ; état actuel non vérifié
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: 'FAQ : lecture et respect des restrictions de copyright demandés (davidrumsey.com/help/faq)'
strategie: Interface LUNA, partenariat DPLA, IIIF présent mais partiel selon une source tierce (archivarix)
lacunes:
- documentation IIIF v1 liée non lue
- limites IIIF propres à David Rumsey non décrites
- documentation spécifique à David Rumsey absente
methode: 'WebSearch « David Rumsey Map Collection IIIF API rate limit terms » : revendeur tiers écarté, LUNA générique sans seuil ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (documentation API LUNA).'
verifie_le: '2026-11-13'
sources:
- url: https://lunaimaging.atlassian.net/wiki/spaces/V75D/pages/655863/LUNA+API+Documentation
  note: '(documentation générique LUNA, extrait : pas de seuil)'
  surveiller: true
---

# David Rumsey Map Collection

**Verdict** : NON TROUVÉ APRÈS RECHERCHE (aucune doc officielle de quota)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « David Rumsey Map Collection IIIF API rate limit terms » : revendeur tiers écarté, LUNA générique sans seuil

## Passe 2 (2026-11-13)
- WebFetch documentation LUNA : aucun seuil ni quota ; pagination par défaut (50, 10) non assimilée à un débit ; OAuth 1.0 pour la Record Data API.
