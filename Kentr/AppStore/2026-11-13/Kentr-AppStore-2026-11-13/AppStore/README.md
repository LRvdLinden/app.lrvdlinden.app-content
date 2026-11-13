# Kentr – App Store-pakket 1.0.0 (build 1)

Eerste App Store-pakket voor Kentr (`app.lrvdlinden.kentr`), gemaakt op 13 november 2026. Er was nog geen bestaande content.

## Inhoud
| Map | Wat |
| --- | --- |
| `screenshots/nl-NL/iphone-6.3/` | 7 screenshots 1206 × 2622 |
| `screenshots/nl-NL/iphone-6.1/` | 7 screenshots 1179 × 2556 |
| `screenshots/nl-NL/ipad-13/` | 7 screenshots 2064 × 2752 |
| `screenshots/nl-NL/ipad-12.9/` | 7 screenshots 2048 × 2732 |
| `marketing/nl-NL/` | header 5244 × 2950 en 3840 × 1646, zoekresultaten 5244 × 2950, 3840 × 2560 en 1920 × 1280 |
| `metadata/nl-NL/`, `metadata/en-US/` | naam, ondertitel, promotietekst, beschrijving, trefwoorden, Wat is nieuw, URL's |
| `metadata/privacy/` | privacyverklaring NL en EN (platte tekst) |
| `metadata/review_information/` | App Review-notities (EN) met NL-kopie, contact, geen demo-account |
| `app-info.md` | categorie, leeftijd, privacylabel, toegankelijkheid, review-instellingen |

Volgorde van de screenshots: 1 Mijn auto's · 2 Kenteken opzoeken · 3 Fiscaal en bijtelling · 4 Kenteken terugvinden · 5 Auto zonder kenteken · 6 Overzicht · 7 Face ID en iCloud.

## Taal van de beelden
Alleen **nl-NL**: de app is alleen Nederlandstalig (`knownRegions` nl/Base, String Catalog alleen `nl`). Engelse beelden zouden de app verkeerd voorstellen. De teksten zijn er wel in NL en EN; App Store Connect toont op de Engelse pagina dan de NL-screenshots. De EN-beschrijving vermeldt dat de app in het Nederlands is.

## Nagemaakte schermen
De app kon hier niet gebouwd worden (geen Xcode). De schermen zijn **nagebouwd in HTML** op basis van de SwiftUI-code in `Kentr/Views/` (zelfde teksten, kleuren, opbouw) en gerenderd met headless Chrome. Verschillen met het echte toestel: lettertype Inter in plaats van SF Pro, iconen benaderen de SF Symbols, en er staan geen Wikimedia-voorbeeldfoto's in (de app toont dan het blauwe autoicoon; dat gebeurt ook als er geen foto is gevonden). Vervang ze bij voorkeur door simulatoropnamen (`xcrun simctl io booted screenshot`) met dezelfde voorbeelddata.

Voorbeelddata is fictief: alle kentekens bevatten klinkers in zijcodes waarin de RDW geen klinkers uitgeeft, dus ze bestaan niet. Prijzen en datums zijn verzonnen maar realistisch; de bijtelling is uitgerekend met de regels uit `Services/Bijtelling.swift`.

De bronbestanden (HTML-sjablonen en renderscripts) staan in de zip in `bron/`, omdat de app-repo voor deze run niet gewijzigd mocht worden.

## Uploadchecklist
1. App aanmaken in App Store Connect (bundle-id `app.lrvdlinden.kentr`, SKU idem, taal Dutch) en de Apple ID in `app-info.md` invullen.
2. Teksten uit `metadata/nl-NL` en `metadata/en-US` plakken (Engelse lokalisatie toevoegen).
3. Screenshots uploaden: iPhone 6,3" (of 6,1") en iPad 13" (of 12,9").
4. Categorie Utilities / Reference, leeftijd 4+, privacylabel "Data Not Collected", toegankelijkheid volgens `app-info.md`.
5. App Review: notes.txt plakken, contactgegevens invullen, "Sign-in required" uit.
6. Controleren dat https://kent.lrvdlinden.app, `/privacy/` en `/support/` online staan.
