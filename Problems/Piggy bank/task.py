class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, d_dollars, d_cents):
        self.dollars += d_dollars
        if self.cents + d_cents > 99:
            self.dollars += int((self.cents + d_cents) / 100)
            self.cents = (self.cents + d_cents) % 100
        else:
            self.cents += d_cents
