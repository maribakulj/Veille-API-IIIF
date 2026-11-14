# Biblioteca Nacional de Portugal – BND (Biblioteca Nacional Digital) — `biblioteca-nacional-de-portugal-bnd`

- **Statut** : audit v2 complet a à f (2026-11-14) ; crash test (g) préparé, non lancé (C15)
- **Pays** : Portugal ; **Vérifié le** : 2026-11-14 (UTC, 01:44-01:50)

## Sources
Doc officielle lue en entier (sources/a1 à a5) : aide, About, mentions légales et documentation technique de la BND ; portail Open Data (index, services, OAI-PMH, identifiants persistants, téléchargements, documentation) ; liste des sets OAI ; deux présentations PDF de la BNP (2021 DCMI, 2019 réutilisation) ; page URN (acesso.urn) ; robots.txt de 9 hôtes.

- Aucune page ne publie de quota, de limite de débit ni de règle pour les robots. Phrase la plus proche : « All data are released under the CC0 License [...]. All data services are free of charge and without authentication. » (opendata.bnportugal.gov.pt/eng_index.htm).
- Pas de doc IIIF publique : la page About ne cite IIIF que comme format des identifiants persistants. L'URL du manifeste vient d'une notice Biblissima (tiers).
- robots.txt : bndigital, permalinkbnd, purl.pt, rnod = `Disallow: /` pour `*` ; oai, urn.bnportugal, urn.porbase, opendata = 404 ; id = 400. Disallow passé outre avec l'accord de Marcel (C12), aucun Crawl-delay pour `*`.

## Tests (config bnd-passe1.json commit 3c5ec02, bnd-passe2.json commit suivant ; tous deux committés avant lancement)
Passe 1 (14 requêtes dont 5 robots.txt) : manifeste IIIF Presentation v2 (200, JSON ; `access-control-allow-origin: *`), OAI Identify et ListMetadataFormats (200), URN BNP (200), URN PORBASE (200), purl.pt/32689 (200), purl.pt/32689/1 (302 vers /32689/1/), recherche HTML BND (200). Passe 2 (6 requêtes) : Image info.json (200, iipsrv), dérivé 256 px, IIIF Search 1.0 et autocomplete (200), notice permalink (302), purl.pt/32689/1/ (délai dépassé). Aucun en-tête de limite (x-ratelimit, Retry-After), aucun 429/403.

## Web (étape f)
institution : présentation DCMI 2021 et PDF BNP lus, rien sur le débit ; utilisateurs : aucun résultat ; tickets : aucun résultat (Biblissima a seulement agrégé les manifestes) ; presentations : page DCMI 2021 lue, silencieuse sur API/limites.

## Conclusion
Aucun quota ni limite de débit publié ou observé ; classe « aucun quota trouvé ». Le seul signal restrictif est un robots.txt `Disallow: /` sur la BND, permalinkbnd et purl.pt. Les services de données ouvertes sont annoncés sans authentification ni frais. Pourquoi non publié : hypothèse non établie : la BNP traite l'accès par API comme de la réutilisation libre (CC0, directive PSI 2019/1024) et ne chiffre pas les volumes. Contacts : bndigital@bnportugal.gov.pt, OpendataBNP@bnportugal.gov.pt.

## Crash test (étape g)

Crash test fait le 2026-11-14 : oai-identify sur oai.bnportugal.gov.pt : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/biblioteca-nacional-de-portugal-bnd.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
