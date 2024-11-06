
class Bank:
    
    def __init__(self, accountHolder, balance, deposit, withdraw):
        self.balance = balance
        self.accountHolder = accountHolder

    def getBalance(self):
        return self.balance
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getHolder(self):
        return self.accountHolder
    


def main():
    balance = 0
    accountHolder = "Matthew Poole"
    deposit = 0
    withdraw = 0

    bank = Bank(accountHolder, balance, deposit, withdraw)
    
    print("The name of the account holder is", bank.getHolder())
    print(f"The initial balance of the account is £{bank.getBalance()}")
    bank.deposit(100)
    print(f"After depositing £100, the balance is £{bank.getBalance()}")
    bank.withdraw(50)
    print(f"After withdrawing £50, the balance is £{bank.getBalance()}")
    bank.withdraw(100)
    print(f"After trying to withdraw £100, the balance is £{bank.getBalance()}")
    print(f"Account name: {bank.getHolder()}")
    print(f"Balance: £{bank.getBalance()}")

main()



