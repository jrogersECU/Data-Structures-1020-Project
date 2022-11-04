from users import Person
import datetime
date = str(datetime.date.today())

# Create a new Person entry in the database
Person_1 = Person('Mutulu Shakur', 10, 12345)
Person_2 = Person('Ricky Bobby', 42, 42069)
def begin_budget():
    # WELCOME MESSAGE (START OF PROGRAM)
    print("****************************************************************************")
    print("*                                                                          *")
    print("*                   Welcome to Bloodhound Budgets!                         *")
    print("*                                                                          *")
    print("****************************************************************************")

    # Request User-Account PIN
    entered_pin = (input('Please Enter Your PIN Below to Get Started: \n')).strip()
    if entered_pin == '1':

        # Display user-name & date
        date = str(datetime.date.today())
        print(Person_1, f"{date:8s}")

        # Display Divider
        print('-' * 35)

        # User Commands
        print(f'{"0 : Deposit":20} {"1 : Withdraw":16s}')
        print(f'{"2 : Get Balance":20s} {"3 : Transfer":16s}')  # Changed "Transfer" to "Withdraw"
        print(f'{"4 : Get Funds":20s}\n')
        user_input = input('Enter your selection:\n').strip().lower()
        print('\n\n\n\n\n')

        if user_input != 'exit':
            if user_input == '0' or user_input.lower() == 'Deposit':
                print("unfinished")




    elif entered_pin == '2':
        date = str(datetime.date.today())
        print(Person_2, f"{date:8s}")

        # Display Divider
        print('-' * 35)

        # User Commands
        print(f'{"0 : Deposit":20} {"1 : Withdraw":16s}')
        print(f'{"2 : Get Balance":20s} {"3 : Transfer":16s}')  # Changed "Transfer" to "Withdraw"
        print(f'{"4 : Get Funds":20s}\n')

    else:
        print("Sorry, invalid PIN")





#Person_1.add_pay_check(1000)
# Deposit PayCheck
#Person_1.add_pay_check(75)

# Add Expense
#Person_1.add_expense(200)
# Add Expense
#Person_1.add_expense(23)

# Request Balance
#Person_1.get_balance()

# Request All User Data
#Person_1.print_all_info()
#Person_2.print_all_info()

# Request Usage Percentage
#Person_1.get_use_percentage()

begin_budget()
