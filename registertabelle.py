from lxml import etree
import csv

# Datei als Bytes öffnen (wichtig wegen der XML-Deklaration)
with open("register.xhtml", "rb") as f:
    tree = etree.parse(f, etree.HTMLParser())

# XPath: Alle Personen-Einträge im Personenregister
entries = tree.xpath('//div[@id="psn"]/div[contains(@class, "entry")]')

# Liste für alle Personen
personen = []

for entry in entries:
    # Name extrahieren
    name = entry.xpath('.//h1[@class="prefname"]/text()')
    name = name[0].strip() if name else ""

    # Geburts- und Sterbejahr extrahieren
    bd_text = entry.xpath('.//div[@class="birthdeath"]/p/text()')
    geburtsjahr = todesjahr = ""
    for text in bd_text:
        text = text.strip()
        if text.startswith("*"):
            geburtsjahr = text.lstrip("*").strip()
        elif text.startswith("✝"):
            todesjahr = text.lstrip("✝").strip()

    # Konfession extrahieren
    konfession = entry.xpath('.//div[@class="faithcontainer"]//li/text()')
    konfession = konfession[0].strip() if konfession else ""

    # Ergebnisse sammeln
    personen.append({
        "Name": name,
        "Geburtsjahr": geburtsjahr,
        "Todesjahr": todesjahr,
        "Konfession": konfession
    })

# Ausgabe als CSV speichern
with open("personenregister.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Name", "Geburtsjahr", "Todesjahr", "Konfession"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for person in personen:
        writer.writerow(person)

print("✓ CSV-Datei 'personenregister.csv' wurde erfolgreich erstellt!")
