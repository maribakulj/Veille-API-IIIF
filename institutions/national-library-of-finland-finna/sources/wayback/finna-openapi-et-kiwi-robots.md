# Finna — compléments lus dans la Wayback Machine (outil ia_get_snapshot, 2026-11-14)

Aucun trafic envoyé à Finna. api.finna.fi et www.kiwi.fi répondent 403 à notre sonde (non contourné).

## 1. Spécification OpenAPI de l'API Finna — capture 2025-08-10 (20250810185213), 120 599 caractères, lue en entier (3 pages)
Réplique : https://web.archive.org/web/20250810185213/https://api.finna.fi/api/v1/?openapi
(Le Swagger « https://api.finna.fi/v1?swagger » n'a qu'une capture 2023 en redirection 302, sans contenu.)

> "title": "Finna.fi", "version": "10.1.4", "description": "Finna REST API is a read-only interface to Finna's search index. Most methods return the data as UTF-8 encoded JSON […] The API supports Cross-Origin Resource Sharing by setting the Access-Control-Allow-Origin HTTP header to * for all requests.", "termsOfService": "https://www.kiwi.fi/display/Finna/Finna+API+Terms+of+Use"

> /search, /record, /list (chemins relatifs à /api/v1). Paramètre limit : "Records to return per page. Set to 0 to return no records." minimum 0, maximum 100, default 20.

> resumptionToken : "A large result set can only be downloaded in batches. You can initiate a batch download by setting resumptionToken to a single asterisk `*`. Each batch will then return a resumptionToken value to use for the next batch […]" ; « The following parameters are not available with resumptionToken: limit, page, facet[] ».

Recherche dans le texte des mots rate, limit (hors paramètre limit), 429, throttl, quota, excessive, too many : aucune mention d'une limite de débit ni d'un code 429 dans la spécification.

## 2. https://www.kiwi.fi/robots.txt — capture 2026-05-04 (20260504140906), 397 caractères
Réplique : https://web.archive.org/web/20260504140906/https://www.kiwi.fi/robots.txt

> User-agent: * / Content-Signal: search=yes, ai-train=no, ai-input=no / Disallow: / / Crawl-delay: 5 (puis Allow vide pour Googlebot, BingBot, ia_archiver, archive.org_bot, Google Scholar, DuckDuckBot, MSNbot, Baidu, YandexBot)

## 3. https://www.kiwi.fi/robots.txt — lu en direct le 2026-11-13 (sources/raw/07.html)
Version « Cloudflare Managed content » : `User-agent: *` avec `Content-Signal: search=yes,ai-train=no,use=reference` et `Allow: /` ; robots d'IA nommés (ClaudeBot, GPTBot, anthropic-ai…) en `Disallow: /`. Notre User-Agent n'est pas nommé : « * » s'applique. Le wiki ne contient que de la documentation (aucune API) ; ses pages répondent 403 (Cloudflare) à notre client, donc non lues en direct. Les deux versions du robots.txt diffèrent (mai 2026 : Disallow / avec Crawl-delay 5 ; nov. 2026 : Allow /) : le plus prudent est retenu, aucune requête vers kiwi.fi hors la lecture du robots.txt.
