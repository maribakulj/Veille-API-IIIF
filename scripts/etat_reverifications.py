#!/usr/bin/env python3
"""Inventorier les vérifications IIIF et rapprocher le registre de réexamen.

Le script ne visite aucune URL, n'écrit pas les data.json et ne modifie pas
BENCHMARK.xlsx. Les statuts documentaires ne prouvent ni HTTP 200 ni absence
de quota. Utilisation :
  python scripts/etat_reverifications.py --root . --out data/etat-reverifications.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


def normalize_url(url: str) -> str:
    """Normalisation conservatrice : casse du domaine, sans effacer les chemins."""
    url = url.strip()
    if url.startswith("mailto:"):
        return "mailto:" + url[7:].casefold()
    try:
        parsed = urlsplit(url)
        if not parsed.scheme or not parsed.netloc:
            return url
        return urlunsplit(
            (parsed.scheme.lower(), parsed.netloc.lower(),
             parsed.path, parsed.query, parsed.fragment)
        )
    except ValueError:
        return url


def preliminary_category(url: str, reason: str) -> str:
    s = (reason or "").casefold()
    if url.startswith("mailto:") or "formulaire (post)" in s:
        return "CONTACT_OU_ACTION_HUMAINE"
    if any(x in s for x in ("captcha", "cloudflare", "403", "waf",
                            "anubis", "défi javascript", "anti-bot",
                            "verifying your browser", "incapsula")):
        return "PROTECTION_OU_REFUS"
    if any(x in s for x in ("timeout", "délai dépassé",
                            "dns", "tls", "certificat", "connexion coupée")):
        return "ERREUR_RESEAU"
    if any(x in s for x in ("404", "ancienne page", "page d'accueil",
                            "renvoie l'accueil", "url tronquée")):
        return "URL_OBSOLETE_OU_DEPLACEE"
    if any(x in s for x in ("page lue", "lue", "lu en direct", "déjà lu")):
        return "LECTURE_DEJA_MENTIONNEE"
    return "A_QUALIFIER"



def qualifier_lecture(matches: list[dict]) -> str:
    """État du CONTENU, indépendant d'un éventuel contrôle HTTP à refaire.

    Seuls les nouveaux statuts de lecture explicitement qualifiés sont promus :
    une ancienne note DOCUMENT_LU non datée n'est pas suffisante.
    """
    status = [m.get("statut_doc_2026_11_14", "") for m in matches]
    direct = (
        "TEXTE_ORIGINAL_LU_2026_11_14",
        "TEXTE_ORIGINAL_LU_RESTRICTION_2026_11_14",
        "REDIRECTION_ORIGINALE_LUE_2026_11_14",
        "PAGE_ORIGINALE_LUE_DEPRECATION_2026_11_14",
        "PDF_NEUF_PAGES_LU_2026_11_14",
    )
    if any(x in direct for x in status):
        return "TEXTE_LU_PAR_LECTEUR_WEB"
    indexed_prefixes = (
        "COPIE_", "PDF_TEXTE_", "JSON_MANIFESTE_EXTRAIT_",
        "ROBOTS_TEXTE_INDEXE_", "PAGE_ENDPOINT_TEXTE_LU_",
    )
    if any(x.startswith(indexed_prefixes) for x in status):
        return "TEXTE_RECUPERE_COPIE_DATEE"
    return "CONTENU_NON_DEMONTRE_PAR_REPRISE_O"


def agregger_constats(matches: list[dict], travail_initial: str) -> dict:
    """Préserver TOUS les constats d'une même URL, même contradictoires.

    Une corroboration de la cible d'un lien ne lève pas un blocage HTTP.
    Aucun statut du registre ne signifie qu'une URL est techniquement close.
    """
    def uniques(values):
        return list(dict.fromkeys(v.strip() for v in values if v and v.strip()))

    statuts = uniques(m.get("statut_doc_2026_11_14", "") for m in matches)
    preuves = uniques(m.get("source_preuve", "") for m in matches)
    actions = uniques(m.get("reste_a_verifier", "") for m in matches)
    return {
        "nombre_constats": len(matches),
        "statut_revision": " | ".join(statuts) if statuts else "NON_REEXAMINE_DANS_REGISTRE",
        "preuve": " | ".join(preuves),
        "reste_a_verifier": " | ".join(actions) if actions else travail_initial,
        "verification_http_independante": "NON_ETABLIE_PAR_LE_REGISTRE",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--ledger", type=Path,
                        default=Path("data/reverifications-chatgpt-2026-11-14.csv"))
    parser.add_argument("--out", type=Path,
                        default=Path("data/etat-reverifications.csv"))
    args = parser.parse_args()
    root = args.root.resolve()
    manual = []
    for path in sorted((root / "institutions").glob("*/data.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        slug = path.parent.name
        for idx, item in enumerate(data.get("a_verifier_manuellement") or [], start=1):
            if not isinstance(item, dict):
                continue
            url = str(item.get("url", "")).strip()
            manual.append({
                "slug": slug, "rang": idx, "url": url,
                "norm_url": normalize_url(url),
                "raison_initiale": str(item.get("pourquoi", "")),
                "recherche_initiale": str(item.get("a_chercher", "")),
            })

    ledger_path = root / args.ledger
    ledger = {}
    if ledger_path.exists():
        with ledger_path.open(encoding="utf-8", newline="") as handle:
            for entry in csv.DictReader(handle):
                key = (entry.get("slug", ""), normalize_url(entry.get("url_initiale", "")))
                ledger.setdefault(key, []).append(entry)

    seen = Counter((x["slug"], x["norm_url"]) for x in manual)
    cross = defaultdict(set)
    for entry in manual:
        cross[entry["norm_url"]].add(entry["slug"])

    records = []
    used = set()
    for item in manual:
        key = item["slug"], item["norm_url"]
        match = ledger.get(key, [])
        for m in match:
            used.add(id(m))
        if seen[key] > 1:
            duplicate = "DOUBLON_DANS_INSTITUTION"
        elif len(cross[item["norm_url"]]) > 1:
            duplicate = "REFERENCE_INTER_INSTITUTIONS"
        else:
            duplicate = ""
        agregat = agregger_constats(match, item["recherche_initiale"])
        records.append({
            "institution": item["slug"],
            "rang": item["rang"],
            "url": item["url"],
            "categorie_preliminaire": preliminary_category(
                item["url"], item["raison_initiale"]),
            "signal_doublon": duplicate,
            "lecture_documentaire": qualifier_lecture(match),
            **agregat,
            "raison_initiale": item["raison_initiale"],
        })

    output = root / args.out
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["institution", "rang", "url", "categorie_preliminaire",
              "signal_doublon", "lecture_documentaire", "nombre_constats", "statut_revision",
              "preuve", "reste_a_verifier", "verification_http_independante",
              "raison_initiale"]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

    covered = sum(x["statut_revision"] != "NON_REEXAMINE_DANS_REGISTRE" for x in records)
    unmatched = [(m.get("slug"), m.get("url_initiale"))
                 for values in ledger.values() for m in values if id(m) not in used]
    summary = {
        "institution_json": len(list((root / "institutions").glob("*/data.json"))),
        "lignes_manuelles": len(records),
        "lignes_avec_constat_ledger": covered,
        "lignes_sans_constat_ledger": len(records) - covered,
        "lignes_avec_plusieurs_constats": sum(x["nombre_constats"] > 1
                                               for x in records),
        "lignes_texte_lu_lecteur_web": sum(x["lecture_documentaire"] ==
                                          "TEXTE_LU_PAR_LECTEUR_WEB"
                                          for x in records),
        "lignes_texte_recupere_copie_datee": sum(x["lecture_documentaire"] ==
                                                "TEXTE_RECUPERE_COPIE_DATEE"
                                                for x in records),
        "lignes_contenu_non_demontre": sum(x["lecture_documentaire"] ==
                                          "CONTENU_NON_DEMONTRE_PAR_REPRISE_O"
                                          for x in records),
        "constats_associes_aux_lignes_manuelles": sum(x["nombre_constats"]
                                                     for x in records),
        "doublons_intra": sum(x["signal_doublon"] == "DOUBLON_DANS_INSTITUTION"
                             for x in records),
        "references_inter_institutions": sum(
            x["signal_doublon"] == "REFERENCE_INTER_INSTITUTIONS"
            for x in records),
        "observations_supplementaires_hors_liste": len(unmatched),
        "observations_hors_liste_exemples": unmatched[:20],
        "categories_preliminaires": dict(Counter(x["categorie_preliminaire"]
                                                for x in records)),
        "note": ("Les categories preliminaires sont heuristiques, non des "
                 "preuves. Les statuts ne certifient pas une requete HTTP."),
        "csv_sortie": str(output),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
