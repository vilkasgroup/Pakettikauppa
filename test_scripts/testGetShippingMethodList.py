from pakettikauppa_app.merchant import PkMerchant

m = PkMerchant(1)
h_config = m.get_api_config('get_shipping_method_list')
print("Config: " + str(h_config))
print("\n")

m.get_shipping_method_list()