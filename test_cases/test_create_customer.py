import logging
import unittest
# from unittest import TestCase
from pakettikauppa_app.reseller import PkReseller

logging.basicConfig(
    level=logging.DEBUG,
)


class TestPkReseller(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._reseller = PkReseller(1)
        cls.logger = logging.getLogger(__name__)

    def test_empty_parameter(self):
        with self.assertRaises(Exception) as e:
            self._reseller.create_customer(**{})
        #self.logger.debug("Exception message = {}".format(e.exception.message))

    def test_too_short_parameter(self):
        self._reseller.create_customer(**{
            'name': 'Vilkas Group Oy Test',
        })

    def test_invalid_key(self):
        with self.assertRaises(KeyError):
            self._reseller.create_customer(**{
                'address2': 'Some street extension'
            })

    def test_create_customer(self):
        self.fail()


if __name__ == '__main__':
    unittest.main(verbosity=2)