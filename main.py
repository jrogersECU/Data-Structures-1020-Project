from users import Person

# Create a new Person entry in the database
Person_1 = Person('Mutulu', 10, 12345)

# Deposit PayCheck
Person_1.add_pay_check(1000)
# Deposit PayCheck
Person_1.add_pay_check(75)

# Add Expense
Person_1.add_expense(200)
# Add Expense
Person_1.add_expense(23)
# Request Balance
Person_1.get_balance()

# Request All User Data
Person_1.print_all_info()

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
