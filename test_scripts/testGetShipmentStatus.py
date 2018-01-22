from pakettikauppa.merchant import PkMerchant

# Vilkas own key for customer id = 65 but end point must be in test mode
API_KEY = 'd4fb618f-1f44-4dc0-bdce-4993f4b91b77'
SECRET = 'b5c95243276d3ff398207f8dea3013fef001e6e5f51fb9cb2252f609608a81'
TRACKING_CODE = 'JJFITESTLABEL1332'

m = PkMerchant(1, API_KEY, SECRET)

_api_config = m.get_api_config('get_shipment_status')
print("Hash config: {}".format(_api_config))
print("\n")


m.get_shipment_status(TRACKING_CODE)
