class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink_to_buy):
        self.wallet -= drink_to_buy.price