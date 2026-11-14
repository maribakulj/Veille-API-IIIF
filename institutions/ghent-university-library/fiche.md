# Ghent University Library (`ghent-university-library`)

- **Classeur** : GLAM-016 · Belgique · **Vérifié le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Chaîne d'hôtes** : `adore.ugent.be/IIIF/manifests/…` (302) → `resolver.lib.ugent.be` (301) → `libcatalog.ugent.be` (Primo, manifeste IIIF 3) → images `eu-img02.ext.exlibrisgroup.com` (Ex Libris).

## Sources
- `adore.ugent.be` et `resolver.lib.ugent.be` : `robots.txt` 404 (autorisé). `lib.ugent.be/robots.txt` : `Allow: /`. `libcatalog.ugent.be/robots.txt` : **`Crawl-delay: 10`**, Disallow `/primaws`, `/discovery/search`, `/nde/search` ; GPTBot, Applebot, Yandex bloqués.
- Aucune page de documentation d'API, de conditions d'usage ou de politique de bots trouvée sur `lib.ugent.be` (pages d'accueil du catalogue = application Primo). Un identifiant d'exemple vient de la page Biblissima (tiers) : licence CC BY-SA 4.0 indiquée par les notices.

## Tests (4 passes, pauses de 6 s puis hôte Primo à Crawl-delay 10 : 1 seule requête sur cet hôte)
302 → 301 → **200** manifeste Primo (83 canevas) → **200** `info.json` et dérivé 200 px (2 930 octets) chez Ex Libris. Aucun 429, aucun en-tête de limite.

## Web
Aucune politique de débit ni de bots de Gand (recherches : seulement des notices Biblissima). 

## Conclusion
Limite chiffrée : seulement `Crawl-delay: 10` (Primo). Aucune limite observée. Confiance : moyenne à faible (pas de doc). Crash test : plafond 200/min, limite éventuelle côté Ex Libris, décision de Marcel utile.
