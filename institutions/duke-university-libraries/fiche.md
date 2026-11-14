# Duke University Libraries (`duke-university-libraries`)

- **Classeur** : GLAM-044 · États-Unis · **Audit v2 le** 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôte** : `repository.duke.edu` (Duke Digital Repository, DDR), `library.duke.edu` (site).

## Sources
Aucune page de doc d'API (ni développeurs, ni IIIF) sur `library.duke.edu/repositories`, `repository.duke.edu/dc` ni sur le GitHub (`duke-libraries/ddr-public`, archivé en 2020). Capture Wayback de l'accueil du DDR avant le défi (sources/wayback) : pas de doc d'API non plus.
Politique de bots, lue en entier : `library.duke.edu/using/off-campus/impact-of-bots` (sources/b) : robots.txt à respecter, « a crawl delay of at least 10 seconds », pas de téléchargements « systematic, bulk, or automatic » de ressources, compte bloqué au-delà de 500 Mo en 30 min pour les ressources proxifiées ; Anubis (preuve de travail) déployé depuis juin 2025. `robots.txt` de `repository.duke.edu` : `Crawl-delay: 10` et Disallow des recherches/facettes.

## Tests (1 passe, 2 requêtes : robots.txt + `/dc`, pause 10 s)
Première tentative archivée (`tests/archive/`, commit de la configuration refusé par le crochet) puis rejeu conforme : `https://repository.duke.edu/dc` répond **200** mais avec la page de défi Anubis (« Making sure you're not a bot! »). C'est un défi JavaScript anti-bot : hôte arrêté, aucun contournement. Aucun 429 ni en-tête de limite. Manifestes et images IIIF non testés (aucune URL documentée, hôte en défi).

## Web (4 catégories)
Institution : page impact-of-bots (lue). Présentations : rapport du pilote Anubis (DukeSpace, PDF non lu : téléchargement interrompu ; résumé de moteur). Utilisateurs et tickets : aucun résultat.

## Conclusion
Limite chiffrée de débit pour l'API : aucune. Règles écrites : crawl-delay 10 s, robots.txt, pas de moissonnage systématique des documents sous licence. Accès : refusé à ce client par défi Anubis (donnée, pas un quota). À faire à la main : voir les liens manifeste dans un navigateur et lire le rapport Anubis. Crash test (g) : impossible (hôte en défi). Confiance : moyenne.
