# Thüringer Universitäts- und Landesbibliothek – Jena (`thuringer-universitats-und-landesbibliothek-jena`)

- **Classeur** : GLAM-075 · Allemagne · audit du 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `zs.thulb.uni-jena.de` (journals@UrMEL, MyCoRe/JPortal), `collections.thulb.uni-jena.de` (Collections@UrMEL), `www.thulb.uni-jena.de` (site TYPO3), `www.urmel-dl.de`, `www.db-thueringen.de` (cités).

## Sources
- Pages lues : accueil et pages « Digitales Kultur- und Sammlungsmanagement », « Open Access », Impressum, Benutzungsordnung de `www.thulb.uni-jena.de`, imprint/privacy/journals de `zs`, impressum/privacy de `collections`, accueil d'UrMEL et de db-thueringen (`sources/a1`, `sources/a2`, hachées dans les `SHA256SUMS`).
- Seule mention d'interfaces : « die Daten können über eine offene Schnittstelle (z. B. OAI-PMH, REST oder IIIF) abgerufen werden » (page Digitales Kultur- und Sammlungsmanagement, `sources/a2/text/03.txt`). **Aucune URL d'API, aucun quota, aucune limite de débit, aucune politique de bots** dans les pages lues. Les liens `rsc/feed/global/atom_1.0` et `rss_2.0` sont donnés par la page d'accueil de `zs`.
- robots.txt (`sources/robots`, `sources/a2`) : `zs` : `Crawl-delay: 10`, `Disallow: /*?`, `/servlets/`, `/browse/`, `/rsc/`, `/api/` ; `collections` : idem + `Allow: /servlets/MCRFileNodeServlet/` ; `db-thueringen.de` : idem avec `Allow: /api/v1/objects/` et `/api/v2/objects/` ; `www.thulb` : TYPO3 standard, pas de Crawl-delay ; `www.urmel-dl.de/robots.txt` : renvoie la page d'accueil HTML (pas de robots.txt) ; `iiif.thulb.uni-jena.de` : DNS inexistant.

## Tests (5 passes, 16 requêtes, pause 10 s = Crawl-delay ; `/rsc/` et `/api/` interdits par robots, lancés avec l'accord de Marcel, option C12)
Flux Atom et RSS `zs` : **200** · page d'objet `/receive/jportal_jparticle_01582058` : **200** · image IIIF v2 (vignette 512) : **200** · `info.json` IIIF Image v2 (niveau 2, `access-control-allow-origin: *`) : **200** · page visionneur : **200** (donne `metsURL`) · sitemaps de `collections` : **200** · `iiif-module.js` : **200** (donne le motif du manifeste) · METS `MCRMETSServlet` : **200** · page d'objet `collections` : **200** · manifeste IIIF Presentation v2 `/api/iiif/presentation/v2/jportal_derivate_00401748/manifest` : **500** (erreur serveur, corps HTML ; réponse réelle, pas de nouvelle tentative). Aucun 429, aucun 403, aucun en-tête de limite (`x-reputation: OK (-0.21)` seul en-tête inhabituel).
OAI-PMH et REST : la doc ne donne pas d'URL, non testés (aucune URL devinée).

## Web (4 recherches)
Aucune politique, plainte ni ticket propre à ThULB/UrMEL trouvé. Indices (résumés de moteur, non vérifiés) : UrMEL « registrierter OAI 2.0 Data Provider » ; présentation DigiCULT 2023 (ThULB DAM sur MyCoRe, IIIF et Massendownload comme interfaces standard) non confirmée par la lecture du PDF.

## Conclusion
Aucun quota publié ; Crawl-delay 10 s dans les robots.txt de `zs`, `collections` et `db-thueringen`. IIIF Image v2 répond en 200 sans en-tête de limite ; le manifeste testé a répondu 500. Contact : urmel_auskunft@thulb.uni-jena.de. Confiance : moyenne.
