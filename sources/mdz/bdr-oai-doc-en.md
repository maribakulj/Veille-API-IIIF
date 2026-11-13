# Bavarian Digital Repository / OAI-PMH (EN), lien depuis la page Interfaces

- URL : https://oai.bsb-muenchen.de/doc/en/bavarian-digital-repository
- Date de lecture (UTC) : 2026-11-13T21:19:28Z
- SHA-256 du texte ci-dessous (UTF-8) : `00903383a7ee1083e391103468f6889a2ab3792fe8d138aad505ff8e48ba7c82`
- Taille HTTP du HTML : 31017 octets (téléchargement complet, non tronqué ; contrôle par curl)
- Méthode : HTML converti en texte (balises, scripts et styles retirés ; menus de navigation conservés, répétés en tête et en pied). Pas de résumé : texte intégral de la page.
- Lecture : intégrale ; la page est lue dans son texte converti, les liens sont dans le HTML brut conservé hors dépôt.

---

Deutsch 

 | 
 Imprint

- 

 Bavarian Digital Repository

- 

 Imprint

Bavarian Digital Repository

The Bavarian Digital Repository (BDR) is developed to be a freely accessible interface for harvesting metadata about all digital representations produced by or in cooperation with the Bavarian State Library. Metadata is derived from B3Kat and BSB ILS. Each data record is published under CC0-Public Domain Dedication.

BDR conforms to the OAI Protocol for Metadata Harvesting (OAI-PMH).

http://bdr.oai.bsb-muenchen.de/OAIHandler?verb=Identify

Each record describes the digitised exemplar of a work. If several exemplars of one work are digitised, several records will exist in BDR as well. Metadata are provided in Dublin Core and MarcXchange (http://bdr.oai.bsb-muenchen.de/OAIHandler?verb=ListMetadataFormats).

MarcXchange transports data in MARC21 strongly according to the specifications documented in Konkordanz MAB2 – MARC 21.

Regionally and locally defined MARC21 fields, specifically assigned fields:

 001

 BDR-ID; Example: BDR-BV001159101-62175

 940 Ind.1=_

 Bibliographic Identifier of the source system

 Subfield a: Identifier of the catalogue system

 Subfield b: Identifier of the OAI-PMH repository

 940 Ind.1=1

 Regional and local codes (MAB 078)

 Subfield e: selection code ebooks

 Subfield f: selection code language area

 Subfield n: selection code interlibrary bibliographies and projects

 Subfield q: library-specific selection codes

 940 Ind.1=2

 Subfield r: ISIL of revising library (in the context of VD18, i.e. bibliography of books printed in German-speaking countries in the 18 th century, MAB 088 subfield r)

 955

 Data of the exemplar

 Subfield a: Shelfmark

 Subfield b: Possessing institution

 Subfield c: Institution's ISIL

 982

 Hyperlink to thumbnail image

You can select several different sets (http://bdr.oai.bsb-muenchen.de/OAIHandler?verb=ListSets):

 all

 All works comprised in the Bavarian Digital Repository (BDR). All subsequent sets are subsets of 'all'.

 cerl

 Digitised manuscripts of the Bavarian State Library

 dgt

 Bavarian State Library digital resources that are curated with DigiTool

 digi19

 Works digitised at the Bavarian State Library that are printed in the 19 th century

 digi20

 Works digitised at the Bavarian State Library that are printed in second half of 20 th century (Digi20 project)

 europeana

 Works digitised at the Bavarian State Library that are delivered to Europeana. At the moment, this set is identic with the set "all".

 ostdok

 Works digitised at the Bavarian State Library that are part of the project "OstDok"

 vd16

 Works digitised at the Bavarian State Library that are part of the bibliography of books printed in German-speaking countries in the 16 th century (VD16)

 vd17

 Works digitised at the Bavarian State Library that are part of the bibliography of books printed in German-speaking countries in the 17 th century (VD17)

 vd18

 Works digitised at the Bavarian State Library that are part of the bibliography of books printed in German-speaking countries in the 18 th century (VD18)

 zssbd

 Serial volumes digitised at the Bavarian State Library

Search for all records:

http://bdr.oai.bsb-muenchen.de/OAIHandler?verb=ListRecords&metadataPrefix=MarcXchange&set=all

The total number of records can be found as attribute completeListSize of element resumptionToken. One record can be enclosed in several sets. A digitised 18th century work for example is part of the sets "all", "europeana" and "vd18". As the set name is part of the OAI identifier, the same record can be found with three different identifiers.

Example record:

http://bdr.oai.bsb-muenchen.de/OAIHandler?verb=GetRecord&metadataPrefix=MarcXchange&identifier=oai:bdr.oai.bsb-muenchen.de:all:BDR-BV001159101-62175

Changes

2015-10-15: Namespace prefix 'oai' cancelled.

Contact: oai(at)bsb-muenchen.de

oai.bsb-muenchen.de © 2025 Bayerische Staatsbibliothek

