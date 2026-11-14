# Universitätsbibliothek Heidelberg (digi.ub.uni-heidelberg.de) — fiche d'audit v2

## Sources
- Pages de l'UB lues en entier (sources/doc, sources/doc2, sources/accueil) : Digitale Bibliothek, Nutzungsbedingungen der Digitalisate, Reproduktion, Workflow technique (dwork), Digilit, Kontakt, Open Access, sitemap. Seule phrase technique : « Die Metadaten können per OAI-Schnittstelle abgerufen werden et enthalten alle zur Nutzung durch den DFG-Viewer notwendigen Angaben » ; la page dwork liste « IIIF-Image-Server: Cantaloupe Image Server ». Les conditions d'usage (« Die Universitätsbibliothek Heidelberg erhebt keine Gebühren für die Nutzung ihrer Digitalisate ») ne disent rien du débit ni des bots.
- robots.txt lus : digi.ub (Disallow /cgi-bin/, /image/, /diglit/_browse_*, …), www.ub et ub (Drupal, rien sur l'API). SemrushBot exclu. Pas de Crawl-delay.
- Les pages d'ouvrage et le flux RSS de digi.ub sont derrière **Anubis** (défi de preuve de travail, « protect the server against the scourge of AI companies aggressively scraping websites ») : non contourné ; lu dans la Wayback Machine (sources/wayback/digi-ub-wayback.md : mention « IIIF Manifest: v2.1, v3.0 », Identify OAI).

## Tests (3 passes, 12 requêtes vers digi.ub, + 1 rejouée)
- OAI-PMH `cgi-bin/digioai.cgi` : Identify, ListMetadataFormats, ListSets, GetRecord (oai_dc) = 200 ; aucun en-tête de limite. (/cgi-bin/ interdit par robots.txt : lancé car autorisé par Marcel, C12.)
- IIIF Presentation v2 et v3 (aaha1928), Image v2 et v3 info.json, dérivé 200×200 = 200 ; Apache / Cantaloupe 5.0.3 ; aucun en-tête de limite.
- RSS `diglit/rss?set=handschriften` : 200 mais page de défi Anubis (« Making sure you're not a bot! ») : pas de flux, pas de contournement.
- Une session (passe 2) archivée dans tests/archive car 5 s seulement la séparaient de la passe 1 ; rejouée.

## Web
Quatre recherches : aucune politique de débit, aucune plainte 429/503, aucun ticket d'outil ciblant Heidelberg ; seule piste, l'étude de cas Europeana (OAI-PMH puis IIIF) citée par un moteur (page en 403 pour WebFetch, non vérifiée).

## Conclusion
Aucun quota ni limite de débit publiés. L'OAI-PMH et l'IIIF répondent sans en-tête de limite. En revanche l'institution protège les pages web par Anubis contre le moissonnage par IA : c'est un refus d'accès à certains clients, pas un quota. Pourquoi pas publié : hypothèse, protection au niveau de l'hôte plutôt que limite documentée ; à demander à ub@ub.uni-heidelberg.de.
