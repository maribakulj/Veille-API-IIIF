# Koninklijke Bibliotheek, Pays-Bas (`kb-nl`)

- **Classeur** : hors des 84 (ajouté) · Pays-Bas · audit v2 du 2026-11-14 (remplace l'ancien audit partiel) · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `www.kb.nl` (site), `jsru.kb.nl` (SRU), `services.kb.nl` (OAI-PMH), `resolver.kb.nl`, `imageviewer.kb.nl`, `lab.kb.nl`, `data.bibliotheken.nl`, `iiif.kb.nl` (DNS non résolu).

## Sources
- Page « Data services: APIs and downloads » et pages de jeux de données (`sources/a2`, `a3`) : données ouvertes téléchargeables sans inscription, « If copyright law allows it, anyone can use the data, free of charge and without conditions » ; deux API (OAI-PMH moissonnage, SRU recherche) ; manuels fournis après accès légal pour Delpher/DBNL ; aucun quota.
- `techniek-anp_0.pdf` (`sources/a4`) : « By default 400 records are harvested by one request » ; moissonnage « outside Dutch office hours (9 am -17pm) » ; exemples d'URL OAI, SRU, résolveur et imaging service.
- `AI statement` (`sources/a6`) : « technical measures to combat crawling of our websites Delpher and DBNL by commercial parties » ; « Our collection remains open to research ».
- `robots.txt` : `www.kb.nl` Crawl-Delay 10 ; `jsru`, `services`, `resolver`, `imageviewer` : `Disallow: /` (autorisé par Marcel, C12) ; `data.bibliotheken.nl` Crawl-delay 2 ; `delpher.nl` Disallow tout sauf moteurs listés ; `iiif.kb.nl` et `resources51.kb.nl` : DNS non résolu.
- Aucun service IIIF cité par la doc KB lue.

## Tests
Sessions du 13/11 archivées (`tests/archive/`, configuration committée après lancement), rejouées : passe 2 (`config/passe2.json`, commit 185dc04 avant lancement), 10 requêtes, pauses 6 s. SRU explain et searchRetrieve : **200** ; OAI Identify, ListSets, ListIdentifiers étroit, GetRecord : **200** ; résolveur HEAD (OCR, image) : **200** ; explain indique maximumRecords défaut 20, maximum 1000. `mdo/browse` : connexion réinitialisée (non réessayée) ; imaging service : 403 « Illegal url as identifier » (identifiant vers l'hôte mort resources51, erreur applicative classée 403 par la sonde). Aucun 429, aucun en-tête de limite.

## Web (4 recherches, une par catégorie)
- Institution : AI statement (ci-dessus).
- Utilisateurs : aucun résultat de plainte 429/503 (résumé de moteur, non vérifié).
- Tickets : KB-harvester (Leiden) attend entre requêtes pour ne pas surcharger le service qui héberge Delpher ; renvoie aux « usage guidelines for Delpher ».
- Présentations : atelier KBNLresearch `intro-kb-apis` : mêmes deux API, pas de limite de débit.

## Conclusion
Aucun quota chiffré. Limites techniques : pages de 20 (SRU, max 1000) et 400 (OAI) ; recommandation de moissonner hors 9 h-17 h. Mesures anti-crawling visant Delpher/DBNL (commercial). Confiance : moyenne. Étape g : à faire (`config/crash-oai-identify.json` prête).
