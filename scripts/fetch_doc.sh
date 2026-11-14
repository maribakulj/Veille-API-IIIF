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
HERE="$(cd "$(dirname "$0")/.." && pwd)"
MAIN="$(cd "$(dirname "$(git -C "$HERE" rev-parse --path-format=absolute --git-common-dir)")" && pwd)"
slug=$(printf '%s' "$out" | sed -n 's#.*institutions/\([^/]*\)/.*#\1#p')
if [ -n "$slug" ]; then
  VEILLE_REPO="$HERE" VEILLE_DATA="$MAIN/data" python3 "$MAIN/scripts/suivi.py" autorise "$slug" || exit 1
fi
mkdir -p "$out/raw"
: > "$out/FETCH.log"
UA="VeilleAPIIIF/0.1 (veille documentaire; github.com/maribakulj/Veille-API-IIIF)"
n=0
bloques=""
while IFS= read -r url; do
  [ -z "$url" ] && continue
  n=$((n+1))
  f="$out/raw/$(printf '%02d' $n).html"
  host=$(printf '%s' "$url" | sed -E 's#^[a-z]+://([^/]+).*#\1#')
  if raison=$(python3 "$MAIN/scripts/hostlock.py" bloque "$host"); then
    : > "$f"
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | SKIP | 0 o | $url" >> "$out/FETCH.log"
    echo "SAUTÉ (hôte $host arrêté, registre partagé : $raison) : $url" >&2
    continue
  fi
  case " $bloques " in
    *" $host "*)
      : > "$f"
      echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | SKIP | 0 o | $url" >> "$out/FETCH.log"
      echo "SAUTÉ (hôte $host déjà en 403/défi/429 : on n'insiste pas) : $url" >&2
      continue ;;
  esac
  python3 "$MAIN/scripts/hostlock.py" attendre "$host" 3
  code=$(curl -sS -L --max-redirs 3 -A "$UA" --max-time 30 -o "$f" -w '%{http_code}' "$url" 2>>"$out/FETCH.log" || echo "ERR")
  python3 "$MAIN/scripts/hostlock.py" redact "$f"
  case "$url" in */robots.txt) python3 "$MAIN/scripts/hostlock.py" noter_robots "$host" "$f" ;; esac
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) | $code | $(wc -c < "$f" 2>/dev/null || echo 0) o | $url" >> "$out/FETCH.log"
  # 403 / 405 / 429 ou défi anti-bot : l'hôte est arrêté pour le reste de la liste (règle : jamais d'insistance) ;
  # un 429 arrête toute la liste.
  if [ "$code" = "429" ]; then echo "429 reçu : arrêt de toute la liste" >&2; break; fi
  gateway=0
  grep -qiE "Missing Authentication Token|API_KEY_MISSING|invalid_apikey" "$f" 2>/dev/null && gateway=1
  fort=0
  if [ "$(wc -c < "$f" 2>/dev/null || echo 0)" -lt 30000 ] && grep -qiE "verifying your browser|human verification|request blocked|just a moment|attention required|making sure you.re not a bot|verification required|checking your browser|cf-turnstile|challenges\.cloudflare\.com|x-amzn-waf-action" "$f" 2>/dev/null; then fort=1; fi
  # 403/405 : bloquant, sauf réponse de passerelle d'API ou de clé manquante ; page 200 : seulement un marqueur FORT de défi
  if { { [ "$code" = "403" ] || [ "$code" = "405" ]; } && [ "$gateway" = "0" ]; } || [ "$fort" = "1" ]; then
    bloques="$bloques $host"
    python3 "$MAIN/scripts/hostlock.py" bloquer "$host" "fetch_doc $code $(date -u +%FT%TZ)"
  fi
  sleep 3
done < "$list"
( cd "$out/raw" && shasum -a 256 *.html > ../SHA256SUMS )
echo "terminé : $n URL, manifeste : $out/SHA256SUMS"
