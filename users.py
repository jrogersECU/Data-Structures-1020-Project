import datetime
import LinkedList

# A class that represents a person/object.
# ALL code below works as desired. Ready For Use!
class Person:

    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password  # Hash for crypto example
        self.income = 0
        self.additional_income = 0
        self.expenses = 0
        self.total = self.income + self.expenses
        self.balance_after_expenses = self.income - self.expenses
        self.remaining_income = self.income + self.additional_income - self.expenses
        self.categories = {
            'Housing': 0,
            'Groceries': 0,
            'Transportation': 0,
            'Utilities': 0,
            'Dining': 0,
            'Entertainment': 0,
        }
        # TODO ********* REPLACE 'ARRAY_LOG' *************
        # REPLACE 'ARRAY_LOG' WITH Double-LinkedList
        # self.log = LinkedList()  # LinkedList used to store & read log entries
        def __init__(self, initial_data):
            self.data = initial_data
            self.next = None
        #self.log = LinkedList()=


    def __str__(self):
        # Returns a String representation of the selected person's name
        return self.name

    def add_log_entry(self, action):

        # A Dictionary of user attributes
        log_data = {
            'key': len(self.array_log) + 1,
            'action': action,
            'date_time': str(datetime.datetime.now()),
            'name': self.name,
            'age': self.age,
            'balance': self.income,
            'additional_income': self.additional_income,
            'full_balance': self.income - self.expenses,
            'expenses': self.expenses,
            # 'use_percentage': self.get_use_percentage(),
            'categories': self.categories
        }
        # TODO ********* APPEND TO Double-LinkedList *************
        # REPLACE 'ARRAY_LOG.APPEND' WITH Double-LinkedList.APPEND
        LinkedList.append

    def add_category_funds(self, category=str, amount=int):
        # If users income/unused funds are >= amount requested, transfer funds to category
        if self.income >= amount:
            print(f'Adding funds to "{category}", Amount: {amount}')
            self.categories[f'{category}'] += amount
            self.expenses += amount
            self.income -= amount
            print(f'Updated "{category}" category in the amount: {amount}. Updated income : {self.income}\n')

        else:
            print('Sorry, but the amount you entered is more than account balance.')
            print('Please try again...')
        print(f"Category : {category}\nAmount : +${self.categories[f'{category}']}\n\n")

    def decrease_category_funds(self, category=str, amount=int):
        # If users income/unused funds are >= amount requested, transfer funds to category
        if int(amount) <= self.expenses:
            print(f'Decreasing funds to "{category}", Amount: ${amount}')
            self.categories[f'{category}'] -= amount
            self.expenses -= amount
            self.income += amount
            print(f'Updated "{category}" category in the amount: {amount}. Updated income : ${self.income}\n')

        else:
            print('Sorry, but the amount you entered is more than your "expenses" balance.')
            print('Please try again...')
        print(f"Category : {category}\nDecreased Amount : -${amount}\n\n")

    def add_custom_category(self, category=str, amount=int):
        self.categories[f'{category}'] = amount
        print(f"Added Category : {category}\nAmount : +${self.categories[f'{category}']}\n\n")

    def remove_category(self, category=str):
        # Grab soon to be deleted data before erasing
        transferred = self.categories[f'{category}']
        del self.categories[f'{category}']
        self.income += transferred

        print(f"Deleted Category : {category}\nAmount Transferred to Income : -${transferred}")

    def transfer_category_funds(self, to_category=str, from_category=str, amount=int):
        # If the category searched exists
        if self.categories[f'{from_category}'] >= amount:
            # If users income/unused funds are >= amount requested, transfer funds to category,
            # Decrease income amount by amount requested.
            self.categories[f'{to_category}'] += amount
            self.categories[f'{from_category}'] -= amount
            print(f"Transferred ${amount}, from {from_category} to {to_category}")
        else:
            print(f'Category amount is less than amount requested, try again...')

    def transfer_all_category_funds(self, to_category=str, from_category=str):
        # If to_category and from_category exist in dictionary, transfer_category_funds.
        if self.categories[f'{to_category}'] and self.categories[f'{from_category}']:
            value = self.categories[f"{from_category}"]
            # print(f"{self.categories[f'{to_category}']}\n\n{self.categories[f'{to_category}']}\n\n")
            # If from_category's value is greater than zero, transfer_category_funds.
            # Add from_category's value to to_category's value
            # Subtract from_category's value from from_category's value
            if self.categories[f'{from_category}'] >= 1:
                self.categories[f'{to_category}'] += self.categories[f'{from_category}']
                self.categories[f'{from_category}'] -= self.categories[f'{from_category}']
                print(f'Transferred ${value}, from {from_category} to {to_category}')
            else:
                print('Zero funds in category transferring *from, try again...')
        else:
            print('Unable to find either category, try again')

    # TODO ********* Interate Through 'log' Double-LinkedList *************
    def print_logs(self):
        print('<-----------------------------------  DATA LOGS  --------------------------------------------->\n')
        # REPLACE ARRAY FOR-LOOP WITH 'log' Double-LinkedList FOR-LOOP
        for log in self.array_log:
            print(log)

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
        self.add_log_entry('Added Expenses')

    def get_balance(self):
        # Returns the 'total balance' -> ( Balance - Expenses )
        print(f'Balance after get_balance function : \n{self.income - self.expenses}\n')
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        self.add_log_entry('Requested Balance')
        return self.balance_after_expenses

    # def get_use_percentage(self):
    #     # Returns the 'total balance' -> ( Income - Expenses )
    #     total = None
    #     if self.expenses > 0:
    #         total = self.expenses / self.income
    #         print(f'"Percentage of Use" after get_use_percentage function : \n{total * 100} %\n')
    #         # Updates the log with a new entry and action used Ex.'Deposited Money'
    #         self.add_log_entry('Requested Use %')
    #     else:
    #         print('You currently have zero expenses...')
    #         # Updates the log with a new entry and action used Ex.'Deposited Money'
    #         self.add_log_entry('Requested Use %')
    #
    #     return total

    def print_category(self, category):
        print(f"{category} : {self.categories[category]}\n\n")
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        self.add_log_entry('Requested Category Value.')

    def print_all_info(self):
        # Updates the log with a new entry and action used Ex.'Deposited Money'
        self.add_log_entry('Requested All Info.')
        # Print all attributes of a Person
        print(f'\nName : {self.name}')
        print(f'Age : {self.age}')
        print(f'Total : {self.total}')
        print(f'Income : {self.income}')
        print(f'Expenses : {self.expenses}')
        print(f'Balance Remaining After Expenses : {self.income - self.expenses}')
        print(f'Expenses :')
        for category, value in self.categories.items():
            print(f'    {category.capitalize()} : {value}')
        print('\n\n')
