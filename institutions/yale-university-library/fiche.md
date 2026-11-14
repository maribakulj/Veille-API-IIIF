# Yale University Library (`yale-university-library`)

- **Classeur** : GLAM-035 · États-Unis · audit v2 du 2026-11-14 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `collections.library.yale.edu` (Digital Collections System : interface Blacklight, manifestes `/manifests/{oid}`, images `/iiif/2/{id}`, OAI `/catalog/oai`), `library.yale.edu`, `web.library.yale.edu`, `guides.library.yale.edu`, `yalelibrary.atlassian.net`.

## Blocage et décision
Dès la passe 1, la page HTML `https://collections.library.yale.edu/catalog/16945082` a reçu **202 à corps vide avec `x-amzn-waf-action: challenge`** (défi AWS WAF, tests/raw/catalogue-item.headers.txt) ; la même réponse (202 vide) avait déjà touché `/catalog/opensearch.xml` et `/catalog/16945082` via fetch_doc (sources/a9, a10). Le manifeste JSON de la passe 1 a répondu **200** (7 326 octets lus, sans en-tête de limite). La passe 2 prévue (OAI, `info.json`, dérivé d'image sur le même hôte) **n'a pas été lancée** : le contrôle d'autorisation de l'environnement a refusé la poursuite des requêtes vers l'hôte après un défi WAF (« Unauthorized Access »). On s'en tient à cette décision prudente : **aucune autre requête vers `collections.library.yale.edu`**, aucun contournement. Les familles non testées sont listées comme `non_teste` avec cette raison et dans `a_verifier_manuellement`.

## Sources
- **Aide des Digital Collections** (`/help_guide`, sources/a2) : « All Digital Collections objects have a corresponding IIIF manifest, which is a JSON file [...] » ; Universal Viewer IIIF ; rien sur le débit.
- **robots.txt** de `collections.library.yale.edu` (sources/a1) : `User-agent: *` : Disallow `/manifests/`, `/pdfs/`, `/mirador/` ; `GPTBot` : Disallow `/pdfs/`, `/iiif/`, `/annotation/`, `/catalog/*/iiif_suggest`, `/catalog/*/iiif_search` ; Sitemap ; aucun Crawl-delay. `library.yale.edu/robots.txt` : Drupal standard (interdictions de chemins techniques).
- **Service catalog** (403 en direct ; Wayback, sources/wayback/service-catalog-dcs.md) : « No visibility restrictions », « Rates & Charges [...] No ».
- **FAQ de 2012** (sources/a7, PDF) : « There are no restrictions on Yale's service for machine harvesting of metadata (http://oai.odai.yale.edu/xcol/) built on [...] OAI-PMH » ; images jusqu'à 1920 × 1920 récoltables, au-delà « CAPTCHA restriction to prevent automatic harvesting ». Document ancien (2012), endpoint probablement remplacé.
- **Manifeste** (passe 1) : liens vers `/catalog/oai` (seeAlso OAI mods), `/iiif/2/{id}` (Image 2, niveau 2), `/download/tiff/{id}`, `/pdfs/{oid}.pdf`.
- Pages de politique (accès, copyright, demande de numérisation), documentation Confluence « Digital Collections Management » (sources/a3, a4, a6, a8) : rien sur les limites.

Remarque d'honnêteté : le motif `/manifests/{oid}` n'est pas écrit dans la doc lue ; il vient d'un lien de page tiers/connaissance de la plateforme, la doc disant seulement que chaque objet a un manifeste (lien dans le menu Tools). L'identifiant 16945082 est tiré de la page d'accueil.

## Tests (1 passe, 2 requêtes d'API plus robots.txt)
`/catalog/16945082` : **202 + défi WAF** ; `/manifests/16945082` : **200**, aucun en-tête de limite (`x-runtime`, `x-request-id`, ETag). Aucun 429.

## Web
- Utilisateurs/tiers : des projets tiers rapportent que le manifeste répond 200 en accès scripté, que la page catalogue renvoie 202 vide et que le JSON Blacklight reçoit un défi (voynich#55 lu ; reste « résumé de moteur, non vérifié »).
- Tickets : voynich PR #55 : « the manifest route is a different endpoint and was never blocked » ; mnemosyne PR #24 sans règle de débit.
- Institution : service catalog, FAQ 2012 (ci-dessus) ; aucune politique de bots.
- Présentations : aucun exposé de l'institution sur les limites (Samvera Connect 2017 : résumé de moteur, non vérifié).

## Pourquoi pas publié ?
Hypothèse : le WAF AWS protège l'interface HTML et la recherche JSON contre le trafic automatisé sans que la limite soit chiffrée en public ; la doc officielle parle d'accès « sans restriction de visibilité ».

## Conclusion
Limite chiffrée : aucune publiée. Observé : défi WAF sur les pages HTML (pas un quota) ; manifeste en 200. Contact : service desk `library.helpdesk@yale.edu` (page du catalogue de services) et formulaire d'aide Digital Collections. Confiance : faible (OAI et images non testés). Crash test (g) impossible à ce stade (défi WAF actif).
