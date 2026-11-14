# e-rara – ETH-Bibliothek et partenaires (GLAM-019)

## Sources
- Doc officielle du wiki e-rara (apiinfo, termsOfUse) : lue dans la Wayback (captures du 2024-09-17), car le wiki est maintenant derrière un défi JavaScript « Verifying your browser » non contourné (`sources/wayback/erara-extraits-wayback.md`, `sources/b`, `sources/v2`).
- Data Map de la ZB Zürich (partenaire) : pages e-rara IIIF, OAI, SRU (`sources/c`, `sources/d`) ; page de présentation de la plateforme ; catalogue opendata.swiss.
- robots.txt : www.e-rara.ch (`Disallow: /` sauf Googlebot et Bingbot ; Crawl-delay 1 pour 10 robots nommés), sru2.visual-library.de (404), www.zb.uzh.ch, data.zb.uzh.ch (404), opendata.swiss (page d'erreur) ; era-prod11.ethz.ch : défi JavaScript, non lu.
- Aucune page de conditions d'usage ne parle d'accès automatisé, de robots ou de débit.

## Tests
Trois passes, 26 requêtes (GET/HEAD, ≥ 6 s, configurations committées avant lancement, Disallow outrepassé sur décision C12 de Marcel).
- OAI-PMH : Identify, ListSets, ListMetadataFormats, GetRecord, ListIdentifiers, ListRecords : 200.
- IIIF : manifeste v20 et alias /zuz/, info.json v21, vignette, full/full (2474x2981 : pas de plafond de taille observé) : 200.
- Téléchargements : RIS, ftpack plain/alto, PDF (HEAD), ALTO3 (HEAD) : 200. SRU (sru2.visual-library.de) : 200.
- Service de recherche du manifeste : 200 mais HTML (probable page de contrôle) : à vérifier dans un navigateur.
- Aucun en-tête de limite, aucun 429.

## Web
Aucune plainte de 429/blocage ni issue GitHub sur e-rara trouvée. Un billet de Source Library (2026-06-02) fixe de lui-même 2 requêtes/s pour e-rara (limite du tiers, pas d'e-rara). Atelier IIIF de l'Université de Berne (2025) : e-rara cité comme source de manifestes, sans limite.

## Conclusion
Aucun quota ni limite de débit publié ; pas de page de conditions d'usage sur l'automatisation. Seuls éléments écrits : robots.txt restrictif, paquets OAI de 10 records, timeouts du format mets. Pourquoi pas publié : hypothèse (non vérifiée) que la plateforme se protège par un défi JavaScript sur les pages plutôt que par des quotas annoncés. Les interfaces de données restent ouvertes sans en-tête de limite. Confiance moyenne (wiki actuel non lisible).
