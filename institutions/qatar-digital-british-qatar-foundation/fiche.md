# Qatar Digital Library — British Library / Qatar Foundation (`qatar-digital-british-qatar-foundation`)

- **Classeur** : GLAM-083 · Qatar · Audit v2 du 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `www.qdl.qa` (site, manifestes IIIF Presentation), `iiif.qdl.qa` (images IIPImage, IIIF Image API 2).

## Sources (étape a)
- **Blocage** : `www.qdl.qa/robots.txt` et `iiif.qdl.qa/robots.txt` : **403 Cloudflare « Just a moment... »** (défi) le 2026-11-14 à 02:55Z. Les deux hôtes sont arrêtés (registre partagé) ; aucun contournement ; toute la doc est lue par Wayback (`sources/wayback/`).
- **robots.txt de www.qdl.qa** (Wayback 2026-03) : `Crawl-delay: 10` ; interdits : recherches, `*/archive/*/search/`, `*/universal-viewer/*`, `*/mirador/*` ; les manifestes `/en/iiif/.../manifest` ne sont pas interdits. `iiif.qdl.qa` : pas de robots lisible.
- **Image options** : IIIF Image API 2.0 sur `iiif.qdl.qa/iiif/images/...` ; « The maximum size of an image that can be retrieved is currently fixed at 1200 pixels at its largest size » ; manifeste : remplacer `archive` par `iiif` et ajouter `/manifest` dans l'URL de l'archive. Aucune limite de débit.
- **Terms of use** : usage personnel et licite ; interdiction des attaques DoS/DDoS ; aucun quota chiffré. Page « Copyright & ethical terms of reuse » : sans capture Wayback, non lue.

## Tests
Aucune requête envoyée (0) : hôtes en 403/défi, la sonde a sauté les 2 endpoints (`tests/journal.log`, « NON LANCÉ : hôte arrêté »).

## Web (étape f)
- Institution : pages officielles lues (Wayback).
- Utilisateurs et tickets : aucun résultat (deux recherches) ; les outils génériques de téléchargement IIIF existent, aucun ticket QDL.
- Présentations : communication IFLA 2019 (lue) sur QDL et les API IIIF ; aucun chiffre de débit.

## Conclusion
Limite chiffrée de débit : aucune publiée ; seule limite documentée : image à 1200 px au maximum ; `Crawl-delay: 10` dans robots.txt. Accès automatisé refusé par Cloudflare (403 anti-bot, pas un quota). Confiance : faible. Crash test impossible. Une demande écrite à QDL (page « Comments or concerns ») ou un test depuis un navigateur seraient nécessaires.
