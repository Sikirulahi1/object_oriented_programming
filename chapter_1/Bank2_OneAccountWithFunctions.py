
accountName = ''
accountBalance = 0
accountPassword = ''


def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password
    
    def show():
        global accountName, accountBalance, accountPassword
        print(' Name', accountName)
        print(' Balance:', accountBalance)
        print(' Password:', accountPassword)
        print()




def getPassword(userPassword):
    global accountName, accountBalance, accountPassword
    userPassword = userPassword.copy()
    return userPassword

def getAccountBalance(userPassword):
    global accountName, accountBalance, accountPassword
    if userPassword == accountPassword:
        return accountBalance
    else:
        print('Invalid password')
        return None

def makeDeposit(userPassword, amountToDeposite):
    global accountName, accountBalance, accountPassword
    if amountToDeposite < 0:
        print("Negative number")
        return None
    if userPassword == accountPassword:
        accountBalance += amountToDeposite
        return accountBalance
    else:
        print("Invlid Password")
        return None

def withdraw(userPassword, amountToWithdraw):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < accountBalance:
        print("You cannot withdraw more than you have in your account")
        return None
    if amountToWithdraw < 0:
        print("Money must be positive")
        return None
    if userPassword == accountPassword:
            accountBalance -= amountToWithdraw
            return accountBalance
    else:
        print("Invlid Password")
        return None


newAccount("Joe", 100, 'soup') # create an account

while True:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    
    choice = input("What do you want to do? ")
    choice = choice.lower()
    choice = choice[0]
    
    print()
    
    if choice == "b":
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getAccountBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
        
    elif choice == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        newBalance = makeDeposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
            
    elif choice == 'q':
            break
    else:
        print('Invalid choice')
    
print("Done!!")
        