import xml.etree.ElementTree as ET



# TEI-Namespace definieren
NS = {'tei': 'http://www.tei-c.org/ns/1.0'}

def extract_sequence(xml_file):
    sequence = []

    # Parsing mit Namespace-Unterstützung
    context = ET.iterparse(xml_file, events=("start",))
    for event, elem in context:
        tag = elem.tag
        if tag.endswith('date'):
            cal = elem.attrib.get('calendar')
            method = elem.attrib.get('datingMethod')
            when = elem.attrib.get('when-custom')
            if cal == '#gregorian' and method == '#gregorian' and when:
                sequence.append(when)
        elif tag.endswith('rs'):
            type_ = elem.attrib.get('type')
            role = elem.attrib.get('role')
            ref = elem.attrib.get('ref')
            if type_ == 'place' and role == 'present' and ref and ref.startswith('plc:'):
                sequence.append(ref.replace('plc:', ''))

    return sequence

if __name__ == "__main__":
    xml_file = input("Geben Sie den Namen der XML Datei. Sie muss im selben Ordner wie das Skript sein")
    result = extract_sequence(xml_file)

    if result:
        for entry in result:
            print(entry)
    else:
        print("⚠️ Keine passenden Einträge gefunden.")
