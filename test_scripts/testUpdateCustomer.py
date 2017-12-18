from pakettikauppa_app.reseller import PkReseller

resel = PkReseller(1)

h_config = resel.get_api_config('update_customer')
print("Config: " + str(h_config))
print("\n")

customer_id = 128
h_update = {
    'name': 'Vilkas Group Oy (Test)',
    'business_id': '12345678-9',
    'customer_service_phone': '12369548',
}
resel.update_customer(customer_id, **h_update)
