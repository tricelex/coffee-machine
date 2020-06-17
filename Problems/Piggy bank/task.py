class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents > 99:
            mm = round(self.cents / 100)
            mn = self.cents % 100
            self.dollars += mm
            self.cents = mn
        # else:

        return f'{self.dollars} {self.cents}'


# mm = PiggyBank(1, 0)
# print(mm.add_money(0, 99))
