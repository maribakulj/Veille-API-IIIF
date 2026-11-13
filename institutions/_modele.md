---
# Modèle de fiche. Les fichiers commençant par « _ » ne sont pas traités par les scripts.
# Copier ce fichier en GLAM-NNN-nom-de-linstitution.md et remplir les champs.
id: GLAM-000                 # identifiant unique, format GLAM-NNN
institution: Nom officiel de l'institution ou de la plateforme
pays: France
statut: NON TROUVÉ APRÈS RECHERCHE (exemple)   # doit commencer par un préfixe reconnu (voir README)
classe: non trouvé après recherche              # doit correspondre au statut (validate.py le vérifie)
statut_quota: ''            # justification du statut, avec la source
debit_iiif: NON PRÉSENT    # chiffre et périmètre, ou NON PRÉSENT SUR CETTE PAGE
iiif_image: ''              # version de l'Image API, avec la page où elle est dite
iiif_presentation: ''
api_recherche: ''
change_discovery: ''
acces: ''                   # clé, compte, accès public : avec la source
moissonnage: ''             # OAI-PMH, dumps, export
robots_waf: ''
bots_ia: ''
droits: ''
strategie: ''
conflits: []                # contradictions entre sources, à trancher
lacunes: ''                 # ce qui n'a pas été trouvé
methode: ''                 # comment la fiche a été établie (recherches, pages lues)
verifie_le: 2026-01-01      # AAAA-MM-JJ, date de la dernière vérification
sources:
  - url: https://exemple.org/doc-api
    note: 'lue : page de documentation API'
    surveiller: true        # true = suivie par check_sources.py ; false si refusée ou non lisible
---

# Nom de l'institution

**Verdict** : reprendre le champ statut.

## Notes

Texte libre : contexte, décisions, points à reconfirmer.

## Traces de vérification

- Date : recherche ou lecture, avec l'URL consultée.
