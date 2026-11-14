# David Rumsey Map Collection (`david-rumsey-map-collection`)

- **Classeur** : GLAM-060 · États-Unis · **Vérifié le** 2026-11-14 par Sonnet 5.5 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôte** : `www.davidrumsey.com` (LUNA Viewer, serveur Apache). Contact : `carto@davidrumsey.com`.

## Sources
Pages lues (`sources/a` à `d`) : accueil, à propos, droits et permissions (« Creative Commons », contact `carto@davidrumsey.com`), FAQ, robots.txt, documentation LUNA Imaging (éditeur) sur IIIF. Aucune page de l'institution ne parle de quota, de débit ni de bots. **robots.txt** : `Crawl-Delay: 500` pour `*` ; Disallow sur `/luna/servlet/as/`, `/luna/servlet/view/search`, `/luna/servlet/search`, export, login, rss, widget, annotation.

## Tests (2 passes, 9 requêtes, pause 500 s : Crawl-Delay)
Passe 1 : manifeste IIIF 2 **200** (en-têtes `ratelimit-limit: 5.0`, `ratelimit-reset: 1`) · collection IIIF de groupe **200** · `fetchMediaSearch` (Disallow, lancé avec l'accord de Marcel, C12) **200**.
Passe 2 : `info.json` image IIIF 2 **200** · miniature 96 px **200** · IIIF Search 1.0 **200** · liste d'annotations **200**. Aucun 429, aucun défi. Le seul en-tête de limite vu est sur le manifeste ; son unité n'est pas documentée.
Non testés : collection IIIF de résultat de recherche (identifiant généré par clic) et téléchargement JP2 (très volumineux).
Écart reconnu : les 13 pages de doc ont été téléchargées à ~3 s d'écart par `fetch_doc.sh` avant l'application du Crawl-Delay 500 s aux sondes.

## Web
Institution : droits et permissions. Utilisateurs : fil iiif-discuss (redirection vers une page de connexion Stanford, CORS : pas un quota) ; recherche sur les robots/reCAPTCHA : aucune plainte propre à Rumsey (LUNA propose reCAPTCHA v3 depuis la 7.5.5.6, résumé de moteur, non vérifié). Tickets : aucun résultat. Présentations : doc LUNA (exemples de manifestes Rumsey, aucune limite).

## Conclusion
Limite chiffrée : aucune publiée ; `ratelimit-limit: 5.0` observé sur le manifeste (unité non documentée) ; Crawl-Delay 500 s = consigne de politesse. Confiance : moyenne. Crash test préparé : `config/crash-info-json.json` (à lancer à la fin).

## Crash test (étape g)

Crash test fait le 2026-11-14 : image-info-json sur www.davidrumsey.com : aucun blocage jusqu'à 200 req/min (plafond 200 req/min).
Journal : `tests/crash/david-rumsey-map-collection.log`. Un test « sans blocage » n'est pas une preuve d'illimitation au-delà du plafond.
