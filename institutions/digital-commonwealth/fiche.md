# Digital Commonwealth (GLAM-055)

## Sources
- Doc API : https://www.digitalcommonwealth.org/api (sources/doc/text/04.txt) : OAI-PMH (https://oai.digitalcommonwealth.org/catalog/oai), JSON en ajoutant .json aux URL de recherche et d'item, IIIF Image 2.0 (https://iiif.digitalcommonwealth.org/iiif/2/), IIIF Presentation 2.0 (/manifest). Aucun quota, aucune limite de débit, aucun en-tête de limite cité. Contact : « Please contact us with any questions or comments. »
- robots.txt www : Crawl-Delay: 5, facettes/téléchargements/comptes interdits ; oai. : 404 ; iiif. : Disallow / ; blog : Disallow /wp-admin/.
- Copyright & Terms of Use et About lus via Wayback (sources/wayback/pages-www.md) : aucune mention de quota ni de bots ; « places no restrictions on public domain material ».
- Wiki GitHub boston-library/solr-core-conf (champs JSON publics) lu : aucun quota. Blog officiel lu : ni API ni bots.
- Hôte www arrêté par le registre partagé après la page /contact (HTTP 200, formulaire reCAPTCHA pris pour un défi) : faux positif, non contourné. www.bpl.org : HTTP 202 corps vide.

## Tests
- Passe 1 (config dc-passe1-oai-iiif.json, 10 s) : OAI Identify 200, OAI ListMetadataFormats 200, IIIF info.json 200 et dérivé pct:10 200 (Disallow / journalisé, autorisé par Marcel C12) ; 6 requêtes envoyées dont 2 robots.txt (search.json, item .json et manifeste du hôte www non lancés en passe 1, voir passe 2). Aucun en-tête RateLimit/Retry-After ; serveurs nginx, Cantaloupe 5.0.6 derrière iiif. Identifiant d'image commonwealth:hd76s0677 tiré de la page d'accueil publique.

- Passe 2 (config dc-passe2-www.json, 10 s, 2026-11-14T04:00Z, blocage reCAPTCHA levé) : search.json?q=Boston 200 (72 412 octets, JSON), item commonwealth:hd76s0677.json 200 (2 203 octets), manifeste /manifest 404 (la doc : « A 404 will be returned if no manifest is available »). 3 requêtes, aucun en-tête de limite, aucun 429.

## Web
- institution : page API et copyright (aucun chiffre).
- presentations, utilisateurs, tickets : aucun résultat propre à Digital Commonwealth (résumés de moteur, non vérifiés) ; requêtes consignées dans data.json. Le moteur signale un hôte de recette qc-dc3dev.bpl.org (non testé) et le dépôt boston-library/blacklight_iiif_search (non lu).

## Conclusion
Aucun quota ni politique de débit publiés ; hypothèse non vérifiée : service public de bibliothèque sans limitation annoncée, avec la seule règle Crawl-Delay: 5. Les familles OAI et IIIF Image sont testées sans signal de limite. JSON de recherche et JSON d'item testés en 200 et manifeste en 404 (passe 2), sans signal de limite. Crash test (g) : config crash-iiif-info.json préparée.

## Crash test (étape g)

Crash test fait le 2026-11-14 : iiif-info sur iiif.digitalcommonwealth.org : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/digital-commonwealth.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
