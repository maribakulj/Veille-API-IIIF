---
id: GLAM-029
institution: Biblioteca Nacional de Portugal – BND
pays: Portugal
statut: DOC LUE, AUCUN CHIFFRE (aide officielle lue ; pas de page d'API IIIF)
classe: doc lue, sans chiffre
statut_quota: DOC LUE, AUCUN CHIFFRE (aide officielle lue ; pas de page d'API IIIF) ; Aide officielle lue ; aucune documentation d'API IIIF officielle trouvée
debit_iiif: Aucun débit, quota, nombre de requêtes, throttling, code 429 ni clé d'API sur la page d'aide officielle de la BND (bndigital.bnportugal.gov.pt/en/help). L'IIIF n'y apparaît que comme format de ressource accessible depuis la fiche ; téléchargement autorisé pour les documents libres, PDF et JPG ; documents « Interno » réservés au réseau interne. Les seuls nombres du texte concernent l'affichage des résultats (10, 20, 50 par page).
iiif_image: NON VÉRIFIÉ (version non précisée)
iiif_presentation: Manifestes IIIF accessibles depuis la fiche (aide BND) ; version non précisée
acces: NON VÉRIFIÉ
moissonnage: Métadonnées BND en open data (RDF/XML, JSON, Turtle) ; données IIIF non décrites
robots_waf: NON VÉRIFIÉ
droits: 'Métadonnées : « free reuse » annoncé ; images : mention PUBLIC DOMAIN sur fiches Biblissima (tiers)'
lacunes:
- doc IIIF technique à trouver
- 'domaine open data : « OPENDATA.bnportugal.pt » (page BND) vs « opendata.bnportugal.gov.pt » (classeur) : à vérifier'
methode: 'WebSearch « BNP IIIF API limite pedidos condições de utilização » : aide BNDigital, sans limite ; WebFetch bndigital.bnportugal.gov.pt/en/help : aucune limite, téléchargement et droits seulement'
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
