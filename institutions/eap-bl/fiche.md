# British Library — Endangered Archives Programme (`eap-bl`)

- **Classeur de référence** : GLAM-003 · **Pays** : Royaume-Uni · **Hôtes** : `eap.bl.uk` (site), `iiif.bl.uk` (images, 403 anti-bot)
- **Vérifié le** : 2026-11-13, par Sonnet 5.5 (reprise complète ; la passe précédente de Haiku affirmait à tort qu'aucun endpoint n'était documenté)
- **Suivi des étapes** : `CONSIGNE-ET-SUIVI.md`

## Ce que la doc officielle dit

- **Endpoint documenté** : le manifeste IIIF. Page « Tools » (`eap.bl.uk/tools`) : « IIIF manifests are available for all archive images on our website », accessibles par l'icône IIIF ou en ajoutant `/manifest` à une URL `archive-file` (exemple : `eap.bl.uk/archive-file/EAP099-1-2-5-2/manifest`). Un outil de téléchargement JPEG exige ce manifeste.
- **Aucun** quota, en-tête de limite, clé, endpoint de statut, ni service d'image documenté.
- **robots.txt** de `eap.bl.uk` (lu en entier) : pour `User-agent: *`, **`Disallow: */manifest*`** (ligne 80), plus `/search/` et des chemins d'administration. **128 robots d'IA nommés** (dont ClaudeBot, GPTBot, anthropic-ai) sont bloqués (`Disallow: /`). Un `Crawl-delay: 2` est rattaché au seul groupe MegaIndex.ru. `www.bl.uk/robots.txt` : `Allow: /`.
- **Réutilisation** : haute résolution « maybe » fournie pour des publications non commerciales, mais « we are not able to do this for large numbers of images or whole collections ».
- **Conditions BL** (`bl.uk/terms`) : « Readers shall not systematically or programmatically download or print any Eresource » — portée « Readers » (lecteurs inscrits), à confirmer pour le site public de l'EAP.

## Contradiction à signaler

La page « Tools » présente les manifestes comme la voie d'accès aux images, mais `robots.txt` les interdit aux robots (`Disallow: */manifest*`). Depuis la consigne C12 de Marcel (14/11/2026), ce Disallow n'arrête plus le test : il est journalisé et la requête part.

## Tests (2026-11-14, `tests/journal.log`, configurations `config/eap-v2-passe1-manifeste.json` et `eap-v2-passe2-images.json`, committées avant lancement)

- Passe 1 (2 requêtes) : `robots.txt` de eap.bl.uk (200), puis le manifeste `eap.bl.uk/archive-file/EAP099-1-2-5-2/manifest` : 200, JSON IIIF Presentation 3, 126 749 octets, derrière Varnish/CloudFront, **aucun en-tête de limite**.
- Le manifeste annonce le service d'images `images.eap.bl.uk` (Image API 2, level2) : hôte nouveau, `robots.txt` lu avant la passe 2 (`sources/suite5`) : 404 après redirection, tout autorisé ; `iiif.bl.uk/robots.txt` : 404.
- Passe 2 (5 requêtes) : `info.json` et vignette `full/!128,128` de `images.eap.bl.uk` : 200 (IIPImage, CloudFront), **aucun en-tête de limite** ; racine `iiif.bl.uk` : **403 anti-bot** (IIS), hôte arrêté, non contourné, listé dans `a_verifier_manuellement`.
- Le guide `bl.uk/collection-guides/iiif` cité par la page de l'IIIF training est en **404** (`sources/suite4`).
- Aucun 429 ; limite jamais observée ni documentée.

## Web (4 catégories, 2026-11-14)

- Institution : robots.txt, politique de réutilisation ; recherche de conditions d'API ou de politique de moissonnage : aucun résultat de plus (résumé de moteur, non vérifié).
- Utilisateurs : aucune plainte 429/503/blocage sur images.eap.bl.uk (résumé de moteur, non vérifié).
- Tickets : aucun ticket GitHub sur eap.bl.uk ; un script tiers (gist, pause `sleep(3)`, 8 fils) lu en entier.
- Présentations : page du prestataire Cogapp lue : « The new site delivers six million images via the open source Universal Viewer and IIIF » et service IIPImage ; rien sur le trafic ni les limites. Presse sur la cyberattaque de 2023 (tiers, résumé).

## Conclusion

- **Limite documentée chiffrée** : non. **Limite observée** : non (manifeste et images en 200, sans en-tête). **403** : oui sur `iiif.bl.uk`.
- **Politique envers les robots** : manifestes interdits, robots d'IA bloqués, pas de haute résolution en volume.
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne.
