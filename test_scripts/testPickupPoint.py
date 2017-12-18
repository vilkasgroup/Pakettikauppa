from pakettikauppa_app.merchant import PkMerchant

m = PkMerchant(1)
h_config = m.get_api_config('search_pickup_points')
print("Config: " + str(h_config))

input_params = {
    'postal_code': '33580',
    'country_code2': 'FI',
    'street_address': 'Nikinväylä 3 B 12',
    'service_provider': None,
    'max_result': None
}
content_string = m.get_pickup_point_req_data(h_config['api_key'], **input_params)
print("Content string " + str(content_string) )

#m.send_request('POST', h_config['api_post_url'], content_string)
m.search_pickup_points(**input_params)