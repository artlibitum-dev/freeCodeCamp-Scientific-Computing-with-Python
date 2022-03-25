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
            list_line += f"{item['description'][:23] :<23}{item['amount'] :>7.2f}\n"
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
    category_list = {}
    key_length = 0
    key_list = []

    for category in categories:
        category_total = 0
        for item in category.ledger:
            amount = int(item['amount'])
            if amount < 0:
                category_total += abs(amount)
        category_list[str(category.name)] = int(category_total)
    
    total = sum(category_list.values())

    # category_list = dict(map(lambda item: (item[0], int((item[1] / total) *100), category_list.items()))
    for key, value in category_list.items():
        key_length = len(key) if key_length < len(key) else key_length
        key_list.append([key])
        category_list[key] = int((value / total) *100)

    title_line =f"Percentage spent by category\n"
    scale_line = ""
    split_line = ""
    footer_line = ""

    for range_label in range(100, -1, -10):
        scale_line += f"{range_label:>3}|" 
        for key, value in category_list.items(): 
            scale_line += f"{'o':^3}" if value >= range_label else f"{'':^3}"
        scale_line += " \n"

    split_line = f"{'':>4}{'-' *(len(category_list) *3)}-\n" 

    for ix in range(key_length):
        footer_line += f"{'':>4}"
        for key in category_list.keys():
            footer_line += f"{key[ix]:^3}" if len(key) > ix else f"{'':^3}"
        footer_line += f" \n"

    return title_line + scale_line + split_line + footer_line[:-1]