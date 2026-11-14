# Österreichische Nationalbibliothek (ÖNB) — `osterreichische-nationalbibliothek-onb`

- **Statut** : audit méthode v2 complet a à f ; étape g (crash test) préparée, à lancer à la fin (consigne C15).
- **Pays** : Autriche (GLAM-027 du classeur de référence)
- **Hôtes** : `iiif.onb.ac.at` (API SACHA, IIIF 2.x), `api.onb.ac.at` (ÖNB-API, IIIF 3), `labs.onb.ac.at` (ÖNB Labs), `www.onb.ac.at`
- **Vérifié le** : 2026-11-14 (UTC), Sonnet 5.5, lot D

## Sources (étape a, d)

| Page | Dossier de preuve | Lecture |
|---|---|---|
| `api.onb.ac.at/` (ÖNB-API : IIIF Presentation 3.0 `/iiif/presentation/v3`, Image 3.0 `/iiif/image/v3`, Content Search 2.0 `/iiif/search/v2`, Search 1.0 déprécié `/iiif/search/v1`, REST `/rest/v1/ie/{ieId}/file|alto|txt|preview|thumbnail`) | `sources/doc/` (raw/01, text/01) | lue en entier ; contact `api@onb.ac.at` (« Questions, feedback or need access? ») ; **aucun quota, aucun en-tête, aucun exemple d'`ieId`** |
| `iiif.onb.ac.at/api/` (swagger SACHA v3.0, 15 routes) | `sources/doc/` (raw/03, text/03) | lue en entier ; section 2.3 « Mass Download Prevention » |
| `iiif.onb.ac.at/`, `/gui/demo.html`, `/gui/manifest.html` | `sources/doc/`, `sources/doc3/` | lues ; la page démo publie les identifiants d'exemple |
| `labs.onb.ac.at` : about, tools, terms, tool/sacha, datasets, tutorials, topic/iiif-jupyter, datasets/lod, dépôt GitLab How-To-ÖNB-API | `sources/doc/`, `sources/doc2/`, `sources/doc4/` | lues ; Nutzungsbedingungen ÖNB Labs (22/11/2018) sans clause de débit ; datasets et README GitLab rendus par JavaScript (voir « à vérifier à la main ») |
| `www.onb.ac.at/en/use`, `/en/legal-notice` | `sources/doc2/` | lues ; conditions de réutilisation (crédit demandé, restriction Google non commerciale), aucune limite de débit |
| robots.txt : `api.onb.ac.at` 404, `iiif.onb.ac.at` **400**, `labs.onb.ac.at` 200 (règles GitLab, `Crawl-delay` seulement en commentaire), `www.onb.ac.at` 200 (Disallow blogs) | `sources/doc/`, `sources/doc2/` | lus avec les yeux : aucun `Crawl-delay` ni `Request-rate` actif |

**Phrases utiles (verbatim)** : « Austrian National Library is contractually obliged to prevent digitized objects of its ABO collection from being downloaded as a whole. Therefore SACHA implements security measures tailored against mass downloading ABO objects. It is not recommended to send multiple concurrent requests or a lot of requests in a very short time, because this might prevent the server from responding to further requests. » (`iiif.onb.ac.at/api/`, 2.3) ; « Increasing the range might cause performance problems. » (collection, searchLimitFrom/To) ; « SACHA only offers digitized objects up until 140 years ago. »

## Endpoints (étape b)

SACHA (`iiif.onb.ac.at`) : images (info.json, redirection 303, image), mets, mods, manifest, canvas, annotation, list, sequence, resource, collection (GET), POST collection, visionneuses `/view/...`. ÖNB-API (`api.onb.ac.at`) : IIIF Presentation v3, Image v3, Search v2 et v1, REST v1. Détail et statut dans `data.json` (`endpoints_documentes`).

## Tests (étape e)

5 passes sur `iiif.onb.ac.at`, 17 requêtes de sonde au total (9 + 8 + 3 + 2 + 2, robots.txt compris), pauses ≥ 6 s, UA du projet, configurations committées avant chaque lancement (`config/onb-passe1…5`), journal `tests/journal.log`, en-têtes `tests/raw/`.
- Manifeste REPO/7445056, info.json, redirection 303 → info.json, image 150 px, mods ABO, mets (HEAD), collection `jerusalem`, manifeste AKON, canvas, sequence, visionneuses Mirador : **200**.
- `annotation/1` et `annotation/00000001` : **400** (« Canvas with this fileID doesn't exist on this manifest. ») ; `list/1` : 400 ; `list/00000001` : **404** (« Only projects that have lists are ABO and ANNO. ») ; `list/page1` sur ABO : **201** ; `resource/00000001.json` (identifiant lu dans la réponse précédente) : 200.
- **Aucun en-tête de limite** (`Retry-After`, `X-RateLimit-*`, `RateLimit-*` absents) dans les 17 réponses ; serveur `nginx` ; aucun 429, aucun 403. `access-control-allow-methods: GET, POST, DELETE, PUT` annoncé.
- **Non testé** : POST `/presentation/collection` (POST interdit par la méthode) ; ÖNB-API `api.onb.ac.at` (IIIF v3, Search, REST) : la doc ne publie aucun `ieId` d'exemple et les identifiants ne se devinent pas (l'exemple est dans un notebook Binder/GitLab illisible sans JavaScript).

## Web (étape f)

Quatre recherches, une par catégorie (14/11/2026).
- **institution** : la doc SACHA 2.3 (ci-dessus) ; rien d'autre.
- **présentations** : présentation IIIF Göttingen 2019, « Simple Access to Cultural Heritage Assets via ONB Labs » (`iiif.io/event/2019/goettingen/program/17/`, lue) : « SACHA provides an implemented IIIF interface, allowing both human users and automated computational tools » ; aucune limite ; page `labs.onb.ac.at/en/topic/iiif-jupyter/` (lue) ; diapositives ÖNB ImageDataMining (PDF, lues) : rien sur les quotas.
- **utilisateurs** et **tickets** : aucun résultat (requêtes dans `data.json`).

## Conclusion

Aucun quota chiffré, aucun en-tête de limite, aucune clé. La seule règle écrite est une **mise en garde sans chiffre** contre les requêtes concurrentes ou en rafale, motivée par l'obligation contractuelle d'empêcher le téléchargement intégral des objets ABO (mesures de sécurité non décrites, jamais déclenchées sur 17 requêtes espacées). Contact : `api@onb.ac.at` (ÖNB-API), `labs@onb.ac.at` (SACHA). Confiance moyenne : l'ÖNB-API v3 n'a pas pu être testée. Étape g : `config/crash-info-json.json` (plafond 200 req/min).
