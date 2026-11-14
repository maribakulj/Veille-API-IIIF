# Wayback — https://open.library.ubc.ca/docs (lecture directe : page « Your request was blocked because our system detected unusual activity », HTTP 200, 4935 o)
Réplique lue : https://web.archive.org/web/20260216142418/https://open.library.ubc.ca/docs (capture du 2026-02-16, statut 200, titre « API Documentation - UBC Library Open Collections »).
Extraits verbatim :
- « To use the Open Collections APIs, you should first register for an API Key : Unregistered users will be limited in the number of requests that can be made. »
- « To control abuse, users are encouraged to register their email address to receive an Open Collections API Key. [...] Unregistered users will be limited in the number of requests that can be made. »
- Paramètre `key` : « Api key — Requests without an api key will be rate limited »
- « https://oc-index.library.ubc.ca is the base URL of the Open Collections API. »
- Endpoints REST (tous GET sauf un POST) : `collections`, `collections/:collection_identifier`, `collections/:collection_identifier/download/collection`, `collections/:collection_identifier/items`, `collections/:collection_identifier/items/:item_identifier`, `collections/:collection_identifier/_total`, `/search/help`, `/search/8.5` (GET), `/search/8.5` (POST, Query DSL).
- Exemples : `https://oc-index.library.ubc.ca/collections/arkley/items/1.0013125` ; `https://oc-index.library.ubc.ca/search/8.5?q=cat` ; paramètre `size` : « Number of responses — 20 ».
- OAI-PMH : « Note: To access Open Collections’ OAI-PMH you need to use a registered api_key in your request header. » ; base `https://oce-index.library.ubc.ca/oai?verb=Identify`.
- IIIF : « Requests can be made to the Open Collections IIIF Endpoint using IIIF 2.0 syntax at: https://iiif.library.ubc.ca » ; exemple `http://iiif.library.ubc.ca/image/cdm.tokugawa.1-0213163/full/1600,900/0/default.png` ; « the item identifiers need to have the dot replaced with a dash to work with the IIIF API. For instance '1.0001258' would become '1-0001258' ».
- « Before using the APIs, please review and comply with our terms of use. » (lien non résolu dans la capture)
Aucun chiffre de limite de débit n'est donné.
