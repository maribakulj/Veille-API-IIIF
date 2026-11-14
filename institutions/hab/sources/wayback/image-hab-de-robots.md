# image.hab.de/robots.txt : lecture par Wayback (hôte en 403, non contourné)

- Requête directe (fetch_doc.sh, 2026-11-14T03:19:55Z) : HTTP 403 Forbidden (Apache/2.4.66), voir sources/portraits2/FETCH.log. L'hôte image.hab.de est donc arrêté pour tous les appels suivants ; aucun test dessus.
- Outil MCP internet-archive, `ia_find_snapshots` (mode history) sur `image.hab.de/robots.txt` : captures de juillet 2024 à mars 2026.
  Extraits verbatim du résultat : `"timestamp":"20260301084431","replay_url":"https://web.archive.org/web/20260301084431/https://image.hab.de/robots.txt","statuscode":"404"` ; `"timestamp":"20251101012716" ... "statuscode":"404"` ; `"timestamp":"20240708220326" ... "statuscode":"404"`.
- Constat : toutes les captures datées renvoient 404 (ou revisit) : aucun robots.txt n'a jamais été publié sur cet hôte d'après Wayback. Le contenu des captures n'a pas été relu par ia_get_snapshot (une 404 n'a pas de texte à extraire).
- Le 403 actuel est un refus Apache générique (« You don't have permission to access this resource »), sans page de défi ni nom de produit anti-bot : ce n'est pas établi comme un quota. Nature non déterminée.
