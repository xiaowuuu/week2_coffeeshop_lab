import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.coffee = Drink("Black coffee", 3.95)
        
    def test_drink_has_name(self):
        expect = "Black coffee"
        actual = self.coffee.name
        self.assertEqual(expect, actual)
    
    def test_drink_has_price(self):
        self.assertEqual(3.95, self.coffee.price)


    