# Huntington Library, Art Museum and Botanical Gardens — `huntington-art-museum-botanical-gardens`

- **Statut** : audit méthode v2 complet à l'exception de l'étape g (crash test, à la fin ; configuration prête : `config/crash-info-json.json`)
- **Pays** : États-Unis (GLAM-058)
- **Hôtes** : `hdl.huntington.org` (Huntington Digital Library, CONTENTdm), `cdm16003.contentdm.oclc.org` (même instance, hôte OCLC), `www.huntington.org` (site vitrine, **429**), `huntington.emuseum.com` (eMuseum, **403**)
- **Vérifié le** : 2026-11-14 (UTC)

## Sources
| Source | Preuve |
|---|---|
| robots.txt de `hdl.huntington.org` et `cdm16003.contentdm.oclc.org` (identiques ; **Crawl-Delay: 1**) | `sources/doc/raw/01.html`, `04.html` |
| Guide de recherche « Collections Up Close » (manifestes IIIF, outil Exhibits) | `sources/doc/raw/05.html` |
| Doc OCLC CONTENTdm : IIIF Image et Presentation API ; robots.txt OCLC (Crawl-delay 5) ; guide IIIF pour la HDL | `sources/oclc/` |
| `www.huntington.org` : **429**, page « Vercel Security Checkpoint » | `sources/doc/raw/06.html`, `FETCH.log` |
| robots.txt de `www.huntington.org`, droits de la Library, « Using the Library », droits de l'Art Museum : lus via Wayback | `sources/wayback/*.md` |
| eMuseum : robots.txt 200 (Content-Signal), accueil **403** | `sources/emuseum/` |
| Recherches web (étape f) | `sources/web/` |

Aucune page du Huntington ne publie de quota, de limite de débit, de politique de moissonnage ni de documentation d'API : la page « Using the Library » dit seulement « High-resolution images can be accessed and downloaded for free ».

## Tests
Trois passes (`config/huntington-passe1-iiif.json`, `passe2-redirections`, `passe3-images`), journal `tests/journal.log`, en-têtes `tests/raw/`.
- Passe 1 : le motif documenté par OCLC `/iiif/info/{alias}/{id}/manifest.json` répond 301 puis 302 (vers `/iiif/2/{alias}:{id}/manifest.json`) ; `info.json` de l'identifiant composé 1503 : **501** « Unsupported source format ».
- Passe 2 : manifeste final 200 (376 ko, GET), 200 en HEAD sur hdl, manifestes de collection et du site : 200 (HEAD).
- Passe 3 : `info.json` (pattern documenté et pattern du manifeste) et vignette `full/150,/0/default.jpg` : 200 sur les deux hôtes.
- **Aucun en-tête de limite** (RateLimit-*, Retry-After, X-RateLimit-*) ; seul `x-oclc-iiif-provider: cantaloupe`. Aucun 429 sur `hdl.huntington.org` ni `cdm16003.contentdm.oclc.org`.
- Non testés : OAI `/oai/` (non documenté), eMuseum (403 Cloudflare), `www.huntington.org` (429 Vercel) : refus d'accès à notre client, pas des quotas.

## Web
- institution : droits de la Library (Wayback) : rien sur API ni débit ; guide IIIF de la HDL.
- utilisateurs : fil iiif-discuss sur `cdm16003.contentdm.oclc.org` (image `full/full` de résolution réduite) : pas de plainte de quota ; pas de fil sur un 429 (résumé de moteur, non vérifié).
- tickets : aucun résultat (requête GitHub sur les deux hôtes).
- presentations : étude de cas OCLC sur le Huntington (propos de l'équipe) : IIIF mis en avant, rien sur les quotas.

## Conclusion
Pas de quota publié : le HDL est une instance CONTENTdm hébergée par OCLC, dont la doc IIIF ne donne aucun chiffre. Seule règle écrite : `Crawl-Delay: 1` dans robots.txt. Aucun mécanisme de limitation observé (22 requêtes sur les hôtes d'API). Pourquoi pas publié : hypothèse, plateforme SaaS OCLC dont la politique est du ressort de l'éditeur ; non confirmé. À contacter : reference@huntington.org. Le site vitrine (Vercel) et l'eMuseum (Cloudflare) sont derrière des défis anti-bot : URL à vérifier à la main (onglet « À vérifier à la main »).
Décision prise seule : le 429 de `www.huntington.org` arrête cet hôte seulement ; les hôtes d'API (OCLC) ont été testés prudemment (≥ 6 s).
