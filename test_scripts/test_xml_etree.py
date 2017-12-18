import xml.etree.ElementTree as ET
from xml.dom import minidom


def parse_xml_file():
    tree = ET.parse('CreateShipmentReqData.xml')
    root = tree.getroot()
    print(root)
    for child in root:
        print(child.tag, child.attrib)

    currency_element = root.find("Shipment/Shipment.Consignment/Consignment.Currency")
    print(currency_element.text)


def create_shipment_xml_data():
    root = ET.Element('eChannel')
    child = ET.SubElement(root, "child")
    child.text = "I am a child"
    child.set("myattribute", "1234")

    # print(ET.tostring(root, encoding='utf8', method='xml'))
    xml_string = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ", encoding="utf-8")
    print(repr(xml_string))


if __name__ == '__main__':
    print("Pasing XML \n")
    parse_xml_file()

    print("Creating XML \n")
    create_shipment_xml_data()