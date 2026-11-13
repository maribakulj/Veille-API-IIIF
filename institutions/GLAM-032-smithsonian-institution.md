---
id: GLAM-032
institution: Smithsonian Institution
pays: États-Unis
statut: PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement)
classe: pas de débit IIIF chiffré
statut_quota: PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement) ; Documentation api.data.gov lue en extrait (recherche de remplacement) ; documentation edan.si.edu non lue
debit_iiif: 'La documentation officielle d''api.data.gov (lue en extrait), plateforme qui gère les clés de l''API Open Access, indique une limite horaire par défaut de 1 000 requêtes par heure et par clé, susceptible de varier selon le service ; les clés de démonstration sont limitées à 30 requêtes par heure et 50 par jour, par adresse IP. Aucune valeur propre à Smithsonian n''a été lue, et l''API est REST : aucun chiffre IIIF.'
iiif_image: 'IIIF Image API (ids.si.edu/ids/iiif/) : démonstration sur page officielle'
iiif_presentation: 'IIIF Presentation API : présentée comme disponible (Mirador, Universal Viewer) ; version non précisée sur la page'
acces: NON PRÉSENT SUR CETTE PAGE
moissonnage: NON PRÉSENT SUR CETTE PAGE
robots_waf: NON PRÉSENT SUR CETTE PAGE
droits: NON PRÉSENT SUR CETTE PAGE
strategie: '« Currently there are millions of image assets that are IIIF enabled. » ; contact : ocio-iiif at si.edu'
lacunes: Lire la page Terms of Use et la doc EDAN ; confirmer si la clé api.data.gov a un quota propre.
methode: 'WebSearch « Smithsonian Open Access API IIIF rate limit api.si.edu terms of use » : pages Open Access et doc tierce ; WebFetch si.edu/openaccess/devtools : aucune limite, clé via api.data.gov ; WebSearch « Smithsonian Open Access API rate limit api.data.gov » : défauts api.data.gov trouvés ; pas de valeur propre à Smithsonian'
verifie_le: '2026-11-13'
sources:
- url: https://api.data.gov/docs/developer-manual
  note: '(lue en extrait : défaut de 1 000 requêtes par heure, variable selon le service)'
  surveiller: true
- url: https://www.si.edu/openaccess/devtools
  note: '(lue : aucun chiffre ; API sur api.data.gov)'
  surveiller: true
- url: https://dashboard.si.edu/openaccess/faq
  note: '(FAQ Open Access, extrait : formats dont IIIF JSON Manifest, sans limite)'
  surveiller: true
- url: https://api.data.gov/signup/
  note: (inscription de la clé, non lue)
  surveiller: false
---

# Smithsonian Institution

**Verdict** : PAS DE DÉBIT IIIF CHIFFRÉ (limite voisine seulement)

## Notes

_À compléter._

## Traces de la boucle de vérification (passe du 13/11/2026)

- WebSearch « Smithsonian Open Access API IIIF rate limit api.si.edu terms of use » : pages Open Access et doc tierce
- WebFetch si.edu/openaccess/devtools : aucune limite, clé via api.data.gov
- WebSearch « Smithsonian Open Access API rate limit api.data.gov » : défauts api.data.gov trouvés ; pas de valeur propre à Smithsonian
