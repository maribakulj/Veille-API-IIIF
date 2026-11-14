# Répliques Wayback (lues via le MCP internet-archive, 2026-11-14)

Pourquoi : www.dri.ie et repository.dri.ie répondent par un défi Cloudflare (« Just a moment... », HTTP 403) dès la 1re requête (robots.txt, 2026-11-14T03:40Z). On ne contourne pas ; les pages sont lues dans le Wayback.

## robots.txt de repository.dri.ie
Réplique : https://web.archive.org/web/20250714090310/https://repository.dri.ie/robots.txt
Extrait verbatim (intégral) :
```
# See http://www.robotstxt.org/wc/norobots.html for documentation on how to use the robots.txt file
#
# To ban all spiders from the entire site uncomment the next two lines:
# User-Agent: *
# Disallow: /
```
=> aucune règle active, aucun Crawl-delay.

## robots.txt de dri.ie
Réplique : https://web.archive.org/web/20260102134912/https://dri.ie/robots.txt
Extrait verbatim (intégral) :
```
User-agent: *
Disallow: /?s=
Disallow: /search/
Sitemap: /sitemap_index.xml
```
=> pas de Crawl-delay.

## Page d'accueil repository.dri.ie (capture 2016-09-22, ancienne)
Réplique : https://web.archive.org/web/20160922135604/https://repository.dri.ie/
Extrait : « The Digital Repository of Ireland End User Agreement. [...] You agree not to use this site for any illegal or unlawful purpose. [...] Any breach of this End User Agreement will lead to the immediate and automatic termination without notice of your access to the services » ; aucun quota ni limite de débit mentionné.

## Standards Adoption (dri.ie/standards-adoption/, capture 2025-08-20)
Réplique : https://web.archive.org/web/20250820132742/https://dri.ie/standards-adoption/
Extraits verbatim : « We also use the International Image Interoperability Framework (IIIF) to make our images interoperable with other IIIF platforms and tools. We support export of data in the BagIt format, as well as providing an OAI-PMH feed for our metadata in Dublin Core and the Europeana Data Model (EDM). Metadata and data can also be accessed via a standards-compliant Application Programming Interface (API). » ; aucune limite de débit mentionnée.

## About us (dri.ie/about-us/, capture 2023-12-15)
Réplique : https://web.archive.org/web/20231215060154/https://dri.ie/about-us/
Extrait : « DRI operates on a Membership Model. » ; pied de page : Privacy Policy, Site Map, Licensing Statement, Accessibility, FAQs ; contact dri@ria.ie. Aucune mention de quota.

## https://repository.dri.ie/api-docs (page « API Documentation » citée par le dépôt dri-documentation)
Aucune capture dans le Wayback (ia_find_snapshots, historique vide, avec et sans barre finale). Non lisible : listée dans a_verifier_manuellement.
