# Recherches web — yale-peabody-museum — 2026-11-14

Requêtes (WebSearch, mode standard) :
1. institution : « Yale LUX Peabody API bots crawlers scraping policy Yale collections data access harvesting » + « collections.peabody.yale.edu terms of use images policy API data download specimens » : conditions d'utilisation du Peabody (peabody.yale.edu/about/terms-of-use, lues en entier : fair use, téléchargement pour usage personnel ou éducatif, aucune règle de débit) ; aucune politique de bots ou d'API trouvée.
2. utilisateurs : « manifests.collections.yale.edu OR lux.collections.yale.edu OR images.collections.yale.edu 429 OR 503 OR "rate limit" OR blocked » : aucun rapport de 429, 503 ou blocage (résultats : pages de manifestes, LoC, autres services).
3. tickets : « github issue "collections.yale.edu" OR "peabody.yale.edu" IIIF manifest harvester OR importer OR connector » : aucun ticket mentionnant les serveurs Yale ; seul voisin : sul-dlss/dlme-airflow (issue « Write csv configs for Yale collections », résumé de moteur, non lu, non vérifié).
4. presentations : « Yale LUX linked open usable data presentation Sanderson Peabody museum collections IIIF Linked Art API infrastructure ».

## Originaux lus
- https://ar5iv.labs.arxiv.org/html/2309.16635 (2023, arXiv:2309.16635, « Analysis of the Usability of Automatically Enriched Cultural Heritage Data », tiers) : cite le Yale Peabody Museum (YPM) ; aucun mot sur limite de débit, bots ou politique d'API publique.
- https://training.iiif.io/advanced_iiif/basics/finding_yale.html (formation IIIF, tiers) : gabarit des manifestes Yale `manifests.collections.yale.edu/{unité}/…`, version v2 par `/v2/` ; seule restriction citée : certains objets de la Yale Library limités au campus ; aucune limite de débit.
- https://guides.iiif.io/guides/collections.peabody.yale.edu/ (guide IIIF du Peabody, tiers) : renvoie à peabody.yale.edu/explore/collections ; aucun URL de manifeste.
- https://news.yale.edu/2025/02/24/breaking-digital-silos-share-cultural-heritage-collections (Yale News, présentation de l'institution mère, lue via WebFetch) : Linked Art et API ; aucune limite, aucun bot.
- GitHub project-lux (lux-middletier docs/api-endpoints.md ; lux-marklogic docs/lux-backend-api-usage.md) : endpoints de l'API de LUX ; aucune limite de débit.

## Résumés de moteur seuls (non vérifiés)
- CNI 2022 « LUX » (Sanderson) : PDF en 403 à WebFetch ; un résultat de moteur indique que le Peabody commençait à utiliser les données et l'infrastructure de LUX (résumé de moteur, non vérifié).
- Avis de 2017 de la Yale University Library sur les limites de téléchargement des ressources sous licence : ne concerne pas les API de LUX ou du Peabody (résumé de moteur, non vérifié).
