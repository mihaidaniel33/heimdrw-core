import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree

def process_xml_to_dataframe(xml_content: bytes) -> pd.DataFrame:
    # Parse XML content
    tree = ET.parse(io.BytesIO(xml_content))
    root = tree.getroot()
    
    # Initialize lists to store data
    data = []
    
    # Example XML processing - adjust according to your XML structure
    for element in root.findall('.//transaction'):  # Adjust the path according to your XML structure
        row = {
            'date': element.find('date').text if element.find('date') is not None else '',
            'description': element.find('description').text if element.find('description') is not None else '',
            'amount': element.find('amount').text if element.find('amount') is not None else '',
            'category': element.find('category').text if element.find('category') is not None else '',
        }
        data.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    return df


def validate_xml(xml_file, xsd_path):
    # Load and parse the schema (XSD)
    print(f'fails here')
    with open(xsd_path, 'rb') as schema_file:
        schema_doc = etree.XML(schema_file.read())
        schema = etree.XMLSchema(schema_doc)

    xml_doc = etree.fromstring(xml_file)

    try:
        schema.assertValid(xml_doc)
        print("✅ XML is valid.")
        return True
    except etree.DocumentInvalid as e:
        print("❌ XML is invalid:")
        print(e)
        return False
