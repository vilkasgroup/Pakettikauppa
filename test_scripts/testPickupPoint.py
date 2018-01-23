from __future__ import absolute_import
from pakettikauppa import merchant

API_KEY = 'd4fb618f-1f44-4dc0-bdce-4993f4b91b77'
SECRET = 'b5c95243276d3ff398207f8dea3013fef001e6e5f51fb9cb2252f609608a81'
# m = merchant.PkMerchant(1)  # use test account from Pakettikauppa
m = merchant.PkMerchant(1, API_KEY, SECRET)  # use own test account
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
print("Content string " + str(content_string))

# m.send_request('POST', h_config['api_post_url'], content_string)
m.search_pickup_points(**input_params)
