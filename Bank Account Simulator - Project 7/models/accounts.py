class Account():
    """Creating the main parent class for accounts with the main functions"""
    def __init__(self, account_id, name, balance=0.0):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    #Creating a method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    #Creting a method to withdraw money from the account
    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance-=amount
            return True
        return False
    
    def get_account_info(self):
        return {
            "account_id": self.account_id,
            "name": self.name,
            "balance": self.balance
        }
    
    def __str__(self):
        return f"Account({self.account_id}, {self.name}, Balance: {self.balance})"
    
    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False
    

class SavingsAccount(Account):
    "Creating a child class for savings account inheriting from Account"
    def __init__(self, account_id, name, balance=0.0, interest_rate=0.01):
        super().__init__(account_id, name, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return interest
    def __str__(self):
        return f"SavingsAccount ID: {self.account_id}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"
    
class CheckingAccount(Account):
    """Creating the CheckingAccount class inheriting from Account"""
    def __init__(self, account_id, balance=0, overdraft_limit=0):
        super().__init__(account_id, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False
    def __str__(self):
        return f"CheckingAccount ID: {self.account_id}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}"
    
    
    

    