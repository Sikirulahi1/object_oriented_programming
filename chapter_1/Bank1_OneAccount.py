accountName = 'john'
accountBalance = 100
accountPassword = 'see'


while True:

    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit') 
    
    action = input('what do you want to do? ')
    action = action.lower()
    action = action[0] # USe the first letter
    
    
    # To get the account balance
    if action == 'b':
        print('Get Balance:')
        userInput = input('Enter your password:')
        if userInput == accountPassword:
            print(f"Your balance is ${accountBalance}")
        else:
            print("Invalid password")
    
    # To make deposit
    elif action == 'd':
        print('Make Deposit: ')
        userInput = input('Enter your password:')
        if userInput == accountPassword:
            userDeposit = int(input('Enter an amount to deposit:'))
            userPassword = input('Please enter the password: ')

            if userDeposit < 0:
                print('Invalid amount, value must be positive')
            elif userPassword != accountPassword:
                print("Invalid password")
            else:
                accountBalance += userDeposit
                print('Your new balance is:', accountBalance)

        else:
            print("Invalid password")
            
    
    # to withdraw
    elif action == 'w':
        print('Make Withdrawal: ')
        userInput = input('Enter your password:')
        if userInput == accountPassword:
            userWithdraw = int("Select an account to withdraw:")
            userPassword = input('Please enter the password: ')

            
            if userWithdraw > accountBalance:
                print('You cannot withdraw more than you have in your account')
            elif userWithdraw < 0:
                print('Invalid amount, value must be positive')
            elif userPassword != accountPassword:
                print('Invalid password')
            else:
                accountBalance -= userWithdraw
                print('Your new balance is:', accountBalance)

        else:
            print("Invalid password")
    
    
    # To show the account    
    elif action == 's':
        print("Show Account: ")
        userInput = input('Enter your password:')
        if userInput == accountPassword:
            print()
            print(f"Your account name is : {accountName}")
            print(f"Your account balance is : {accountBalance}")
            print(f"Your account password is : {accountPassword}")
            print()
        else:
            print("Invalid password")
        
    elif action == 'q':
        break
    else:
        print('Invalid action')

print('Done')