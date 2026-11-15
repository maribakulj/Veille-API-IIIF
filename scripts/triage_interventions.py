#!/usr/bin/env python3
"""Séparer les URL IIIF non lues des VRAIES actions humaines.

Entrée : data/etat-reverifications.csv, produit par etat_reverifications.py.
Ne visite aucune API et ne présume jamais d'une autorisation de crawler.
Ce triage est documentaire : une vérification de HTTP live demeure distincte.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

NON_LU = "CONTENU_NON_DEMONTRE_PAR_REPRISE_O"

# Les exceptions sont limitées aux démarches identifiées en lisant les sources,
# jamais à une supposition de quota ou d'accès public. La saisie et l'envoi
# d'un formulaire nécessitent une action explicite de l'utilisateur.
EXPLICIT_ACTIONS = {
    "mailto:bndigital@bnportugal.gov.pt":
        ("DEMANDE_INSTITUTIONNELLE", "Contacter la BNP pour la politique de script IIIF et le débit admis"),
    "https://docs.google.com/forms/d/1Fe1H4nOhFkrLpaeBpLAnSrIMYvcAxnYWm0IU9a6IkFA/viewform":
        ("DEMANDE_INSTITUTIONNELLE", "Obtenir une clé Harvard Art Museums si la recherche exige l'API officielle"),
    "https://contactus.npm.gov.tw/Web/case-apply.jsp?l=1&TArea=1":
        ("DEMANDE_INSTITUTIONNELLE", "Formulaire NPM : identité, captcha et confirmation par courriel, non soumis"),
    "https://archive.org/services/tasks.php?rate_limits=1&cmd=modify_xml.php":
        ("AUTORISATION_COMPTE", "Service Tasks Internet Archive sous authentification, hors IIIF ; écarter si non nécessaire"),
    "https://web.library.yale.edu/lit/servicecatalog/164929":
        ("AUTORISATION_COMPTE", "Page Yale institutionnelle SSO ; contacter équipe technique plutôt que contourner"),
}


# Substitutions prouvées dans la documentation officielle : on ne prétend
# PAS que l'ancienne URL donne le même contenu aujourd'hui.
OFFICIAL_SUBSTITUTES = {
    "https://emuseum.nich.go.jp/terms?locale=en":
        "https://emuseum.nich.go.jp/about?langId=en&webView=0",
    "https://www.qdl.qa/en/copyright-and-ethical-terms-reuse":
        "https://qdl.qa/en/copyright-ethical-terms-reuse",
    "https://dl.ndl.go.jp/ja/terms":
        "https://dl.ndl.go.jp/sitepolicy",
}


def qualifier(row: dict) -> dict:
    """Décision d'aiguillage, jamais une affirmation de disponibilité HTTP."""
    url = row["url"]
    states = row.get("statut_revision", "")
    path = urlsplit(url).path.lower()
    query = urlsplit(url).query.lower()
    if url in EXPLICIT_ACTIONS:
        kind, action = EXPLICIT_ACTIONS[url]
        return {"classe": kind, "intervention_utilisateur": "OUI_SI_NECESSAIRE",
                "action": action, "priorite": "P2"}

    if url in OFFICIAL_SUBSTITUTES:
        return {"classe": "SUBSTITUT_OFFICIEL_LU",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Ancienne URL non lue ; lire le remplacement institutionnel : " +
                          OFFICIAL_SUBSTITUTES[url],
                "priorite": "P3"}

    if url.endswith("/robots.txt"):
        return {"classe": "ROBOTS_OU_POLITIQUE_CRAWL",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Consulter les règles du domaine exact ou demander la politique au mainteneur ; aucun quota IIIF inféré",
                "priorite": "P2"}

    if "DOUBLON_DANS_INSTITUTION" in row.get("signal_doublon", "") or (
            row.get("signal_doublon") == "REFERENCE_INTER_INSTITUTIONS"):
        return {"classe": "REFERENCE_PARTAGEE",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Conserver une source et mutualiser la vérification sans multiplier les demandes",
                "priorite": "P3"}

    # Un info.json dont l'ancien client a suivi un 301 n'est PAS une
    # URL obsolète tant que le JSON n'a pas été récupéré.
    if path.endswith(("info.json", "/manifest", "/manifest.json", "/collection.json")) or (
            ".json" in path or ".xml" in path):
        return {"classe": "SERVICE_TECHNIQUE_A_VERIFIER",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Récupérer le contenu JSON/XML ou vérifier l'endpoint officiel depuis client autorisé",
                "priorite": "P1"}

    old = ("ANCIENNE_", "URL_", "REDIRECTION_", "PAGE_404", "PAGE_GENERIC",
           "PAGE_ANCIENNE", "DOCUMENT_SUBSTITUTION", "REST_URL_404")
    if any(part.startswith(old) for part in states.split(" | ")) or (
            "404" in states and not any(k in path for k in
                                     ("/iiif/", "/manifest", "info.json"))):
        return {"classe": "LIEN_HISTORIQUE_OU_DEPLACE",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Documenter nouvelle URL officielle, ne pas relire indéfiniment l'ancienne",
                "priorite": "P3"}

    if url.lower().endswith((".pdf", ".zip")):
        return {"classe": "PIECE_PDF_OU_ARCHIVE",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Lire les sections ou figures utiles ; distinguer PDF partiel, complet et simple lien",
                "priorite": "P2"}

    if ("SSO" in states or "AUTH_" in states or
            "SIGN_IN" in states or "COMPTE" in states):
        return {"classe": "AUTORISATION_COMPTE",
                "intervention_utilisateur": "OUI_SI_NECESSAIRE",
                "action": "Procédure officielle d'authentification ou demande de renseignement",
                "priorite": "P2"}

    if ("/iiif/" in path or "/manifest" in path or "info.json" in path or
            "/oai" in path or "api-docs" in path or "swagger" in path or
            "openapi" in path or "swagger" in query or
            "/v1/" in path or "/v2/" in path or "/rest/" in path or
            path.endswith("/feed/")):
        return {"classe": "SERVICE_TECHNIQUE_A_VERIFIER",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Vérifier corps JSON/XML et en-têtes depuis client autorisé, ou source institutionnelle actuelle",
                "priorite": "P1"}

    if any(k in states for k in
           ("DEFI_", "403", "401", "WAF", "CONNEXION_ECHOUEE", "HTTP_OUVERT")):
        return {"classe": "SOURCE_PROTEGEE_OU_INACCESSIBLE",
                "intervention_utilisateur": "CONDITIONNEL",
                "action": "Chercher source officielle alternative ; demander accès si indispensable à l'usage",
                "priorite": "P2"}

    if any(k in states for k in
           ("SHELL_", "NON_EXTRAIT", "DOCUMENT_NON_RECUPERE", "PAGE_EXTRACTEUR",
            "PAGE_TERMES_NON_LUE")):
        return {"classe": "PAGE_NON_EXPLOITABLE",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Chercher une page équivalente ou documentation sans demander de navigation humaine",
                "priorite": "P2"}

    if path in ("", "/") or url.endswith("/"):
        return {"classe": "RACINE_SANS_CONTRAT",
                "intervention_utilisateur": "NON_PAR_DEFAUT",
                "action": "Identifier point d'accès documenté ; page racine vide n'est pas une API en panne",
                "priorite": "P3"}

    return {"classe": "DOCUMENT_A_RECHERCHER",
            "intervention_utilisateur": "CONDITIONNEL",
            "action": "Source institutionnelle ou archive officielle à rechercher avant sollicitation",
            "priorite": "P2"}


def generate(rows: list[dict]) -> tuple[list[dict], dict]:
    result = []
    for row in rows:
        if row["lecture_documentaire"] != NON_LU:
            continue
        decision = qualifier(row)
        result.append({
            "institution": row["institution"],
            "rang": row["rang"],
            "url": row["url"],
            "type_de_suite": decision["classe"],
            "intervention_utilisateur": decision["intervention_utilisateur"],
            "priorite": decision["priorite"],
            "action_concrete": decision["action"],
            "statuts_documentaires": row["statut_revision"],
            "preuves_ou_notes": row["preuve"],
            "date_triage": "2026-11-15",
            "preuve_http_actuelle": "NON_ETABLIE_PAR_CE_TRIAGE",
        })
    counts = Counter(r["type_de_suite"] for r in result)
    return result, {
        "entrees_non_lues": len(result),
        "types_de_suite": dict(sorted(counts.items())),
        "demandes_explicites_ou_comptes": sum(
            r["intervention_utilisateur"] == "OUI_SI_NECESSAIRE" for r in result),
        "interventions_conditionnelles": sum(
            r["intervention_utilisateur"] == "CONDITIONNEL" for r in result),
        "non_a_faire_manuellement_par_defaut": sum(
            r["intervention_utilisateur"] == "NON_PAR_DEFAUT" for r in result),
        "note": ("Triage documentaire : pas de preuve que les pages non lues "
                 "sont indisponibles en HTTP ou qu'aucune action externe "
                 "n'est jamais nécessaire."),
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--infile", type=Path,
                   default=Path("data/etat-reverifications.csv"))
    p.add_argument("--out", type=Path,
                   default=Path("data/triage-interventions-humaines.csv"))
    p.add_argument("--summary", type=Path,
                   default=Path("data/resume-triage-interventions.json"))
    a = p.parse_args()
    with a.infile.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result, summary = generate(rows)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["institution", "rang", "url", "type_de_suite",
              "intervention_utilisateur", "priorite", "action_concrete",
              "statuts_documentaires", "preuves_ou_notes", "date_triage",
              "preuve_http_actuelle"]
    with a.out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(result)
    a.summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2),
                         encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
