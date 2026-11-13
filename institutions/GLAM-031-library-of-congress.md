---
id: GLAM-031
institution: Library of Congress
pays: États-Unis
statut: CHIFFRE TROUVÉ (page officielle ; application IIIF à préciser)
classe: chiffre publié
statut_quota: 'CHIFFRE TROUVÉ (page officielle ; application IIIF à préciser) ; Tableau reconfirmé verbatim (WebFetch) : Image Services 150 requêtes par minute, blocage d''une heure ; la page ne nomme ni IIIF ni tile.loc.gov'
debit_iiif: 'Page officielle « Working within Limits » (loc.gov/apis/json-and-yaml/working-within-limits/) : tableau des limites actuelles, ligne « Image Services » : 150 requêtes par minute, blocage de 1 heure en cas de dépassement. La page ajoute que la limitation est « strongly encouraged » et qu''il faut prévoir une pause sur les codes 429 et les CAPTCHA. La page des services d''images (loc.gov/apis/micro-services/image-services/, API IIIF sur tile.loc.gov) renvoie à cette page pour les limites, sans en reproduire la valeur. Point d''attention : la page des limites ne cite pas tile.loc.gov explicitement.'
iiif_image: Image Services « implemented using the IIIF Image API » (page officielle loc.gov/apis/micro-services/image-services)
iiif_presentation: NON PRÉSENT dans les sources lues (guide IIIF 2024 seulement)
acces: 'Aucune clé ni authentification : « The API is accessible to the public with no API key or authentication required. » (page officielle)'
moissonnage: 'Recommandation de pagination : ≤ 1 000 éléments par page (JSON/YAML, pas IIIF)'
robots_waf: 'Gestion attendue des codes 429 et des CAPTCHA HTML : « Users may want to add handling to pause when encountering 429 status codes and HTML CAPTCHA responses. » (page officielle)'
bots_ia: NON PRÉSENT dans les sources lues
droits: NON PRÉSENT dans les sources lues
conflits:
- 'Page juridique loc.gov/legal : « no more than 10 requests per minute to our applications » (recommandation générale, périmètre différent des services d''images)'
lacunes:
- règle d'appliquer le quota (IP, clé) non détaillée
- conditions de réutilisation des images non lues
methode: 'WebSearch « Library of Congress IIIF API rate limit requests per second loc.gov iiif » : page officielle des limites trouvée ; WebFetch working-within-limits : tableau Image Services 150/min, 1 h ; résumé non verbatim ; WebFetch image-services : renvoi vers les limites, sans valeur propre'
verifie_le: '2026-11-13'
sources:
- url: https://www.loc.gov/apis/json-and-yaml/working-within-limits/
  note: '(tableau : Image Services 150/min, 1 h)'
  surveiller: true
- url: https://www.loc.gov/apis/micro-services/image-services/
  note: (renvoi vers « Working within Limits », pas de valeur propre)
  surveiller: true
- url: https://blogs.loc.gov/thesignal/2018/05/iiif-at-the-library-of-congress/
  note: '(blog 2018 : jusqu''à 30 requêtes IIIF par seconde en heure de pointe ; ancien, non retenu)'
  surveiller: true
---

# Library of Congress

**Verdict** : CHIFFRE TROUVÉ (page officielle ; application IIIF à préciser)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Library of Congress IIIF API rate limit requests per second loc.gov iiif » : page officielle des limites trouvée
- WebFetch working-within-limits : tableau Image Services 150/min, 1 h ; résumé non verbatim
- WebFetch image-services : renvoi vers les limites, sans valeur propre
