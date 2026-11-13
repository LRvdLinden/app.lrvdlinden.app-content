# -*- coding: utf-8 -*-
import pathlib, sys
A = pathlib.Path(sys.argv[1])
M = A / "metadata"
def w(rel, text):
    p = M / rel; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.strip() + "\n", encoding="utf-8")

w("copyright.txt", "© 2026 Léon van der Linden")
w("primary_category.txt", "UTILITIES")
w("secondary_category.txt", "REFERENCE")

URLS = dict(support_url="https://kent.lrvdlinden.app/support/", marketing_url="https://kent.lrvdlinden.app",
            privacy_url="https://kent.lrvdlinden.app/privacy/")
for loc in ("nl-NL", "en-US"):
    for k, v in URLS.items(): w(f"{loc}/{k}.txt", v)

# ---------------- NL ----------------
w("nl-NL/name.txt", "Kentr: autohistorie & kenteken")
w("nl-NL/subtitle.txt", "RDW-data, BPM en bijtelling")
w("nl-NL/promotional_text.txt",
  "Alle auto's die je ooit had op één plek. Zoek elk Nederlands kenteken op en zie catalogusprijs, bruto BPM, APK en een indicatie van de bijtelling.")
w("nl-NL/keywords.txt",
  "auto,kentekencheck,apk,catalogusprijs,fiscale waarde,auto van de zaak,youngtimer,occasion,voertuig")
w("nl-NL/description.txt", """
Kentr houdt elke auto bij die je ooit hebt gehad: van je eerste auto tot je huidige. Met kenteken, of alleen merk en type als je het kenteken niet meer weet. Zoek elk Nederlands kenteken op met de openbare gegevens van de RDW en zie in één oogopslag de techniek, de APK en de fiscale waarde.

MIJN AUTO'S
• Voeg auto's toe met kenteken of alleen merk, model en bouwjaar
• Periode van bezit, ook als je alleen de jaartallen nog weet
• Hoe je de auto kreeg, aankoop- en verkoopprijs, kilometerstanden en notities
• Eigen foto, of automatisch een voorbeeldfoto van hetzelfde model (Wikimedia Commons, met bronvermelding)
• Zoek in je lijst op merk, model, kenteken, kleur of jaar

KENTEKEN OPZOEKEN
• Merk, model, carrosserie, kleur, brandstof, vermogen, gewicht en verbruik
• APK-vervaldatum, kilometerstandoordeel, WAM-verzekering en open terugroepacties
• Zie direct of een auto is geïmporteerd: eerste toelating en eerste toelating in Nederland
• Voeg een opgezochte auto met één tik toe aan je eigen lijst

FISCALE WAARDE EN BIJTELLING
• Catalogusprijs (de fiscale waarde), bruto BPM en CO2-uitstoot
• Indicatie van de bijtelling per maand en per jaar: 22%, het verlaagde tarief voor elektrische auto's met de grens per startjaar, de regel van 60 maanden en youngtimers (35% van de dagwaarde)
• Een indicatie, geen fiscaal advies

KENTEKEN TERUGVINDEN
• Kenteken van je oude auto vergeten? Zoek in de RDW-gegevens op merk, model, kleur en bouwjaar
• Herken je oude kenteken in de lijst en koppel het met één tik aan je auto
• De RDW publiceert geen eigenaren: Kentr laat auto's zien die bij je omschrijving passen

OVERZICHT
• Hoeveel auto's en merken je had, totale en gemiddelde bezitsduur
• Je langst gehouden en je eerste auto, zelf gereden kilometers
• Verdeling per merk, brandstof en decennium

VEILIG EN PRIVÉ
• Vergrendel de app met Face ID
• Synchroniseert via je eigen iCloud met je iPhone en iPad
• Geen account, geen advertenties, geen tracking en geen eigen server

Kentr gebruikt open data van de RDW (opendata.rdw.nl) en is geen app van de RDW of de Belastingdienst.

Meer apps van de ontwikkelaar vind je op lrvdlinden.app.
""")
w("nl-NL/release_notes.txt", """
De eerste versie van Kentr:
• Al je auto's op één plek, met of zonder kenteken
• Kenteken opzoeken bij de RDW: techniek, APK, catalogusprijs en bruto BPM
• Indicatie van de bijtelling
• Vergeten kenteken terugvinden op merk, model, kleur en bouwjaar
• Automatische voorbeeldfoto per model
• Face ID-vergrendeling en synchronisatie via iCloud
""")

# ---------------- EN ----------------
w("en-US/name.txt", "Kentr: Dutch car history")
w("en-US/subtitle.txt", "RDW data, BPM and company car")
w("en-US/promotional_text.txt",
  "Every car you ever owned in one place. Look up any Dutch licence plate and see the list price, gross BPM, APK and an estimate of the company car tax benefit.")
w("en-US/keywords.txt",
  "netherlands,license,licence,plate,registration,vehicle,lookup,apk,mot,tax,bijtelling,kenteken,garage")
w("en-US/description.txt", """
Kentr keeps track of every car you have ever owned, from your first car to the one you drive today. With a licence plate, or just the make and model if you no longer remember the plate. Look up any Dutch licence plate using the public open data of the RDW (the Dutch vehicle authority) and see the specs, the APK (MOT) and the tax value at a glance.

The app is available in Dutch and is made for cars registered in the Netherlands.

MY CARS
• Add cars with a licence plate or with just make, model and year
• Period of ownership, even if you only remember the years
• How you got the car, purchase and sale price, mileage and notes
• Your own photo, or an automatic example photo of the same model (Wikimedia Commons, with attribution)
• Search your list by make, model, plate, colour or year

LICENCE PLATE LOOKUP
• Make, model, body type, colour, fuel, power, weight and consumption
• APK expiry date, odometer verdict, insurance status and open recalls
• See right away whether a car was imported: first registration and first registration in the Netherlands
• Add a car you looked up to your own list with one tap

TAX VALUE AND COMPANY CAR BENEFIT
• List price (the tax value), gross BPM and CO2 emissions
• Estimate of the Dutch company car tax benefit (bijtelling) per month and per year: 22%, the reduced rate for electric cars with its cap per starting year, the 60-month rule and youngtimers (35% of the current value)
• An estimate, not tax advice

FIND A FORGOTTEN PLATE
• Forgot the plate of your old car? Search the RDW data by make, model, colour and year
• Recognise your old plate in the list and link it to your car with one tap
• The RDW does not publish owners: Kentr shows cars that match your description

OVERVIEW
• How many cars and makes you have had, total and average ownership
• Your longest-kept and your first car, kilometres you drove
• Breakdown by make, fuel and decade

SAFE AND PRIVATE
• Lock the app with Face ID
• Syncs with your iPhone and iPad through your own iCloud
• No account, no ads, no tracking and no server of our own

Kentr uses open data from the RDW (opendata.rdw.nl) and is not an app of the RDW or the Dutch Tax Administration.

More apps from the developer: lrvdlinden.app
""")
w("en-US/release_notes.txt", """
The first version of Kentr:
• All your cars in one place, with or without a licence plate
• Licence plate lookup with RDW data: specs, APK, list price and gross BPM
• Company car tax benefit estimate
• Find a forgotten plate by make, model, colour and year
• Automatic example photo per model
• Face ID lock and iCloud sync
""")

# ---------------- App Review ----------------
R = "review_information"
w(f"{R}/first_name.txt", "Léon")
w(f"{R}/last_name.txt", "van der Linden")
w(f"{R}/phone_number.txt", "TODO: Léon vult telefoonnummer in App Store Connect in")
w(f"{R}/email_address.txt", "TODO: Léon vult e-mailadres in App Store Connect in")
w(f"{R}/demo_required.txt", "false")
w(f"{R}/demo_user.txt", "TODO: niet nodig (geen inlog)")
w(f"{R}/demo_password.txt", "TODO: niet nodig (geen inlog)")
w(f"{R}/notes.txt", """
WHAT THE APP DOES
Kentr lets people in the Netherlands keep a personal list of every car they have owned, with or without a licence plate. For Dutch licence plates it shows public vehicle data from the RDW (the Dutch vehicle authority) open data service: specs, APK (MOT) expiry, list price (tax value), gross BPM and an estimate of the Dutch company car tax benefit. It can also help users find the forgotten plate of an old car. The app is in Dutch.

HOW TO TEST
1. Launch the app: an animated splash screen (about 4 seconds), then a 3-page welcome screen. Tap "Volgende" twice and "Aan de slag" (or "Overslaan").
2. Tab "Terugvinden" (find a plate): enter Merk "VOLKSWAGEN", Model "Golf", choose Van 2015 and Tot en met 2015, and tap "Zoek kentekens". A list of matching Dutch plates appears. Tap one to see the full RDW data, then tap "Dit was mijn auto – toevoegen" and "Bewaar" to add it to your list.
3. Tab "Opzoeken" (look up): type any 6-character Dutch licence plate (for example one from step 2, or a plate seen on a car in the Netherlands) and tap the search button. You will see vehicle data, the "Fiscaal" section (list price, BPM, first registration) and "Bijtelling (indicatie)" (company car benefit estimate). Tap "Toevoegen aan mijn auto's" to add it.
4. Tab "Mijn auto's": tap + to add a car manually. Leave the plate empty and fill in only Merk and Model (e.g. "Volkswagen" / "Golf") and a year: the car is saved with "Kenteken onbekend". Open it and tap "Kenteken terugvinden" to search for its plate.
5. Tab "Overzicht": statistics about the saved cars (count, makes, ownership duration, fuel, decade).
6. Tab "Instellingen": toggle "Vergrendel met Face ID" (app lock), toggle the automatic example photo, appearance, links to privacy policy and support, "Wat is nieuw", the welcome screen again, and the "More apps from the developer" card.

REGION AND DATA NOTES
The vehicle data covers vehicles registered in the Netherlands only. Plates from other countries return "Niet gevonden" (not found); this is expected. Search results in "Terugvinden" are capped at 200; a narrower search gives a shorter list. The bijtelling (company car benefit) is an indicative calculation based on Dutch tax rules up to 2027 and is labelled as "geen fiscaal advies" (not tax advice).

DATA SOURCES
- RDW Open Data (opendata.rdw.nl), datasets "Gekentekende voertuigen" and "Brandstof": public open data, free to reuse, no API key. The RDW does not publish owner data and the app does not show any personal data. The app is not affiliated with, or endorsed by, the RDW or the Dutch Tax Administration; it says "Bron: RDW Open Data" in the app.
- Example photos: Wikipedia / Wikimedia Commons API (freely licensed images), shown with the author and licence, labelled "Voorbeeldfoto, niet jouw auto" (example photo, not your car). Only make, model and year are sent. Can be turned off in Settings.

PERMISSIONS
- Face ID: only requested when the user turns on "Vergrendel met Face ID" in Settings (off by default). Without it the app works normally.
- Photos: the user can pick a photo of their car with the system photo picker (PHPicker), which needs no library permission.
- No location, contacts, camera, tracking or notification permission is requested.

ACCOUNT
No login required. Data is stored on the device and synced through the user's own private iCloud database (CloudKit). The remote-notification background mode is used only for silent CloudKit sync pushes; the app shows no notifications.

IN-APP PURCHASES / ADS
The app is free and contains no in-app purchases, subscriptions or ads.

OTHER
- A review prompt (requestReview) appears at most once a week, at the earliest 4 hours after first use and never during the splash, welcome or lock screen.
- Settings contains a "More apps from the developer" card that opens lrvdlinden.app.
""")
w(f"{R}/notes-nl.txt", """
(Nederlandse kopie voor Léon – niet uploaden; in App Store Connect gaat notes.txt in het Engels)

WAT DE APP DOET
Met Kentr houden mensen in Nederland een eigen lijst bij van alle auto's die ze hebben gehad, met of zonder kenteken. Voor Nederlandse kentekens toont de app openbare voertuiggegevens van RDW Open Data: techniek, APK-vervaldatum, catalogusprijs (fiscale waarde), bruto BPM en een indicatie van de bijtelling. Ook helpt de app om het vergeten kenteken van een oude auto terug te vinden. De app is Nederlandstalig.

ZO TEST JE
1. Start de app: geanimeerd splashscreen (ca. 4 seconden), daarna een welkomstscherm van 3 pagina's. Tik twee keer op "Volgende" en dan op "Aan de slag" (of "Overslaan").
2. Tab "Terugvinden": vul Merk "VOLKSWAGEN" en Model "Golf" in, kies Van 2015 en Tot en met 2015 en tik op "Zoek kentekens". Er verschijnt een lijst met passende kentekens. Tik op een resultaat voor alle RDW-gegevens, tik op "Dit was mijn auto – toevoegen" en "Bewaar".
3. Tab "Opzoeken": typ een willekeurig Nederlands kenteken van 6 tekens (bijvoorbeeld uit stap 2) en tik op de zoekknop. Je ziet de voertuiggegevens, "Fiscaal" (catalogusprijs, BPM, eerste toelating) en "Bijtelling (indicatie)". Met "Toevoegen aan mijn auto's" voeg je hem toe.
4. Tab "Mijn auto's": tik op + om handmatig een auto toe te voegen. Laat het kenteken leeg en vul alleen Merk, Model en een bouwjaar in: de auto wordt bewaard met "Kenteken onbekend". Open hem en tik op "Kenteken terugvinden".
5. Tab "Overzicht": statistieken over de bewaarde auto's (aantal, merken, bezitsduur, brandstof, decennium).
6. Tab "Instellingen": "Vergrendel met Face ID", automatische voorbeeldfoto, weergave, links naar privacyverklaring en support, "Wat is nieuw", welkomstscherm opnieuw tonen en de kaart "Meer apps van de ontwikkelaar".

REGIO EN GEGEVENS
Alleen in Nederland geregistreerde voertuigen. Buitenlandse kentekens geven "Niet gevonden"; dat is de bedoeling. Bij Terugvinden zijn de resultaten beperkt tot 200. De bijtelling is een indicatie volgens de regels t/m 2027, met de vermelding "geen fiscaal advies".

GEGEVENSBRONNEN
- RDW Open Data (opendata.rdw.nl), datasets "Gekentekende voertuigen" en "Brandstof": openbare open data, vrij te hergebruiken, geen API-sleutel. De RDW publiceert geen eigenaren en de app toont geen persoonsgegevens. Geen band met de RDW of de Belastingdienst; in de app staat "Bron: RDW Open Data".
- Voorbeeldfoto's: API van Wikipedia/Wikimedia Commons (vrij gelicenseerd), met maker en licentie en de tekst "Voorbeeldfoto, niet jouw auto". Alleen merk, model en bouwjaar worden meegestuurd. Uit te zetten in Instellingen.

TOESTEMMINGEN
- Face ID: alleen als de gebruiker "Vergrendel met Face ID" aanzet (standaard uit).
- Foto's: via de systeemfotokiezer (PHPicker), geen toestemming voor de fotobibliotheek nodig.
- Geen locatie, contacten, camera, tracking of meldingen.

ACCOUNT
Geen inlog. Gegevens staan op het toestel en in de eigen privé-iCloud-database van de gebruiker (CloudKit). De achtergrondmodus remote-notification is alleen voor stille CloudKit-synchronisatie; de app toont geen meldingen.

AANKOPEN / ADVERTENTIES
Gratis, geen in-app-aankopen, abonnementen of advertenties.

OVERIG
- Beoordelingsverzoek (requestReview) hooguit eens per week, op z'n vroegst 4 uur na het eerste gebruik, nooit tijdens splash, welkomstscherm of vergrendeling.
- In Instellingen staat de kaart "Meer apps van de ontwikkelaar" naar lrvdlinden.app.
""")

# ---------------- privacy ----------------
w("privacy/privacy-policy-nl.txt", """
Privacyverklaring Kentr
Laatst bijgewerkt: 13 november 2026

Kentr is een app van LRvdLinden (lrvdlinden.app). Kort gezegd: Kentr heeft geen account, geen eigen server en geen tracking. De ontwikkelaar verzamelt geen gegevens.

Gegevens die je zelf invoert
De auto's die je toevoegt (kenteken, merk, model, periode, prijzen, kilometerstanden, notities en foto's) worden op je apparaat opgeslagen. Staat iCloud aan, dan worden ze via je eigen privé-iCloud-database van Apple gesynchroniseerd met je andere apparaten. LRvdLinden heeft geen toegang tot deze gegevens.

Opvragen bij de RDW
Als je een kenteken opzoekt of terugvindt, stuurt de app een verzoek rechtstreeks naar de open-data-dienst van de RDW (opendata.rdw.nl). Daarin staan alleen het kenteken of je zoekcriteria (zoals merk, model, kleur en bouwjaar). Er worden geen persoonsgegevens meegestuurd. De RDW verwerkt dit verzoek volgens haar eigen voorwaarden.

Voorbeeldfoto's van Wikipedia
Staat "Zoek automatisch een voorbeeldfoto" aan (standaard), dan zoekt Kentr een vrije foto van hetzelfde merk en model via de API van Wikipedia/Wikimedia Commons (wikipedia.org). Daarbij worden alleen merk, model en bouwjaar meegestuurd, geen kenteken en geen persoonsgegevens. Je kunt dit uitzetten in Instellingen › Foto's.

Face ID
Als je de app-vergrendeling aanzet, gebruikt Kentr Face ID, Touch ID of je toegangscode via iOS. De app krijgt alleen te horen of het ontgrendelen gelukt is; biometrische gegevens verlaten nooit je apparaat.

Geen analytics, advertenties of tracking
Kentr bevat geen analytics, geen advertenties en geen tracking van derden. De app slaat een paar instellingen lokaal op (zoals weergave en het moment waarop om een beoordeling is gevraagd).

Je rechten
Al je gegevens staan bij jou. Je verwijdert een auto in de app; als je de app verwijdert en de gegevens uit iCloud wist (Instellingen › [je naam] › iCloud), zijn ze helemaal weg.

Contact
Vragen over privacy? Kijk op https://kent.lrvdlinden.app/support/ of lrvdlinden.app.
Volledige versie: https://kent.lrvdlinden.app/privacy/
""")
w("privacy/privacy-policy-en.txt", """
Kentr Privacy Policy
Last updated: 13 November 2026

Kentr is an app by LRvdLinden (lrvdlinden.app). In short: Kentr has no account, no server of its own and no tracking. The developer does not collect any data.

Data you enter yourself
The cars you add (licence plate, make, model, period, prices, mileage, notes and photos) are stored on your device. If iCloud is on, they are synced to your other devices through your own private Apple iCloud database. LRvdLinden has no access to this data.

Requests to the RDW
When you look up or search for a licence plate, the app sends a request directly to the open data service of the RDW (opendata.rdw.nl). It contains only the plate or your search criteria (such as make, model, colour and year). No personal data is sent. The RDW handles the request under its own terms.

Example photos from Wikipedia
If "Zoek automatisch een voorbeeldfoto" (automatic example photo) is on (default), Kentr looks for a freely licensed photo of the same make and model through the Wikipedia/Wikimedia Commons API (wikipedia.org). Only make, model and year are sent, never the plate or personal data. You can turn this off in Settings › Photos.

Face ID
If you turn on the app lock, Kentr uses Face ID, Touch ID or your passcode through iOS. The app is only told whether unlocking succeeded; biometric data never leaves your device.

No analytics, ads or tracking
Kentr contains no analytics, no ads and no third-party tracking. The app stores a few settings locally (such as appearance and when a rating was last requested).

Your rights
All your data stays with you. Delete a car in the app; if you delete the app and erase its data from iCloud (Settings › [your name] › iCloud), it is gone completely.

Contact
Questions about privacy? See https://kent.lrvdlinden.app/support/ or lrvdlinden.app.
Full version (Dutch): https://kent.lrvdlinden.app/privacy/
""")
