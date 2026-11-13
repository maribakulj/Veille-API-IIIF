---
id: GLAM-026
institution: Universitätsbibliothek Heidelberg
pays: Allemagne
statut: DOC LUE, AUCUN CHIFFRE (conditions d’utilisation lues ; documentation technique absente de cette page)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil, quota ni throttling sur la page des conditions ; clé non précisée'
debit_iiif: 'Aucun chiffre de limite de requêtes, de débit ni de quota sur la page des conditions. Les images sont marquées Public Domain Mark 1.0, avec une demande de mention de la bibliothèque : c’est une règle d’attribution, non un plafond. La page ne mentionne ni IIIF ni API, ne renvoie qu’à des pages de commande de reproductions, et ne dit pas si une clé est requise.'
iiif_image: 'Documentée – Image API v2 : digi.ub.uni-heidelberg.de/iiif/2/{identifiant}.jpg (extrait de manifest institutionnel)'
iiif_presentation: 'Documentée – manifest : digi.ub.uni-heidelberg.de/diglit/iiif/{id}/manifest (extrait de manifest institutionnel relu le 13/11/2026)'
api_recherche: NON PRÉSENT dans les sources lues
acces: NON PRÉSENT dans les sources lues
moissonnage: Lien seeAlso vers METS dans les manifestes ; bulk NON PRÉSENT
robots_waf: NON PRÉSENT dans les sources lues
bots_ia: NON PRÉSENT dans les sources lues
droits: 'CGU images : crédit « Universitätsbibliothek Heidelberg / Signature / page » ; demandes ultérieures par contact'
lacunes:
- documentation IIIF ou API non liée sur la page lue
- clé non précisée
- documentation technique à demander au service de numérisation
methode: 'WebSearch « Universitätsbibliothek Heidelberg IIIF Schnittstelle Nutzungsbedingungen » : conditions d''images, sans API ; WebFetch conditions d''utilisation des images : aucune limite, contact digitalisierung@ub ; Passe 2 (2026-11-13) : 1 WebFetch, résumé d’extraction (conditions d’utilisation).'
verifie_le: '2026-11-13'
sources:
- url: https://digi.ub.uni-heidelberg.de/en/bpd/projekt/nutzungsbedingungen.html
  note: '(lue : aucun chiffre)'
  surveiller: true
- url: https://ub.uni-heidelberg.de/fr/helios/digi/nutzung/Welcome.html
  note: (conditions d'utilisation des images, sans chiffre lu en extrait)
  surveiller: true
---

# Universitätsbibliothek Heidelberg

**Verdict** : DOC LUE, AUCUN CHIFFRE (conditions d'utilisation des images lues)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Universitätsbibliothek Heidelberg IIIF Schnittstelle Nutzungsbedingungen » : conditions d'images, sans API
- WebFetch conditions d'utilisation des images : aucune limite, contact digitalisierung@ub

## Passe 2 (2026-11-13)
- WebFetch conditions : aucun seuil ni throttling ; clé non précisée ; attribution exigée, non plafond.
