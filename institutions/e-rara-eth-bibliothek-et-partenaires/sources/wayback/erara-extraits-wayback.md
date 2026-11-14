# e-rara — extraits verbatim lus dans la Wayback Machine (outil ia_get_snapshot, lus le 2026-11-14)

Raison : depuis fin 2026 le wiki et les pages d'e-rara sont derrière un contrôle « Verifying your browser » (JavaScript) : nos requêtes ne reçoivent que cette page (12 561 octets, sources/b/raw/01-04.html ; copies Wayback de nov. 2026 identiques). On ne le contourne pas : les pages sont lues dans des copies de 2024, d'avant le contrôle. Aucun trafic envoyé à e-rara par ce biais. Extraits recopiés à la main.

## 1. « Schnittstellen und Datenabzug » — https://www.e-rara.ch/wiki/apiinfo — capture 2024-09-17 (20240917151351), 8 113 caractères
Réplique : https://web.archive.org/web/20240917151351/https://www.e-rara.ch/wiki/apiinfo

> Zum Nutzen von Forschung und Lehre stellt e-rara.ch verschiedene Schnittstellen für den Abzug und die Weiterverwendung von Daten bereit.
> Das Protokoll OAI-PMH enthält sechs Basisfunktionen, die an die baseURL https://www.e-rara.ch/oai mit „?verb=" angefügt werden : Identify, ListSets, ListMetadataFormats, GetRecord, ListRecords, ListIdentifiers.
> resumptionToken: Pro Abfrage liefert der Server Pakete von jeweils 10 Records zurück zusammen mit einem Token.
> Anmerkung: Es gibt z.T. sehr umfangreiche Titel in e-rara.ch. Werden Records solcher Titel im MetadataFormat=mets geharvestet, kann es sein, dass die Aktion fehlschlägt, da einfach die Datenmenge zu gross ist und die Übertragung in ein Timeout läuft.
> Volltexte : https://www.e-rara.ch/[domain]/download/ftpack/[typ]/[VLID] (typ = plain | alto). Beispiele: www.e-rara.ch/zut/download/ftpack/plain/6341733 ; www.e-rara.ch/zut/download/ftpack/alto/6341733
> PDF : https://www.e-rara.ch/download/pdf/[VLID].pdf. Beispiel: www.e-rara.ch/download/pdf/6341733.pdf
> RIS : https://www.e-rara.ch/[domain]/download/format/ris/[VLID]. Beispiel: www.e-rara.ch/zut/download/format/ris/6341733
> IIIF : Auf jeder Titelseite findet sich im Bereich «IIIF» ein Link zum IIIF-Manifest. […] einzelne Bilder direkt via IIIFServer: https://www.e-rara.ch/i3f/v21/[VLID]/full/0/0/default.jpg

Aucun chiffre de débit ni de quota.

## 2. « Nutzungsbedingungen » — https://www.e-rara.ch/wiki/termsOfUse — capture 2024-09-17 (20240917173448), 4 991 caractères
Réplique : https://web.archive.org/web/20240917173448/https://www.e-rara.ch/wiki/termsOfUse

> Auf der Plattform e-rara stellen die beteiligten Institutionen ihre Digitalisate wann immer möglich kostenfrei zum Herunterladen zur Verfügung. Die Lizenzierungsart und die Nutzungsbedingungen sind individuell bei jedem Dokument angegeben.
> […] unter Creative Commons BY-SA 4.0 lizenziert […] Public Domain Mark […]

Aucune règle sur l'accès automatisé, le débit ou les robots.

## 3. robots.txt — https://www.e-rara.ch/robots.txt — capture 2024-09-22 (20240922222956), 91 caractères ; version actuelle lue directement (sources/v2/raw/01.html)
Réplique : https://web.archive.org/web/20240922222956/https://www.e-rara.ch/robots.txt

> User-agent: * / Disallow: / ; User-agent: Bingbot / Disallow: ; User-agent: Googlebot / Disallow:
(version actuelle : en plus `Crawl-delay: 1` pour DotBot, AhrefsBot, DataForSeoBot, Applebot, Bytespider, Amazonbot, GPTBot, ClaudeBot, ImagesiftBot, MJ12bot)
