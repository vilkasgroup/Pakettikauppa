"""Pakettikauppa app

This module provides base functionality for Pakettikauppa integration

"""
__version__ = '0.1'
__author__ = 'Porntip Chaibamrung'

import hashlib
import hmac
import requests
import logging
import json
from functools import wraps


def check_api_name(function):
    @wraps(function)
    def decorated_function(self, param):
        if param is None or param == '':
            raise PakettikauppaException("API name", "Missing API name")

        #print("API name variable type " + str(type(param).__name__))
        self.logger.debug("API name variable type={}".format(type(param).__name__))
        if str(type(param).__name__) != 'str':
            raise PakettikauppaException(param, "Invalid parameter type")
        else:
            return function(self, param)

    # or use this line => return wraps(function)(decorated_function)
    return decorated_function


class PakettikauppaException(Exception):
    pass


class Pakettikauppa:
    _base_api_end_point = None
    logger = None

    def __init__(self, is_test_mode=0):
        """
        Constructor for this class.
        """
        logging.basicConfig(
            #    filename="pakettikauppa.log",
            #    format="%(asctime)s:%(levelname)s:%(message)s",
            level=logging.DEBUG,
        )
        self.set_logger()

        if is_test_mode == 1:
            Pakettikauppa._base_api_end_point = 'https://apitest.pakettikauppa.fi'
        else:
            Pakettikauppa._base_api_end_point = 'https://api.pakettikauppa.fi'
        #if self.isinstance(PkMerchant):

    def set_logger(self):
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        return self.logger

    def get_api_config(self, api_suffix=None, api_key=None, secret_key=None):
        if api_suffix is None:
            raise PakettikauppaException("API suffix", "Missing API suffix")
        _api_post_url = Pakettikauppa._base_api_end_point + api_suffix
        _api_config = {
            'api_post_url' : _api_post_url,
            'api_key': api_key,
            'api_secret': secret_key
        }
        return _api_config

    def get_hash_sha256(self, secret_key, **kwargs):
        secret_key = str(secret_key)
        self.logger.debug("Secret key: {}".format(secret_key))

        my_lst = []
        for key in sorted(kwargs):
            self.logger.debug("Key={}, Value={}".format(key, kwargs[key]))
            my_lst.append( str(kwargs[key]) )
        plain_text = '&'.join(map(str, my_lst))
        self.logger.debug("Plain text={}".format(plain_text))

        message_bytes = bytes(plain_text, 'utf-8')
        secret_bytes = bytes(secret_key, 'utf-8')

        hash = hmac.new(secret_bytes, message_bytes, hashlib.sha256)

        # to lowercase hexits
        digest_string = hash.hexdigest()
        self.logger.debug("Digest string={}".format(digest_string))
        return str(digest_string)

    def get_md5_hash(self, api_key, secret_key, routing_id):
        routing_key_data = str(api_key) + str(routing_id) + str(secret_key)
        self.logger.debug("Routing key data={}".format(routing_key_data))
        digest_string = hashlib.md5(routing_key_data.encode('utf-8')).hexdigest()
        self.logger.debug("MD5 Digest string={}".format(digest_string))
        return digest_string

    def get_api_end_point(self):
        return self._base_api_end_point

    def send_request(self, send_method='POST', _api_post_url=None, req_input=None, **headers):
        if headers is None:
            headers = {
                #'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
                'Content-Encoding': 'utf-8'
            }

        if send_method == 'POST':
            if req_input is None:
                res_obj = requests.post(_api_post_url, headers=headers)
            else:
                res_obj = requests.post(_api_post_url, data=req_input, headers=headers)

        else:
            if req_input is None:
                res_obj = requests.get(_api_post_url, headers=headers)
            else:
                res_obj = requests.get(_api_post_url, headers=headers, data=req_input, params=req_input)

        # self.logger.debug("Request headers={}".format(res_obj.request.headers))

        # Response data object is in 'res_obj' variable
        self.logger.debug("Response status code={}".format(res_obj.status_code))
        # self.logger.debug("Response content={}".format(res_obj.content))
        # self.logger.debug("Response text={}".format(res_obj.text))

        return res_obj

    def get_res_json_data(self, res_obj):
        list_data = res_obj.json()
        self.logger.debug("Response JSON data={}".format(list_data))

        # self.logger.debug("data item={}".format(json.loads(list_data)))
        for item in list_data:
            self.logger.debug("item={}".format(item))
            self.logger.debug("\n")

    def return_data(self, res_obj=None):
        if res_obj is not None:
            try:
                list_data = res_obj.json()
                self.mylogger.debug("Response: {}".format(list_data))
            except Exception:
                raise Exception("Unable to parse JSON data")
            finally:
                return list_data
        else:
            return None
