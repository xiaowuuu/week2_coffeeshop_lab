import unittest
from src.coffee_shop import CoffeeShop

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100)

    def test_coffee_shop_has_name(self):
        expected = "The Prancing Pony"
        actual = self.coffee_shop.name
        self.assertEqual(expected, actual)

    # @unittest.skip("delete this line to run the test")
    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_increase_till(self):
        self.coffee_shop.change_till_by_amount(10)
        self.assertEqual(110, self.coffee_shop.till)

    
    def test_descrease_till(self):
        self.coffee_shop.change_till_by_amount(-10)
        self.assertEqual(90, self.coffee_shop.till)

    def test_sold_drink(self):
        expected = ("Latte", 3)
        actual = self.coffee_shop.drinks  
        self.assertEqual(expected, actual)