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

La page « Tools » présente les manifestes comme la voie d'accès aux images, mais `robots.txt` les interdit aux robots. Notre sonde étant un client automatisé, **je renonce à les tester**, comme le prévoit la consigne (une interdiction écrite dans la doc dispense de tester).

## Tests

Aucune requête d'API envoyée à `eap.bl.uk`. L'hôte d'images `iiif.bl.uk` renvoie 403 anti-bot (voir `institutions/british-library/`), et aucun endpoint d'image n'est documenté pour l'EAP.

## Web

Politique de l'institution envers les robots : `robots.txt` (ci-dessus). Presse : cyberattaque d'octobre 2023, restauration progressive jusqu'en octobre 2024 (tiers, résumé). Outils tiers de téléchargement par manifeste existent (iiif-download…). **Aucune plainte, aucun quota, aucune politique de moissonnage de l'EAP** n'a été trouvé.

## Conclusion

- **Limite documentée chiffrée** : non. **Limite observée** : non testable. **403** : oui sur `iiif.bl.uk`.
- **Politique envers les robots** : manifestes interdits, robots d'IA bloqués, pas de haute résolution en volume.
- **Moyen d'interroger le quota** : aucun.
- **Confiance** : moyenne.
