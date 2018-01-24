# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath('../'))

from pakettikauppa.merchant import PkMerchant
from datetime import datetime


# Vilkas own key for customer id = 65 but end point must be in test mode
API_KEY = 'd4fb618f-1f44-4dc0-bdce-4993f4b91b77'
SECRET = 'b5c95243276d3ff398207f8dea3013fef001e6e5f51fb9cb2252f609608a81'
ROUTING_ID = '1464524676'
ORDER_ALIAS = 'ORDER10002'


def create_shipment_input_data(merchant_object):
    dict_data = {
        'eChannel': {
            'ROUTING': {
                'Routing.Account': API_KEY,
                'Routing.Key': merchant_object.get_routing_key(ROUTING_ID),
                'Routing.Id': ROUTING_ID,
                'Routing.Name': ORDER_ALIAS,
                'Routing.Time': datetime.now().strftime('%Y%m%d%H%M%S'),
                # - Ignored parameters in Pakettikauppa
                # 'Routing.Target' => { 'content' => '' },
                # 'Routing.Source' => { 'content' => '' },
                # 'Routing.Version'  => { 'content' => '' },
                # 'Routing.Mode' => { 'content' => '' },
            },
            'Shipment': {
                'Shipment.Sender': {
                    'Sender.Contractid': '',
                    'Sender.Name1': 'Vilkas Group Oy äÅ',
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
                    'Recipient.Addr1': 'Nikinväylä 3 test',
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
                    'Consignment.Product': '90010',  # - Posti's product code 2103
                    'Consignment.Contentcode': 'D',  # Order->get('PR_ContentCode')
                    'Consignment.ReturnInstruction': 'E',  # Order->get('PR_ReturnInstruction')
                    #'Consignment.ReturnInstruction': None,
                    'Consignment.Invoicenumber': ORDER_ALIAS,
                    'Consignment.Merchandisevalue': 150,  # Order->get('PR_Merchandisevalue')
                    'Consignment.Currency': 'eur',
                    'Consignment.AdditionalInfo': {
                        # Order->get('PR_AdditionalInfoText')
                        'AdditionalInfo.Text': "Order no.: 1107-1 -- Reference no.: 284554"
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
                            'Parcel.Reference': '123456', # not mandatory
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
                            #'Parcel.ParcelService': [
                            #    {
                            #        'ParcelService.Servicecode': 'parcel service code'
                            #    },
                            #    {
                            #        'ParcelService.Servicecode': 'parcel service code 2'
                            #    },
                            #]
                        },
                        {
                            'Parcel.Reference': '123457',
                            'Parcel.Packagetype': 'PC',
                            'Parcel.Weight': {'weight_unit': 'kg', 'value': '1.2'},
                            'Parcel.Volume': {'unit': 'm3', 'value': '0.6'},
                            'Parcel.Infocode': '1012',
                            'Parcel.Contents': 'Muttereita ja puita',  # product description
                            'Parcel.ReturnService': '123',
                            # Customs declaration info (for medicine)
                            'Parcel.contentline': {},
                            #'Parcel.contentline': {
                            #    'contentline.description': 'Puita',
                            #    'contentline.quantity': 1,
                            #    'contentline.currency': 'EUR',
                            #    'contentline.netweight': 1,
                            #    'contentline.value': 100,
                            #    'contentline.countryoforigin': 'FI',
                            #    'contentline.tariffcode': '9608101000',
                            #},
                            # this is not really needed in Pakettikauppa but Prinetti
                            'Parcel.ParcelService': None
                        },
                    ]
                } #  end Shipment.Consignment
            }  # end Shipment
        }  # end eChannel
    }

    return dict_data


if __name__ == '__main__':
    # This uses testing data set
    # m = PkMerchant(1)
    # m.get_create_shipment_test_req_data()

    m = PkMerchant(1, API_KEY, SECRET)
    req_input = create_shipment_input_data(m)
    print("request input: {}".format(req_input))
    print("\n")

    _api_config = m.get_api_config('create_shipment')
    print("Hash config: {}".format(_api_config))
    print("\n")

    xml_string = m.get_xml_shipment_req_data(**req_input)
