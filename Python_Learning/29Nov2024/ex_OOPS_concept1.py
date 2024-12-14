class Account:

    def __init__(self, balance, accountNo):
        self.balance = balance
        self.accountNo = accountNo

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs", amount, "was debited", "from account", self.accountNo)
        print("total balance = ",self.get_balance())

    def credit(self, amount):
            self.balance = self.balance + amount
            print("Rs", amount, "was credited", "to account", self.accountNo)
            print("total balance = ",self.get_balance() )

    def get_balance(self):
        return self.balance

acc1 = Account(100000, 123456565)
acc1.debit(2000)
acc1.credit(3000)

