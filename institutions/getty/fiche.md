# Getty — Open Content, Linked Art, IIIF (`getty`)

- **Classeur** : GLAM-048 · États-Unis · **Refonte v2 le** 2026-11-14 (Sonnet 5.5) ; l'ancien audit Haiku du 2026-11-13 (7 requêtes, doc tronquée, configuration committée après lancement) est archivé tel quel dans `tests/archive/` · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `data.getty.edu` (API Linked Art, SPARQL), `media.getty.edu` (IIIF Presentation et Image), `www.getty.edu` (conditions).

## Sources
- **Doc API** (`data.getty.edu`, Nuxt : lue via les payload.json, `sources/a`, `sources/a2`) : quatre API (Museum Collection, Provenance Index, LinkedArt JavaScript Library, ID Management Service). Museum Collection : REST `/museum/collection/<type>/<id>`, ActivityStreams, SPARQL, IIIF Image et Presentation sur `media.getty.edu`. Citations : « We are providing this data without restrictions for all to enjoy. » ; « Images are not always available under the same terms as the dataset. » Aucune limite de débit, aucune clé, aucun en-tête, aucun endpoint de statut. Contacts : MuseumCollections@getty.edu, provenanceindex@getty.edu, rights@getty.edu.
- **Terms of Use** et **Open Data and APIs** de `www.getty.edu` (lues en entier, texte extrait) : conditions du site, droits des images ; aucune règle de débit ni de moissonnage.
- **robots.txt** : `data.getty.edu` 404 (tout autorisé) ; `www.getty.edu` : Disallow `/cgi-bin`, `/slampoets`, `/research/collections/mirador/`, `/art/collection/` pour Yeti, AhrefsBot interdit, pas de Crawl-delay ; `media.getty.edu` : **503** à chaque lecture (à vérifier au navigateur).

## Tests (3 passes, configurations committées avant lancement)
Passe 1 `data.getty.edu` (10 requêtes dont robots) : activity-stream et page 1, objet, personne, Provenance Index (flux et notice) en **200** ; les deux SPARQL sans requête en **400** (« No query parameter included », réponse normale). Passe 2 `media.getty.edu` (5) : deux manifestes, `info.json` et dérivé 600 px en **200**, serveur IIPImage derrière Varnish/CloudFront. Passe 3 `www.getty.edu` (3) : 302 puis 200. Aucun 429, 403 ni en-tête de limite. Non testés : ID Management Service (pas d'URL d'exemple), bibliothèque JavaScript.

## Web (4 catégories)
- institution : doc API lue ; rien sur le débit.
- utilisateurs : article tiers lu (navigating.art, 2026) : accès « without any API key », rien sur les limites.
- tickets : aucun ticket sur `media.getty.edu` / `data.getty.edu` ; les 429 trouvés concernent Getty Images (service commercial distinct).
- présentations : annonce 2017 (30 000 images en IIIF) et exposé IIIF 2024, résumé de moteur, non vérifié ; aucune politique de débit.

## Conclusion
Limite chiffrée : aucune. Règle écrite : données libres, images sous conditions distinctes. Aucun 429 ni en-tête de limite en 18 requêtes. Confiance : moyenne. À demander par écrit à MuseumCollections@getty.edu. Crash test (g) : configuration `config/crash-media-info.json` prête, non lancé.
