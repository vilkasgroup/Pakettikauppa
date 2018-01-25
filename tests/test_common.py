import unittest
from pakettikauppa.merchant import decode_pdf_content, PkMerchant


class TestGeneral(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_empty_pdf_content(self):
        with self.assertRaises(ValueError):
            decoded_pdf_content_string = decode_pdf_content('')

    def test_get_api_conf(self):
        merchant = PkMerchant(1)
        h_config = merchant.get_api_config('list_customer')
        self.assertIsNotNone(h_config)


if __name__ == '__main__':
    unittest.main(verbosity=2)

