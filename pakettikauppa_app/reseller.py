"""This is a module for Pakettikauppa integration for resellers to use

The module provides below functionality:
    1. Create customer
    2. Update customer
    3. Get list of customer
    4. De-activate customer

"""
__version__ = '0.1'
__author__ = 'Porntip Chaibamrung'

import re
import logging
from time import time
from pakettikauppa_app.pakettikauppa import Pakettikauppa, PakettikauppaException, check_api_name


class PkReseller(Pakettikauppa):
    _api_key = None
    _secret = None
    _isInTestMode = 1

    def __init__(self, is_test_mode=0, api_key=None, secret=None):
        """
        Constructor for this class.
        """
        self._isInTestMode = is_test_mode

        super().__init__(self._isInTestMode)

        self.mylogger = logging.getLogger(__name__)

        if self._isInTestMode == 1:
            self._api_key = '11111111-1111-1111-1111-111111111111'
            self._secret = 'FEDCBA0987654321'
        else:
            if api_key is None or api_key == '':
                raise PakettikauppaException("API key", "Missing API key")
            else:
                self._api_key = api_key
            if secret is None or secret == '':
                raise PakettikauppaException("Secret key", "Missing API secret key")
            else:
                self._secret = secret

    @check_api_name
    def get_api_suffix(self, api_name=None):
        __api_mapping = {
            'create_customer': '/customer/create',
            'update_customer': '/customer/update',
            'list_customer': '/customer/list',
            'deactivate_customer': '/customer/deactivate'
        }

        if api_name in __api_mapping:
            retval = str(__api_mapping[api_name])
            self.mylogger.debug("Api suffix: {}".format(retval))
            return retval
        else:
            raise PakettikauppaException(
                KeyError,
                "Invalid API name. Possible value are 'create_customer', 'update_customer', 'list_customer' \
                and 'deactivate_customer'"
            )

    def get_api_config(self, api_name=None):
        _api_suffix = self.get_api_suffix(api_name)
        _api_config = super().get_api_config(_api_suffix, self._api_key, self._secret)
        return _api_config

    def clean_up_phone_data(self, phone_string=None):
        if phone_string is None or phone_string == '':
            return ''
        else:
            phone_string = str(phone_string)
            # self.mylogger.debug("Original phone string={}".format(phone_string))

            formatted_string = re.sub('\D', '', phone_string)
            # self.mylogger.debug("Formatted phone string={}".format(formatted_string))
            return formatted_string

    def get_customer_list(self):
        _api_config = self.get_api_config('list_customer')

        input_req_data = {
            'api_key': self._api_key,
            'timestamp': str(int(time())),
        }

        # Calculate MAC
        digest_string = self.get_hash_sha256(self._secret, **input_req_data)
        input_req_data['hash'] = digest_string
        self.mylogger.debug("Hash input data={}".format(input_req_data))

        res_obj = super().send_request('POST', _api_config['api_post_url'], input_req_data)
        return self.return_data(res_obj)

    def create_customer(self, **kwargs):
        h_config = self.get_api_config('create_customer')

        _hInputData = self.get_create_customer_req_data(**kwargs)

        res_obj = super().send_request('POST', h_config['api_post_url'], _hInputData)
        #print("Response " + str(res_obj.json()))
        #return
        return self.return_data(res_obj)

    def get_create_customer_req_data(self, **kwargs):
        if kwargs is None:
            raise PakettikauppaException("Require input parameters")
        if len(kwargs) == 0:
            raise Exception(KeyError("Require input parameters"))

        _mandatory_keys = ('name', 'business_id', 'street_address', 'post_office', 'postcode', 'country', 'phone',
                           'email', 'contact_person_name', 'contact_person_phone', 'contact_person_email')

        for key in kwargs:
            if key not in _mandatory_keys:
                raise Exception(KeyError("Invalid key"))

        _hInputData = {
            'api_key': self._api_key,
            'name': kwargs['name'],
            'business_id': kwargs['business_id'],
            'payment_service_provider': kwargs['payment_service_provider'],
            'psp_merchant_id': kwargs['psp_merchant_id'],
            'marketing_name': kwargs['marketing_name'],
            'street_address': kwargs['street_address'],
            'post_office': kwargs['post_office'],
            'postcode': kwargs['postcode'],
            'country': kwargs['country'],
            'phone': self.clean_up_phone_data(kwargs['phone']),
            'email': kwargs['email'],
            'contact_person_name': kwargs['contact_person_name'],
            'contact_person_phone': self.clean_up_phone_data(kwargs['contact_person_phone']),
            'contact_person_email': kwargs['contact_person_email'],
            'customer_service_phone': self.clean_up_phone_data(kwargs['customer_service_phone']),
            'customer_service_email': kwargs['customer_service_email'],
        }

        # Calculate MAC
        digest_string = self.get_hash_sha256(self._secret, **_hInputData)
        _hInputData['hash'] = digest_string
        self.mylogger.debug("Hash input data={}".format(_hInputData))

        return _hInputData

    def update_customer(self, customer_id, **kwargs):
        customer_id = str(customer_id)
        if customer_id == '':
            raise PakettikauppaException(ValueError, "Customer id is empty")

        self.mylogger.debug("Updating customer id={}".format(customer_id))

        _api_config = self.get_api_config('update_customer')

        update_req_data = self.get_update_customer_req_data(customer_id, **kwargs)

        if update_req_data is None:
            self.mylogger.debug("No update request data found")
            return None
        else:
            res_obj = super().send_request('POST', _api_config['api_post_url'], update_req_data)
            return self.return_data(res_obj)

    def get_update_customer_req_data(self, customer_id, **kwargs):
        _accepted_keys = {'name', 'business_id', 'payment_service_provider', 'psp_merchant_id', 'marketing_name',
                          'street_address', 'post_office', 'postcode', 'country', 'phone', 'email',
                          'contact_person_name', 'contact_person_phone', 'contact_person_email',
                          'customer_service_phone', 'customer_service_email'
                          }

        length_arguments = len(kwargs)
        self.mylogger.debug("Length of input params={}".format(length_arguments))

        if length_arguments == 0:
            return None

        update_req_data = {
            'api_key': self._api_key,
            'customer_id': customer_id,
        }

        for key in kwargs:
            if key in _accepted_keys:
                item_value = kwargs[key]
                if item_value is not None and item_value != '':
                    update_req_data[key] = item_value
                else:
                    continue
            else:
                #raise PakettikauppaException(KeyError)
                raise PakettikauppaException("Invalid input key parameter")

        # Calculate MAC
        digest_string = self.get_hash_sha256(self._secret, **update_req_data)
        update_req_data['hash'] = digest_string
        self.mylogger.debug("Hash update input data={}".format(update_req_data))

        return update_req_data

    def deactivate_customer(self, customer_id):
        customer_id = str(customer_id)
        self.mylogger.debug("De-activating customer id={}".format(customer_id))

        _api_config = self.get_api_config('deactivate_customer')

        input_req_data = {
            'api_key': self._api_key,
            'customer_id': customer_id,
            'timestamp': str(int(time())),
        }

        # Calculate MAC
        digest_string = self.get_hash_sha256(self._secret, **input_req_data)
        input_req_data['hash'] = digest_string
        self.mylogger.debug("Hash de-activate input data={}".format(input_req_data))

        res_obj = super().send_request('POST', _api_config['api_post_url'], input_req_data)
        return self.return_data(res_obj)