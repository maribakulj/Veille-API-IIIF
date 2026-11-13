# Finna — extraits verbatim lus dans la Wayback Machine (outil ia_get_snapshot, lus le 2026-11-13)

Raison : `api.finna.fi`, `www.finna.fi` et `www.kiwi.fi` (wiki) renvoient 403 à notre sonde (anti-bot) ; on n'insiste pas. Aucun trafic envoyé à Finna. Extraits recopiés à la main (curl sur Wayback refusé par le système).

## 1. https://api.finna.fi/robots.txt — capture 2025-05-31 (20250531011820), 27 caractères
Réplique : https://web.archive.org/web/20250531011820/https://api.finna.fi/robots.txt

> User-agent: *
> Disallow: /

## 2. https://finna.fi/robots.txt — capture 2026-05-02 (20260502071508), 1833 caractères
Réplique : https://web.archive.org/web/20260502071508/https://finna.fi/robots.txt

> User-agent: * … Crawl-delay: 1 … Disallow: /*/api/ … Disallow: /SearchApi/ … Disallow: /Search/ … Disallow: /Browse/ … Disallow: /AJAX/ …
> (bloqués entièrement : anthropic-ai, ClaudeBot, Claude-Web, CCBot, ChatGPT-User, GPTBot, Google-Extended, Bytespider, Diffbot, SemrushBot, PetalBot, etc.)

## 3. Finna API Terms of Use — capture 2025-06-12 (20250612130525), 4513 caractères
Réplique : https://web.archive.org/web/20250612130525/https://www.kiwi.fi/display/Finna/Finna+API+Terms+of+Use

> No registration is required to use the open application programming interface (API) of the Finna.fi service. The National Library may, however, choose to introduce registrations if the functions of the interface must be restricted, e.g., to avoid excessive server load.

> The metadata provided through the interface is licenced under the Creative Commons CC0 1.0 Universal Public Domain Dedication. […] Use of the linked resources must comply with the terms of use indicated with the resource or in the fields imageRights and accessRestrictions.

> It is recommended, however, that the source of the data, i.e. the Finna.fi service, be mentioned […] as well as the organisations which produced the data.

Aucun chiffre de débit.

## 4. Page « Finna API Documentation In English » — capture 2026-01-26 (20260126231351)
Réplique : https://web.archive.org/web/20260126231351/https://www.kiwi.fi/spaces/Finna/pages/440828359/Finna+API+Documentation+In+English
Liste : Finna API (in English), Finna API Terms of Use, Authentication API, OAI-PMH Harvesting Interface, OIDC Provider.

## Non lu
« Finna API (in English) » (spécification Swagger `https://api.finna.fi/v1?swagger`, doc principale) : 403 live, aucune copie Wayback trouvée (3 URL essayées). Les limites éventuelles qu'elle contient (`limit` 0–100, 100 000 résultats max, rapportés par une recherche web) ne sont pas vérifiées dans l'original.
