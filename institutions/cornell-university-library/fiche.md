# Cornell University Library — portail Digital Collections (`cornell-university-library`)

- **Classeur** : GLAM-043 · États-Unis · audit v2 du 2026-11-14 (Sonnet 5.5) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôte IIIF documenté** : `digital.library.cornell.edu` (portail Blacklight + Solr + IIIF). Hôtes lus : `www.library.cornell.edu`, `guides.library.cornell.edu`, `digitalscholarship.library.cornell.edu`, `cornell-colab.github.io`.

## Sources
- **About** du portail (Wayback, capture 2026-01-01) : « powered by Blacklight, Solr, and IIIF » ; aucune URL d'API ni de quota. Extraits dans `sources/wayback/digital-library-cornell.md`.
- **Guidelines for Using Materials from Our Collections** (`library.cornell.edu/libraries/policies/using-media-from-collections/`, lu en direct, `sources/a2`) : droits d'auteur, domaine public « may be used for free without permission » ; aucune règle de débit.
- Terms of Use de la collection `aerialny` (Wayback) : libre usage pour étude et recherche ; aucune limite de débit.
- Guides de humanités numériques (`digitalscholarship`, `guides`, `cornell-colab.github.io`) : comment publier ses propres manifestes ; **Cornell ne figure pas dans leur liste de dépôts IIIF**. Aucun quota.
- **robots.txt** : `digital.library.cornell.edu` 403 en direct (Wayback du 2026-04-27 : un commentaire seul, tout autorisé) ; `www.library.cornell.edu` : `Disallow: /wp-admin/` ; `guides.library.cornell.edu` : **`Crawl-delay: 10`** pour `*` et robots d'IA nommés en `Disallow: /` ; `digitalscholarship` : pas de robots.txt ; `iiif.library.cornell.edu` : DNS inexistant.

## Tests
2 requêtes vers `digital.library.cornell.edu` (robots.txt par `fetch_doc.sh`, puis `/about` par la sonde, configuration committée avant) : **403 Forbidden** nginx de 118 octets, sans page de défi, aucun en-tête de limite. Hôte arrêté, aucun contournement. IIIF Presentation et Image du portail : non testés (la doc ne donne aucune URL d'API ; l'hôte refuse notre client). Aucun 429.

## Web (4 catégories)
- institution : page des lignes directrices lue ; aucune politique de bots/débit.
- utilisateurs : aucun résultat sur des 403/429 Cornell (seulement des articles généraux sur les bots d'IA, résumé de moteur, non vérifié).
- tickets : aucun résultat sur un outil tiers interrogeant `digital.library.cornell.edu`.
- présentations : billet DSPS 2016 sur le lancement du portail (résumé de moteur, non vérifié) ; aucune politique d'API.

## Conclusion
Limite chiffrée : aucune pour le portail. Seule valeur écrite : Crawl-delay 10 s sur `guides.library.cornell.edu` (autre service). Le 403 est un refus d'accès à ce client, pas un quota. À refaire depuis un navigateur ou par demande écrite via le formulaire de contact du portail. Confiance : faible. Crash test (g) impossible : aucun hôte testable.
