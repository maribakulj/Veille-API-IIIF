# Révérifications documentaires effectuées le 14 novembre 2026

Source de la liste à reprendre : `institutions/*/data.json`, champ `a_verifier_manuellement`. Référence : commit `c6bc71173f861502bd96d438f4489328ccf81b9e` de `claude/veille-iiif-quotas`.

**Convention de preuve** : « lu par l'outil web » signifie qu'un service de lecture web a fourni le texte de la page et sa source, **pas** qu'un client HTTP de la sonde a obtenu 200, ni que la page sera accessible sans JS depuis un autre réseau. Les dates de dernière indexation de la source varient. Aucune de ces vérifications n'est un test de charge ou de quota observé.

## Europeana (`institutions/europeana/`)

| URL inscrite comme manuelle | Résultat documentaire | Décision / reste à faire |
| --- | --- | --- |
| https://pro.europeana.eu/page/apis | **Lue via redirection** vers https://api.europeana.eu/en, page publique « Europe's cultural heritage, via APIs » ; source consultée 2026-11-14 | Remplacer l'ancienne adresse dans les liens de veille ; ne pas la présenter comme une page détaillant les plafonds |
| https://pro.europeana.eu/page/search | **Lue via redirection** vers https://api.europeana.eu/en, page d'accueil API générale | Retrouver la documentation spécifique de Search dans la knowledge base ; ne pas considérer la redirection comme une documentation Search |
| https://pro.europeana.eu/page/api-libraries-and-plugins | **Lue via redirection** vers https://europeana.atlassian.net/wiki/spaces/EF/pages/2385870932/Libraries+and+Plugins ; liste Python / Java / Node / plugins visible | Pas de quota numérique mis en évidence dans le texte examiné ; contrôle indépendant des quotas non nécessaire pour cette page de bibliothèques |
| https://pro.europeana.eu/project/iiif-europeana-working-group | **Lue**, page mise à jour au 28 avril 2026 ; activités et contacts du groupe de travail | Source institutionnelle de gouvernance IIIF ; pas une page de politique de quotas |
| https://pro.europeana.eu/robots.txt | **Non vérifiée** via ce passage | Garder en attente : règles robots du domaine courant |

**Point de politique déjà documenté dans le dépôt, reconfirmé le 2026-11-14 :** https://europeana.atlassian.net/wiki/spaces/EF/pages/2462351393/Accessing+the+APIs distingue clés personnelles (limites réduites progressivement jusqu'en avril 2026) et clés projet (limites plus élevées) ; pas de chiffres dans la section publique inspectée. https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417 (« API FAQ ») affirme au contraire l'absence de throttling : la contradiction doit rester explicitement conservée et datée. **Ne pas extrapoler** ces conditions au service IIIF, documenté séparément.

Sources de contrôle : 
- https://api.europeana.eu/en
- https://europeana.atlassian.net/wiki/spaces/EF/pages/2385870932/Libraries+and+Plugins
- https://pro.europeana.eu/project/iiif-europeana-working-group
- https://europeana.atlassian.net/wiki/spaces/EF/pages/2462351393/Accessing+the+APIs
- https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417/Europeana+API+FAQ

## e-rara (`institutions/e-rara-eth-bibliothek-et-partenaires/`)

| URL inscrite comme manuelle | Résultat documentaire | Décision / reste à faire |
| --- | --- | --- |
| https://www.e-rara.ch/wiki/apiinfo | **Texte lu**, interface OAI-PMH et export IIIF documentés. L'OAI est paginé par paquets de 10 enregistrements et `resumptionToken`. Les très grands METS peuvent expirer. | Cette taille de page **n'est pas une limite de débit** ; pas de requêtes/minute constatées dans le passage lu. Conserver la vérification HTTP séparée. |
| https://www.e-rara.ch/wiki/termsOfUse | **Texte lu**, licences PDM et CC BY-SA selon les notices, obligations de citation et conditions d'utilisation des fichiers. | Conditions de réutilisation ≠ politique d'accès automatisé ; aucune valeur de quota déduite. |
| https://www.e-rara.ch/wiki/aboutERara | **Texte lu**, description de la plateforme et rôle de l'OAI-PMH dans l'échange des métadonnées (Gallica citée). | Peut sortir de la liste des lectures manuelles, sous réserve de distinguer le statut historique d'accès de la lecture actuelle. |
| https://era-prod11.ethz.ch/robots.txt | **Non vérifié** | Règles exactes de ce sous-hôte restent à constater par HTTP. |
| https://www.e-rara.ch/i3f/manifest/6341733/search?q=Bibel | **Non vérifié comme endpoint** | Réponse Content Search et en-têtes non établis par la lecture web. |

Sources : https://www.e-rara.ch/wiki/apiinfo ; https://www.e-rara.ch/wiki/termsOfUse ; https://www.e-rara.ch/wiki/aboutERara. Consultées le 2026-11-14 par lecture web (la source `aboutERara` était indexée antérieurement).

## e-manuscripta (`institutions/e-manuscripta-bibliotheques-partenaires-suisses/`)

| URL inscrite comme manuelle | Résultat documentaire | Décision / reste à faire |
| --- | --- | --- |
| https://www.e-manuscripta.ch/wiki/apiinfo | **Texte lu** : OAI-PMH, accès à divers fichiers, IIIF ; paquets de 10 enregistrements OAI, possibilité de timeout sur les METS volumineux | Aucun plafond de requêtes/minute déduit ; endpoint IIIF à distinguer de l'OAI. |
| https://www.e-manuscripta.ch/wiki/termsOfUse | **Texte lu** : licences selon les documents ; **la copie systématique de fichiers vers d'autres serveurs exige un accord écrit préalable** du gestionnaire ou des institutions | La vérification documentaire de cette interdiction est faite. Elle ne doit pas être convertie en autorisation de moissonnage. |

Sources : https://www.e-manuscripta.ch/wiki/apiinfo ; https://www.e-manuscripta.ch/wiki/termsOfUse, consultées 2026-11-14. `robots.txt` lui-même n'était pas lisible par l'outil web pendant ce passage ; conserver les preuves originales du dépôt.

## Cardiff (`institutions/cardiff-university-library/`)

| URL inscrite comme manuelle | Résultat documentaire | Décision / reste à faire |
| --- | --- | --- |
| https://www.cardiff.ac.uk/help/termsofuse | **Texte lu** : restrictions de copie / reproduction du contenu du **site universitaire**, autorisations selon usages ; aucun plafond d'API chiffré dans cette page | Ne pas appliquer automatiquement ces conditions générales aux ressources IIIF sous CC des collections numériques. |
| https://www.cardiff.ac.uk/special-collections/explore | **Texte lu** : lien officiel vers les Digital Special Collections, contenu annoncé comme IIIF-enabled, réutilisable sous licence Creative Commons | Le libellé soutient l'ouverture des images, pas une absence de rate limit. |
| https://www.cardiff.ac.uk/special-collections/about-us | **Texte lu** : accès public gratuit aux collections et mission du département | Informative, aucune limite API documentée par cette page. |
| https://www.cardiff.ac.uk/robots.txt | **Non vérifié en direct** par l'outil de lecture web | Garder une action technique pour la version actuelle de robots.txt. |
| https://igelu.org/wp-content/uploads/2022/10/Unlocking-your-collections-with-Alma-Digital-and-IIIF.pdf | **PDF ouvert, contrôle visuel partiel** des pages 2, 8, 17, 29 sur 29 | Présentation d'Alison Harvey sur Alma Digital et IIIF ; ne pas conclure « aucune limite » sans examen complet des 29 diapositives. |

Sources : https://www.cardiff.ac.uk/help/termsofuse ; https://www.cardiff.ac.uk/special-collections/explore ; https://www.cardiff.ac.uk/special-collections/about-us ; PDF IGeLU ci-dessus. Consultées 2026-11-14.

## Bilan de cette passe
- **12 URL auparavant signalées pour lecture manuelle** désormais **lisibles au niveau documentaire** : Europeana 4, e-rara 3, e-manuscripta 2, Cardiff 3 = **12 URL** au total (incluant deux anciennes URL Europeana menant à la même page d'accueil). Elles ne constituent pas 12 contrôles HTTP autonomes.
- **3 URL robots.txt / endpoints et le PDF restant** ne sont pas clôturés, ainsi que tous les autres dossiers non repris dans cette note.
- Les restrictions d'accès et les étapes a–g du dépôt initial n'ont pas été réécrites ; cet audit doit être rapproché des fichiers de preuve et du script de génération Excel.

## Suite de la boucle
Reprendre les URL des dossiers restant dans `institutions/` selon `PLAN-RATTRAPAGE-CHATGPT.md`; ne marquer « consulté » que lorsqu'une page source complète est disponible ; ne pas assimiler un résultat de recherche, une archive et une réponse HTTP. Les entrées dont le texte est trouvé mais dont le statut API ou robots reste inconnu doivent être reclassées plutôt qu'effacées.
