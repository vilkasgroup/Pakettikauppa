import unittest
from pakettikauppa.merchant import decode_pdf_content


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
            decode_pdf_content('')


if __name__ == '__main__':
    unittest.main(verbosity=2)

