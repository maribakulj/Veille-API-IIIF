# Radboud University Library (GLAM-074)

## Sources
- Page « Browsing special collections » (www.ru.nl) : les œuvres numérisées s'ouvrent par le bouton « Online access » de RUQuest et par la banque d'images numérique ; aucune règle de débit (`sources/doc/`).
- Collections spéciales : https://bijzonderecollecties.ubn.ru.nl/ est une instance CONTENTdm (OCLC) avec `iiifEnabled: true` ; robots.txt : `Crawl-Delay: 1`, `Disallow: /oai/`, `/utils/` (`sources/b/`).
- Dépôt Radboud Repository (DSpace) : robots.txt `Crawl-delay: 10` ; conditions d'utilisation : réutilisation libre avec mention de la source, usage commercial interdit, aucune règle de débit (`sources/doc/`, `sources/b/`).
- Doc OCLC CONTENTdm (IIIF, dmwebservices) : aucune règle de débit ; robots.txt de help.oclc.org : `Crawl-delay: 5`, `Request-rate: 1/5` (`sources/c/`, `sources/e/`).
- Projet Open Topstukken (Maastricht + Radboud) : page de projet, aucune API ni quota.

## Tests
Six passes de sonde (journal `tests/journal.log`) :
- CONTENTdm : manifeste global (301, 302 puis 200), manifeste de collection Handschriften, manifeste d'objet Handschriften:12155, info.json d'image sur cdm21010 et sur le site, dmwebservices, OAI (Disallow /oai/ testé sous C12) : tous en 200, aucun en-tête de limite (`x-oclc-iiif-provider: cantaloupe`).
- Dépôt : description OpenSearch 200, OAI Identify : délai de lecture dépassé en passe 2 (pas un 429), 200 au nouvel essai en passe 3 ; REST `/rest/communities` : 404.
- Aucun 403, CAPTCHA ni 429. Crash test préparé : `config/crash-image-info.json` (non lancé).

## Web
- presentations : page du projet Open Topstukken, lue en entier.
- institution, tickets, utilisateurs : aucun résultat utile (résultats de Leiden, Sherpa en résumé de moteur). Le budget de recherche de la session a été épuisé après cinq recherches.

## Conclusion
Aucun quota ni limite de débit publiés ; seuls les Crawl-delay des robots.txt (10 s dépôt, 1 s collections, 5 s doc OCLC). Les API sont celles de CONTENTdm/OCLC (IIIF 2, dmwebservices, OAI) et de DSpace (OAI, OpenSearch), répondant sans en-tête de limite. Confiance moyenne.
