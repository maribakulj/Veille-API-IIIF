# e-Museum / National Institutes for Cultural Heritage – Japon (`e-museum-national-institutes-for-cultural-herita`)

- **Classeur** : GLAM-081 · Japon · audit v2 du 2026-11-14 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `emuseum.nich.go.jp` (e国宝 / e-Museum), `colbase.nich.go.jp` (ColBase, hôte voisin), `www.nich.go.jp`.

## Sources
- **robots.txt** : `emuseum.nich.go.jp/robots.txt` et `colbase.nich.go.jp/robots.txt` renvoient une page HTML (la page d'accueil / l'application ColBase), donc pas de règles ; `www.nich.go.jp` : seul `/wp-admin/` est exclu. Aucun Crawl-delay.
- **Doc** (sources/a1 à a4) : Terms of Use de la page About (usage hors exceptions du droit d'auteur interdit ; « This website automatically collects user information (access logs) such as your domain name, IP address... ») ; guide e-Museum ; page « About IIIF » (/about2) : « e-Museum is compatible with Presentation API 2.1.1 and Image API 2.1.1 », lien « IIIF Manifest » sous la visionneuse ; annonce du 2022-02-01 « 画像を相互運用するための国際的な枠組みであるIIIFに対応しました ». Aucune phrase sur un quota, une limite de débit ou une API de recherche. La page de détail annonce un `link rel=search` (OpenSearch).

## Tests (2 passes, 5 requêtes, pauses 6 s)
- Manifeste `https://emuseum.nich.go.jp/iiifapi/100005000/manifest.json` : **200** (Presentation 2, 1 canevas 3615 x 9154) ; description OpenSearch `description/eKokuho_ja.xml` : **200** ; `info.json` d'image : **200** (réponse déclarant le contexte Image API 3) ; dérivé 200 px : **200** ; recherche OpenSearch RSS (`result2/?...opensearch=1`) : **200**. Aucun en-tête de limite (`X-RateLimit-*`, `Retry-After`), aucun 429 ni 403.
- En-têtes observés : `server: Apache`, `access-control-allow-origin: *`.

## Web
- Utilisateurs/tickets : un ticket dezoomify (lovasoa/dezoomify#597) signale un échec de téléchargement de tuiles sur emuseum.nich.go.jp, attribué à l'index des tuiles et à la configuration, non à un blocage ; aucune plainte de limite.
- Institution et présentations : la recherche WebSearch n'a pas pu être exécutée (budget de la session épuisé) ; à refaire quand il se réapprovisionne.

## Conclusion
Aucun quota ni limite de débit publiés ni observés (5 requêtes, 200 partout). IIIF 2.1 (manifeste) et service d'image fonctionnels. Confiance : faible à moyenne (recherches web incomplètes).
