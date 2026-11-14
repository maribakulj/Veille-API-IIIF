# State Library Victoria (GLAM-075)

## Sources
- Doc officielle SLV LAB (tutoriel IIIF, « Exploring SLV URLs », glossaire), pages open data, GitHub statelibraryvic/opendata, robots.txt de handle, viewer, find, lab, www : `sources/v2` et `sources/b` (SHA256SUMS).
- Citation : « The SLV uses Primo for its public-facing catalogue, as well as other systems such as Rosetta and IIIF to deliver digitised content. » Aucun quota ni limite de débit publiés. Réutilisation : métadonnées CC BY 4.0 ; images du domaine public libres.
- rosetta.slv.vic.gov.au (manifestes IIIF 2.1, serveur d'images) : 403 Cloudflare « Attention Required » sur robots.txt : hôte arrêté, non contourné ; Wayback illisible (`sources/wayback/rosetta-wayback.md`).

## Tests
- Passe 1 : handle (301 puis 302 vers viewer), viewer 200, find (Primo) 200, sans en-tête de limite.
- Passe 2 : API REST Primo /primaws/sourceRecord : 200, notice MARC, sans en-tête de limite (Disallow /primaws lancé, C12).
- Crawl-delay 10 (find) et 1 (handle) respectés. Aucun 429.

## Web
- institution : open data (lu) ; présentations : billet SLV LAB (lu) ; utilisateurs et tickets : aucun résultat (recherches ciblées impossibles : plafond de recherches web de la session).

## Conclusion
Aucun quota publié ni observé sur les hôtes testés ; les endpoints IIIF eux-mêmes (rosetta) refusent ce client en 403 : non testés, à vérifier à la main. Confiance faible. Étape g : configuration préparée sur l'API Primo (crash-primaws-record.json).
