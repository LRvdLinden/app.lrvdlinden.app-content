# App-content

Marketingmateriaal per app: App Store-pakketten en social-media-content, als zip per datum.

Indeling: `<App>/<Soort>/<JJJJ-MM-DD>/`. In elke datummap staat de zip en ernaast een map met dezelfde naam (zonder `.zip`) met de uitgepakte inhoud, zodat je de bestanden direct op GitHub kunt bekijken.

## Pasr
- `Pasr/AppStore/`: App Store-pakket (screenshots per toestel, promobeelden, teksten NL en EN, review-notities, privacy).
  2026-11-27: pakket voor 1.0.5 (build 66), verdeeld over drie zips vanwege de 100 MB-grens van GitHub: `Pasr-AppStore-2026-11-27.zip` (LEESMIJ, app-icoon, teksten NL en EN, iPhone 6,9"/6,5"/6,3"/6,1" en Apple Watch), `Pasr-AppStore-2026-11-27-iPad-en-promo.zip` (iPad 13" en promobeelden) en `Pasr-AppStore-iPhoneDuo-2026-11-27.zip` (iPhone Duo binnenscherm); samen uitgepakt in de map `Pasr-AppStore-2026-11-27/`. Screenshots alleen nl-NL (de app is alleen Nederlands), 10 per toestel. Nieuw: tickets in de stijl van Apple Wallet, Voeg toe aan Pasr en de klantenkaart van een zaak; Apple Watch Ultra 3 (422×514) in een Ultra 3-mockup met een reserve zonder kader, Series 46 mm (416×496) zonder kader, en een grote Ultra 3-mockup (1688×2056) als promobeeld. Teksten bijgewerkt: promotietekst, beschrijving, trefwoorden, nieuw in deze versie, review-notities en App Privacy. Schermen nagebouwd uit de SwiftUI-code (Playwright). Bron: `appstore/` in LRvdLinden/app.lrvdlinden.pasr (`appstore/source/`, PR #38).
  2026-11-27-2: zelfde pakket, met de knop Voeg toe aan Pasr in de scène Voeg toe aan Pasr hoger (naast de naam van de zaak, niet meer half achter het venster): iPhone 07 (6,9"/6,5"/6,3"/6,1"), iPad 10 en Duo 09 opnieuw gemaakt, en de ingevulde review-notities (testevent en klantenkaart bij de demo-zaak Apple Review). Zips `Pasr-AppStore-2026-11-27-2.zip`, `Pasr-AppStore-2026-11-27-2-iPad-en-promo.zip` en `Pasr-AppStore-iPhoneDuo-2026-11-27-2.zip`, uitgepakt in `Pasr-AppStore-2026-11-27-2/`. Bron: PR #40 in LRvdLinden/app.lrvdlinden.pasr.
- `Pasr/Socials/`: banners en postteksten voor Instagram/Facebook (post en story), met alt-teksten.
  2026-11-27: `Pasr-Socials-2026-11-27.zip` plus dezelfde bestanden uitgepakt in de map `Pasr-Socials-2026-11-27/` (alleen Nederlands, algemene promotie van app en pasr.nl): Instagram/Facebook-post 1080×1080 en 1080×1350, story/reels 1080×1920, LinkedIn-post 1200×627, Facebook-cover 1640×624 en LinkedIn-cover 1584×396, met `posts.md` (postteksten en alt-teksten). Bron: `social/pasr-2026-11-27/` in LRvdLinden/app.lrvdlinden.pasr.
  2026-11-27-2: Instagram Reel (Nederlands, algemene promotie van app en pasr.nl): `Pasr-Socials-2026-11-27-2.zip` plus dezelfde bestanden uitgepakt in de map `Pasr-Socials-2026-11-27-2/`: `reel-1080x1920.mp4` (19,0 s, 30 fps, H.264, stille audiotrack; muziek kies je zelf in Instagram), omslag `reel-cover-1080x1920.png` en `posts.md` (caption, hashtags en alt-teksten). Bron: `social/pasr-reels-2026-11-27/` in LRvdLinden/app.lrvdlinden.pasr (PR #44).
- `Pasr/OG/`: OG-afbeeldingen van pasr.nl per datum (zip én uitgepakte map), homepage en `/zakelijk/` (Nederlands). Bron: `tools/og/` in LRvdLinden/app.lrvdlinden.pasr, gepubliceerd in `website/og/`.
  2026-11-23: voorbeeld van de OG-afbeelding per stempelkaart (`/zakelijk/kaart/<kaart-id>/`, Nederlands, 1200×630). Op de site krijgt elke gepubliceerde kaart er automatisch een (`/og/zakelijk/<kaart-id>.png`). Bron: `tools/make_kaart_pages.py` in LRvdLinden/app.lrvdlinden.pasr (branch `gedeelde-pasr`).
  2026-11-27: `Pasr-OG-2026-11-27.zip` plus dezelfde bestanden uitgepakt in de map `Pasr-OG-2026-11-27/`: `home-nl.png` (pasr.nl, Pasr voor klanten) en `zakelijk-nl.png` (pasr.nl/zakelijk/ en zakelijk-subpagina's, Pasr Zakelijk), beide Nederlands, 1200×630. Bron: `tools/og/build_og_html.py` en `tools/og/render.py` in LRvdLinden/app.lrvdlinden.pasr, gepubliceerd in `website/og/`.

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.pasr` (`appstore/` en `social/`).

## Pasr Zakelijk
- `Pasr Zakelijk/Socials/`: social banners en postteksten. 2026-11-27: `PasrZakelijk-Socials-2026-11-27.zip` plus dezelfde bestanden uitgepakt in de map `PasrZakelijk-Socials-2026-11-27/` (alleen Nederlands, algemene promotie van de app en pasr.nl/zakelijk): Instagram/Facebook-post 1080×1080 en 1080×1350, story/reels 1080×1920, LinkedIn-post 1200×627, Facebook-cover 1640×624 en LinkedIn-cover 1584×396, met `posts.md` (postteksten en alt-teksten). Bron: `social/pasr-zakelijk-2026-11-27/` in LRvdLinden/app.lrvdlinden.pasr.
  2026-11-27-2: Instagram Reel (Nederlands, algemene promotie van de app en pasr.nl/zakelijk): `PasrZakelijk-Socials-2026-11-27-2.zip` plus dezelfde bestanden uitgepakt in de map `PasrZakelijk-Socials-2026-11-27-2/`: `reel-1080x1920.mp4` (19,5 s, 30 fps, H.264, stille audiotrack; muziek kies je zelf in Instagram), omslag `reel-cover-1080x1920.png` en `posts.md` (caption, hashtags en alt-teksten). Bron: `social/pasr-zakelijk-reels-2026-11-27/` in LRvdLinden/app.lrvdlinden.pasr (PR #44).
- `Pasr Zakelijk/AppStore/`: App Store-pakket voor versie 1.0.0 (build 2) van de app voor ondernemers (bundle `app.lrvdlinden.pasrzakelijk`). Screenshots in NL en EN (de app is tweetalig) voor iPhone 6,9" (1320×2868), 6,5" (1284×2778), 6,3" (1206×2622) en 6,1" (1179×2556) en iPad 13" (2064×2752), 7 per toestel en taal, de productpagina-beelden (header 5244×2950 en 3840×1646, zoekresultaten 5244×2950, 3840×2560 en 1920×1280), het app-icoon, de teksten in NL en EN in `metadata/`, de privacytekst, de review-notities (Engels met Nederlandse kopie; demo-account, contact en Apple ID nog TODO) en `app-info.md` met categorie, leeftijd, privacylabel en toegankelijkheid. Zelfde stijl als de beelden van Pasr, met het icoon van Pasr Zakelijk en het mintgroene "ZAKELIJK". De schermen zijn nagebouwd in HTML op basis van de SwiftUI-code, met voorbeelddata (Koffiebar De Hoek).
- `Pasr Zakelijk/AppStore/2026-11-27/`: beelden voor versie 1.0.4 (build 21), in twee zips vanwege de limiet van 100 MB: `PasrZakelijk-AppStore-2026-11-27-NL.zip` en `-EN-US.zip` (elk de screenshots en productpagina-beelden van die taal plus de gedeelde teksten, bron en icoon), en het complete pakket uitgepakt in `PasrZakelijk-AppStore-2026-11-27/PasrZakelijk-AppStore/`. Nieuw: 10 screenshots per iPhone/iPad-toestel (o.a. tickets aan de deur, klantenkaart met korting, gezamenlijke acties), 7 Mac-screenshots 2880×1800 in een MacBook-mockup, het icoon van build 21 en de officiële Pasr-stempel. De teksten zijn nog die van 1.0.0 (tekstupdate volgt na goedkeuring). Schermen nagebouwd uit de SwiftUI-code. Bron: `zakelijk/appstore/` in LRvdLinden/app.lrvdlinden.pasr (PR #39).

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.pasr` (branch `gedeelde-pasr`, map `zakelijk/appstore/`, bron in `zakelijk/appstore/source/`).

## A-Alerts
- `A-Alerts/AppStore/`: App Store-pakketten. 2.0.0 (2026-11-08) in één zip. 2.0.1 (build 68, 2026-11-09, met het tabblad Nieuws, AMBER Alert en Vermist Kind Alert) in twee zips vanwege de limiet van 100 MB per bestand: `-iPhone` (iPhone 6,3" en 6,1", marketingbeelden, teksten NL en EN, review-notities, privacy) en `-iPad-Mac-Watch-TV` (screenshots voor iPad, Mac, Apple Watch en Apple TV). Screenshots alleen NL. Op 2026-11-13 zijn de afbeeldingen van 2.0.1 vernieuwd met schermen uit build 84 (teksten ongewijzigd), weer in twee zips: `2026-11-13/A-Alerts-AppStore-2026-11-13-iPhone.zip` en `-iPad-Mac-Watch-TV.zip`.
- `A-Alerts/Socials/`: banners (Instagram/Facebook post 1:1 en 4:5, story/reels, Facebook- en LinkedIn-cover), OG-afbeeldingen van a-alerts.nl en postteksten met alt-teksten (NL). Per datum een map; vanaf 2026-11-10 met de iconen van AMBER Alert en Vermist Kind en posts over het tabblad Nieuws. 2026-11-11: Instagram-banners (post 1:1 en 4:5, story) over live helikopters volgen en het verkeer. 2026-11-15: complete set van vijf onderwerpen (P2000, verkeer, nieuws, helikopters, waarschuwingen), elk als Instagram/Facebook-post 1:1 en 4:5 en als story/reels, met echte schermen van de app. 2026-11-28: twee Instagram Reels (mp4, 1080×1920, 16 s, zonder geluid) over de meldingen en over helikopters en waarschuwingen, elk met een reel-cover, plus captions, hashtags en alt-teksten in `posts.md`.

De bronbestanden staan in de app-repo `LRvdLinden/p2000-apeldoorn` (branch `a-alerts`: `AppStore/`, `social/` en `website/og/`).

## Weekdot
- `Weekdot/AppStore/`: App Store-pakket voor versie 1.0.3, in drie losse zips vanwege de limiet van 100 MB per bestand op GitHub: `-NL`, `-EN-US` en `-EN-GB`. Elke zip bevat de screenshots van die taal voor iPhone, iPad, Mac en Apple Watch, plus de teksten met Wat is nieuw. NL en EN-US bevatten ook de promobeelden, het icoon en de review-notities. EN-GB is optioneel, met dezelfde tekst en schermen als EN-US.
- `Weekdot/Socials/`: banners (Instagram/Facebook post 1:1 en 4:5, story/reels, Facebook- en LinkedIn-cover, Homey-forumbanner) met postteksten en alt-teksten (NL), plus de OG-afbeeldingen van weekdot.com (NL en EN).
- `Weekdot/Homey/`: Store-assets van de Homey-app `nl.lrvdlinden.weekdot` 1.0.2: icon.svg, app-afbeeldingen small/large/xlarge, previews van de 7 widgets (licht en donker), de forumbanner en het forumtopic met de changelog.

- `Weekdot/AppStore/Weekdot-AppStore-iPhoneDuo-2026-11-20.zip`: 8 iPhone Duo-screenshots (binnenscherm 2007×2853, staand) in NL en EN, gemaakt met `appstore/tools/duo.js` op basis van de iPad-opnames (zelfde regular-indeling), voor versie 1.0.5.

De bronbestanden staan in de app-repo `LRvdLinden/weekdot` (`appstore/`, `social/`, `website/og/` en `nl.lrvdlinden.weekdot/`).

## Simple Chess
- `Simple Chess/AppStore/`: App Store-pakket voor versie 3.0.1 (build 6), in vier losse zips per taal (`-NL`, `-EN-US`, `-DE`, `-FR`) vanwege de limiet van 100 MB per bestand op GitHub. Elke zip bevat de screenshots van die taal voor iPhone 6.3", iPhone 6.9", iPad 13" en iPad 12.9", de promobanners (5244×2950, 3840×1646, 3840×2560, 1920×1280), de teksten (naam, ondertitel, promotietekst, beschrijving, trefwoorden, Wat is nieuw), de CHANGELOG en het app-icoon.
- `Simple Chess/Socials/`: banners voor Instagram/Facebook (post 1:1 en 4:5) en story/reels in NL en EN, met postteksten en alt-teksten.

De bronbestanden staan in de app-repo `LRvdLinden/kidschess` (`AppStore/`, `social/` en `tools/`).

## VlagDagen
- `VlagDagen/AppStore/`: App Store-pakket voor versie 2.0.1. Bevat screenshots voor iPhone 6,3" (1206 × 2622) en iPad 13" (2064 × 2752), promobanners (5244 × 2950, 3840 × 1646, 3840 × 2560 en 1920 × 1280), het app-icoon, de App Store-teksten (NL) en de changelog.
- `VlagDagen/Socials/`: banners (Instagram/Facebook-post 1:1 en 4:5, story/reels, Facebook- en LinkedIn-cover) en de OG-afbeelding voor vlagdagen.nl, met postteksten en alt-teksten (NL).

De bronbestanden staan in de app-repo `LRvdLinden/nl.lrvdlinden.vlagdagen` (`AppStore/` en `social/`).

## DevTools
- `DevTools/AppStore/`: App Store-pakket voor versie 1.0.2 (build 23), Engels (en-US). Bevat de screenshots voor iPhone 6.9" en 6.3", iPad 13", Mac (2880×1800 en 1280×800) en Apple Watch (Ultra en Series), de productpagina-beelden (header, zoekresultaten, universal), de promobeelden, de teksten in `metadata/` (naam, ondertitel, promotietekst, beschrijving, trefwoorden, Wat is nieuw, URL's), de review-notities, de README met alle App Store Connect-velden en de CHANGELOG.
- `DevTools/Socials/`: banners in NL en EN voor Instagram/Facebook (post 1:1 en 4:5) en story/reels, in drie onderwerpen (overzicht, statistieken, reviews), plus de Homey-forumbanner. Per taal een `posts.md` met postteksten en alt-teksten.
- `DevTools/Homey/`: Store-assets van de Homey-app `nl.lrvdlinden.appstoreconnect` (App Store Connect) 1.1.1: icon.svg, app-afbeeldingen small/large/xlarge, de iconen en afbeeldingen van beide drivers (App Store-app en Alle apps), previews van de 3 widgets (licht en donker), de forumbanner en het forumtopic met de changelog.

De bronbestanden staan in de app-repo `LRvdLinden/DevTools` (`AppStore/` en `nl.lrvdlinden.appstoreconnect/`).

## Tunr
- `Tunr/AppStore/`: App Store-pakket voor versie 1.0.0 (build 51): Engelse screenshots uit de echte app voor iPhone 6,9" en 6,3", iPad 13", Mac en Apple TV, de Apple TV-merkbeelden (Top Shelf, app-iconen), promobeelden (header en zoekresultaten), het app-icoon en de App Store-teksten in NL en EN. Nog zonder Apple Watch-screenshots.
- `Tunr/Socials/`: banners in NL en EN (Instagram/Facebook-post 1:1 en 4:5, story/reels, Facebook- en LinkedIn-cover) met postteksten en alt-teksten, plus de OG-afbeelding van tunr.online.

De bronbestanden staan in `LRvdLinden/int-radio-app` (`social/` en `tools/make_social.py`) en `LRvdLinden/tunr-beheer` (`appstore/tunr/en`).

## HealthSync
- `HealthSync/AppStore/`: App Store-pakket van de iPhone-app HealthSync, in twee losse zips per taal (`-NL` en `-EN`). Elke zip bevat de screenshots van die taal voor alle iPhone-formaten (6.9", 6.5", 6.3", 6.1" en 5.5"), de productpagina-headers (met iPhones en als artwork, 5244×2950 en 3840×1646), de App Store-teksten (inclusief Wat is nieuw voor 1.0.1), het privacybeleid, de App Store Connect-instellingen met review-notities en het app-icoon.
- `HealthSync/Socials/`: banners voor HealthSync en Apple Health voor Homey samen (Instagram/Facebook post 1:1 en 4:5, story/reels, Facebook- en LinkedIn-cover, Homey-forumbanner) in NL en EN, met postteksten en alt-teksten.
- `HealthSync/Homey/`: Store-assets van de Homey-app `nl.lrvdlinden.applehealth` 1.0.3: app-icoon en afbeeldingen small/large/xlarge, het driver-icoon en de driverafbeeldingen, previews van de 14 widgets (licht en donker), de capability-iconen, de forumbanners (NL en EN) en het forumtopic met de changelog.

De bronbestanden staan in de app-repo's `LRvdLinden/Apple-HealthSync-ios` (`appstore/`) en `LRvdLinden/Apple-HealthSync-Homey` (`assets/`, `drivers/`, `widgets/`).

## Liftr
- `Liftr/AppStore/`: App Store-pakket voor versie 1.0.0, in NL en EN. Bevat screenshots voor iPhone 6,3" en 6,1", iPad 13" en Apple Watch (6 maten), promobeelden (header 5244×2950 en 3840×1646, zoekresultaten 5244×2950, 3840×2560 en 1920×1280), de teksten in `metadata/` (naam, ondertitel, promotietekst, beschrijving, trefwoorden, Wat is nieuw, URL's), de review-notities, de privacyverklaring en `app-info.md` met categorie, leeftijd, privacylabel, toegankelijkheid en de medische-hulpmiddelverklaring.
- `Liftr/AppStore/Liftr-AppStore-iPhoneDuo-2026-11-22.zip`: aanvulling met iPhone Duo-screenshots in NL en EN: buitenscherm 1398×2034 (7 per taal) en binnenscherm 2007×2853 (5 per taal).
- `Liftr/Socials/`: banners in NL en EN voor Instagram/Facebook (post 1:1 en 4:5), story/reels en de Facebook- en LinkedIn-cover, met per taal een `posts.md` met postteksten en alt-teksten. De link op de banners is liftr.nu.

De bronbestanden staan in de app-repo `LRvdLinden/nl.lrvdlinden.liftr` (`AppStore/`, `social/`, `tools/appstore/` en `tools/social/`).
## Bingr
- `Bingr/AppStore/`: App Store-pakket voor versie 1.0.5, in twee losse zips per taal (`-NL` en `-EN-US`) vanwege de limiet van 100 MB per bestand op GitHub. Elke zip bevat de screenshots van die taal voor iPhone 6,3" en 6,1", iPad 13", Apple TV en Mac, de promobeelden, de teksten (met de definitieve Wat is nieuw van 1.0.5), app-info, privacy en de review-notities (zonder wachtwoord van het demo-account).
- `Bingr/Socials/`: banners voor algemene promotie (Instagram/Facebook post 1:1 en 4:5, story/reels, Facebook- en LinkedIn-cover) in NL en EN, met postteksten en alt-teksten.

De bronbestanden staan in de app-repo `LRvdLinden/iptv-ios-appletv` (`AppStore/` en `social/`).

## PixelForges
- `PixelForges/OG/`: OG-afbeelding van pixelforges.nl (NL, 1200×630), gebruikt op de homepage en de privacypagina, met een README per afbeelding (pagina, taal, formaat, alt-tekst).
- `PixelForges/Socials/`: banners in de PixelForges-huisstijl (NL): Instagram/Facebook-post 1:1, portfolio- en prijzen-post 4:5, story/reels, Facebook-omslag, LinkedIn-bedrijfsbanner en persoonlijke achtergrond, X-header, profielfoto's, webbanners (728×90, 970×250, 300×250, 160×600), presentatiedia 1920×1080, e-mailhandtekening en logo's, met `posts.md` met postteksten en alt-teksten. De kleinere formaten ook in `2x/`.

De bronbestanden staan in de site-repo `LRvdLinden/pixelforges` (`brand/templates/`, `brand/render.py` en `site/og.png`).

## lrvdlinden.app
- `lrvdlinden.app/OG:image/`: de OG-afbeeldingen van lrvdlinden.app per datum: NL (live op de site), EN en de vierkante versie (1080×1080).
- `lrvdlinden.app/Socials/`: banners voor algemene promotie in NL en EN (Instagram/Facebook post 1:1 en 4:5, story/reels, LinkedIn-post, X/Bluesky/Threads, Facebook- en LinkedIn-cover), met per taal een `posts.md` met postteksten en alt-teksten.

De bronbestanden staan in de site-repo `LRvdLinden/app.lrvdlinden` (`social/`, `tools/social/` en `site/og-image*.jpg`).

## Bekendr
- `Bekendr/AppStore/`: App Store-pakket voor versie 1.0.0 (build 1). Bevat screenshots (alleen NL, de app is alleen Nederlandstalig) voor iPhone 6,3" (1206×2622) en 6,1" (1179×2556), iPad 13" (2064×2752) en 12,9" (2048×2732) en Mac (2880×1800, 2560×1600, 1440×900, 1280×800), de productpagina-beelden (header 5244×2950 en 3840×1646, zoekresultaten 5244×2950, 3840×2560 en 1920×1280), de teksten in NL en EN in `metadata/` (naam, ondertitel, promotietekst, beschrijving, trefwoorden, Wat is nieuw, URL's), de privacyverklaring, de review-notities en `app-info.md` met categorie, leeftijd, privacylabel en toegankelijkheid. De zip met `-2` is bijgewerkt met Vandaag, routes, feedback en het nieuwe privacylabel (feedback, apparaatnummer als hash en grove locatie voor het weer).
- `Bekendr/Socials/`: banners (NL, algemene promotie van app en website) voor Instagram/Facebook (post 1:1 en 4:5), story/reels, LinkedIn-post, X/Bluesky/Threads, Facebook-cover en LinkedIn-cover, met `posts.md` met postteksten en alt-teksten. De zip met `-2` is de bijgewerkte set met "Download in de App Store en Google Play". `Bekendr-Socials-2026-11-12.zip`: twee Instagram-posts (1080×1080 en 1080×1350, NL, algemene promotie, link naar de website) met posttekst en alt-teksten.
- `Bekendr/OG/`: OG-afbeelding van bekendr.lrvdlinden.app (NL, 1200×630) voor de homepage, privacy en support.

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.bekendr` (`AppStore/`, `social/` en `website/og/`).

## René Smaal Karate
- `René Smaal Karate/Socials/`: banners voor algemene promotie van renesmaal.nl (Stichting RSK Apeldoorn) in het Nederlands: Instagram/Facebook-post 1:1 en 4:5, story/reels, LinkedIn-post en de Facebook- en LinkedIn-cover, in de huisstijl van de site (navy, Barlow/Barlow Condensed, clublogo). Met `posts.md` met postteksten en alt-teksten. De links op de banners zijn renesmaal.nl en renesmaal.nl/proefles.

Er is geen repo voor deze website; de bronbestanden (`bron/build.py` en het logo) zitten in de zip zelf.

## Bert van de Wiel
- `Bert van de Wiel/OG/`: og:image (1200 × 630, NL) voor de persoonlijke startpagina bertvandewiel.nl: home.

Er is geen repo voor deze website; het sjabloon (`bron/og.html`) en het renderscript zitten in de zip zelf.

## Noodpakket
- `Noodpakket/AppStore/`: App Store-pakket voor versie 1.0.0. Bevat screenshots voor iPhone 6,3" (1206 × 2622), iPhone 6,1" (1179 × 2556) en iPad 13" (2064 × 2752), promobanners (5244 × 2950, 3840 × 1646, 3840 × 2560 en 1920 × 1280), de App Store-teksten, privacyteksten, app-info en App Review-notities, in het Nederlands en Engels.
- `Noodpakket/OG/`: og:images (1200 × 630, NL) voor noodpakket.lrvdlinden.app: home, support en privacy.
- `Noodpakket/Socials/`: banners voor algemene promotie van app en website (Instagram/Facebook-post 1:1 en 4:5, story/reels, LinkedIn-post, X/Bluesky/Threads, Facebook- en LinkedIn-cover, Homey-forumbanner en OG), met postteksten en alt-teksten (NL).

Sinds `2026-11-11-2` gebruikt Noodpakket de nieuwe huisstijl (paars en geel, met een 72-uursring als icoon en een afbeelding bij elk onderdeel van het pakket). De sets van `2026-11-11` zijn nog in de oude groene stijl en blijven als historie bewaard.

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.noodkoffer` (`AppStore/`, `social/`, `web/og/` en `design/appstore-src/`).

## Pairr
- `Pairr/Socials/`: banners voor algemene promotie van app en website in NL en EN (aparte sets): Instagram/Facebook-post 1:1 en 4:5, story/reels en de Facebook- en LinkedIn-cover, met per taal `posts.md` met posttekst en alt-teksten. CTA: "Binnenkort in de App Store" en pairr.lrvdlinden.app.
- `Pairr/AppStore/`: App Store-pakket voor versie 1.0.0 (build 7). Screenshots in NL en EN (de app is meertalig) voor iPhone 6,3" (1206×2622) en 6,1" (1179×2556), iPad 13" (2064×2752) en 12,9" (2048×2732), Mac (2880×1800, 2560×1600, 1440×900, 1280×800) en Apple Watch (416×496 en 422×514), de productpagina-beelden (header 5244×2950 en 3840×1646, zoekresultaten 5244×2950, 3840×2560 en 1920×1280), de teksten in NL en EN in `metadata/`, de privacyverklaring, de review-notities en `app-info.md` met categorie, leeftijd, privacylabel en toegankelijkheid. De schermen zijn nagemaakt in HTML op basis van de SwiftUI-code.
- `Pairr/OG/`: og:image van pairr.lrvdlinden.app (1200 × 630, Engelse tekst), gebruikt op alle pagina's in NL en EN (home, privacy, support). De set `2026-11-12-2` noemt de prijs (eenmalige aankoop van € 0,99) in plaats van gratis.

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.pairr` (`AppStore/`, `tools/appstore/`, `tools/web/`, `web/og/`, `tools/social/` en `social/`).

## Kentr
- `Kentr/AppStore/`: App Store-pakket voor versie 1.0.0 (build 1). Bevat screenshots (alleen NL, de app is alleen Nederlandstalig) voor iPhone 6,3" (1206×2622) en 6,1" (1179×2556) en iPad 13" (2064×2752) en 12,9" (2048×2732), 7 per toestel, de productpagina-beelden (header 5244×2950 en 3840×1646, zoekresultaten 5244×2950, 3840×2560 en 1920×1280), de teksten in NL en EN in `metadata/` (naam, ondertitel, promotietekst, beschrijving, trefwoorden, Wat is nieuw, URL's), de privacyverklaring, de review-notities en `app-info.md` met categorie, leeftijd, privacylabel ("Data Not Collected") en toegankelijkheid. De schermen zijn nagemaakt in HTML op basis van de SwiftUI-code, met fictieve kentekens; de bronbestanden (`bron/`) zitten in de zip.
- `Kentr/Socials/`: banners voor de lancering van de app (NL, de app is alleen Nederlandstalig): Instagram/Facebook-post 1:1 en 4:5, story/reels, LinkedIn-post, X/Bluesky/Threads, Facebook-cover en LinkedIn-cover, met `posts.md` met postteksten en alt-teksten. CTA: "Binnenkort in de App Store" en kent.lrvdlinden.app. De schermen zijn nagebouwd in HTML op basis van de SwiftUI-code; alle kentekens zijn fictief.

De bronbestanden van de socials (`bron/build.py`, de HTML per banner en het icoon) zitten in de zip zelf; de app staat in `LRvdLinden/app.lrvdlinden.Kentr`.

## 112Heli
- `112Heli/OG/`: og:images van 112heli.lrvdlinden.app (1200 × 630, alleen NL): home (ook voor privacy, support en 404), live kaart en toestellen (ook voor een los toestel), met een `README.md` met alt-teksten. De set `2026-11-14-2` gebruikt de EC135 als standaard-Zulu in plaats van de AW139. De set `2026-11-15` heeft de nieuwe huisstijl: blauwe achtergrond met witte radar, rode markering en het nieuwe app-icoon.

- `112Heli/AppStore/`: App Store-pakket voor versie 1.0.0 (build 7). Screenshots alleen in NL (de app is alleen Nederlandstalig) voor iPhone 6,3" (1206×2622) en 6,1" (1179×2556), iPad 13" (2064×2752) en 12,9" (2048×2732), Mac (2880×1800, 2560×1600, 1440×900, 1280×800) en Apple TV (3840×2160 en 1920×1080), de productpagina-beelden (header 5244×2950 en 3840×1646, zoekresultaten 5244×2950, 3840×2560 en 1920×1280), de teksten in NL en EN in `metadata/`, de privacyverklaring (ook voor Apple TV), de review-notities en `app-info.md` met categorie, leeftijd, privacylabel en toegankelijkheid. De schermen zijn nagebouwd in HTML op basis van de SwiftUI-code; bronnen in `tools/appstore/` van de app-repo. Vanaf `2026-11-15` in de nieuwe huisstijl (blauw met het nieuwe app-icoon); de Apple TV-screenshots zijn ongewijzigd. De set `2026-11-28` (build 14) heeft 8 Mac- en 8 Apple TV-screenshots (toestellen, toesteldetail, historie, vlucht terugkijken, instellingen, Max; op Apple TV ook route, weer, info) en nieuwe store-teksten in NL en EN; iPhone, iPad en productpagina-beelden zijn gelijk aan `2026-11-15`.
- `112Heli/Socials/`: banners voor algemene promotie van app en website (alleen NL): Instagram/Facebook-post 1:1 en 4:5, story/reels en LinkedIn-post, met `posts.md` met postteksten en alt-teksten. CTA: "Binnenkort in de App Store" en 112heli.lrvdlinden.app. De set `2026-11-15` is in de nieuwe blauwe huisstijl en heeft ook een Facebook-omslag (1640×624) en LinkedIn-omslag (1584×396). De set `2026-11-28` is een Instagram-reel (1080×1920, 18,6 s, zonder geluid) met cover en `posts.md` met posttekst en alt-teksten (alleen NL); bron in `social/reel/` van de app-repo.

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.112heli` (`website/og/`, `social/src/` en `social/`).

## MV3
- `MV3/OG/`: og:image van mv3jet.nl (de set `2026-11-15` nog met het oude adres mv3.lrvdlinden.app) (1200 × 630, alleen NL) voor de homepage, met een `README.md` met de alt-tekst. Website door PixelForges.
- `MV3/Socials/`: banners voor algemene promotie van de website (alleen NL): Instagram/Facebook-post 1:1 en 4:5 en story/reels, met `posts.md` met postteksten en alt-teksten. CTA: mv3jet.nl (vanaf de set `2026-11-15-2`; de eerste set noemt nog mv3.lrvdlinden.app).

De bronbestanden staan in de repo `LRvdLinden/app.lrvdlinden.112heli`, map `mv3/` (`mv3/tools/` voor de og-afbeelding, `mv3/social/` voor de banners).
