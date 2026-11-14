# Digital Commonwealth (GLAM-055)

## Sources
- Doc API : https://www.digitalcommonwealth.org/api (sources/doc/text/04.txt) : OAI-PMH (https://oai.digitalcommonwealth.org/catalog/oai), JSON en ajoutant .json aux URL de recherche et d'item, IIIF Image 2.0 (https://iiif.digitalcommonwealth.org/iiif/2/), IIIF Presentation 2.0 (/manifest). Aucun quota, aucune limite de débit, aucun en-tête de limite cité. Contact : « Please contact us with any questions or comments. »
- robots.txt www : Crawl-Delay: 5, facettes/téléchargements/comptes interdits ; oai. : 404 ; iiif. : Disallow / ; blog : Disallow /wp-admin/.
- Copyright & Terms of Use et About lus via Wayback (sources/wayback/pages-www.md) : aucune mention de quota ni de bots ; « places no restrictions on public domain material ».
- Wiki GitHub boston-library/solr-core-conf (champs JSON publics) lu : aucun quota. Blog officiel lu : ni API ni bots.
- Hôte www arrêté par le registre partagé après la page /contact (HTTP 200, formulaire reCAPTCHA pris pour un défi) : faux positif, non contourné. www.bpl.org : HTTP 202 corps vide.

## Tests
- Passe 1 (config dc-passe1-oai-iiif.json, 10 s) : OAI Identify 200, OAI ListMetadataFormats 200, IIIF info.json 200 et dérivé pct:10 200 (Disallow / journalisé, autorisé par Marcel C12) ; search.json, item .json et manifeste du hôte www NON LANCÉS (hôte arrêté). 6 requêtes envoyées dont 2 robots.txt. Aucun en-tête RateLimit/Retry-After ; serveurs nginx, Cantaloupe 5.0.6 derrière iiif. Identifiant d'image commonwealth:hd76s0677 tiré de la page d'accueil publique.

## Web
- institution : page API et copyright (aucun chiffre).
- presentations, utilisateurs, tickets : aucun résultat propre à Digital Commonwealth (résumés de moteur, non vérifiés) ; requêtes consignées dans data.json. Le moteur signale un hôte de recette qc-dc3dev.bpl.org (non testé) et le dépôt boston-library/blacklight_iiif_search (non lu).

## Conclusion
Aucun quota ni politique de débit publiés ; hypothèse non vérifiée : service public de bibliothèque sans limitation annoncée, avec la seule règle Crawl-Delay: 5. Les familles OAI et IIIF Image sont testées sans signal de limite. JSON de recherche, JSON d'item et manifeste Presentation non testés (hôte www arrêté), à lancer lors de la clôture quand le registre le permettra (24 h) : URL dans a_verifier_manuellement. Crash test (g) : config crash-iiif-info.json préparée.
