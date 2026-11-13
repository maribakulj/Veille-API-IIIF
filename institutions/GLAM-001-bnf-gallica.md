---
id: GLAM-001
institution: BnF – Gallica
pays: France
statut: CHIFFRE TROUVÉ (page officielle)
classe: chiffre publié
statut_quota: 'CHIFFRE TROUVÉ (page officielle) ; Présentée comme transitoire : « La BnF est en train de déployer un gestionnaire d’API » ; date de mise à jour absente, seul « © 2020 BnF » figure sur la page'
debit_iiif: 'API IIIF Image : 5 appels/min en /full/full/ ou full/>1000 px ; bande passante 832 Ko/s ; API .TexteBrut 5/min ; API .PDF 4/min ; API image .highres 50/min ; dépassement = 429 Too Many Requests'
iiif_image: 'Extrait de page officielle api.bnf.fr : « API Image ... implémentée en version 1.1 à la BnF » (spec actuelle 3.0)'
iiif_presentation: 'Extrait de page officielle : « API Présentation ... implémentée en version 2.0 à la BnF » (spec actuelle 3.0). CONFLIT avec une 1re extraction « Version 2 » : retenir l''extrait explicite'
api_recherche: 'Page officielle : API de recherche et d''authentification « non implémentées à la BnF »'
change_discovery: ND
acces: Accès « ouvert sans restriction, sauf en cas d'usage abusif » (data.gouv.fr, fiche de l'API IIIF Gallica, source BnF)
moissonnage: 'OAI-NUM : notices Dublin Core, entrepôt mis à jour chaque semaine (bnf.fr/node/969) ; aucun quota cité sur cette page'
robots_waf: NON PRÉSENT SUR CETTE PAGE
bots_ia: NON PRÉSENT SUR CETTE PAGE
droits: Renvoi vers « Conditions d'utilisation des contenus de Gallica » (non reproduites)
conflits:
- 'Fiche technique de la page api.bnf.fr : « Version2 » (ambigu : la page cite aussi Image 1.1 et Presentation 2.0 dans une autre extraction)'
lacunes: Limite réelle de débit non publiée dans les pages lues ; à demander à la BnF si besoin.
methode: 'WebFetch fiche IIIF : pas de limite (échec de la première passe) ; WebSearch « api.bnf.fr IIIF Gallica 5 requêtes par minute » ; WebSearch « conditions d’utilisation limitation requêtes par minute » → node/232 ; WebFetch node/232 : limites confirmées, citées mot pour mot'
verifie_le: '2026-11-13'
sources:
- url: https://api.bnf.fr/fr/node/232
  note: ''
  surveiller: true
---

# BnF – Gallica

**Verdict** : CHIFFRE TROUVÉ (page officielle)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebFetch fiche IIIF : pas de limite (échec de la première passe)
- WebSearch « api.bnf.fr IIIF Gallica 5 requêtes par minute »
- WebSearch « conditions d’utilisation limitation requêtes par minute » → node/232
- WebFetch node/232 : limites confirmées, citées mot pour mot
