from pakettikauppa_app.merchant import PkMerchant, decode_pdf_content, write_pdf_to_file
from datetime import datetime


# This data set work for test account
API_KEY = '00000000-0000-0000-0000-000000000000'
SECRET = '1234567890ABCDEF'
ROUTING_ID = '1479035179'
ORDER_ALIAS = 'ORDER001'

# This data set is not working
# Vilkas own key for customer id = 65 but end point must be in test mode
API_KEY = 'd4fb618f-1f44-4dc0-bdce-4993f4b91b77'
SECRET = 'b5c95243276d3ff398207f8dea3013fef001e6e5f51fb9cb2252f609608a81'
ROUTING_ID = '1464524676'
ORDER_ALIAS = 'ORDER10001'


def create_shipment_input_data(merchant_object):
    dict_data = {
        'eChannel': {
            'ROUTING': {
                'Routing.Account': API_KEY,
                'Routing.Key': merchant_object.get_routing_key(ROUTING_ID),
                'Routing.Id': ROUTING_ID,
                'Routing.Name': ORDER_ALIAS,
                'Routing.Time': datetime.now().strftime('%Y%m%d%H%M%S'),
                # - Ignored parameters in Pakettikauppa
                # 'Routing.Target' => { 'content' => '' },
                # 'Routing.Source' => { 'content' => '' },
                # 'Routing.Version'  => { 'content' => '' },
                # 'Routing.Mode' => { 'content' => '' },
            },
            'PrintLabel': {
                'responseFormat': "File",  # "File" and "inline" are supported. "File" is default
                'content': {
                    # Send request for multiple shipping labels
                    # this is for test credential
                    #'TrackingCode': [
                    #    {
                    #        'Code': 'JJFITESTLABEL601'
                    #    },
                    #    {
                    #        'Code': 'JJFITESTLABEL602'
                    #    },
                    #]
                    #
                    # or use this way to send a request for one shipping label
                    # This is for Vilkas API key
                    'TrackingCode': {
                        'Code': 'JJFITESTLABEL1332'
                    }
                }
            }
        }
    }
    return dict_data


if __name__ == '__main__':
    # This uses testing data set
    # m = PkMerchant(1)
    # m.get_create_shipment_test_req_data()

    # test with own define API key and secret
    m = PkMerchant(1, API_KEY, SECRET)

    # test with static test credential
    #m = PkMerchant(1)

    req_input = create_shipment_input_data(m)
    print("request input: {}".format(req_input))
    print("\n")

    _api_config = m.get_api_config('create_shipment')
    print("Hash config: {}".format(_api_config))
    print("\n")

    #m.get_xml_shipping_label_req_data(**req_input)

    dict_res_data = m.get_shipping_label(**req_input)
    encoded_pdf_content = dict_res_data['PDFcontent']

    decoded_pdf_content = decode_pdf_content(encoded_pdf_content)
    #output_file = 'shipping_label_output.pdf'
    #write_pdf_to_file(output_file, decoded_pdf_content)
