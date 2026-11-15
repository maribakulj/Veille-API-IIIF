#!/usr/bin/env python3
"""Contrôler la traçabilité des observations de rattrapage ajoutées aux data.json.

Les données institutionnelles sont la source du benchmark. Toute entrée web ajoutée
par les rapports VERIFICATIONS-CHATGPT doit pointer vers un rapport *versionné*
qui nomme expressément la même URL. Le contrôle est local, sans réseau.

Attention : ce contrôle de correspondance n'authentifie PAS une copie Web et ne
remplace ni un original sauvegardé (SHA-256), ni une mesure HTTP, ni la méthode
complète a–g (CONSIGNE-ET-SUIVI.md). Les sources originales restent à conserver
dans sources/ quand leur capture est autorisée et possible.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

DATE = re.compile(r"^20\d\d-\d\d-\d\d$")
PREFIX = "VERIFICATIONS-CHATGPT-"


def verifier(root: Path) -> tuple[int, list[str]]:
    erreurs: list[str] = []
    total = 0
    rapports: dict[str, str] = {}
    for data_path in sorted((root / "institutions").glob("*/data.json")):
        data = json.loads(data_path.read_text(encoding="utf-8"))
        fiche_path = data_path.with_name("fiche.md")
        fiche = fiche_path.read_text(encoding="utf-8") if fiche_path.is_file() else ""
        for index, web in enumerate(data.get("web") or [], start=1):
            if not isinstance(web, dict):
                continue
            preuve = str(web.get("preuve", ""))
            if not preuve.startswith(PREFIX):
                continue
            total += 1
            ident = f"{data_path.parent.name}:web[{index}]"
            url = str(web.get("url", "")).strip()
            if not url.startswith(("https://", "http://")):
                erreurs.append(f"{ident}: URL manquante ou invalide")
            if not DATE.fullmatch(str(web.get("date", ""))):
                erreurs.append(f"{ident}: date de consultation YYYY-MM-DD manquante")
            if not str(web.get("citation", "")).strip():
                erreurs.append(f"{ident}: résumé/citation manquant")
            if not re.fullmatch(r"VERIFICATIONS-CHATGPT-[\w.-]+\.md", preuve):
                erreurs.append(f"{ident}: preuve hors des rapports racine autorisés ({preuve})")
                continue
            preuve_path = root / preuve
            if not preuve_path.is_file():
                erreurs.append(f"{ident}: rapport absent ({preuve})")
                continue
            if preuve not in rapports:
                rapports[preuve] = preuve_path.read_text(encoding="utf-8")
            if url not in rapports[preuve]:
                erreurs.append(f"{ident}: URL absente du rapport {preuve}")
            if preuve not in fiche:
                erreurs.append(f"{ident}: rapport non cité dans fiche.md ({preuve})")
    return total, erreurs


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    total, erreurs = verifier(root)
    for message in erreurs:
        print("ERREUR PREUVE :", message)
    print(f"Observations complémentaires validées : {total} ; erreurs : {len(erreurs)}")
    if total == 0:
        print("ERREUR : aucune observation récente vérifiée ; possible mauvais dossier.")
        return 1
    return 1 if erreurs else 0


if __name__ == "__main__":
    raise SystemExit(main())
