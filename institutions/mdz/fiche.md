# Bayerische Staatsbibliothek / MDZ (Digitale Sammlungen) — `mdz`

- **Statut** : audit v2 complet a à f (rejeu v3 du 2026-11-14) ; crash test (g) préparé, non lancé (C15)
- **Pays** : Allemagne
- **Vérifié le** : 2026-11-14 (UTC, sonde 01:39-01:41)

## Sources
Doc officielle lue en entier (sources/ : interfaces EN/DE, FAQ EN/DE, download-options, technologies, disclaimer, contact, mentions, aide, doc OAI-PMH BDR sur oai.bsb-muenchen.de) ; robots.txt de 4 hôtes (sources/robots/) ; réplique Wayback de l'OAI Identify (sources/wayback/bdr-oai-identify.md).

- `https://www.digitale-sammlungen.de/en/interfaces` : « Please note that there is a limit to the number of requests that can be made to the Image API per 24 hours. » ; « there is a limit to the number of OCR downloads that can be made per 24 hours. Access to the Presentation API is unlimited. » Aucun chiffre, aucun 429/Retry-After cité, `Access-Control-Allow-Origin: *`.
- `download-options` : « The maximum order size per day/user is limited » (commandes PDF/DaFo, hors API IIIF), sans chiffre.
- FAQ, search-help, technologies, disclaimer, contact : aucune règle de débit.
- OAI-PMH BDR (oai.bsb-muenchen.de/doc/en/bavarian-digital-repository) : endpoint `http://bdr.oai.bsb-muenchen.de/OAIHandler`, CC0, contact oai@bsb-muenchen.de ; aucune limite citée.
- robots.txt : www = `Disallow:` vide ; api = 404 ; oai = `Disallow: /verovio`, `Crawl-delay: 5` (notre pause de 6 s le respecte) et plusieurs robots d'IA/SEO exclus ; bdr = 500 (fetch_doc) puis 403.

## Tests (passe 1, config mdz-passe1.json committée au commit 21b73aa avant lancement ; 12 requêtes dont 3 robots.txt)
| Endpoint | Statut | En-têtes de limite |
|---|---|---|
| manifeste (2 exemples de la doc non rejoués : 1 manifeste) | 200 | aucun |
| manifeste 2 (bsb00130380_00157_u001) | 200 | aucun |
| collection/top | 200 | aucun |
| Image info.json | 200 | aucun |
| Image full/200, | 200 | x-ratelimit-limit 25001, remaining 25000, reset 3 |
| Image full/full (exemple doc) | 200 | idem |
| OCR hOCR | 200 | x-ratelimit-limit 5001, remaining 5000, reset 17 |
| RSS mdz.xml | 200 | aucun |
| OAI BDR Identify | 403 Apache | arrêt de l'hôte, a_verifier_manuellement + Wayback |

Anciennes sessions (21:04-21:07Z, et mdz-nouveaux.json non committée du 21:20Z) archivées verbatim dans `tests/archive/` ; elles montraient la même chose (x-ratelimit identique entre deux appels : remaining ne décroît pas, ce n'est pas un compteur en direct).

## Web (étape f, 4 catégories)
- **institution** : page interfaces (officielle) ; GitHub dbmdz (wolpi) : aucune mention de quota.
- **utilisateurs** : aucun résultat spécifique à MDZ (requête 429 / too many requests / blocked ; résumé de moteur, non vérifié).
- **tickets** : sourcelibrary-v2 #5448 (lu en original, 2026-10 à 11) : demande d'IP autorisée envoyée à mdz@ le 01/10, réponse toujours en attente ; « 622 of the failures are MDZ over-quota placeholder images » ; images 1x1 de 457 octets en 200 au dépassement (affirmation d'un tiers, non vérifiée par nous) ; débit estimé ~22 000 pages/jour (tiers). Mirador #4542 : canvases 1x1 d'un manifeste BSB, sans lien avec un quota.
- **presentations** : KIMWS 2017 (BSB, IIIF), résumé de moteur seul (original en timeout), aucune limite signalée.

## Conclusion
Quotas par 24 h existants mais non chiffrés (Image, OCR) ; Presentation annoncée illimitée. En-têtes x-ratelimit-* présents sur Image/OCR (limit 25001 et 5001) mais non documentés et sans décompte visible. Au dépassement, un tiers rapporte un placeholder 1x1 en 200 plutôt qu'un 429 : à détecter par les clients. OAI-PMH BDR inaccessible à la sonde (403) : à vérifier à la main. Aucun 429 reçu. Pourquoi non publié : hypothèse (non établie) : protection anti-abus ; la FAQ invoque des contraintes de « data volumes and budget » sans lien direct. Contact : mdz@bsb-muenchen.de.
