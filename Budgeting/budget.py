
from operator import truediv


def create_spend_chart(categories):
    return None

class Category:
    def __init__ (self, name):
        self.name = name
        self.ledger = list()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output
    
    
    def deposit (self, amount, des = ""):
        """A deposit method that accepts an amount and description. 
        If no description is given, it should default to an empty string. 
        The method should append an object to the ledger list in the form of 
        {"amount": amount, "description": description}."""
        #self.ledger.append({"amount": amount, "description": des})
        status = False
        for item in self.ledger:
            if item["description"] == des:
                item["amount"] += amount
                status = True
        if (not status):
            self.ledger.append({"amount": amount, "description": des})

    def withdraw (self, amount, description = ""):
        """Positive amount passed in should be stored in the ledger as a negative number. 
        If there are not enough funds, nothing should be added to the ledger. 
        This method should return True if the withdrawal took place, and False otherwise."""
        if self.check_funds(amount):
            self.ledger.append({"amount" : -amount, "description": description})
            return True
        return False
    
    def get_balance (self):
        """A get_balance method that returns the current balance of the budget category 
        based on the deposits and withdrawals that have occurred."""
        total = 0
        for stuff in self.ledger:
            total += stuff["amount"]
        return total

    def transfer(self, amount, category):
        """Accepts an amount and another budget category as arguments. 
        Adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
        The method should then add a deposit to the other budget category with the amount and the description 
        "Transfer from [Source Budget Category]". 
        If there are not enough funds, nothing should be added to either ledgers. 
        This method should return True if the transfer took place, and False otherwise."""
        if (self.check_funds(amount)):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False


    def check_funds (self, amount):
        """Method that acc epts an amount as an argument. 
        It returns False if the amount is greater than the balance of the budget category 
        Returns True otherwise. 
        This method should be used by both the withdraw method and transfer method."""
        total = self.get_balance()
        if (amount > total):
            return False
        elif amount < 0:
            return False
        return True
    