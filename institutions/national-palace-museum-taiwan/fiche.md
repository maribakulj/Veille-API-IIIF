# National Palace Museum – Taiwan (`national-palace-museum-taiwan`)

- **Classeur** : GLAM-080 · Taïwan · audit v2 du 2026-11-14 · Suivi : `CONSIGNE-ET-SUIVI.md`
- **Hôtes** : `digitalarchive.npm.gov.tw` (notices, manifestes), `iiifod.npm.gov.tw` (images), `www.npm.gov.tw`, `theme.npm.edu.tw`.

## Sources
- Déclaration d'ouverture des données (`sources/doc`, `sources/doc2`) : images 1 Mpx en CC0, 6 Mpx en CC BY 4.0, sans demande, sans limite d'usage, gratuit. Aucune limite de débit.
- Page de notice (`sources/doc3`) : lien « Copier le lien IIIF » vers `Integrate/GetJson?cid=2383&dept=U` ; le PDF `NPMIIIF.pdf` (description du service IIIF) n'a pu être téléchargé (délai dépassé deux fois ; `sources/doc4`, `sources/doc5`) : à vérifier à la main.
- robots.txt : `digitalarchive` Disallow vide ; `www` 404 ; `theme.npm.edu.tw` boucle de redirections ; `iiifod` délai dépassé.

## Tests (2 passes, configurations committées avant lancement, pauses 6 s)
- Passe 1 : manifeste GET 200 (6,4 ko, aucun en-tête de limite, CORS ouvert) ; HEAD 555.
- Passe 2 : liste d'annotations 200 (corps vide) ; `info.json` et vignette sur `iiifod.npm.gov.tw` : délai dépassé (aucun 403, 429 ni défi).
- Aucun 429, aucun en-tête de limite.

## Web (4 recherches, une par catégorie)
- Institution : déclaration d'ouverture lue, pas de limite de débit.
- Utilisateurs, tickets, présentations : aucun résultat utile. GreatFire signale un blocage depuis la Chine continentale (résumé de moteur, non vérifié). Une Open API à clé est citée dans une présentation de hackathon (non lue, à vérifier).

## Conclusion
Limite chiffrée : aucune. Pas d'en-tête de limite. Le service d'images n'a pas répondu depuis ce poste (cause inconnue). Confiance : faible. Décision prise seul : crash test prévu sur le manifeste (`config/crash-manifeste.json`), à lancer à la fin.
