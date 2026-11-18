# Recontrôle documentaire : Göttingen, Heidelberg, ÖNB et MDZ (14/11/2026)

Audit par lecture de sources web officielles, sans appel de charge ni mesure d'en-têtes. Sources de vérité source : `claude/veille-iiif-quotas` au SHA `c6bc71173f861502bd96d438f4489328ccf81b9e`. Ce document se borne à qualifier **les manques et erreurs d'inférence** et n'altère pas les preuves HTTP des dossiers.

## GLAM-025 · SUB Göttingen / GDZ

**URL historique à vérifier** : `https://www.sub.uni-goettingen.de/wir-ueber-uns/portrait/digital-policies-grundsaetze-fuer-die-digitalen-angebote-der-sub-goettingen/digitaler-zugang/`, redirigeant précédemment vers l'accueil.

**Nouvelle URL officielle lue intégralement** : `https://www.sub.uni-goettingen.de/ueber-uns/ordnungen-und-leitlinien/digital-policies` (titre « Digital Policies », consultée le 14/11/2026). Elle rassemble désormais les politiques « Digitale Produktion », « Digitaler Zugang », métadonnées et IT. La SUB soutient des **interfaces ouvertes**, la réutilisation large et la documentation de ses services, sous réserve des licences, droits et contraintes techniques ; aucun seuil chiffré d'API / minute sur cette page. Il s'agit d'une **résolution de l'accès à la politique institutionnelle**, pas d'une preuve de quotité IIIF.

Autre source officielle `https://www.sub.uni-goettingen.de/forschung/forschungswerkzeuge` : la SUB documente TIFY, le GDZ comme dépôt IIIF, et des outils Goobi/TextAPI. Cette page est **un catalogue de services**, pas une politique de rate limit. L'ancienne page spécialisée `.../digitale-bibliothek/digitale-werkzeuge/iiif-bei-der-sub-goettingen/` reste obsolète et ne doit pas être considérée comme rouverte. **Classement** : page de politique = documentation retrouvée ; page spécialisée IIIF = alternative de documentation de service retrouvée, ancien chemin toujours non récupérable.

## GLAM-026 · Universitätsbibliothek Heidelberg

L'URL à vérifier `https://digi.ub.uni-heidelberg.de/en/bpd/projekt/nutzungsbedingungen.html` est apparue dans l'index web avec un texte de conditions (« Terms of Use for Digital Images ») mais son ouverture a **dépassé le délai**, donc sa version live n'est pas attestée en lecture directe. **Ne pas fermer cette URL comme lue intégralement**.

**Source officielle équivalente, vérifiée** : `https://www.ub.uni-heidelberg.de/Englisch/helios/digi/nutzung/` (titre « Terms of Use for Digital Images from Heidelberg University Library » ; dernière mise à jour affichée 22/07/2025). Distingue **Public Domain Mark**, **CC BY-SA 4.0**, **In Copyright**, **In Copyright / out-of-commerce**, avec règles propres à chaque œuvre. La bibliothèque ne facture pas la réutilisation des reproductions dans les conditions applicables. **Ce n'est pas une absence de quota d'API**.

**Erreur de nature/source à corriger** dans `institutions/universitatsbibliothek-heidelberg/data.json` : `limites_documentees[0].nature = « Aucune limite de débit documentée »` alors que `valeur` cite `Die Universitätsbibliothek Heidelberg erhebt keine Gebühren für die Nutzung ihrer Digitalisate` (aucuns **frais** d'utilisation). La gratuité et la limitation de débit sont orthogonales. Reclasser en **condition de licence/gratuité**, et conserver `IIIF/OAI rate limit non établi` sans extrapoler. La source citée est un texte de droits, **pas une documentation de throttling**.

Pages d'item `/diglit/Cimelia1975`, RSS `/diglit/rss?set=handschriften` et cas Europeana restent à vérifier techniquement, sans contourner Anubis.

## GLAM-027 · Österreichische Nationalbibliothek (ÖNB)

**Documentation de référence publique lue** : `https://api.onb.ac.at/`. Cette page distingue explicitement :
- IIIF Presentation **3** : `/iiif/presentation/v3` ;
- IIIF Image **3** : `/iiif/image/v3` ;
- IIIF Content Search **2** : `/iiif/search/v2` ;
- Content Search **1** : `/iiif/search/v1` (**dépréciée**) ;
- endpoints REST `/rest/v1/ie/{ieId}/file/{fileName}`, `alto/{pageNumber}`, `txt/{pageNumber}`, `preview`, `thumbnail`.

Le site recommande le notebook d'exemples `https://labs.onb.ac.at/gitlab/labs-team/how-to-oenb-api`. **Cette page GitLab n'est pas exploitable en entier par l'outil web** : coquille JS « Loading », projet daté du 19/10/2026. Le catalogue `https://labs.onb.ac.at/en/datasets/` renvoie également une coquille sans description des jeux. Les `ieId` publics précis du notebook, et donc les tests de toutes les familles d'API, **restent ouverts** : pas d'identifiant inventé. Aucune limite chiffrée de débit visible sur l'accueil `api.onb.ac.at`, ce qui ne démontre pas l'illimitation.

## GLAM-024 · Bayerische Staatsbibliothek / MDZ

**Source officielle relue** : `https://www.digitale-sammlungen.de/en/interfaces` (section « IIIF APIs », consultée le 14/11/2026). Le texte explicite **trois régimes distincts** :
1. **Presentation API IIIF v2**, accès annoncé **illimité** ;
2. **Image API v2**, nombre de requêtes limité **par 24 h**, valeur numérique non publiée sur cette page ;
3. **Téléchargements OCR**, nombre limité **par 24 h**, valeur non publiée.

Les faits sont **déjà présents** dans `institutions/mdz/data.json`, donc ce n'est pas une découverte nouvelle. La valeur de la limite Image/OCR doit rester `non chiffrée` sans deviner un seuil par l'absence de 429. Les contacts MDZ demeurent la piste pour obtenir les chiffres. L'interface `bdr.oai.bsb-muenchen.de` en 403 Apache est un contrôle OAI technique séparé. La déclaration « unlimited » ne vaut **que pour Presentation**, non pour l'institution entière.

## Points d'intégration prioritaire

- [P0] **Heidelberg** : gratuité de réutilisation mal catégorisée comme preuve relative aux rate limits.
- [P1] **Göttingen** : remplacer les chemins historiques restructurés par la nouvelle politique et la page de services, en conservant l'historique.
- [P1] **ÖNB** : documentation multi-famille accessible mais notebook et identifiants d'exemple non récupérés ; ne pas cocher endpoints testés.
- [P2] **MDZ** : distinguer trois régimes, déjà correctement documentés dans le JSON ; ne pas dupliquer les limites existantes.

Aucun fichier canonique ou classeur n'est modifié par ce recontrôle ; il doit être intégré par le pipeline de validation avec la régénération `BENCHMARK.xlsx`.
