# Passe U — relire les 126 entrées dont le contenu n'était pas démontré (15/11/2026)

**Point de départ vérifié :** GitHub Actions #43708979962 avait 260/260 URL de `a_verifier_manuellement` **classées** (aucune sans constat), mais **126 sans texte documentaire certifié** par le script. Cette passe retente les URL originales et lit, lorsqu'elles ne répondent pas, les **pages de substitution officielles**. Ne pas convertir les anciens 403 en 200 : une copie indexée datée ou une redirection vers une page d'accueil n'est pas une nouvelle sonde HTTP. Pas de requêtes répétées contre un WAF, de surcharge, de contournement de challenge ni de connexion avec clé.

## Résultats nouveaux sur les URL originales

| Institution / URL | Résultat réellement obtenu | Date de copie | Limite |
|---|---|---|---|
| Art Institute of Chicago, `https://www.artic.edu/robots.txt` | **Texte robots obtenu**, exceptions `/press/exhibition-press-room`, `/search` indirectes, `/ajaxData`, etc. | 15/11 | Robots du domaine `www` ; IIIF sur ce même domaine a son propre accès HTTP à tester |
| AIC, `https://www.artic.edu/articles/902/public-access-to-our-public-presence-sharing-our-api` | **Article institutionnel récupéré**, contexte de l'API et du partage des collections | 28/08 | Pas de quota IIIF |
| AIC, `https://www.artic.edu/iiif/2/b3974542-b9b4-7568-fc4b-966738f61d78/info.json` | **Page 301 renvoyant sur la même adresse**, **pas de JSON IIIF** | 05/07 | Reste non lu |
| BNE, `https://bnedigital.bne.es/bd/es/simple` | **Page d'accueil BNE Digital indexée**, interface de recherche, texte « Procesando » | 13/10 | Ne prouve pas fonctionnement des endpoints IIIF |
| BNE, `https://datos.bne.es/inicio.html` | **Page Linked Open Data indexée**, dernière mise à jour de ses données affichée **17/06/2026** | 23/10 | Données bibliographiques LOD ≠ image IIIF |
| BNE, `https://www.bne.es/en/catalogs/hispanic-digital-library` | **Page officielle BNE Digital récupérée**, lien vers la nouvelle interface | 08/11 | La redirection institutionnelle éclaire la migration |
| Cardiff, `https://www.cardiff.ac.uk/special-collections/explore` | **Texte de la page récupéré**, lien Digital Special Collections, mention d'objets IIIF et d'une licence CC BY 4.0 pour les contenus numériques IIIF indiqués | 29/10 | Licence de réutilisation ≠ absence de limite HTTP |
| Cardiff, `https://www.cardiff.ac.uk/special-collections/about-us` | Page officielle *About us* récupérée | 30/10 | Pas quota |
| Cambridge CUDL, `https://cudl.lib.cam.ac.uk/help/` | **Aide Cambridge Digital Library récupérée**, exemples de liens `/view/[item id]/[image number]` et mention d'une ancienne démarche IIIF | 30/09 | Source potentiellement historique, pas de limite actuelle |
| CUDL, `https://cudl.lib.cam.ac.uk/robots.txt` | `fetch_error` et code 200 sans corps exploitable, **pas un fichier robots lu** | 15/11 | Ouvert |
| CUDL, `https://cudl.link/v1/metadata/` et `/v1/transcription/tei/diplomatic/internal/MS-ADD-03958/i111` | **Connexion échouée pour les deux routes** | 15/11 | Pas de preuve de fonctionnement |
| Cultural Japan, `https://app.cultural.jp/iiif-collection/collection.json` | `fetch_error` avec code 200 sans corps utile | 15/11 | **JSON toujours non lu**, ne pas classer comme disponible |
| Digital Commonwealth, `https://www.digitalcommonwealth.org/for_institutions` | Document **301** seulement, sans information institutionnelle | 12/07 | La page actuelle `/institutions` est l'équivalent trouvé, pas même URL |
| Digital Commonwealth, `https://www.digitalcommonwealth.org/privacy` | **Texte original de la politique de confidentialité récupéré** | 21/10 | Pas conditions d'extraction ni quotas |
| NICH e-Museum, `https://emuseum.nich.go.jp/terms?locale=en` | **Contenu du portail japonais d'accueil**, pas une page `Terms` isolée | 15/11 | Ne pas conclure que les droits étaient intégralement lus ici ; la source officielle `/about?langId=en&webView=0` reste le remplacement |
| e-rara, `https://www.e-rara.ch/wiki/aboutERara` | **Page « What is e-rara? » récupérée**, numérisation et bibliographie DOI | 31/10 | Pas de rate-limit |
| EAP British Library, `https://eap.bl.uk/about-eap` et `https://eap.bl.uk/terms` | **404 sur les deux anciennes URL** | 15/11 | Remplacements officiels : `https://eap.bl.uk/about-programme`, `https://eap.bl.uk/reuse-collections-and-takedown-policy` (textes récupérés) |
| Edinburgh Art, `https://collections.ed.ac.uk/art/terms` et `https://collections.ed.ac.uk/art/feedback` | Respectivement **404** et erreur réseau | 15/11 | Sources de droits/contact alternatives déjà dans le rapport C, mais **pas** preuve du contenu des URL originales |
| Europeana, `https://pro.europeana.eu/page/search` | **Page générale des API**, pas l'ancien contrat Search | 10/11 | Ne pas déduire quota |
| Europeana, `https://pro.europeana.eu/page/api-libraries-and-plugins` | **Contenu réel « Libraries and Plugins »** de la base de connaissance | 06/11 | Aucun plafond chiffré |
| Europeana, `https://pro.europeana.eu/project/iiif-europeana-working-group` | Texte institutionnel du groupe IIIF/Europeana | 26/09 | Gouvernance, pas débit |
| Huntington, `https://researchguides.huntington.org/imagingservices` | **Guide Aeon Imaging Services** récupéré, demandes d'images et droits | 30/10 | Limites de commande d'images ne sont pas un quota IIIF |
| Library of Congress, `https://www.loc.gov/apis/` | **Répertoire officiel des APIs** récupéré | 07/11 | Ne pas attribuer quota global aux services IIIF |
| Finna, `https://www.kiwi.fi/spaces/Finna/pages/440828359/Finna+API+Documentation+In+English` | Navigation et éléments Confluence récupérés, **pas démonstration d'une lecture intégrale de cette page** | 05/11 | Le contrat REST exact est dans OpenAPI v11.0.3, rapport T |
| UCD, `https://www.ucd.ie/library/` | Page de bibliothèque récupérée | 09/07 | Pas IIIF |
| Leicester, `https://le.ac.uk/library/about/policies` | **Index officiel des politiques** complet, notamment réutilisation des données et conditions d'archives | 13/11 | Aucun quota dans cet index |
| NDL, `https://dl.ndl.go.jp/ja/terms` | **Bandeau cookies et lien /sitepolicy**, pas page des droits attendue | 14/11 | La source alternative `https://dl.ndl.go.jp/sitepolicy` est lisible (rapport P) |
| Norvège, `https://www.nb.no/services/search/v2/` | **301 sans adresse finale exploitable** | 04/11 | OpenAPI Catalog Search (autre famille) n'est pas équivalent démontré |

## Pages de substitution officielles documentées

- **EAP** : `https://eap.bl.uk/about-programme` (texte sur le programme, 28/10), `https://eap.bl.uk/reuse-collections-and-takedown-policy` (droits, 01/11).
- **Göttingen** : `https://www.sub.uni-goettingen.de/ueber-uns/ordnungen-und-leitlinien/digital-policies` : **contenu réel de la politique digitale** indexé le 01/10, avec notamment sections sur la standardisation et l'archivage pérenne. Ne pas assimiler ce document à un contrat d'API.
- **Digital Commonwealth** : `https://www.digitalcommonwealth.org/institutions` : liste d'institutions et pages de contributeurs, mais **pas** la même procédure que `/for_institutions`.
- **Huntington** : `https://www.huntington.org/digital-library` retourne maintenant un texte **« Page Was Not Found »** ; ne pas marquer comme page de bibliothèque numérique lue.

## Mesure de lecture et conséquences

Les nouvelles copies indexées rendent des **contenus réellement récupérés** pour plusieurs pages autrefois marquées comme 403, notamment BNE, Cardiff, CUDL Help, Europeana et LoC, sans effacer les anciens refus de la sonde. Inversement, la page robots CUDL, le JSON Cultural Japan, les deux routes `cudl.link` et l'IIIF Image AIC **ne sont toujours pas extraits**. Les données de ce rapport sont utilisables dans `data/reverifications-chatgpt-2026-11-14.csv`, mais aucune limite technique par minute n'est extrapolée.

**Le classement complet des 260 entrées du 15/11 n'est pas une déclaration de résolution complète.** Les `data.json`, fiches et `BENCHMARK.xlsx` restent inchangés ; la PR reste brouillon.
