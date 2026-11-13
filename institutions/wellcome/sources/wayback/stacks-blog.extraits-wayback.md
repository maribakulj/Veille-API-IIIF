# Wellcome Collection — blog « Stacks » : extraits verbatim (copies Wayback)

- **Raison** : `stacks.wellcomecollection.org` (Medium) renvoie 403 à notre sonde et à l'outil de lecture. Les billets sont lus dans la Wayback Machine, sans envoyer de trafic à Wellcome. Le téléchargement par `curl` de copies Wayback est refusé par le système : les extraits sont recopiés à la main, vérifiables via les URL de réplique.
- **Lues le** : 2026-11-13 (texte intégral lu avec `ia_get_snapshot`).

## 1. « Crawlers, floods and fleets: a year of keeping our digital collections open » (Robert Kenny, ingénieur principal de Wellcome Collection)

- **Publié** : 2026-10-16 · **Capture** : 2026-11-04 05:37:57 UTC (20261104053757) · 19 622 caractères
- **Réplique** : https://web.archive.org/web/20261104053757/https://stacks.wellcomecollection.org/crawlers-floods-and-fleets-a-year-of-keeping-our-digital-collections-open-10af777199c4

> We publish that same material in machine-readable form through a public catalogue API and through IIIF […]. Anyone who wants to work with our collections at scale has a route built for them.

> The IIIF API is meant to be read by scripts, and it has to work when our images are embedded in someone else's page or opened in a viewer we do not control, where nobody can answer a challenge, so the techniques we used on our search pages would have broken it. **Instead, we set budgets: a fixed number of requests a minute for a given harvester or network however many addresses it used.** The supplier of our IIIF API added a per-address limit on full-size images (the most expensive requests to serve) and helped us set it high enough that a university library, whose readers reach us from one address, would not be caught.

> Many of the scripts in our logs identify themselves with a project name or contact details. We left those alone where their rate was one we could serve and gave them a budget where it was not. **Our principle is that a bulk user who tells us who they are gets the benefit of the doubt**, which we do not extend to a fleet presenting itself as ten thousand people.

> One harvester spread itself across a few thousand addresses rented from a cloud provider and downloaded 6 terabytes of PDFs in a fortnight. […] On the IIIF API behind those pages, requests roughly doubled, from around 9 million a day to between 17 and 20 million.

> **Our developer documentation already points anyone who wants the whole catalogue to the daily snapshot rather than the API, whether they are a PhD student or a large company: say who you are in your user agent, read robots.txt, spread your requests over time and use our API.**

> We backed it up with rate limits at our content delivery network (CDN). […] rewriting our robots.txt, asking crawlers who gathered training data for AI models to stay away, while still welcoming the ones that are used by AI assistants.

> We added a JavaScript challenge in front of the search pages. […] The AI agents our robots.txt welcomes and the services that build link previews are therefore turned away too.

## 2. « Ten years and counting: Wellcome Collection and IIIF » (Jonathan Cates)

- **Publié** : 2026-10-09 · **Capture** : 2026-10-18 08:27:35 UTC (20261018082735) · 13 122 caractères
- **Réplique** : https://web.archive.org/web/20261018082735/https://stacks.wellcomecollection.org/ten-years-and-counting-wellcome-collection-and-iiif-9015cdcdefd8

> This summer a fleet of automated browsers roughly doubled the traffic to our IIIF services. IIIF is designed to be read by software, and we want it to stay that way, but performance, resilience and cost will matter as much in the next ten years as openness did in the last.

> Today our catalogue describes more than 1.1 million works, and 361,783 of them have a IIIF manifest. […] Every manifest is available in both version 2 and version 3 of the Presentation API, and anyone can use them.
