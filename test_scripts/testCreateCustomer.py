from pakettikauppa_app.reseller import PkReseller

resel = PkReseller(1)

h_config = resel.get_api_config('create_customer')
print("Config: " + str(h_config))
print("\n")

_hInputData = {
    'name': 'Vilkas Group Oy (Test)',
    'business_id': '12345678-9',
    'payment_service_provider': '',
    'psp_merchant_id': '',
    'marketing_name': '',
    'street_address': 'Finlaysoninkuja 19',
    'post_office': 'Tampere',
    'postcode': '33210',
    'country': 'Finland',
    'phone': '+35812345A5',
    'email': 'tipi@vilkas.fi',
    'contact_person_name': 'Porntip Härkönen',
    'contact_person_phone': '0123456789',
    'contact_person_email': 'tipi+test@vilkas.fi',
    'customer_service_phone': '',
    'customer_service_email': '',
}
resel.get_h_req_data(**_hInputData)

#resel.create_customer(**_hInputData)