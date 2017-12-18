import unittest
from pakettikauppa_app.reseller import PkReseller


class TestUpdateCustomer(unittest.TestCase):
    a_reseller = PkReseller(1)

    def test_skip_passing_customer_id(self):
        with self.assertRaises(TypeError):
            self.a_reseller.update_customer()

        # with self.assertRaises(Exception) as context:
        #    self.a_reseller.update_customer()
        #    print(context.exception)
        #
        # self.assertTrue('This is broken' in str(context.exception))
    def test_passing_empty_customer_id(self):
        print("Test passing empty string to customer id parameter")
        with self.assertRaises(Exception):
            self.a_reseller.update_customer('')
        print(Exception)

    def test_passing_wrong_args_type(self):
        with self.assertRaises(TypeError):
            self.a_reseller.update_customer(123, {})

    def test_passing_empty_update_dict(self):
        self.assertIsNone(self.a_reseller.update_customer(123, **{}))

    def test_passing_invalid_key(self):
        with self.assertRaises(Exception):
            self.a_reseller.update_customer(123, **{ 'vat_id': 'FI12345-6'})
        #self.a_reseller.update_customer(123, **{'vat_id': 'FI12345-6'})

    def test_passing_valid_key(self):
        input_data = {'marketing_name': 'My super cool company'}
        self.assertTrue(self.a_reseller.get_update_customer_req_data(123, **input_data))


if __name__ == '__main__':
    unittest.main(verbosity=2)
