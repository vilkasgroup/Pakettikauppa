from collections import namedtuple

Mapping = namedtuple('Mapping', 'create_customer update_customer')

api_mapping = Mapping('/customer/create','/customer/update')

print(api_mapping)
print("\n")

print(api_mapping[0])

print(api_mapping.create_customer)

key = 'create_customer'
print(api_mapping.key)

#api_mapping[0] = 'new path'
#print(api_mapping[0])

api_mapping = ['new path']
print(api_mapping[0])
print("\n")
print(api_mapping)