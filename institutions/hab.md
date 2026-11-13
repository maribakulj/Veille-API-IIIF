# Herzog August Bibliothek Wolfenbüttel — `hab`

- **Statut** : vérifiée (partiellement : pas de manifeste IIIF testé, aucune URL IIIF documentée trouvée)
- **Pays** : Allemagne
- **Point d'entrée testé** : `https://diglib.hab.de/` (Wolfenbütteler Digitale Bibliothek) ; endpoints OAI-PMH `http://oai.hab.de/?verb=Identify`
- **Vérifié le** : 2026-11-13 (sonde vers 21:07:58 à 21:08:11 UTC)
- **Vérifié par** : agent de veille (Claude Haiku 5.5), session de veille `claude/veille-iiif-quotas`

## 1. Documentation officielle

| Source (URL) | Consultée le | Ce qu'elle dit des quotas / limites / débit |
|---|---|---|
| https://www.hab.de/en/iiif-international-interfaces-for-digitised-cultural-assets/ (page IIIF de la HAB, 18/12/2019) | 2026-11-13 (WebFetch, résumé par un petit modèle, non vérifié brut) | Liste quatre API sans URL ni version : « Image API », « Presentation API » (« supplies metadata (in the JSON-LD format) »), « Authentication API » (« serves to regulate access to certain objects if required »), « Content Search API » (« enables full-text searching and annotations within an object »). Aucune limite. Renvoie à `diglib.hab.de/?link=167` (PURL), sans manifeste. |
| http://diglib.hab.de/nutzungshinweise.html (Nutzungshinweise, citée par `?link=012`) | 2026-11-13 (WebFetch, non vérifié brut) | Pas de quota, débit, fréquence ni règle d'usage automatisé. Licence : images HAB « publiées dans le domaine public » ; données structurelles (facsimile.xml, tei-struct.xml, tei-msDesc.xml) « CC0 » ; autres données « CC BY-SA 4.0 sauf mention contraire ». Accès : « Nicht frei über die Homepage der Bibliothek verfügbare Angebote unterliegen gesonderten Nutzungsregeln » ; contact auskunft@hab.de. Cadre : Benutzungsordnung für Landesbibliotheken. |
| https://diglib.hab.de/ (accueil, fiche « Wolfenbütteler Digitale Bibliothek ») | 2026-11-13 (WebFetch, puis sonde) | Pas de limite lue. Indique une interface OAI : « Über eine OAI-Schnittstelle werden bibliographische … » ; métadonnées « dürfen von jedermann über die OAI-Schnittstelle abgerufen » (cité via la page Nutzungshinweise). |
| https://www.hab.de/de/home/bibliothek/digitale-bibliothek-wdb/standards-dokumentation.html | 2026-11-13 (WebFetch, résumé) | Documentation de codage éditorial (TEI), pas d'API. Rien sur les quotas. Contacts : baumgarten@hab.de (contenu/technique), parlitz@hab.de (maintenance). |

Conclusion documentaire : **aucune URL de manifeste, d'info.json ou d'API de recherche n'a été trouvée dans la documentation consultée**. Aucune limite chiffrée documentée.

## 2. Recherche élargie

- Termes cherchés : « Herzog August Bibliothek diglib IIIF Manifest API Dokumentation » ; « diglib.hab.de IIIF manifest URL "diglib.hab.de" iiif presentation ».
- Sources examinées : résultats de recherche (non lus en entier) ; page IIIF de la HAB (corps non récupéré par le résumé) ; présentation Zenodo 2021 (David Maus, SUB Hamburg) : prototype METS vers IIIF réalisé en coopération HAB / Bodleian, dont l'exemple de manifeste pointe vers `hab.bodleian.ox.ac.uk`, pas vers diglib.hab.de ; documentation générique digilib (Manifester `…/digilib/Manifester/IIIF/3/…`), qui s'applique à toute installation digilib et n'est pas attribuée à la HAB.
- Résultat : rien de documenté pour un manifeste `diglib.hab.de`. Le site `hab.bodleian.ox.ac.uk/de/digitalisate/` est cité comme lieu de consultation des manuscrits numérisés (page HAB IIIF). Non testé en profondeur : aucune URL de manifeste de ce site n'est documentée.
- Non cherché (faute de budget et de piste) : Wayback sur diglib.hab.de, forums IIIF, issues GitHub.

## 3. Tests d'appel (voir `tests/hab.log`)

| # | Heure UTC | URL (sans identifiant) | Méthode | Statut | En-têtes de limite | Corps (résumé) | Délai depuis précédent |
|---|---|---|---|---|---|---|---|
| 1 | 21:07:58 | https://diglib.hab.de/ | GET | 200 | aucun | HTML « Wolfenbütteler Digitale Bibliothek » | - |
| 2 | 21:08:04 | http://diglib.hab.de/?link=167 | GET | 302 | aucun | HTML (la cible de redirection n'est pas journalisée par la sonde) | 6 s |
| 3 | 21:08:05 | http://oai.hab.de/?verb=Identify | GET | 200 | aucun | XML OAI-PMH | 1 s (hôte différent) |
| 4 | 21:08:10 | http://diglib.hab.de/nutzungshinweise.html | GET | 200 | aucun | HTML « Nutzungshinweise für Online-Angebote » | 5 s |
| 5 | 21:08:11 | https://hab.bodleian.ox.ac.uk/de/digitalisate/ | GET | 200 | aucun | HTML (site Bodleian) | 1 s (hôte différent) |

Non réalisés : aucun manifeste ni info.json testé (aucune URL documentée pour `diglib.hab.de`). Pas de 403 ni de 429. Requêtes : 5 sur un plafond de 15. Le script a respecté la pause de 6 s par hôte.

## 4. Conclusion sur les limites

- Limite **documentée** (citation et URL) : non. Les Nutzungshinweise ne mentionnent ni quota ni débit ; l'usage automatisé n'y est pas traité.
- Limite **observée** (429 ou en-tête de quota reçu) : non (5 requêtes, aucun en-tête de limite).
- Accès refusé à ce client (403 anti-bot / défi Cloudflare) : non.
- L'API annonce-t-elle ses limites dans la réponse ? non observé (aucune limite annoncée).
- Mécanisme observé : aucun.
- Valeurs trouvées (quota, fenêtre) : aucune.
- Blocages rencontrés : aucun. Limite de la sonde : elle ne suit pas les redirections, donc la cible du 302 de `?link=167` n'est pas journalisée.

## 5. Pourquoi ce n'est pas publié (si c'est le cas)

- Trouvé (avec source) : la HAB annonce ses API IIIF (Image, Presentation, Authentication, Content Search) sans URL publique dans la page consultée ; l'OAI-PMH est documenté et répond. Le prototype IIIF connu passe par l'hôte Bodleian.
- Hypothèses (étiquetées comme telles) : hypothèse 1 : le service IIIF de diglib.hab.de existe mais n'est pas documenté publiquement sous une URL stable (non vérifié). Hypothèse 2 : la production IIIF est hébergée sur `hab.bodleian.ox.ac.uk` (non vérifié, pas de manifeste testé).

## 5 bis. Recherche ciblée des quotas (2026-11-13)

Recherche menée après la sonde, sans nouvelle requête vers l'API. Aucun endpoint de statut ni en-tête de quota trouvé, donc aucune configuration `scripts/config/hab-quota.json` n'a été écrite.

a) **Endpoint de statut de quota** : non trouvé — termes cherchés : « Herzog August Bibliothek diglib IIIF manifest API Rate Limit Kontakt » ; « Nutzungsbedingungen automatisierte Zugriffe Abfragen Beschränkung API » ; « diglib.hab.de IIIF manifest API ». Doc lue : http://diglib.hab.de/copyright.html (consultée 2026-11-13, WebFetch) : aucun endpoint de statut. La page se dit elle-même « veraltet » et renvoie à `nutzungshinweise.html`.
b) **En-têtes de limite documentés** : non trouvé — la doc ne cite aucun en-tête. Observé (sonde du 13/11, 5 requêtes) : aucun en-tête de limite.
c) **Clé ou compte donnant un quota** : non trouvé. Phrase exacte (copyright.html) : « Nicht frei zugängliche Angebote unterliegen gesonderten Nutzungsregeln » ; ces règles ne concernent pas un quota de débit.
d) **Contact officiel pour un quota** : trouvé — auskunft@hab.de. Phrase exacte (copyright.html, consultée 2026-11-13) : « die von der Auskunft der Bibliothek (auskunft@hab.de) erfragt werden können ». Cette adresse est citée pour les règles d'usage des offres non libres, pas pour un quota ; elle reste la piste la plus directe.

Standard : le brouillon IETF `draft-ietf-httpapi-ratelimit-headers` (RateLimit-Limit / RateLimit-Remaining / RateLimit-Reset) n'est pas une norme ; la spécification IIIF n'a pas été relue sur ce point.

Conclusion : moyen d'interroger le quota : **non**. Piste : demander à auskunft@hab.de une politique de débit pour l'Image API et le manifeste, une fois l'URL IIIF connue.

## 6. Confiance et pistes restantes

- Niveau de confiance : moyen sur l'absence de limite annoncée (conditions lues en résumé) ; faible sur les endpoints IIIF (aucune URL documentée).
- Ce qui reste à vérifier, et comment :
  1. Lire la page IIIF de la HAB (`https://www.hab.de/en/iiif-international-interfaces-for-digitised-cultural-assets/`) dans un navigateur pour récupérer les URL de manifeste, s'il y en a.
  2. Demander à auskunft@hab.de (ou baumgarten@hab.de) l'URL du manifeste IIIF, les versions de l'API et une éventuelle politique de débit.
  3. Tester plus tard un manifeste précis, une fois son URL documentée, avec 2 requêtes espacées de 6 s.
