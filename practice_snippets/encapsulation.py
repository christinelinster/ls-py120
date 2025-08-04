class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if self._balance > amount and amount > 0:
            self._balance -= amount
            return True
        return False 
    
    def get_balance(self):
        return self._balance
    
    # This demonstrates encapsulation by hiding the internal _balance attribute while providing controlled access through 
    # public methods. The private attributes cannot be accessed directly from outside the class. 

    