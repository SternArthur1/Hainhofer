import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog

# Datei auswählen
Tk().withdraw()
file_path = filedialog.askopenfilename(
    title="Wähle die XML-Datei aus",
    filetypes=[("XML-Dateien", "*.xml"), ("Alle Dateien", "*.*")]
)

if not file_path:
    print("Keine Datei ausgewählt.")
    exit()

# XML einlesen
tree = ET.parse(file_path)
root = tree.getroot()

# TEI-Namespace registrieren
namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Alle <tei:rs type="person" ...> finden
all_rs_persons = root.findall('.//tei:rs[@type="person"]', namespaces)

# Nur ref-Werte extrahieren, die mit 'psn:' anfangen
psn_refs = [
    el.get('ref') for el in all_rs_persons
    if el.get('ref', '').startswith('psn:')
]

# Doppelte entfernen (falls gewünscht)
unique_refs = sorted(set(psn_refs))

# Ausgabe
for ref in unique_refs:
    print(ref)