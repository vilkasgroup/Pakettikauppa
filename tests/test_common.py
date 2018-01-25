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

