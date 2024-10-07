# Klasse anlegen
class Account:
    # Konstruktor-Methode
    def __init__(self, account_nr, holder, balance):
        self.account_nr = account_nr
        self.holder = holder
        self.balance = balance
        self.sum_income = 0
        self.sum_expense = 0

    # Methode zum Einzahlen
    def income(self, value):
        self.value = value
        self.balance += self.value
        self.sum_income += self.value

    # Methode zum Auszahlen
    def expense(self, value):
        self.value = value
        self.balance -= self.value
        self.sum_expense += self.value

    def total_balance(self):
        return self.balance
    
    # def get_account_info(self):
    #     return f"Account-No: {self.account_nr}\nHolder: {self.holder}\nBalance: {self.balance}€"