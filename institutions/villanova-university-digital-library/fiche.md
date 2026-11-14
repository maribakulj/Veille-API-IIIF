# Villanova University – Digital Library (`villanova-university-digital-library`)

- **Classeur** : GLAM-055 · États-Unis · **Vérifié le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `digital.library.villanova.edu` (VuDL/VuFind, Fedora + serveur IIIF), `library.villanova.edu` (site Falvey).

## Sources
Doc de l'institution lue : site Falvey (`sources/b`, `sources/c`), robots.txt de `library.villanova.edu` (Crawl-delay 10 pour `*`, nombreux robots d'IA interdits). L'hôte `digital.library.villanova.edu` est en **403** dès robots.txt : pages lues par Wayback (`sources/wayback/`, captures de 2025 et 2024) : aucune mention de quota, d'API ou de bots. Contact : `digitallibrary@villanova.edu`.

## Tests (1 passe, 2 requêtes)
robots.txt : **403** ; page d'accueil : **403** (`server: Microsoft-Azure-Application-Gateway/v2`, corps « We could not process this request »). Arrêt de l'hôte. Le manifeste `…/Item/vudl:92879/Manifest` cité par un ticket tiers n'est pas testé. Refus d'accès à notre client, **pas un quota**. Étape g impossible.

## Web
Institution : robots.txt Falvey. Utilisateurs : aucun résultat (résumé de moteur, non vérifié). Tickets : GitLab DLG #62 (manifeste Villanova importé dans Spotlight, sans mention de limite) et README de VuDL (Cantaloupe, rien sur les limites). Présentations : aucune politique d'API trouvée (résumé de moteur, non vérifié).

## Conclusion
Aucune limite chiffrée publiée ; API non testable (403). À vérifier à la main : voir `a_verifier_manuellement`. Confiance : faible.
