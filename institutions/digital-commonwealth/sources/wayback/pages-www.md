# Pages de www.digitalcommonwealth.org lues via le MCP internet-archive (hote arrete dans le registre, aucune requete directe)

Date de lecture : 2026-11-14. Cause de l'arret de l'hote : la page /contact (HTTP 200) contient un formulaire reCAPTCHA (balise recaptcha.net) que fetch_doc.sh a pris pour un defi ; le registre partage a arrete l'hote pour 24 h. Faux positif a notre avis, mais on ne le contourne pas.

## /copyright (replique https://web.archive.org/web/20261005090016/https://www.digitalcommonwealth.org/copyright, statut 200)
Extraits verbatim :
- "Digital Commonwealth provides access to copyrighted materials strictly for noncommercial educational and research purposes and places no restrictions on public domain material."
- "Digital Commonwealth does not charge permission fees for use of such material and does not grant or deny permission to publish or otherwise distribute material in its collections."
- Aucune mention de quota, de limite de debit, de moissonnage ni de bots.

## /about_dc (replique https://web.archive.org/web/20261005180051/https://www.digitalcommonwealth.org/about_dc, statut 200)
Extraits verbatim :
- "Digital Commonwealth is a statewide program that provides free digitization services, digital preservation, and online access to cultural heritage materials from Massachusetts institutions. The program is operated by the Boston Public Library as part of its Library for the Commonwealth services."
- Aucune mention d'API, de quota ni de debit.

## /for_institutions, /privacy, /harmful_content_statement, /search/opensearch.xml
Non lus : /for_institutions n'a qu'une capture sans statut (replique 20260918160248, statut "-") ; les autres n'ont pas ete lus (pages hors API ; opensearch.xml : capture 20260925062231 statut 200 existe, description de recherche).
