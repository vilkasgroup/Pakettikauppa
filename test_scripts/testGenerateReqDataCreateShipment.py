from pakettikauppa.merchant import PkMerchant

merchant = PkMerchant(1)

simple_dict_data = merchant.get_simple_test_data_create_shipment()

req_data = merchant.get_proper_req_data_create_shipment(**simple_dict_data)
print("Request data = {}".format(req_data))

xml_req_data = merchant.get_xml_shipment_req_data(**req_data)
print("\n\n")

expected_xml_req_data = merchant.get_create_shipment_test_req_data()
