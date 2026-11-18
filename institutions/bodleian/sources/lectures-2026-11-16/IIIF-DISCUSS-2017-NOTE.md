# Lecture complémentaire : « Crawler Etiquette — a request » (IIIF-Discuss)

**Source originale** : https://groups.google.com/g/iiif-discuss/c/Z3GVdj6s61w

- Message publié le **13 novembre 2017** par un représentant de Digital Bodleian.
- **Lecture réalisée le 16 novembre 2026** ; texte public obtenu via un extracteur documentaire, `acquired_at` : **2026-11-15** ; environ 5 085 caractères récupérés, fil lu en entier.
- **Statut de preuve : note de lecture sourcée**, pas copie des octets HTML originaux ni fichier `SHA256SUMS` de l'original. Les conclusions ci-dessous restent vérifiables à l'URL ; ne pas présenter cette note comme une capture exhaustive originale.

## Constats tirés du texte (2017, historique)

1. L'équipe demande un **User-Agent descriptif avec coordonnées de contact** ou adresse de projet, afin de pouvoir joindre un collecteur avant de bloquer l'accès.
2. Elle propose une **pause volontaire**, citant **500 millisecondes entre requêtes** comme exemple de comportement raisonnable. Ce n'est **pas** un quota officiel de **120 requêtes/minute**, ni un plafond testé ou imposé par serveur.
3. En cas de transfert de volumes considérables, elle encourage à **contacter la bibliothèque** pour convenir d'une méthode adaptée, plutôt que d'accumuler des requêtes simultanées.
4. Elle préfère **ne pas implémenter de limitation automatique**, en partie pour ne pas dégrader les visionneuses d'images tuilées. Elle demande aussi de **ne pas contourner un blocage** par des adresses IP ou VPN alternatifs.
5. Une réponse distincte d'un autre participant recommande de respecter `robots.txt` et les signaux **HTTP 429** et **`Retry-After`**. Il s'agit d'une recommandation générale, **pas d'un en-tête observé sur IIIF Bodleian**.

## Interprétation de politique

- **Politique historique** de courtoisie envers les moissonneurs, explicite dès 2017.
- **Aucune limite chiffrée contraignante** ni preuve de quota IIIF en 2026 n'est fournie.
- La documentation institutionnelle plus récente `https://digital.bodleian.ox.ac.uk/developer/iiif/` confirme que les moissonnages importants devraient être annoncés à l'équipe. Lecture du texte de la doc enregistrée en copie datée 2026-10-05.
- Le `robots.txt` de l'hôte `iiif.bodleian.ox.ac.uk` demeure **non lu (réponse 400)** dans cette passe. **Ne pas déduire les règles du `robots.txt` du domaine `digital.bodleian.ox.ac.uk`**.

Cette lecture approfondit **l'étape f**, elle **ne réalise pas** de tests HTTP supplémentaires ni d'étape g.
