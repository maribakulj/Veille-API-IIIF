# e-manuscripta.ch — extraits verbatim lus dans la Wayback Machine (outil ia_get_snapshot, 2026-11-14)

Raison : www.e-manuscripta.ch sert aujourd'hui une page « Verifying your browser » (défi JavaScript de Visual Library, 177 caractères) à notre client (fetch_doc, 2026-11-14) et dans les captures récentes de la Wayback (home 2026-11-08, apiinfo 2026-10-04). On ne contourne pas le défi ; on lit des captures antérieures au défi (avant 2025-08).

## 1. Page « Schnittstellen und Datenabzug » (wiki/apiinfo) — capture 2025-03-07 (20250307173039), 7 521 caractères, lue en entier
Réplique : https://web.archive.org/web/20250307173039/https://www.e-manuscripta.ch/wiki/apiinfo

> Zum Nutzen von Forschung und Lehre stellt e-manuscripta.ch verschiedene Schnittstellen für den Abzug und die Weiterverwendung von Daten bereit. […] (OAI-PMH), Volltexten, PDFs, RIS-Dateien und die Möglichkeiten von IIIF.
> OAI : baseURL https://www.e-manuscripta.ch/oai avec « ?verb= » : Identify, ListSets, ListMetadataFormats, GetRecord (identifier, metadataPrefix), ListRecords (from/until, set, metadataPrefix, resumptionToken), ListIdentifiers.
> resumptionToken : « Pro Abfrage liefert der Server Pakete von jeweils 10 Records zurück zusammen mit einem Token. »
> « Es gibt z.T. sehr umfangreiche Titel in e-manuscripta.ch. Werden Records solcher Titel im MetadataFormat=mets geharvestet, kann es sein, dass die Aktion fehlschlägt, da einfach die Datenmenge zu gross ist und die Übertragung in ein Timeout läuft. »
> PDF : https://www.e-manuscripta.ch/download/pdf/[VLID].pdf ; exemple www.e-manuscripta.ch/download/pdf/1384091.pdf ; « Für einen maschinellen Download […] bietet es sich an, die VLIDs in einem ersten Schritt via OAI zu harvesten ».
> RIS : https://www.e-manuscripta.ch/[domain]/download/format/ris/[VLID] ; exemple www.e-manuscripta.ch/zuz/download/format/ris/1384091.
> IIIF : « Auf jeder Titelseite findet sich im Bereich «IIIF» ein Link zum IIIF-Manifest. » ; image : https://www.e-manuscripta.ch/i3f/v21/[VLID]/full/0/0/default.jpg.

Aucun chiffre de débit, aucun quota, aucun en-tête de limite, aucune règle sur les robots dans cette page.

## 2. Page « Nutzungsbedingungen / Terms and conditions of use » (wiki/termsOfUse) — capture 2025-03-08 (20250308000344), 5 718 caractères, lue en entier
Réplique : https://web.archive.org/web/20250308000344/https://www.e-manuscripta.ch/wiki/termsOfUse

> « Systematic copying of files onto other servers is permitted only with the prior consent in writing of the portal's administrative office or the holding institution(s). »
> Trois licences par document : domaine public (Public Domain Mark) ; droits chez les institutions (CC BY-SA 4.0, source à citer) ; droits restreints (usage scientifique, privé, non commercial, source à citer).
> « If an e-manuscripta.ch partner institution mistakenly publishes digital files without the consent of the copyright holders, you are asked to contact e-manuscripta.ch on contact@e-manuscripta.ch . »

Aucune limite de débit chiffrée ni règle sur les robots.

## 3. Page d'accueil — capture 2025-06-01 (20250601100525)
Réplique : https://web.archive.org/web/20250601100525/https://www.e-manuscripta.ch/
Pied de page : « Powered by ETH Library — Visual Library Server 2025 » ; menu : Interfaces and Data Extraction, Terms of Use, Credits, Contact. 201 872 titres.

## 4. https://www.e-manuscripta.ch/robots.txt
Lu en direct le 2026-11-14 (sources/a1/raw/01.html, 89 octets) : « User-agent: * / Disallow: / / User-agent: Bingbot / Disallow: / User-agent: Googlebot / Disallow ». Captures Wayback 2025-02 à 2026-03 : même digest (LTZQZVYU…), longueur 367-394 octets avec en-têtes. Disallow: / pour les robots autres que Bingbot et Googlebot, depuis au moins février 2025.

## 5. Wayback de https://www.e-manuscripta.ch/wiki/apiinfo — 2026-09-02 à 2026-10-04
Captures de 4 777-4 803 octets (2026-09-02, 2026-10-04) : la dernière lisible ne contient que le défi « Verifying your browser ».
