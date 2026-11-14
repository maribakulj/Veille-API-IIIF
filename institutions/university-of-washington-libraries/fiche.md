# University of Washington Libraries (GLAM-054)

## Sources
- Digital Collections : https://digitalcollections.lib.washington.edu/ (page d'accueil lue ; pages /digital/* = coquille JavaScript sans texte, voir a_verifier_manuellement). robots.txt : Crawl-Delay 1, Disallow /digital/search/, /oai/ (sources/doc/text/01.txt).
- Site des bibliothèques : www.lib.washington.edu (Crawl-delay 10) et lib.uw.edu (Disallow vide) ; conditions générales UW https://www.washington.edu/online/terms/ (sources/doc-b/text/08.txt) : « University of Washington may block, suspend, or terminate your use of the website at any time for any reason. »
- Doc de la plateforme CONTENTdm d'OCLC (IIIF Presentation 2.1.1, Image 2 niveau 1, dmwebservices) : sources/doc et sources/doc-b ; robots.txt help.oclc.org : Crawl-delay 5, Request-rate 1/5.
- Aucune page UW ne documente d'API, de quota ni de politique de moissonnage. Les pages « Ordering & Use » et « search-tips » n'ont pas pu être lues (403 Cloudflare sur l'hôte à la 6e requête, hôte arrêté ; aucune capture Wayback) : listées dans a_verifier_manuellement.
- Manifeste UW lu via Wayback (sources/wayback/manifest-kccollects-343.md) : il annonce l'hôte OCLC cdm16786.contentdm.oclc.org (manifeste, collection, image, OAI).

## Tests
- Passe 1 (config uw-passe1-iiif.json) : 4 endpoints sur l'hôte UW, tous « NON LANCÉ » (hôte arrêté, registre partagé, 403 Cloudflare du 2026-11-14T02:23:16Z) ; 0 requête.
- Passe 2 (uw-passe2-cdm16786.json) : 11 requêtes sur cdm16786.contentdm.oclc.org à 10 s : manifeste d'objet 200, info.json 200, dérivé 150 px 200, manifeste de collection 200 (après 302), manifeste global (301 puis 302), OAI GetRecord 200 (Disallow /oai/ journalisé, autorisé par Marcel C12), dmwebservices 302 vers une page 404 d'OCLC (autre hôte, non suivi). Aucun en-tête RateLimit / Retry-After.
- Passe 3 (uw-passe3-sitewide.json) : manifeste global final /iiif/2/manifest.json 200 (24 ko lus). 2 requêtes.
- En-têtes : x-oclc-iiif-provider: cantaloupe, cookie TS01 (pare-feu applicatif), aucun en-tête de limite.

## Web (4 catégories)
- institution : conditions UW (blocage à tout moment, sans chiffre).
- presentations : projet iSchool 2021 sur IIIF/Mirador à UW (aucun chiffre de quota).
- utilisateurs : recherche « "digitalcollections.lib.washington.edu" IIIF manifest harvesting rate limit 403 » : aucun résultat propre à UW (résumé de moteur, non vérifié) ; contexte : OCLC écrit que les pics sur CONTENTdm viennent de bots et qu'elle bloque les moissonneurs (sources/doc-d).
- tickets : recherche GitHub sur l'hôte : aucun résultat (résumé de moteur, non vérifié).
- Non lu : jewishstudies.washington.edu (WebFetch refusé par le système de permissions, domaine UW) ; indice de moteur seulement : Mirador mis en place sur toutes les collections juste avant la fin du printemps 2019.

## Conclusion
Aucun quota ni politique d'API publiés par UW. Hypothèse (non vérifiée) : UW délègue l'hébergement et les API à OCLC (CONTENTdm) et n'ajoute pas de règle propre. Seul fait observé : un 403 Cloudflare côté UW à la 6e requête, déclencheur inconnu, non assimilable à un quota ; côté OCLC, 13 requêtes à 10 s sans en-tête ni blocage. Crash test (g) : config crash-image-info.json préparée sur l'hôte OCLC (limite non documentée, plafond selon le réseau détecté), à lancer à la fin.
