# *** Not Properly Coded, Not Ready For Use ***
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.node = TransactionNode()

    def add_transaction_node(self, new_node):
        # If LinkedList is empty, then add data to both head and tail nodes
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node


# *** Not Properly Coded, Not Ready For Use ***
class TransactionNode:
    # Pointers for a Double-LinkedList
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


# A class that represents a person/object.
# ALL code below works as desired. Ready For Use!
class Person:

    # TODO Move funds between different categories
    # TODO Implement a class of categories wich can be combined or printed

    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password
        self.income = 0
        self.additional_income = 0
        self.expenses = 0
        self.balance_after_expenses = self.income - self.expenses
        self.remaining_income = self.income + self.additional_income - self.expenses
        self.categories = {
            'Housing': None,
            'Groceries': None,
            'Transportation': None,
            'Utilities': None,
            'Dinning': None,
            'Entertainment': None,
        }
        self.log = LinkedList()  # LinkedList used to store & read log entries
        self.array_log = []

    def __str__(self):
        # Returns a String representation of the selected person's name
        return self.name

    def add_log_entry(self, action):
        log_count = 0
        # TODO -> Add date/time attribute to log_data
        # A Dictionary of user attributes
        log_data = {
            'key': log_count + 1 if log_count > 0 else 1,
            'action': action,
            'name': self.name,
            'age': self.age,
            'balance': self.income,
            'additional_income': self.additional_income,
            'full_balance': self.income - self.expenses,
            'expenses': self.expenses,
            'use_percentage': self.get_use_percentage(),

            'categories': self.categories
        }
        # self.log.add_transaction_node(log_data)
        log_count += 1
        self.array_log.append(log_data)

    def add_category_funds(self, category=str, amount=int):
        # If the category searched exists
        if self.categories[f'{category}']:
            # If users income/unused funds are >= amount requested, transfer funds to category,
            # Decrease income amount by amount requested.
            if self.income >= int(amount):
                self.categories[f'{category}'] += amount
                self.income -= amount
        print(f"Category : {category}\nAmount : $ +{self.categories[f'{category}']}")

    def decrease_category_funds(self, category=str, amount=int):
        # If the category searched exists
        if self.categories[f'{category}'] >= amount:
            # If users income/unused funds are >= amount requested, transfer funds to category,
            # Decrease income amount by amount requested.
            self.income += amount
            self.categories[f'{category}'] -= amount
            print(f"Decreased {category} expense by ${amount}")
        else:
            print(f'Category amount {amount}')
            print(f'Category amount is less than amount requested, try again...')

    def add_custom_category(self, category=str, amount=int):
        self.categories[f'{category}'] = amount
        print(f"Added Category : {category}\nAmount : $ +{self.categories[f'{category}']}")

    def remove_category(self, category=str):
        transferred = self.categories[f'{category}']
        if self.categories[f'{category}']:
            self.income += self.categories[f'{category}']
        del self.categories[f'{category}']
        print(f"Deleted Category : {category}\nAmount Transferred to Income : $ {transferred}")

    def transfer_category_funds(self, to_category=str, from_category=str, amount=int):
        # If the category searched exists
        if self.categories[f'{from_category}'] >= amount:
            # If users income/unused funds are >= amount requested, transfer funds to category,
            # Decrease income amount by amount requested.
            self.categories[f'{to_category}'] += amount
            self.categories[f'{from_category}'] -= amount
            print(f"Transferred ${amount} from {from_category} to {to_category}")
        else:
            print(f'Category amount is less than amount requested, try again...')

    def transfer_all_category_funds(self, to_category=str, from_category=str):
        # If to_category and from_category exist in dictionary, transfer_category_funds.
        if self.categories[f'{to_category}'] and self.categories[f'{from_category}']:
            # If from_category's value is greater than zero, transfer_category_funds.
            # Add from_category's value to to_category's value
            # Subtract from_category's value from from_category's value
            if self.categories[f'{from_category}'] >= 1:
                self.categories[f'{to_category}'] += self.categories[f'{from_category}']
                self.categories[f'{from_category}'] -= self.categories[f'{from_category}']
                print(self.categories[f'{from_category}'])
                print(self.categories[f'{to_category}'])
                print(f'Transferred [amount] from {from_category} to {to_category}')
            else:
                print('Zero funds in category transferring *from, try again...')
        else:
            print('Unable to find either category, try again')

    # TODO Create a function to add additional custom categories
    # TODO Create a function to handle addition of expense for a category value
    # TODO Create a function to handle decrease of expense for a category value

    def print_logs(self):
        while self.log.head:
            print(f'{self.log.head.data}')
            self.log.head = self.log.head.next
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        self.add_log_entry('Printed Log Entries')

    def add_pay_check(self, amount):
        # Prints the current balance
        print(f'Previous Balance : {self.income}')
        # Adds current 'balance' with 'input amount'
        self.income += amount
        # Prints the new 'balance'
        print(f'Updated Balance : {self.income}\n')
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        self.add_log_entry('Deposited Money Into Account')

    def add_expense(self, amount):
        # Prints the current 'expenses' amount
        print(f'User added {amount} to their account\n')
        print(f'Previous Expenses : {self.expenses}')
        # Adds current 'expenses' with 'input amount'
        self.expenses += amount
        # Prints the new 'expenses' amount
        print(f'Updated Expenses : {self.expenses}\n')
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        self.add_log_entry('Updated Expenses')

    def get_balance(self):
        # Returns the 'total balance' -> ( Balance - Expenses )
        print(f'Balance after get_balance function : \n{self.income}\n')
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        self.add_log_entry('Requested Balance')
        return self.balance_after_expenses

    def get_use_percentage(self):
        # Returns the 'total balance' -> ( Income - Expenses )
        total = None
        if self.expenses > 0:
            total = self.expenses / self.income
            print(f'"Percentage of Use" after get_use_percentage function : \n{total * 100} %\n')
        else:
            print('You currently have zero expenses...')
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        # self.add_log_entry('Requested Percentage Use')
        return total

    def print_all_info(self):
        # Print all attributes of a Person
        print(f'\nName : {self.name}')
        print(f'Age : {self.age}')
        print(f'Income : {self.income}')
        print(f'Expenses : {self.expenses}')
        print(f'Balance Remaining After Expenses : {self.income - self.expenses}')
        print(f'Expenses :')
        for category, value in self.categories.items():
            print(f'    {category.capitalize()} - {value}')
        print('\n\n')
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        self.add_log_entry('Requested All Info.')
