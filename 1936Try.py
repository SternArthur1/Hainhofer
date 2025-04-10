import xml.etree.ElementTree as ET

# Korrekter Pfad zur Datei
file_path = '/Users/annagisiger/Desktop/HainhoferProjekt1936/Muenchen-1636-14 (4).xml'
tree = ET.parse(file_path)
root = tree.getroot()

# TEI-Namespace registrieren
namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Alle <date>-Elemente finden
dates = root.findall('.//tei:date', namespaces)

def extract_text_recursive(elem):
    return ''.join(elem.itertext()).strip()

# Texte aus den <date>-Elementen extrahieren
date_texts = [extract_text_recursive(elem) for elem in dates if extract_text_recursive(elem)]

# Ausgabe
for date in date_texts[:1000]:
    print(date)
import xml.etree.ElementTree as ET

# Load and parse the XML file
file_path = '/Users/annagisiger/Desktop/HainhoferProjekt1936/Muenchen-1636-14 (4).xml'
tree = ET.parse('/Users/annagisiger/Desktop/HainhoferProjekt1936/Muenchen-1636-14 (4).xml')
root = tree.getroot()

# Register namespace
namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Find all elements with type="person"
places = root.findall('.//*[@type="place"]', namespaces)

# Function to recursively extract text content
def extract_text_recursive(elem):
    """Recursively extract all text from an element including its children."""
    return ''.join(elem.itertext()).strip()

# Extract and clean person names
places = [extract_text_recursive(elem) for elem in places if extract_text_recursive(elem)]

# Output preview
for place in places [:1000]:
    print(place)
    import xml.etree.ElementTree as ET

# Load and parse the XML file
file_path = '/Users/annagisiger/Desktop/HainhoferProjekt1936/Muenchen-1636-14 (4).xml'
tree = ET.parse('/Users/annagisiger/Desktop/HainhoferProjekt1936/Muenchen-1636-14 (4).xml')
root = tree.getroot()

# Register namespace
namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Find all elements with type="person"
persons = root.findall('.//*[@type="person"]', namespaces)

# Function to recursively extract text content
def extract_text_recursive(elem):
    """Recursively extract all text from an element including its children."""
    return ''.join(elem.itertext()).strip()

# Extract and clean person names
person_names = [extract_text_recursive(elem) for elem in persons if extract_text_recursive(elem)]

# Output preview
for name in person_names[:1000]:
    print(name)