class Bank():
    def __init__(self, money):
        self.money = money

    def deposit(self, price):
        self.money += price
        print(self.money)

    def draw(self, price):
        self.money -= price
        print(self.money)
    