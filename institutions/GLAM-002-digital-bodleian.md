---
id: GLAM-002
institution: Digital Bodleian
pays: Royaume-Uni
statut: DOC LUE, AUCUN CHIFFRE (règle de contact seulement)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil de requêtes, quota ni clé d’API sur les pages lues ; règle de contact pour moissonnage volumineux'
debit_iiif: 'Aucun seuil de débit IIIF, quota ni clé d’API publié sur les pages lues (developer/iiif, developer/data, faq) ni sur les conditions d’utilisation liées. Règle de contact pour moissonner un nombre significatif de manifestes, sans seuil. Les valeurs rows (20, 40, 100) sont une taille de page, et les réglages maxWidth, maxHeight, maxArea de l’Image API ne sont pas chiffrés : ni l’un ni l’autre n’est un débit.'
iiif_image: v2.1 par défaut ; v3.0 via négociation de contenu (Accept)
iiif_presentation: v2.1 par défaut ; v3.0 via négociation de contenu ; 406 si ressource absente dans la version demandée
api_recherche: "API de données publique (developer/data) : recherche et collections, taille de page 20, 40 ou 100 ; aucun débit publié"
change_discovery: Flux ActivityStreams annoncé par la FAQ (iiif.bodleian.ox.ac.uk/iiif/activity/all-changes), non ouvert
acces: Aucune clé mentionnée pour les manifestes
moissonnage: Moissonnage autorisé pour indexation et agrégateurs ; contact support (digital-bodleian@bodleian.ox.ac.uk) ou e-mail dans User-Agent pour volume important ; réhébergement des images déconseillé
robots_waf: WAF et 429 NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE (crawlers mentionnés seulement pour doublons de collections)
droits: Aucune licence ni condition formelle sur la page
lacunes:
- WAF/CDN
- limites éventuelles non publiées
- "conditions d’utilisation : lues en passe 1 seulement, à relire"
- "flux ActivityStreams : annoncé par la FAQ, non ouvert"
methode: 'WebSearch « Bodleian IIIF image API rate limit requests per minute » : aucun résultat officiel ; WebSearch « Digital Bodleian IIIF terms of use API usage limits » → pages officielles ; WebFetch developer/iiif : aucune limite, règle de contact pour moissonnage ; WebFetch terms : aucun quota, droit de restriction générique ; Passe 2 (2026-11-13) : 1 WebSearch, 3 WebFetch (developer/iiif, developer/data, faq). La page faq renvoie vers les conditions d’utilisation, lues en passe 1 seulement.'
verifie_le: '2026-11-13'
sources:
- url: https://digital.bodleian.ox.ac.uk/developer/iiif
  note: ''
  surveiller: true
- url: https://digital.bodleian.ox.ac.uk/terms/
  note: (aucun quota ; droit de restreindre l’accès, sans seuil)
  surveiller: true
- url: https://digital.bodleian.ox.ac.uk/developer/data/
  note: 'API de données publique : aucun chiffre ; endpoints compte soumis à authentification (401)'
  surveiller: true
- url: https://digital.bodleian.ox.ac.uk/faq
  note: Aucun seuil ; liens vers IIIF, flux d’activité et téléchargements sans quota annoncé
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

## Passe 2 (2026-11-13)
- WebFetch developer/iiif : aucune limite publiée ; règle de contact pour moissonnage volumineux.
- WebFetch developer/data : aucun débit ; rows (20, 40, 100) = taille de page ; endpoints compte renvoient 401 sans authentification ; pas de clé mentionnée pour les endpoints publics.
- WebFetch faq : aucun débit, quota ni seuil de moissonnage ; pas d’export OAI-PMH, mais collections IIIF et flux d’activité publiés ; licence CC BY-NC 4.0 pour la plupart des contenus.
- À reconfirmer : la mention de limites imposées par le serveur, relevée en passe 1, n’apparaît pas dans les extraits relus en passe 2.
- Lectures par WebFetch : résumés de l’outil, à reconfirmer mot à mot avant publication.
