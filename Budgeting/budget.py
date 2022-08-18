
from operator import truediv


def create_spend_chart(categories):
    return None

class Category:
    def __init__ (self, cgry):
        self.cgry = cgry
        self.ledger = list()
    
    def deposit (self, amount, des = ""):
        """A deposit method that accepts an amount and description. 
        If no description is given, it should default to an empty string. 
        The method should append an object to the ledger list in the form of 
        {"amount": amount, "description": description}."""
        #self.ledger.append({"amount": amount, "description": des})
        for cat in self.ledger:
            if 

    def withdraw (self, amount):
        """Positive amount passed in should be stored in the ledger as a negative number. 
        If there are not enough funds, nothing should be added to the ledger. 
        This method should return True if the withdrawal took place, and False otherwise."""
        if self.check_funds(amount):
            return True
        return False
    
    def get_balance (self):
        """A get_balance method that returns the current balance of the budget category 
        based on the deposits and withdrawals that have occurred."""
        total = 0
        for stuff in self.ledger:
            total += stuff["amount"]
        return total

    def check_funds (self, amount):
        """Method that accepts an amount as an argument. 
        It returns False if the amount is greater than the balance of the budget category 
        Returns True otherwise. 
        This method should be used by both the withdraw method and transfer method."""
        total = self.get_balance()
        if (amount > total):
            return False
        elif amount < 0:
            return False
        return True