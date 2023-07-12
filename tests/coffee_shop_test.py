import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):
    
    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100)
        self.latte = Drink("Latte", 3)
        self.ying = Customer("Ying", 10, 30)


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
        
        self.coffee_shop.sell_drink(self.latte, self.ying)
        self.assertEqual(103, self.coffee_shop.till)
        self.assertEqual(7, self.ying.wallet)