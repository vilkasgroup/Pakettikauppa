import unittest
from pakettikauppa.merchant import decode_pdf_content, PkMerchant


class TestGeneral(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._merchant = PkMerchant(1)

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_empty_api_key(self):
        with self.assertRaises(Exception):
            merchant = PkMerchant(0, None, 'test')

    def test_empty_secret_key(self):
        with self.assertRaises(Exception):
            merchant = PkMerchant(0, 'test', None)

    def test_create_merchant_object_in_live(self):
        creation_ok = 1
        try:
            merchant = PkMerchant(0, 'test api', 'test secret')
        except Exception:
            creation_ok = 0

        self.assertIs(creation_ok, 1)

    def test_empty_pdf_content(self):
        with self.assertRaises(ValueError):
            decoded_pdf_content_string = decode_pdf_content('')

    def test_invalid_api_name_call(self):
        with self.assertRaises(Exception):
            h_config = self._merchant.get_api_config('list_customer')

    def test_get_api_conf(self):
        h_config = self._merchant.get_api_config('get_shipping_method_list')
        self.assertIsNotNone(h_config)


if __name__ == '__main__':
    unittest.main(verbosity=2)

