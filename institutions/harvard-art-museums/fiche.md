# Harvard Art Museums — `harvard-art-museums`

- **Statut** : audit v2 complet a à f (2026-11-14) ; crash test (g) préparé, non lancé (C15)
- **Pays** : États-Unis ; **Vérifié le** : 2026-11-14 (UTC, 01:51-01:56)

## Sources
Page https://harvardartmuseums.org/collections/api, conditions d'utilisation, licences, FAQ, contact, vie privée, dépôt GitHub harvardartmuseums/api-docs (README, sections/iiif, image, object), robots.txt de 6 hôtes (sources/a1 à a6).

- README : « Respect other users of the API by limiting the number of API calls to 2500 per day. » ; « We reserve the right to block or cancel your access to the API service without prior notice. » ; clé obligatoire (« Requests that contain a bad, invalid, or missing API key will return a 401 Unauthorized error. ») ; usage non commercial ; cache limité à deux semaines.
- sections/iiif.md : « The IIIF image and presentation services are separate from our main data API. They do not require an access key. » Aucune limite chiffrée pour l'IIIF.
- robots.txt : api et nrs = `Disallow: /` pour `*` (passé outre avec l'accord de Marcel, C12) ; iiif, ids.lib : 404 ; mps.lib : indisponible ; site principal : seulement des robots d'IA exclus.

## Tests (3 passes, configurations harvard-passe1/2/3 committées avant lancement ; 15 requêtes dont 5 robots.txt)
Passe 1 : API /object sans clé 401 (une seule requête, aucune clé utilisée) ; IIIF collection top, manifeste object 299843, manifeste gallery 1600 en 200 ; nrs.harvard.edu info.json et dérivé en 303 vers ids.lib.harvard.edu ; Mirador 3 en 200. Passe 2 : ids.lib.harvard.edu info.json 302 vers mps.lib.harvard.edu, dérivé 200 px 200. Passe 3 : mps.lib.harvard.edu info.json 200. Aucun en-tête de limite (x-ratelimit, Retry-After), aucun 429 reçu.

## Web (étape f)
- institution : README du dépôt GitHub de l'institution (2 500/jour).
- utilisateurs/tickets : issue publique api-docs #29 (28-29/04/2026, lue en original) : « HTTP 429 from ids.lib.harvard.edu — Tokyo AWS IP blocked at CDN level », blocage au niveau IP sur les téléchargements d'images, malgré environ une requête par 10 s ; réponse d'un contributeur Harvard : le problème est connu, pas de liste blanche, téléchargement en masse pas disponible pour l'instant. Autres tickets sans rapport avec le quota.
- presentations : deux pistes trouvées par moteur de recherche (article « The HAM API at 10 », présentation IIIF New England 2018), non lues (404 pour l'article) ; listées à vérifier.

## Conclusion
Limite documentée : 2 500 appels par jour sur l'API de données à clé (recommandation, avec droit de blocage), non vérifiée faute de clé. IIIF sans clé ni limite publiée, aucun en-tête de limite. Un blocage CDN par IP (429) sur l'hôte d'images ids.lib.harvard.edu est documenté par un tiers et confirmé par Harvard comme connu : risque réel pour des téléchargements depuis des IP de cloud, non observé depuis notre IP. Pourquoi non publié : hypothèse non établie : la limite d'images est appliquée par un CDN d'infrastructure (Harvard Library) et non par le musée ; Harvard dit « researching and testing options ».
