# App-content

Marketingmateriaal per app: App Store-pakketten en social-media-content, als zip per datum.

Indeling: `<App>/<Soort>/<JJJJ-MM-DD>/`. In elke datummap staat de zip en ernaast een map met dezelfde naam (zonder `.zip`) met de uitgepakte inhoud, zodat je de bestanden direct op GitHub kunt bekijken.

## Pasr
- `Pasr/AppStore/`: App Store-pakket (screenshots per toestel, promobeelden, teksten NL en EN, review-notities, privacy).
- `Pasr/Socials/`: banners en postteksten voor Instagram/Facebook (post en story), met alt-teksten.

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.pasr` (`appstore/` en `social/`).

## A-Alerts
- `A-Alerts/AppStore/`: App Store-pakketten. 2.0.0 (2026-11-08) in één zip. 2.0.1 (build 68, 2026-11-09, met het tabblad Nieuws, AMBER Alert en Vermist Kind Alert) in twee zips vanwege de limiet van 100 MB per bestand: `-iPhone` (iPhone 6,3" en 6,1", marketingbeelden, teksten NL en EN, review-notities, privacy) en `-iPad-Mac-Watch-TV` (screenshots voor iPad, Mac, Apple Watch en Apple TV). Screenshots alleen NL.
- `A-Alerts/Socials/`: banners (Instagram/Facebook post 1:1 en 4:5, story/reels, Facebook- en LinkedIn-cover), OG-afbeeldingen van a-alerts.nl en postteksten met alt-teksten (NL). Per datum een map; vanaf 2026-11-10 met de iconen van AMBER Alert en Vermist Kind en posts over het tabblad Nieuws. 2026-11-11: Instagram-banners (post 1:1 en 4:5, story) over live helikopters volgen en het verkeer.

De bronbestanden staan in de app-repo `LRvdLinden/p2000-apeldoorn` (branch `a-alerts`: `AppStore/`, `social/` en `website/og/`).

## Weekdot
- `Weekdot/AppStore/`: App Store-pakket voor versie 1.0.3, in drie losse zips vanwege de limiet van 100 MB per bestand op GitHub: `-NL`, `-EN-US` en `-EN-GB`. Elke zip bevat de screenshots van die taal voor iPhone, iPad, Mac en Apple Watch, plus de teksten met Wat is nieuw. NL en EN-US bevatten ook de promobeelden, het icoon en de review-notities. EN-GB is optioneel, met dezelfde tekst en schermen als EN-US.
- `Weekdot/Socials/`: banners (Instagram/Facebook post 1:1 en 4:5, story/reels, Facebook- en LinkedIn-cover, Homey-forumbanner) met postteksten en alt-teksten (NL), plus de OG-afbeeldingen van weekdot.com (NL en EN).
- `Weekdot/Homey/`: Store-assets van de Homey-app `nl.lrvdlinden.weekdot` 1.0.2: icon.svg, app-afbeeldingen small/large/xlarge, previews van de 7 widgets (licht en donker), de forumbanner en het forumtopic met de changelog.

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

## Noodpakket
- `Noodpakket/AppStore/`: App Store-pakket voor versie 1.0.0. Bevat screenshots voor iPhone 6,3" (1206 × 2622), iPhone 6,1" (1179 × 2556) en iPad 13" (2064 × 2752), promobanners (5244 × 2950, 3840 × 1646, 3840 × 2560 en 1920 × 1280), de App Store-teksten, privacyteksten, app-info en App Review-notities, in het Nederlands en Engels.
- `Noodpakket/OG/`: og:images (1200 × 630, NL) voor noodpakket.lrvdlinden.app: home, support en privacy.
- `Noodpakket/Socials/`: banners voor algemene promotie van app en website (Instagram/Facebook-post 1:1 en 4:5, story/reels, LinkedIn-post, X/Bluesky/Threads, Facebook- en LinkedIn-cover, Homey-forumbanner en OG), met postteksten en alt-teksten (NL).

Sinds `2026-11-11-2` gebruikt Noodpakket de nieuwe huisstijl (paars en geel, met een 72-uursring als icoon en een afbeelding bij elk onderdeel van het pakket). De sets van `2026-11-11` zijn nog in de oude groene stijl en blijven als historie bewaard.

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.noodkoffer` (`AppStore/`, `social/`, `web/og/` en `design/appstore-src/`).

## Pairr
- `Pairr/Socials/`: banners voor algemene promotie van app en website in NL en EN (aparte sets): Instagram/Facebook-post 1:1 en 4:5, story/reels en de Facebook- en LinkedIn-cover, met per taal `posts.md` met posttekst en alt-teksten. CTA: "Binnenkort in de App Store" en pairr.lrvdlinden.app.
- `Pairr/AppStore/`: App Store-pakket voor versie 1.0.0 (build 7). Screenshots in NL en EN (de app is meertalig) voor iPhone 6,3" (1206×2622) en 6,1" (1179×2556), iPad 13" (2064×2752) en 12,9" (2048×2732), Mac (2880×1800, 2560×1600, 1440×900, 1280×800) en Apple Watch (416×496 en 422×514), de productpagina-beelden (header 5244×2950 en 3840×1646, zoekresultaten 5244×2950, 3840×2560 en 1920×1280), de teksten in NL en EN in `metadata/`, de privacyverklaring, de review-notities en `app-info.md` met categorie, leeftijd, privacylabel en toegankelijkheid. De schermen zijn nagemaakt in HTML op basis van de SwiftUI-code.
- `Pairr/OG/`: og:image van pairr.lrvdlinden.app (1200 × 630, Engelse tekst), gebruikt op alle pagina's in NL en EN (home, privacy, support).

De bronbestanden staan in de app-repo `LRvdLinden/app.lrvdlinden.pairr` (`AppStore/`, `tools/appstore/`, `tools/web/`, `web/og/`, `tools/social/` en `social/`).
