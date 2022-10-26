
# *** Not Properly Coded, Not Ready For Use ***
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.node = TransactionNode()

    def add_transaction_node(self, data):
        # If LinkedList is empty, then add data to both head and tail nodes
        if self.log.head == None and self.log.tail == None:
            self.log.head == data
            self.log.tail == data
        elif self.log.head and self.log.tail:
            self.log.tail = data


# *** Not Properly Coded, Not Ready For Use ***
class TransactionNode:
    # Pointers for a Double-LinkedList
    def __init__(self):
        self.data = None
        self.next = None
        self.previous = None


# A class that represents a person/object.
# ALL code below works as desired. Ready For Use!
class Person:

    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password
        self.balance = 0
        self.additional_income = 0
        self.expenses = 0
        self.balance_after_expenses = self.balance - self.expenses
        self.remaining_income = self.balance + self.additional_income - self.expenses
        self.log = LinkedList()  # LinkedList used to store & read log entries

    def __str__(self):
        # Returns a String representation of the selected person's name
        return self.name

    def add_pay_check(self, amount):
        # Prints the current balance
        print(f'Previous Balance : {self.balance}')
        # Adds current 'balance' with 'input amount'
        self.balance += amount
        # Prints the new 'balance'
        print(f'Updated Balance : {self.balance}\n')

    def add_expense(self, amount):
        # Prints the current 'expenses' amount
        print(f'User added {amount} to their account\n')
        print(f'Previous Expenses : {self.expenses}')
        # Adds current 'expenses' with 'input amount'
        self.expenses += amount
        # Prints the new 'expenses' amount
        print(f'Updated Expenses : {self.expenses}\n')

    def additional_pay(self, add_income):
        # Prints the current 'balance'
        print(f'Previous Balance : {self.balance}')
        # Prints the current 'additional income' value
        print(f'Previous Additional Income : {self.additional_income}\n')
        # Adds current 'balance' with 'additional income' amount
        self.balance += add_income
        # Adds the current 'additional income' amount with the 'input amount'
        self.additional_income += add_income
        # Prints the new 'balance'
        print(f'Updated Balance : {self.balance}')
        # Prints the new 'additional income' amount
        print(f'Updated Additional Income : {self.additional_income}\n')

    def get_balance(self):
        # Returns the 'total balance' -> ( Balance - Expenses )
        print(f'Balance after get_balance function : \n{self.balance}\n')
        return self.balance_after_expenses

    def get_use_percentage(self):
        # Returns the 'total balance' -> ( Balance - Expenses )
        total = None
        if self.expenses != 0:
            total = self.expenses / self.balance
        else:
            total = -1
        print(f'"Percentage of Use" after get_use_percentage function : \n{total * 100} %\n')
        return total

    def print_all_info(self):
        # Print all attributes of a Person
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')
        print(f'Balance : {self.balance}')
        print(f'Additional Income : {self.additional_income}')
        print(f'Full Balance : {self.balance + self.additional_income}')
        print(f'Expenses : {self.expenses}')
        print(f'Balance Remaining After Expenses : {self.balance - self.expenses}')
