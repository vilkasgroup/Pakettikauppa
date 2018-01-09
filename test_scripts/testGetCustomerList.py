#!/usr/bin/env python

from pakettikauppa_app.reseller import PkReseller

resel = PkReseller(1)

h_config = resel.get_api_config('list_customer')
# h_config = resel.get_api_config('test')
print("Config: " + str(h_config))
print("\n")

resel.get_customer_list()
