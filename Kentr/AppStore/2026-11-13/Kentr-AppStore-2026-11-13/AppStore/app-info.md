# Kentr – App-informatie voor App Store Connect

Versie 1.0.0 (build 1) · bundle-id `app.lrvdlinden.kentr` · team EU3UY476T6 · iPhone en iPad · iOS/iPadOS 17+ · alleen Nederlands

## Algemene informatie (General Information)
| Veld | Waarde |
| --- | --- |
| Bundle ID | `app.lrvdlinden.kentr` (geen extensies) |
| SKU | `app.lrvdlinden.kentr` |
| Apple ID | TODO: Léon vult in na het aanmaken van de app in App Store Connect |
| Primary Language | Dutch |
| App-talen | Nederlands (alleen; `knownRegions` = nl, Base) |
| Primary Category | Utilities – praktisch hulpmiddel: kenteken opzoeken en je eigen autohistorie bijhouden |
| Secondary Category | Reference – naslag van openbare voertuiggegevens (RDW) |
| Content Rights | Ja, de app toont inhoud van derden: RDW Open Data (opendata.rdw.nl, datasets Gekentekende voertuigen en Brandstof; openbare open data, vrij te hergebruiken) en vrij gelicenseerde voorbeeldfoto's van Wikimedia Commons, getoond met maker en licentie. Bron staat in de app. |
| License Agreement | Apple Standard EULA |
| Prijs | Gratis, geen in-app-aankopen, geen abonnementen, geen advertenties |
| Copyright | © 2026 Léon van der Linden |
| Support URL | https://kent.lrvdlinden.app/support/ |
| Marketing URL | https://kent.lrvdlinden.app |
| Privacy Policy URL | https://kent.lrvdlinden.app/privacy/ |
| Export compliance | `ITSAppUsesNonExemptEncryption` = false (alleen HTTPS van het systeem) |

## Leeftijdsclassificatie (Age Rating)
Alle vragen **None / No**: geen geweld, seks, grof taalgebruik, drugs, gokken, horror of medische informatie; geen onbeperkte webtoegang (alleen links naar de eigen website, RDW Open Data en lrvdlinden.app, die in Safari openen); geen door gebruikers gedeelde inhoud; geen chat. Uitkomst: **4+**.

## App Privacy (privacylabel)
**Data Not Collected.**
- Geen account, geen analytics, geen crash-SDK, geen advertenties, geen tracking (geen ATT). SDK's van derden: geen.
- De auto's van de gebruiker staan alleen op het toestel en in de eigen privé-iCloud-database (CloudKit `iCloud.app.lrvdlinden.kentr`); de ontwikkelaar kan er niet bij.
- Kenteken of zoekcriteria gaan rechtstreeks naar opendata.rdw.nl; merk, model en bouwjaar rechtstreeks naar wikipedia.org (voorbeeldfoto, uit te zetten). De ontwikkelaar ontvangt of bewaart niets.
- Face ID via LocalAuthentication: de app krijgt alleen "gelukt/niet gelukt".
- `PrivacyInfo.xcprivacy`: `NSPrivacyTracking` = false, geen verzamelde gegevenstypen, alleen UserDefaults (CA92.1).

## Toegankelijkheid (Accessibility Nutrition Labels)
Per apparaat (iPhone, iPad), alleen wat in de code is gecontroleerd:
| Kenmerk | Status |
| --- | --- |
| Dark Interface | Geclaimd: alle eigen kleuren hebben een lichte en donkere variant; keuze Automatisch/Licht/Donker in Instellingen |
| Larger Text | Geclaimd: systeemtekststijlen (Dynamic Type) en `@ScaledMetric` voor iconen |
| Differentiate Without Color Alone | Geclaimd: status en waarschuwingen hebben altijd tekst en een icoon (bv. "Er staat een terugroepactie open") |
| VoiceOver | Niet geclaimd tot Léon het op een toestel heeft getest (kentekenplaten, rijen en tegels hebben wel toegankelijkheidslabels) |
| Voice Control | Niet geclaimd (niet getest) |
| Sufficient Contrast | Niet geclaimd (niet gemeten) |
| Reduced Motion | Niet geclaimd: het splashscreen houdt geen rekening met "Verminder beweging" |
| Captions / Audio Descriptions | Niet van toepassing (geen video of audio) |

## App Review Information
- Notes: `metadata/review_information/notes.txt` (Engels, voor App Store Connect, 3.850 tekens); Nederlandse kopie in `notes-nl.txt`.
- Sign-in required: **No** (geen account).
- Contact: Léon van der Linden; telefoon en e-mail: TODO (zelf invullen in App Store Connect).
- Bijlage: niet nodig.
