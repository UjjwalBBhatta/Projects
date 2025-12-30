from src.transaction_history import add_transaction

class Account():
    """Creating the main parent class Account"""
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
    # Now we require a category when depositing
    def deposit(self, amount, category="General"):
        if amount > 0:
            self.balance += amount
            add_transaction(amount, category, f"Deposit to {self.account_id}")
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            # Pass the Category and Description!
            add_transaction(amount, "Withdrawal", f"Withdrew from {self.account_id}")
            return True
        return False
    def get_balance(self):
        return self.balance
    def get_account_id(self):
        return self.account_id
    def __str__(self):
        return f"Account ID: {self.account_id}, Balance: {self.balance}"
    def transfer(self, target_account, amount):
        if self.withdraw(amount): 
            target_account.deposit(amount, "Transfer") 
            return True
        return False
    def card_linked(self, card_number):
        # Placeholder for card linking logic
        return True
    

class SavingsAccount(Account):
    """Creating the SavingsAccount class inheriting from Account"""
    def __init__(self, account_id, balance=0, interest_rate=0.02):
        super().__init__(account_id, balance)
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
            add_transaction(amount, "Withdrawal", f"Overdraft Withdrawal {self.account_id}")
            return True
        return False
    def __str__(self):
        return f"CheckingAccount ID: {self.account_id}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}"
    

    