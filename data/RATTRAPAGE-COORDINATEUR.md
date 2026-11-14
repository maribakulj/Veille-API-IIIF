# Rattrapages à faire par le coordinateur (tests marqués `non_teste` à cause d'un blocage du registre partagé jugé à tort)
- digital-commonwealth (lot A) : JSON de recherche, JSON d'item, manifeste Presentation sur www.digitalcommonwealth.org (faux positif reCAPTCHA).
- cardiff-university-library (lot A) : passe 3 images Ex Libris eu-img02 (info.json + dérivé) (403 de passerelle, pas un anti-bot).
- Vérifier aussi, à la fin, toute institution dont `non_teste` mentionne « registre partagé » ou « NON LANCÉ ».
- huntington-art-museum-botanical-gardens (lot E) : décision de l'agent : le 429 « Vercel Security Checkpoint » de www.huntington.org n'a arrêté que cet hôte, pas toute l'institution (la consigne d'origine dit « 429 = stop de l'institution ») : à confirmer par Marcel.
- utrecht-university-library (lot E) : catégorie web « tickets » non cherchée (quota de recherche épuisé) : refaire la recherche.
- waseda (lot E) : un agent a téléchargé un PDF par curl depuis web.archive.org (écart au briefing, hors domaine d'institution).
