# Extrait Wayback — https://artgallery.yale.edu/robots.txt (défi Cloudflare 403 en direct)
Réplique : https://web.archive.org/web/20260501015815/https://artgallery.yale.edu/robots.txt (capture du 2026-05-01, 200). Lu en entier via MCP internet-archive le 2026-11-14 ; pas de Crawl-delay ni de Request-rate.

> User-agent: *  [...règles Drupal : Disallow /core/, /admin/, /search/, /user/... ; Disallow: /collection/search/grid* ; Disallow: /collection?* ; Allow: /collection?page= ; Disallow: /collection?page=*&*]
> #Block AI crawlers  User-agent: AddSearchBot ... ClaudeBot ... GPTBot ... Scrapy ... img2dataset ... (liste de ~150 agents d'IA et de moissonnage)  Disallow: /

Le robots.txt bloque entièrement environ 150 agents d'IA ou de moissonnage nommés ; notre User-Agent (VeilleAPIIIF/0.1) n'y figure pas et relève du groupe « * ».
