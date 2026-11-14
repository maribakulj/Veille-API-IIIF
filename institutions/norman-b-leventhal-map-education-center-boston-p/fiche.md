# Norman B. Leventhal Map & Education Center – Boston Public Library (`norman-b-leventhal-map-education-center-boston-p`)

- **Classeur** : GLAM-062 · États-Unis · audit v2 du 2026-11-14 · suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `collections.leventhalmap.org` (portail), `www.digitalcommonwealth.org` (JSON, manifestes), `oai.digitalcommonwealth.org` (OAI-PMH), `iiif.digitalcommonwealth.org` (images IIIF), `www.leventhalmap.org` (site), `cartinal.leventhalmap.org` (guides).

## Sources (étape a)
- Page « Digital Collections » (LMEC) : manifeste = suffixe `/manifest.json` sur l'URL de la notice ; recherche JSON à `collections.leventhalmap.org/search.json`.
- `digitalcommonwealth.org/api` : JSON (`.json`), IIIF Image 2.0 (`iiif.digitalcommonwealth.org/iiif/2/`), Presentation 2.0 (`/manifest`), OAI-PMH (`oai.digitalcommonwealth.org/catalog/oai`) ; aucune limite citée. `/copyright` : « places no restrictions on public domain material », usage non commercial pour le matériel sous droit.
- Dépôts GitHub `bplmaps/collections-api` (notebooks JSON et IIIF), `bplmaps/iiif-tools` ; guide `cartinal.leventhalmap.org` : aucune limite.
- `robots.txt` : `collections.leventhalmap.org` **Crawl-Delay: 15** (ligne sans `User-agent`, donc ignorée par un analyseur strict) + Disallow des facettes et téléchargements ; `www.digitalcommonwealth.org` **Crawl-Delay: 5** ; `iiif.digitalcommonwealth.org` **Disallow: /** ; `oai.` et `cartinal.` : 404 ; `www.leventhalmap.org` : 404 (page d'erreur 27 ko) ; stockage Azure : 400.

## Tests (étape e, 2 passes, 14 requêtes, configurations committées avant lancement)
Passe 1 (11 requêtes, 6 s) : recherche JSON LMEC, manifeste, notice HTML, recherche JSON DC, notice JSON DC, manifeste DC, OAI `Identify`, `opensearch.xml` : tous **200**. Passe 2 (3 requêtes, 15 s) : `info.json` et vignette 200×200 sur `iiif.digitalcommonwealth.org` : **200** (Disallow: / journalisé, testé avec l'accord C12). Aucun 429, aucun en-tête de limite.
Réserve : en passe 1 la pause vers `collections.leventhalmap.org` a été de 6 s, le Crawl-Delay 15 de ce robots.txt n'étant pas lu par la sonde (ligne orpheline) ; passe 2 à 15 s.

## Web (4 recherches, une par catégorie)
Aucune politique de bots ni de débit, aucune plainte 429/403, aucun ticket d'outil ; l'annonce IIIF Consortium (2023) et le wiki GitHub des champs de l'API ne citent aucune limite.

## Conclusion
Limite chiffrée : aucune. Seuls signaux : Crawl-Delay 15 s (portail LMEC) et 5 s (Digital Commonwealth) ; API ouvertes, sans clé. Confiance : moyenne.
