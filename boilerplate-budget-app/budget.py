class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0

    def __repr__(self) -> str:
        pass


    def deposit(self, amount, description = ""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        enough_funds = self.check_funds(amount)

        if enough_funds : 
            self.balance -= amount
            self.ledger.append({"amount":  - amount, "description": description})

        return enough_funds

    def get_balance(self):
        return self.balance

    def transfer(self, amount, instance):
        enough_funds = self.check_funds(amount)

        if enough_funds : 
            self.withdraw(amount, f"Transfer to {instance.name}" )
            instance.deposit(amount,  f"Transfer from {self.name}" )

        return enough_funds

    def check_funds(self, amount):
        return False if self.balance < amount else True


def create_spend_chart(categories):
    pass