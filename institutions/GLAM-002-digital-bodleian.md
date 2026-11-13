---
id: GLAM-002
institution: Digital Bodleian
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE (règle de contact seulement)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE (règle de contact seulement) ; '
debit_iiif: 'Aucun seuil de débit, quota ni clé d’API sur la page de documentation et les conditions d’utilisation lues. Règle annoncée : contacter l’équipe avant de moissonner « un nombre significatif » de manifestes ; mention de « server-imposed limits » sans valeur.'
iiif_image: v2.1 par défaut ; v3.0 via négociation de contenu (Accept)
iiif_presentation: v2.1 par défaut ; v3.0 via négociation de contenu ; 406 si ressource absente dans la version demandée
api_recherche: Non vérifié sur la page
change_discovery: Flux ActivityStreams annoncé (page /developer/data à lire)
acces: Aucune clé mentionnée pour les manifestes
moissonnage: Moissonnage autorisé pour indexation et agrégateurs ; contact support (digital-bodleian@bodleian.ox.ac.uk) ou e-mail dans User-Agent pour volume important ; réhébergement des images déconseillé
robots_waf: WAF et 429 NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE (crawlers mentionnés seulement pour doublons de collections)
droits: Aucune licence ni condition formelle sur la page
lacunes:
- page /developer/data non lue
- WAF/CDN
- limites éventuelles non publiées
methode: 'WebSearch « Bodleian IIIF image API rate limit requests per minute » : aucun résultat officiel ; WebSearch « Digital Bodleian IIIF terms of use API usage limits » → pages officielles ; WebFetch developer/iiif : aucune limite, règle de contact pour moissonnage ; WebFetch terms : aucun quota, droit de restriction générique'
verifie_le: '2026-11-13'
sources:
- url: https://digital.bodleian.ox.ac.uk/developer/iiif
  note: ''
  surveiller: true
- url: https://digital.bodleian.ox.ac.uk/terms/
  note: (aucun quota ; droit de restreindre l’accès, sans seuil)
  surveiller: true
---

# Digital Bodleian

**Verdict** : DOC LUE, AUCUN CHIFFRE (règle de contact seulement)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Bodleian IIIF image API rate limit requests per minute » : aucun résultat officiel
- WebSearch « Digital Bodleian IIIF terms of use API usage limits » → pages officielles
- WebFetch developer/iiif : aucune limite, règle de contact pour moissonnage
- WebFetch terms : aucun quota, droit de restriction générique
