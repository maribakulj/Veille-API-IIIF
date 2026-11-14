# Biblioteca Nacional de España (`bne`)

- **Classeur** : hors 84 (ajouté) · Espagne · Refonte v2 le 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `datos.bne.es` (données liées, SPARQL), `bdh.bne.es` (ancienne BDH), `bdh-rd.bne.es` (visionneuse BDH), `bnedigital.bne.es` (BNE Digital, lancée fin 2025), `www.bne.es` / `bne.es` (site), `bnelab.bne.es` (BNElab).

## Sources
- Lecture directe le 2026-11-14 : `bnedigital.bne.es/robots.txt` : `User-agent: * / Disallow: /` (sauf Googlebot et bingbot : Allow /) ; `www.bne.es`, `bne.es` : robots Drupal, aucune règle sur IIIF ; `bnelab.bne.es` : WordPress standard ; `datos.bne.es` : 404. `bdh.bne.es`, `bdh-rd.bne.es`, `datos.bne.es/inicio.html`, `bnelab.bne.es/datos/`, `bne.es`, `bnedigital.bne.es/bd/es/simple`, `www.bne.es/en/catalogs/...` : **403 page de blocage Cloudflare** (non contourné ; ces hôtes arrêtés 24 h).
- Via Wayback (sources/wayback/bne-pages-via-wayback.md) : données sous CC0, SPARQL, téléchargements complets, contact `info.datosenlazados@bne.es` et `bnelab@bne.es` ; règles de reproduction (PDF) ; robots de bdh-rd.bne.es (Disallow /json/, /oai.vm, /pdf.raw...). Aucune doc d'API IIIF, aucune limite de débit.

## Tests
Aucune requête de sonde sur les hôtes en 2026-11-14 : tous bloqués (403) dès la lecture de leur doc. Les cinq requêtes du 2026-11-13 (303, 404, 308, 301, 308 ; aucun en-tête de limite) ont été lancées avant le commit de leur configuration : archivées verbatim dans `tests/archive/`, non rejouables (403 actuel).

## Web (4 recherches)
Institution : licence Creative Commons Attribution 4.0 des images numériques de la BNE (procédure de reproduction, résumé de moteur) ; présentations : lancement de BNE Digital (CENL, 1er décembre 2025) ; utilisateurs et tickets : aucun résultat.

## Conclusion
Limite chiffrée : aucune trouvée. Règle écrite : données CC0 (datos.bne.es) ; images CC BY 4.0 (résumé de moteur). Le site est derrière un WAF Cloudflare qui bloque le client de veille (403) : accès IIIF non vérifiable. Confiance : faible.
