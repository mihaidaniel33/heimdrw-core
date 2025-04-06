from lxml import etree


def validate_xml(xml_file, xsd_path):
    # Load and parse the schema (XSD)
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
