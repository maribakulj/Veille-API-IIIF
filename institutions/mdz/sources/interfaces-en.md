# Interfaces (EN) — page principale des API

- URL : https://www.digitale-sammlungen.de/en/interfaces
- Date de lecture (UTC) : 2026-11-13T21:20:13Z
- SHA-256 du texte ci-dessous (UTF-8) : `69f321e4dbe15364c788f2c8c5584c8ec89421f8e539677fca518895b2fe4a97`
- Taille HTTP du HTML : 41093 octets (téléchargement complet, non tronqué ; contrôle par curl)
- Méthode : HTML converti en texte (balises, scripts et styles retirés ; menus de navigation conservés, répétés en tête et en pied). Pas de résumé : texte intégral de la page.
- Lecture : intégrale ; la page est lue dans son texte converti, les liens sont dans le HTML brut conservé hors dépôt.

---

Search

 metadata

 full texts

 Filter

 keep active filters

- 
 Zu deutscher Sprachversion wechseln

 RSS

- 
 Collections

- 
 The MDZ

- 

 2D and 3D Digitization

- 

 Technologies and Software Development

- 

 Digital Long-term Preservation

- 

 Publications of the MDZ (In Selection)

- 
 Our Data Services

- 

 Download Options

- 

 Interfaces

- 

 Reproduction Orders (€)

- 
 Help

- 

 Search Help

- 

 Viewer Help

- 

 FAQ

- 

 Contact

- 

 Imprint

- 

 Privacy Policy

- 

 Disclaimer

- 

 Accessibility

 Close main menu

 Search

 metadata

 full texts

 Filter

 keep active filters

An error occurred while serving your page

Please make sure that you are using an up-to-date and supported browser (Edge, Firefox from version 68, Chrome from version 86, Safari from version 12). Otherwise we can't guarantee that the website is working as intended.
If you are already using an up-to-date browser, please try refreshing the site.
If the error persists, please get in touch via mdz@bsb-muenchen.de.

Interfaces

- 

 IIIF APIs

- 

 Presentation API

- 

 Image API

- 

 Bavarian Digital Repository

- 

 RSS Feed

IIIF APIs

You can integrate the contents of the Bavarian State Library, which are provided in the IIIF standard, directly into web offers via the APIs (Application Programming Interface) without having to download and maintain the data yourself.

When using a digital copy, please note the rights statement under which it is provided. Commercial use may be excluded. You can find more information on this in our 

FAQ

.

The interfaces described below provide their responses with the 

Access Control Allow-Origin: *

 header, making it possible to use provided data directly in client-side JavaScript applications. The Bavarian State Library provides the 

IIIF Presentation API

 and the 

IIIF Image API

. The former one delivers so called manifests of digital objects in JSON-LD format. Inside the manifests Image API endpoints for each facsimile image are referenced. An info.json file is available at each of these end points, which allows information about the image to be retrieved immediately.

Presentation API

You can use this interface to access the metadata of an object in JSON format, the so-called manifests. In addition to a range of bibliographic metadata (.metadata), you will find a data structure that lists all pages ('canvases') of an object (.sequences[0].canvases). Each of these canvas entries refers (under .images[0].resource.service[@id]) to the corresponding image API under which the image is accessible for the page. 

If available, OCR (full text) for the page is linked under .seeAlso[@id] in hOCR format. Please note that there is a limit to the number of OCR downloads that can be made per 24 hours. Access to the Presentation API is unlimited.

URL IIIF manifest: 

https://api.digitale-sammlungen.de/iiif/presentation/v2/{object_id}/manifest

Examples of a manifest:

https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00012345/manifest

https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00130380_00157_u001/manifest

Underlying specification: 

https://iiif.io/api/presentation/2.1/

URL top collection: 

https://api.digitale-sammlungen.de/iiif/presentation/v2/collection/top

Underlying specification: 

https://iiif.io/api/presentation/2.1/#collection

Image API

You can use this interface to access the digital image data in the Digital Collections. You can use the URL to control which section you would like to receive in which size, which rotation and which format. For more details, please consult the 

documentation of the IIIF Image API

.

- 

https://api.digitale-sammlungen.de/iiif/image/v2/{image_id}/{region}/{size}/{rotation}/{quality}.{format}

Example of an image file:

https://api.digitale-sammlungen.de/iiif/image/v2/bsb00109992_00001/full/full/0/default.jpg

- 

https://api.digitale-sammlungen.de/iiif/image/v2/{image_id}/info.json

Example of an info.json file:

https://api.digitale-sammlungen.de/iiif/image/v2/bsb00103155_00013/info.json

Underlying specification: 

https://iiif.io/api/image/2.1/

Please note that there is a limit to the number of requests that can be made to the Image API per 24 hours.

- 

https://api.digitale-sammlungen.de/ocr/{object_id}/{page_num}

Example of an OCR XML file:

https://api.digitale-sammlungen.de/ocr/bsb00000001/00010

Please note that there is a limit to the number of OCR downloads that can be made per 24 hours. 

Visit us on 

Github

. There you can find opensource IIIF software developed by the MDZ.

Bavarian Digital Repository

The 

Bavarian Digital Repository (BDR)

 is developed to be a freely accessible interface for harvesting metadata about all digital representations produced by or in cooperation with the Bavarian State Library. BDR conforms to the OAI Protocol for Metadata Harvesting (OAI-PMH).

RSS Feed

The 

RSS feed of the Munich DigitiZation Center

 presents the 50 most recent additions to the Digital Collections in the order in which they are made available online.

 The MDZ

 2D and 3D Digitization

 Technologies and Software Development

 Digital Long-term Preservation

 Publications of the MDZ (In Selection)

 Our Data Services

 Download Options

 Interfaces

 Reproduction Orders (€)

 Help

 Search Help

 Viewer Help

 FAQ

- 

 Contact

- 

 Imprint

- 

 Privacy Policy

- 

 Disclaimer

- 

 Accessibility

- 

 Sitemap

