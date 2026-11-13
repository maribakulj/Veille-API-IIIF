#!/usr/bin/env bash
# Télécharge des pages de documentation (GET, une par une, pause de 3 s) et
# produit un manifeste SHA-256 reproductible.
#
# Usage : scripts/fetch_doc.sh <liste_urls.txt> <dossier_sortie>
# Résultat : <dossier_sortie>/raw/<n>.html, <dossier_sortie>/SHA256SUMS,
#            <dossier_sortie>/FETCH.log (URL, statut HTTP, date UTC, taille).
# Ne suit pas de liens : seules les URL de la liste sont téléchargées.
set -u
list="$1"; out="$2"
mkdir -p "$out/raw"
: > "$out/FETCH.log"
UA="VeilleAPIIIF/0.1 (veille documentaire; github.com/maribakulj/Veille-API-IIIF)"
n=0
while IFS= read -r url; do
  [ -z "$url" ] && continue
  n=$((n+1))
  f="$out/raw/$(printf '%02d' $n).html"
  code=$(curl -sS -L --max-redirs 3 -A "$UA" --max-time 30 -o "$f" -w '%{http_code}' "$url" 2>>"$out/FETCH.log" || echo "ERR")
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | $code | $(wc -c < "$f" 2>/dev/null || echo 0) o | $url" >> "$out/FETCH.log"
  sleep 3
done < "$list"
( cd "$out/raw" && shasum -a 256 *.html > ../SHA256SUMS )
echo "terminé : $n URL, manifeste : $out/SHA256SUMS"
