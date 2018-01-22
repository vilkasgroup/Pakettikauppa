"""
import collections

Town = collections.namedtuple("Town", "name population coordinates capital state_bird")

town_list = []

town_list.append(Town('Town 1', '10', '10.10', 'Capital 1', 'Turkey'))
town_list.append(Town('Town 2', '11', '11.11', 'Capital 2', 'Duck'))

town_dictionary = {t.name: t for t in town_list}
print(town_dictionary['Town 1'][0])

town_dictionary['Town 1'] = ['My town']
print(town_dictionary['Town 1'][0])
"""
from pakettikauppa.reseller import PkReseller

resel = PkReseller(1)

print("Whole mapping " + str(resel._api_mapping))

org_name = resel.get_api_suffix('list_customer').__PkReseller__.__api_mapping['list_customer'][0]
print("Original text " + str(org_name))

resel._api_mapping['list_customer'] = 'changed value'

print("Changed text " + resel._api_mapping['list_customer'][0])

