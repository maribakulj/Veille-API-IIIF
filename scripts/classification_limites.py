#!/usr/bin/env python3
"""Typologie prudente des restrictions documentaires pour le benchmark IIIF.

Une valeur contenant des chiffres peut désigner une taille, des droits, une
pagination ou une directive robots. Elle ne doit pas devenir automatiquement
une limite de débit, et une recommandation n'est pas un quota contraignant.
Le tri reste indicatif pour les anciennes données hétérogènes.
"""
from __future__ import annotations

import re


def categorie(lim: dict) -> str:
    nature = str(lim.get("nature", "")).casefold()
    scope = str(lim.get("perimetre", "")).casefold()
    if "hors iiif" in nature or "hors iiif" in scope:
        return "Autre API ou prestation (hors IIIF)"
    if any(k in nature for k in ("crawl-delay", "crawl delay", "request-rate",
                                  "robot", "exploration")):
        return "Directive robots.txt (≠ quota API)"
    if any(k in nature for k in ("pagination", "taille", "résultat",
                                  "resultat", "paquet", "lot oai",
                                  "paramètre limit", "parametre limit")):
        return "Pagination, dimensions ou volume par réponse"
    if any(k in nature for k in ("indicatif", "recommand", "politesse",
                                  "courtoisie", "best practice")):
        return "Recommandation (pas nécessairement contraignante)"
    if any(k in nature for k in ("droit", "licence", "crédit",
                                  "credit", "conditions", "copyright")):
        return "Droits et conditions de réutilisation"
    if "limite de débit" in nature or "limite waf" in nature:
        return "Seuil de débit indiqué (famille API à vérifier)"
    if "quota" in nature or "fréquence" in nature:
        return "Quota ou fréquence de service à qualifier"
    return "Autre règle ou contexte (ne pas assimiler à un quota)"


def seuil_debit_explicitement_identifie(lim: dict) -> bool:
    """Sous-ensemble CONSERVATEUR de débits, pas un recensement exhaustif.

    L'approbation de l'étape d, la source officielle et les données à
    revalider sont vérifiées ailleurs, par le générateur principal.
    """
    nature = str(lim.get("nature", "")).casefold()
    if not ("limite de débit" in nature or "limite waf" in nature):
        return False
    if categorie(lim) != "Seuil de débit indiqué (famille API à vérifier)":
        return False
    valeur = str(lim.get("valeur", ""))
    fenetre = str(lim.get("fenetre", "")).casefold()
    if not re.search(r"\d", valeur):
        return False
    return any(k in fenetre for k in
               ("minute", "seconde", "heure", "jour", "24 h", "5 min", "second",
                "hour", "day", "month", "mois"))


if __name__ == "__main__":
    raise SystemExit("Module de classification, à importer depuis le générateur")
