# Recherches web — vatican — 2026-11-14

Requêtes (WebSearch, mode standard) :
1. institution : « Vatican Library DigiVatLib IIIF API terms of use bots harvesting policy »
2. utilisateurs : « digi.vatlib.it iiif 403 OR 429 OR 503 blocked download manifest problem »
3. tickets : « github issue digi.vatlib.it iiif manifest harvesting Vatican Library »
4. presentations : « Vatican Library digital library IIIF presentation conference DigiVatLib infrastructure Mellon Stanford Thematic Pathways »

## Originaux lus (WebFetch, sites de tiers)
- https://groups.google.com/g/iiif-discuss/c/Fc1epNUG1N0 (20/09/2016, utilisateur) : « I'm getting a 403 forbidden response for image requests to the digital vatican server. » ; réponse : soupçon d'un blocage par en-tête Referer, « This is all speculative, though. » ; autre cause avancée : bloqueur de publicités (URL contenant « AD_ », « Blocked by Client ») ; identifiants de service d'image changeant d'un jour à l'autre. Aucune mention de limite de débit.
- https://digitalia.cultura.gov.it/article/download/2632/1840/14641 : Paola Manoni (Responsable du Coordinamento dei Servizi Informatici de la BAV), « L'adozione del IIIF nell'ecosistema digitale della Biblioteca Apostolica Vaticana », DigItalia 2-2020, DOI 10.36181/digitalia-00017 (institution). Lu en texte (pdftotext, extrait dans digitalia-2020-manoni-extrait-pdftotext.txt) : aucune occurrence de rate, limit, quota, bot, crawl, download, traffic.
- https://parisbible.github.io/2022-10-31-bible-hunting-Italy (31/10/2022, tiers) : digi.vatlib.it permet d'« obtain a IIIF manifest » ; « Generally, the rights are reserved for the Vatican Apostolic Library and a watermark is applied to the images downloaded. » Aucune limite de débit.

## Résumés de moteur seuls (non vérifiés)
- Presse 2020 « Vatican enlists bots to protect library from hackers » : sécurité informatique, pas politique de moissonnage (résumé de moteur, non vérifié).
- Programme de la conférence IIIF 2017 au Vatican (sched.com) : trouvé dans les résultats, non lu.

## Catégorie tickets
Aucun ticket GitHub/GitLab d'outil tiers mentionnant digi.vatlib.it trouvé par la recherche (la recherche renvoie un fil de liste, des articles et le dépôt sul-dlss/dlme-airflow sans rapport avec le Vatican). Dans la fiche antérieure : PR Antonio-Faure/mnemosyne#40 (« no enumerable IIIF Collection and no JSON search endpoint », « keyless »), non relue cette fois.
