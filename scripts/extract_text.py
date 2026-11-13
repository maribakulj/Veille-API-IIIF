#!/usr/bin/env python3
"""Extrait le texte lisible des pages HTML téléchargées par fetch_doc.sh.

Usage : python3 scripts/extract_text.py <dossier_sources>   (ex. institutions/bnf-gallica/sources/suite3)
Écrit <dossier>/text/NN.txt (texte brut, sans scripts ni styles) pour chaque raw/NN.html,
et affiche pour chaque page : taille du texte et phrases contenant des termes de limite,
de quota, de robots, d'API ou de contact. Le contrôle est reproductible : même entrée,
même sortie.
"""
import html
import re
import sys
from pathlib import Path

TERMES = (r"limit\w*|quota\w*|per (?:minute|hour|day)|par (?:minute|heure|jour)|\d+ ?(?:appels?|requêtes?|requests?)|"
          r"rate|throttl\w*|robots?|bots?|crawl\w*|moissonn\w*|harvest\w*|scrap\w*|automat\w*|"
          r"intelligence artificielle|\bIA\b|\bAI\b|API|IIIF|captcha|429|Retry-After|"
          r"contact\w*|licen[cs]e\w*|réutilis\w*|conditions d.utilisation|terms of use|abus\w*|interdit\w*|prohib\w*")


def texte(chemin):
    s = Path(chemin).read_text(encoding="utf-8", errors="replace")
    s = re.sub(r"(?is)<(script|style|noscript|svg).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|tr|section|article)>", "\n", s)
    t = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"[ \t\r\f\v]+", " ", re.sub(r"\n\s*\n+", "\n", t)).strip()


def main():
    dossier = Path(sys.argv[1])
    sortie = dossier / "text"
    sortie.mkdir(exist_ok=True)
    motif = re.compile(TERMES, re.I)
    for f in sorted((dossier / "raw").glob("*.html")):
        t = texte(f)
        (sortie / (f.stem + ".txt")).write_text(t + "\n", encoding="utf-8")
        phrases = [p.strip() for p in re.split(r"(?<=[.!?])\s+|\n", t) if 20 < len(p.strip()) < 400]
        sel = []
        for p in phrases:
            if motif.search(p) and p not in sel:
                sel.append(p)
        print(f"== {f.name} : {len(t)} caractères, {len(sel)} phrases à termes sensibles")
        for p in sel[:int(sys.argv[2]) if len(sys.argv) > 2 else 8]:
            print("   -", p[:230])


if __name__ == "__main__":
    main()
