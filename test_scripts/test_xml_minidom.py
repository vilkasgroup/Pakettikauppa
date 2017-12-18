from xml.dom import minidom


def create_shipment_xml_data():
    doc = minidom.Document()

    root = doc.createElement('eChannel')
    doc.appendChild(root)

    routing_element = doc.createElement('ROUTING')

    routing_account_element = doc.createElement('Routing.Account')
    account_text = doc.createTextNode('00000000-0000-0000-0000-000000000000')
    routing_account_element.appendChild(account_text)
    routing_account_element.setAttribute('color', 'white')
    routing_element.appendChild(routing_account_element)

    root.appendChild(routing_element)

    xml_str = doc.toprettyxml(indent="  ", encoding="utf-8")
    print(repr(xml_str))


def parse_xml_file():
    doc = minidom.parse("CreateShipmentReqData.xml")
    name = doc.getElementsByTagName("Shipment.Consignment")[0]
    node_name = name.nodeName
    node_list = name.childNodes
    node_length = len(node_list)
    print("Length of node list " + str(node_list))

    print(name.getElementsByTagName("Consignment.Currency")[0].data)
    for node in node_list:
        if node.nodeType == node.TEXT_NODE:
            get_node_list_text(node)
        else:
            print(node.tagName)


def get_node_list_text(node):
    print("Node data " + node.data)


if __name__ == '__main__':
    create_shipment_xml_data()
    print("\n")

    parse_xml_file()
