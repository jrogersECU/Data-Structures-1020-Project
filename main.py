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
        # Added slot for transaction
        # log and exit
        print(f'{"0 : Deposit":20} {"1 : Withdraw":16s}')
        print(f'{"2 : Get Balance":20s} {"3 : Transfer":16s}')
        print(f'{"4 : Get Funds":20s} {"5 : View Transaction Log"}')
        print(f'{"6 : Exit":20s}\n')

        #Ask User for next input
        # Added groundwork for the user functions
        user_input = input('Enter your selection:\n').strip().lower()
        print('\n\n\n\n\n')

        if user_input != 'exit':
            if user_input == '0' or user_input.lower() == 'Deposit':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '1' or user_input.lower() == 'Withdraw':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '2' or user_input.lower() == 'Get Balance':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '3' or user_input.lower() == 'Transfer':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '4' or user_input.lower() == 'Get Funds':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '5' or user_input.lower() == 'View Transaction Log':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '6' or user_input.lower() == 'Exit':
                print("Thank you for choosing Bloodhound Budgets!")
                # reset program
                begin_budget()




    elif entered_pin == '2':
        date = str(datetime.date.today())
        print(Person_2, f"{date:8s}")

        # Display Divider
        print('-' * 35)

        # User Commands
        # Added slot for transaction log and exit
        print(f'{"0 : Deposit":20} {"1 : Withdraw":16s}')
        print(f'{"2 : Get Balance":20s} {"3 : Transfer":16s}')
        print(f'{"4 : Get Funds":20s} {"5 : View Transaction Log"}')
        print(f'{"6 : Exit":20s}\n')

        # Ask User for next input
        # Added groundwork for the user functions
        user_input = input('Enter your selection:\n').strip().lower()
        print('\n\n\n\n\n')

        if user_input != 'exit':
            if user_input == '0' or user_input.lower() == 'Deposit':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '1' or user_input.lower() == 'Withdraw':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '2' or user_input.lower() == 'Get Balance':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '3' or user_input.lower() == 'Transfer':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '4' or user_input.lower() == 'Get Funds':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '5' or user_input.lower() == 'View Transaction Log':
                print("unfinished please press 1 to return to main program")
                user_input = input()
                # reset program
                if user_input == '1':
                    begin_budget()

            if user_input == '6' or user_input.lower() == 'Exit':
                print("Thank you for choosing Bloodhound Budgets!")
                # reset program
                begin_budget()

    else:
        #Added user command to restart program on invalid input
        print("Sorry, invalid PIN, press 1 to restart")
        user_input = input()
        if user_input == '1':
            begin_budget()






#Person_1.add_pay_check(1000)
# Deposit PayCheck
#Person_1.add_pay_check(75)

# Add Expense
#Person_1.add_expense(200)
# Add Expense

Person_1.add_expense(23)


# Request Balance
#Person_1.get_balance()

# Request All User Data
#Person_1.print_all_info()
#Person_2.print_all_info()

# Add Category Funds
Person_1.add_category_funds('Housing', 331)
# Decrease Category Funds
Person_1.decrease_category_funds('Housing', 300)
# Display Category Value
Person_1.print_category('Housing')
# Create Additional Category
Person_1.add_custom_category('Dating', 100_000)
# Transfer Category to Category Funds
Person_1.transfer_category_funds('Housing', 'Dating', 10_000)
# Transfer All Category Funds
Person_1.transfer_all_category_funds('Housing', 'Dating')
# Display All Person's Info
Person_1.print_all_info()
# Display Person's Log
Person_1.print_logs()

Request Usage Percentage
Person_1.get_use_percentage()

begin_budget()

