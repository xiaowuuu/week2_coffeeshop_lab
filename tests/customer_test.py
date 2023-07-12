import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Ying", 10)

    def test_customer_has_name(self):
        expect = "Ying"
        actual = self.customer.name
        self.assertEqual(expect, actual)

    def test_customer_wallet(self):
        expect = 10
        actual = self.customer.wallet
        self.assertEqual(expect, actual)
    
    
    