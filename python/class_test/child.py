from parent import Bank

class ChildBank(Bank):
    def __init__(self, money):
        super().__init__(money)
        self.money = money + 500