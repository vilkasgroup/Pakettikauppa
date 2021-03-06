#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import unicode_literals
import sys
import logging
from unittest import TestCase, main
from pakettikauppa.merchant import PkMerchant
from datetime import datetime

logging.basicConfig(
    level=logging.DEBUG,
)


class TestCreateShipment(TestCase):
    @classmethod
    def setUpClass(cls):
        # Vilkas own key for customer id = 65 but end point must be in test mode
        # customer id = 65
        # 'd4fb618f-1f44-4dc0-bdce-4993f4b91b77'
        # 'b5c95243276d3ff398207f8dea3013fef001e6e5f51fb9cb2252f609608a81'
        #cls.API_KEY = '4f10f3dc-cbc7-47a6-abf7-ec2f8189977f'
        #cls.SECRET = '8b6510ef94f2cb9da3d4320d12ae1cd9c880a71be4e8e983e170a71482d43a278b0d53c4a39ef283'
        cls.API_KEY = '00000000-0000-0000-0000-000000000000'
        cls.SECRET = '1234567890ABCDEF'
        cls.ROUTING_ID = '1464524676'
        cls.ORDER_ALIAS = 'ORDER10002'

        # for special character testing
        if sys.version_info < (3, 0):
            # Python 2.7
            cls._recipient_address = 'Nikinväylä 3 test'.decode('utf-8').encode('utf-8')
            cls._additional_info_text = "ÄOrder no.: " + cls.ORDER_ALIAS + "-- Reference no.: 00001"
            cls._additional_info_text = cls._additional_info_text.decode('utf-8').encode('utf-8')
        else:
            # Python 3.6
            cls._recipient_address = 'Nikinväylä 3 test'
            cls._additional_info_text = "ÄOrder no.: " + cls.ORDER_ALIAS + "-- Reference no.: 00001"

        # when using own account we must ensure that we have enough funds otherwise we will get error message
        cls._merchant = PkMerchant(1, cls.API_KEY, cls.SECRET)
        cls._pk_test_merchant = PkMerchant(1)

        cls.logger = logging.getLogger(__name__)

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_empty_parameter(self):
        """
        Test passing empty parameter to the function
        """
        with self.assertRaises(Exception) as e:
            self._merchant.create_shipment(**{})
        # self.logger.debug("Exception message = {}".format(e.exception))

    def test_missing_root_element(self):
        """
        Test when passing dictionary without expected root element
        """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'InvalidKey': 'KeyValue'
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "'eChannel key is missing'")

    def test_missing_routing_element(self):
        """
        Test passing root element but without routing element in dictionary data
        """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'InvalidKey': 'Value'
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "'ROUTING key is missing'")

    def test_missing_shipment_element(self):
        """
        Test passing dictionary without Shipment element.
        """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {
                        'Routing.Account': 'test',
                        'Routing.Id': '',
                        'Routing.Key': '',
                        'Routing.Name': '',
                        'Routing.Time': '',
                    },
                    'InvalidKey': 'Value'
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "'Shipment key is missing'")

    def test_empty_routing(self):
        """
        Test passing routing element with empty value.
        """
        with self.assertRaises(ValueError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {},
                    'Shipment': {}
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        self.assertEqual(str(e.exception), "Missing routing data")

    def test_wrong_data_type_routing(self):
        """ Test passing incorrect routing data structure. """
        with self.assertRaises(TypeError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': 'test',
                    'Shipment': {}
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "Missing routing data")

    def test_missing_keys_in_routing(self):
        """ Test passing correct data structure for Routing element but incorrect key. """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {
                        'InvalidKey': 'test'
                    },
                    'Shipment': {}
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))

    def test_missing_sender(self):
        """ Test passing Shipment element without sender data. """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {
                        'Routing.Account': 'test',
                        'Routing.Id': '',
                        'Routing.Key': '',
                        'Routing.Name': '',
                        'Routing.Time': '',
                    },
                    'Shipment': {
                        'InvalidKey': '',
                    }
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "'Missing Shipment.Sender key'")

    def test_missing_sender_info(self):
        """ Test passing Shipment.Sender element without data. """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {
                        'Routing.Account': 'test',
                        'Routing.Id': '',
                        'Routing.Key': '',
                        'Routing.Name': '',
                        'Routing.Time': '',
                    },
                    'Shipment': {
                        'Shipment.Sender': {},
                    }
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))

    def test_missing_recipient(self):
        """ Test passing without recipient data. """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {
                        'Routing.Account': 'test',
                        'Routing.Id': '',
                        'Routing.Key': '',
                        'Routing.Name': '',
                        'Routing.Time': '',
                    },
                    'Shipment': {
                        'Shipment.Sender': {
                            'Sender.Name1': 'Vilkas Group Oy',
                            'Sender.Addr1': 'Finlaysoninkuja 19',
                            'Sender.Postcode': '33210',
                            'Sender.City': 'Tampere',
                            'Sender.Country': 'FI',
                            'Sender.Phone': '',
                            'Sender.Vatcode': '1234567-8',
                            'Sender.Email': 'tipi@vilkas.fi',
                        },
                    }
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "'Missing Shipment.Recipient key'")

    def test_missing_recipient_info(self):
        """ Test passing Shipment.Recipient element without recipient data. """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {
                        'Routing.Account': 'test',
                        'Routing.Id': '',
                        'Routing.Key': '',
                        'Routing.Name': '',
                        'Routing.Time': '',
                    },
                    'Shipment': {
                        'Shipment.Sender': {
                            'Sender.Name1': 'Vilkas Group Oy',
                            'Sender.Addr1': 'Finlaysoninkuja 19',
                            'Sender.Postcode': '33210',
                            'Sender.City': 'Tampere',
                            'Sender.Country': 'FI',
                            'Sender.Phone': '',
                            'Sender.Vatcode': '1234567-8',
                            'Sender.Email': 'tipi@vilkas.fi',
                        },
                        'Shipment.Recipient': {}
                    }
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "'Missing mandatory key in Shipment.Recipient element'")

    def test_missing_consignment(self):
        """ Test passing without consignment data. """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {
                        'Routing.Account': 'test',
                        'Routing.Id': '',
                        'Routing.Key': '',
                        'Routing.Name': '',
                        'Routing.Time': '',
                    },
                    'Shipment': {
                        'Shipment.Sender': {
                            'Sender.Name1': 'Vilkas Group Oy',
                            'Sender.Addr1': 'Finlaysoninkuja 19',
                            'Sender.Postcode': '33210',
                            'Sender.City': 'Tampere',
                            'Sender.Country': 'FI',
                            'Sender.Phone': '',
                            'Sender.Vatcode': '1234567-8',
                            'Sender.Email': 'tipi@vilkas.fi',
                        },
                        'Shipment.Recipient': {
                            'Recipient.Name1': 'Receiver name',
                            'Recipient.Addr1': self._recipient_address,
                            'Recipient.Postcode': '33100',
                            'Recipient.City': 'Tampere',
                            'Recipient.Country': 'FI',
                            'Recipient.Phone': '123456789',
                            'Recipient.Email': 'tipi@vilkas.fi',
                        }
                    }
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "'Missing Shipment.Consignment key'")

    def test_missing_consignment_info(self):
        """ Test passing Shipment.Consignment element without data. """
        with self.assertRaises(KeyError) as e:
            self._merchant.create_shipment(**{
                'eChannel': {
                    'ROUTING': {
                        'Routing.Account': 'test',
                        'Routing.Id': '',
                        'Routing.Key': '',
                        'Routing.Name': '',
                        'Routing.Time': '',
                    },
                    'Shipment': {
                        'Shipment.Sender': {
                            'Sender.Name1': 'Vilkas Group Oy',
                            'Sender.Addr1': 'Finlaysoninkuja 19',
                            'Sender.Postcode': '33210',
                            'Sender.City': 'Tampere',
                            'Sender.Country': 'FI',
                            'Sender.Phone': '',
                            'Sender.Vatcode': '1234567-8',
                            'Sender.Email': 'tipi@vilkas.fi',
                        },
                        'Shipment.Recipient': {
                            'Recipient.Name1': 'Receiver name',
                            'Recipient.Addr1': self._recipient_address,
                            'Recipient.Postcode': '33100',
                            'Recipient.City': 'Tampere',
                            'Recipient.Country': 'FI',
                            'Recipient.Phone': '123456789',
                            'Recipient.Email': 'tipi@vilkas.fi',
                        },
                        'Shipment.Consignment': {}
                    }
                }
            })
        # self.logger.debug("Exception message = {}".format(e.exception))
        # self.assertEqual(str(e.exception), "'Missing mandatory key in Shipment.Consignment element'")

    def test_create_with_test_req_data(self):
        """ Test generated test request data. """
        req_data = self._merchant.get_create_shipment_test_req_data()
        dict_res = self._merchant.create_shipment(**req_data)

        status = dict_res['status']
        dict_tracking_code = dict_res['trackingcode']
        # tracking_url = dict_tracking_code['tracking_url']
        tracking_code = dict_tracking_code['value']
        self.assertIsNotNone(dict_res) and self.assertTrue(status) and self.assertIsNotNone(tracking_code)

    def test_create_multiple_parcel_with_test_req_data(self):
        """ Test generated test request data. """
        req_data = self._merchant.get_create_multi_parcels_shipment_test_data()
        dict_res = self._merchant.create_shipment(**req_data)

        status = dict_res['status']
        dict_tracking_code = dict_res['trackingcode']
        # tracking_url = dict_tracking_code['tracking_url']
        tracking_code = dict_tracking_code['value']
        self.assertIsNotNone(dict_res) and self.assertTrue(status) and self.assertIsNotNone(tracking_code)

    def test_create_shipment(self):
        """ Test creating shipment with proper data structure. """
        req_input = {
            'eChannel': {
                'ROUTING': {
                    'Routing.Account': self.API_KEY,
                    'Routing.Key': self._merchant.get_routing_key(self.ROUTING_ID),
                    'Routing.Id': self.ROUTING_ID,
                    'Routing.Name': self.ORDER_ALIAS,
                    'Routing.Time': datetime.now().strftime('%Y%m%d%H%M%S'),
                },
                'Shipment': {
                    'Shipment.Sender': {
                        'Sender.Contractid': '',
                        'Sender.Name1': 'Vilkas Group Oy',
                        'Sender.Name2': '',
                        'Sender.Addr1': 'Finlaysoninkuja 19',
                        'Sender.Addr2': '',
                        'Sender.Addr3': '',
                        'Sender.Postcode': '33210',
                        'Sender.City': 'Tampere',
                        'Sender.Country': 'FI',
                        'Sender.Phone': '',
                        'Sender.Vatcode': '1234567-8',
                        'Sender.Email': 'tipi@vilkas.fi',
                    },
                    'Shipment.Recipient': {
                        # 'Recipient.Code': '',
                        'Recipient.Name1': 'John Doe',
                        'Recipient.Name2': '',
                        'Recipient.Addr1': self._recipient_address,
                        'Recipient.Addr2': '',
                        'Recipient.Addr3': '',
                        'Recipient.Postcode': '33100',
                        'Recipient.City': 'Tampere',
                        'Recipient.Country': 'FI',
                        'Recipient.Phone': '123456789',
                        'Recipient.Vatcode': '',
                        'Recipient.Email': 'tipi@vilkas.fi',
                    },
                    'Shipment.Consignment': {
                        'Consignment.Reference': '3211479032410',
                        'Consignment.Product': '2103',  # - Posti's product code 2103, product code for Bussipaketti is 90010 but then below pickup point is not available
                        'Consignment.Contentcode': 'D',
                        'Consignment.ReturnInstruction': 'E',
                        # 'Consignment.ReturnInstruction': None,
                        'Consignment.Invoicenumber': self.ORDER_ALIAS,
                        'Consignment.Merchandisevalue': 150,
                        'Consignment.Currency': 'eur',
                        'Consignment.AdditionalInfo': {
                            'AdditionalInfo.Text': self._additional_info_text
                        },
                        'Consignment.AdditionalService': [
                            {
                                'AdditionalService.ServiceCode': '2106',  # pickup point service
                                'AdditionalService.Specifier': {
                                    'name': 'pickup_point_id',
                                    'value': '8547',
                                }
                            },
                            {
                                'AdditionalService.ServiceCode': '3101',  # cash on delivery service
                                'AdditionalService.Specifier': [
                                    {
                                        'name': 'amount',
                                        'value': '150'
                                    },
                                    {
                                        'name': 'account',
                                        'value': 'FI2180000012345678'
                                    },
                                    {
                                        'name': 'codbic',
                                        'value': 'DABAFIHH'
                                    },
                                    {
                                        'name': 'reference',
                                        'value': '12344'
                                    },
                                ]
                            },
                        ],
                        'Consignment.Parcel': [
                            {
                                'Parcel.Reference': '123456',  # not mandatory
                                'Parcel.Packagetype': 'PC',
                                'Parcel.Weight': {'weight_unit': 'kg', 'value': '1.2'},
                                'Parcel.Volume': {'unit': 'm3', 'value': '0.6'},
                                'Parcel.Infocode': '1012',
                                'Parcel.Contents': 'Test products',  # product description
                                'Parcel.ReturnService': '123',
                                # Customs declaration info (for medicine)
                                'Parcel.contentline': {
                                    'contentline.description': 'Puita',
                                    'contentline.quantity': 1,
                                    'contentline.currency': 'EUR',
                                    'contentline.netweight': 1,
                                    'contentline.value': 100,
                                    'contentline.countryoforigin': 'FI',
                                    'contentline.tariffcode': '9608101000',
                                },
                                # this is not really needed in Pakettikauppa but Prinetti
                                'Parcel.ParcelService': []
                            },
                        ]
                    }  # end Shipment.Consignment
                }  # end Shipment
            }  # end eChannel
        }
        dict_res = self._merchant.create_shipment(**req_input)
        status = dict_res['status']
        dict_tracking_code = dict_res['trackingcode']
        # tracking_url = dict_tracking_code['tracking_url']
        tracking_code = dict_tracking_code['value']
        self.assertIsNotNone(dict_res) and self.assertTrue(status) and self.assertIsNotNone(tracking_code)


if __name__ == '__main__':
    main(verbosity=2)
