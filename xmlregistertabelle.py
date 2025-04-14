from lxml import etree

# XHTML-Datei als Bytes öffnen
with open("register.xhtml", "rb") as f:
    tree = etree.parse(f, etree.HTMLParser())

# Personen-Einträge extrahieren
entries = tree.xpath('//div[@id="psn"]/div[contains(@class, "entry")]')

# Neues XML-Wurzelelement
root = etree.Element("personenregister")

for entry in entries:
    # Name
    name = entry.xpath('.//h1[@class="prefname"]/text()')
    name = name[0].strip() if name else ""

    # Geburts- und Sterbejahr
    bd_text = entry.xpath('.//div[@class="birthdeath"]/p/text()')
    geburtsjahr = todesjahr = ""
    for text in bd_text:
        text = text.strip()
        if text.startswith("*"):
            geburtsjahr = text.lstrip("*").strip()
        elif text.startswith("✝"):
            todesjahr = text.lstrip("✝").strip()

    # Konfession
    konfession = entry.xpath('.//div[@class="faithcontainer"]//li/text()')
    konfession = konfession[0].strip() if konfession else ""

    # Person-Element erzeugen
    person_el = etree.SubElement(root, "person")

    name_el = etree.SubElement(person_el, "name")
    name_el.text = name

    geburtsjahr_el = etree.SubElement(person_el, "geburtsjahr")
    geburtsjahr_el.text = geburtsjahr

    todesjahr_el = etree.SubElement(person_el, "todesjahr")
    todesjahr_el.text = todesjahr

    konfession_el = etree.SubElement(person_el, "konfession")
    konfession_el.text = konfession

# Baum erzeugen und als XML speichern
baum = etree.ElementTree(root)
baum.write("personenregister.xml", encoding="utf-8", xml_declaration=True, pretty_print=True)

print("✓ XML-Datei 'personenregister.xml' wurde erfolgreich erstellt.")
