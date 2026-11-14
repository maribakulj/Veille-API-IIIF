# National Diet Library – Japon (`national-diet-library-japan`)

- **Classeur** : GLAM-076 · Japon · audit v2 du 2026-11-14 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `ndlsearch.ndl.go.jp` (NDL Search : SRU, OpenSearch, OpenURL, OAI-PMH), `www.dl.ndl.go.jp` / `dl.ndl.go.jp` (Digital Collections, IIIF), `lab.ndl.go.jp`, `www.ndl.go.jp`, `current.ndl.go.jp`.

## Sources
- **robots.txt** (sources/a1, a5, a8) : ndlsearch `Disallow: /api` ; dl.ndl.go.jp `Disallow: /api/` mais `Allow: /api/iiif/` ; www.ndl.go.jp `Allow: /` ; lab.ndl.go.jp : quelques Disallow ; current.ndl.go.jp : /wp-admin/. Aucun Crawl-delay.
- **Doc NDL Search API** (sources/a2, a3, a4) : page « 17. How to use NDL Search API », citation : « We restrict the number of concurrent accesses to prevent server overload. When we receive a large amounts of requests from a particular IP address on a continuous basis, we might block access to the website. » Spécification 1.5 (2026-09-25) : au plus 500 résultats par requête (200 par défaut), pas de résultat au-delà du 500e, OAI-PMH : `from` obligatoire, période d'un an au plus, 200 notices par resumptionToken ; usage commercial soumis à demande.
- **IIIF Digital Collections** : guide officiel `IIIF_interface_Jp.pdf` (sources/a7) : manifeste `https://www.dl.ndl.go.jp/api/iiif/{PID}/manifest.json`, Image API `.../{PID}/{contenu}/full/full/0/default.jpg`, `info.json` ; conditions IIIF et annonce de 2018 lues via Wayback (`sources/wayback/ndl-dl-iiif-licence.md`) car dl.ndl.go.jp est une application JavaScript (coquille de 4 298 o pour toute URL). Aucune limite de débit dans le guide IIIF.

## Tests
- **Passe 1** (`ndl-v2-passe1.json`, 3 requêtes sur 8) : OpenSearch : délai dépassé (30 s) ; SRU : **429** (corps XML : « Too Many Requests / 同時アクセス数の上限に達したため、リクエストの制限を行っています », via CloudFront, aucun en-tête `Retry-After` ni `X-RateLimit-*`). Conformément à la règle, arrêt de l'institution : OpenURL, OAI-PMH (3 verbes), description OpenSearch et manifeste IIIF **non lancés**. Le 429 confirme le mécanisme « limite de connexions simultanées » annoncé par la doc (limite globale côté NDL, dès la 2e requête ; seuil chiffré inconnu).

## Web
- Recherches : guide IIIF officiel trouvé ; aucune plainte ni ticket sur un 429 NDL Search ; recherche GitHub interne : rien de pertinent ; article zenn (tiers) : rien sur les limites. Les catégories tickets et présentations n'ont pas eu de WebSearch propre (budget de session épuisé).

## Conclusion
Limite documentée : plafond de requêtes simultanées et blocage d'IP en cas de forte charge continue, sans chiffre ; limites de volume (500 résultats, OAI-PMH sur 1 an). Limite observée : 429 « limite de connexions simultanées » sur le SRU. IIIF non testé (arrêt 429). Confiance : moyenne.
