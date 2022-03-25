class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0

    def __repr__(self) -> str:
        title_line =f"{self.name:*^30}\n"
        list_line = ""
        total = 0.0

        for item in self.ledger:
            list_line += f"{item['description'][:23] :<23}{item['amount'][:7] :>7.2f}\n"
            total += item['amount']

        total_line = f"Total: {total:.2f}"

        return title_line + list_line + total_line



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