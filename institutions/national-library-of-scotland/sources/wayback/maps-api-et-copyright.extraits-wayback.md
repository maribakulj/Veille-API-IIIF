# NLS (maps.nls.uk) — extraits verbatim de deux pages lues dans la Wayback Machine

- **Raison** : `maps.nls.uk` et `digital.nls.uk` renvoient à notre sonde une page « Human Verification » (CAPTCHA, statut 405). On ne la contourne pas ; les pages sont lues dans la Wayback Machine, sans envoyer de trafic au NLS.
- **Lecture** : outil `ia_get_snapshot`, texte complet lu le 2026-11-13. Le téléchargement par `curl` de copies Wayback est refusé par le système : les extraits sont recopiés à la main, vérifiables via les URL de réplique.

## 1. Historic Maps API — https://maps.nls.uk/projects/api/

- **Capture** : 2025-11-14 22:44:49 UTC (horodatage 20251114224449), statut 200, 16 788 caractères
- **Réplique** : https://web.archive.org/web/20251114224449/https://maps.nls.uk/projects/api/

> From March 2022, these layers all moved to the MapTiler Cloud API. There is no longer a fixed annual subscription fee, but different plans for different types of usage and quantity. **There is a 'free' tier for all non-commercial subscribers using 100,000 tile requests per month or less.**

> This work is licensed under a Creative Commons Attribution 3.0 Unported Licence. […] The only condition is that you must display an attribution to the National Library of Scotland, together with a link to our website, whenever our map is used.

**Portée** : ce quota concerne les **couches de cartes géoréférencées servies par MapTiler Cloud** (tuiles XYZ), pas le service IIIF d'images du NLS. Il faut une clé MapTiler (`?key=_YOUR_KEY_HERE`).

## 2. Copyright — https://maps.nls.uk/copyright.html

- **Capture** : 2025-12-03 20:47:50 UTC (horodatage 20251203204750), statut 200, 8 830 caractères
- **Réplique** : https://web.archive.org/web/20251203204750/https://maps.nls.uk/copyright.html

> We encourage re-use of the Library's map images based on certain conditions of use. However, we do not have complete rights over all images on this website. […] CC-BY. You are welcome to use some images displayed on the Map Images website for commercial, non-commercial, educational and private purposes under the terms of the Creative Commons Attribution (CC-BY) licence. Use is conditional on provision of attribution.

Le texte ne contient **aucune** règle sur l'accès automatisé, le débit, les robots ou le téléchargement en masse.

## 3. FAQ — https://maps.nls.uk/help/

**Non lue** : CAPTCHA pour notre sonde, et aucune copie Wayback n'existe depuis 2024 (`ia_find_snapshots` : « No snapshots found »).
