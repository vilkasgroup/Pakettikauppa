import sys
import unittest
import logging
from six.moves import reload_module

logging.basicConfig(
    level=logging.DEBUG,
)


class TestGeneral(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(__name__)

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_reloading_module(self):
        no_error = 1
        try:
            reload_module(sys)
        except Exception as e:
            no_error = 0
            self.logger.debug("Exception message = {}".format(e.exception))

        self.assertTrue(no_error)


if __name__ == '__main__':
    unittest.main(verbosity=2)

