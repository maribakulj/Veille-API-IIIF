# KU Leuven Libraries (GLAM-072)

## Sources
- Pages officielles lues (v2, b, c) : digitisation, copyright (expo), conditions d'usage, images as open data, dépôt GitHub de l'institution, poster Zenodo, robots.txt (bib, expo, Limo). Empreintes : `sources/{v2,b,c}/SHA256SUMS`.
- Captures Wayback (hôtes libis.be illisibles en direct) : `sources/wayback/libis-wayback.md`.
- Aucune documentation publique d'API IIIF, de quota ou de limite de débit trouvée. Citation : « Everyone interested may download and freely use these images. » (images avant 1901, via le visualiseur Limo/Teneo).

## Tests
- Passe 1 (4 endpoints, 7 requêtes avec robots) : resolver, services et repository.teneo.libis.be : délai de 30 s dépassé à chaque fois.
- Passe 2 : manifeste services.libis.be/m2/manifest/IE11541569 et miniature resolver : délai dépassé ; page collection de Limo : HEAD 200, aucun en-tête de limite.
- Aucun 403, 429 ni CAPTCHA. Cause des délais inconnue (hôtes lents, ou filtrage réseau silencieux) ; bib.kuleuven.be a répondu 200 sur les deux premières pages puis dépassé le délai.
- Robots : Disallow: / sur resolver et repository.teneo (Wayback), testé quand même (C12).

## Web
- institution : politique images en libre usage, rien sur bots/débit.
- présentations : poster Zenodo 2024 (lu), présentation LIBIS 2017 (résumé de moteur, non vérifié).
- utilisateurs, tickets : aucun résultat.

## Conclusion
Aucun quota publié ; limite non observée ; les hôtes IIIF/Teneo de LIBIS n'ont jamais répondu depuis ce poste, donc rien n'a pu être mesuré. Confiance faible. À vérifier à la main : voir `a_verifier_manuellement`. Étape g : configuration crash préparée sur la page de collection de Limo (seul endpoint vu en 200).

## Crash test (étape g)

Crash test fait le 2026-11-14 : limo-collection sur kuleuven.limo.libis.be : aucun blocage jusqu'à 12 req/min (plafond 12 req/min).
Journal : `tests/crash/ku-leuven-libraries.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
