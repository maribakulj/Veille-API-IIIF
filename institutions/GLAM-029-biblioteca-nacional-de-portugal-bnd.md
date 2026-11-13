---
id: GLAM-029
institution: Biblioteca Nacional de Portugal – BND
pays: Portugal
statut: DOC LUE, AUCUN CHIFFRE (page d’aide lue ; pas d’API documentée)
classe: doc lue, sans chiffre
statut_quota: 'DOC LUE, AUCUN CHIFFRE : aucun seuil ni quota ; téléchargements sans plafond annoncé'
debit_iiif: 'Aucun seuil publié sur la page d’aide. Les résultats s’affichent par 10, 20 ou 50 : c’est un réglage d’affichage. Téléchargements PDF et JPG sans plafond de nombre ni de taille annoncé. IIIF est cité une fois, pour ouvrir une ressource depuis la page de notice, sans limite. Les documents marqués « Interno » ne se téléchargent pas : règle de droits, non un débit.'
iiif_image: NON VÉRIFIÉ (version non précisée)
iiif_presentation: Manifestes IIIF accessibles depuis la fiche (aide BND) ; version non précisée
acces: NON VÉRIFIÉ
moissonnage: Métadonnées BND en open data (RDF/XML, JSON, Turtle) ; données IIIF non décrites
robots_waf: NON VÉRIFIÉ
droits: 'Métadonnées : « free reuse » annoncé ; images : mention PUBLIC DOMAIN sur fiches Biblissima (tiers)'
lacunes:
- aucune API documentée sur la page d’aide
- documentation IIIF de la plateforme non trouvée
methode: 'WebSearch « BNP IIIF API limite pedidos condições de utilização » : aide BNDigital, sans limite ; WebFetch bndigital.bnportugal.gov.pt/en/help : aucune limite, téléchargement et droits seulement ; Passe 2 (2026-11-13) : 1 WebFetch (aide).'
verifie_le: '2026-11-13'
sources:
- url: https://bndigital.bnportugal.gov.pt/en/help
  note: '(lue : aucun chiffre)'
  surveiller: true
- url: https://bndigital.bnportugal.gov.pt/en/about-us
  note: '(présentation : identifiants pérennes incluant IIIF, sans chiffre)'
  surveiller: true
- url: https://www.gov.br/bn/pt-br/atuacao/processamento-e-preservacao/diretorio-de-preservacao-pasta/arquivos/apresentacao-inovacoes-tecnologicas-na-bndigital-iiif.pdf
  note: '(présentation d''une autre BN, non officielle pour la BND : hors périmètre)'
  surveiller: true
---

# Biblioteca Nacional de Portugal – BND

**Verdict** : DOC LUE, AUCUN CHIFFRE (aide officielle lue ; pas de page d'API IIIF)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « BNP IIIF API limite pedidos condições de utilização » : aide BNDigital, sans limite
- WebFetch bndigital.bnportugal.gov.pt/en/help : aucune limite, téléchargement et droits seulement

## Passe 2 (2026-11-13)
- WebFetch en/help : aucun seuil ; affichage 10, 20 ou 50 par page ; PDF et JPG sans plafond annoncé ; pas de clé ni d’API mentionnée.
