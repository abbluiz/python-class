def checkEnteredPin(correctPin, enteredPin):
    return (correctPin == enteredPin)

def withdrawl(currentBalance, withdrawlAmount):

    if (currentBalance - float(withdrawlAmount)) < 0.00:
        return currentBalance
    else:
        return (currentBalance - float(withdrawlAmount))

def didUserEnteredValidWithdrawlOption(option):

    validOptions = [10, 20, 40, 60, 80, 100]

    if option in validOptions:
        return True
    
    return False

def displayMainMenu():
    print("\nPress 1 for your balance")
    print("Press 2 to make a withdrawl")
    print("Press 3 to deposit")
    print("Press 4 to return card\n")

def displayWithdrawlMenu():
    print("\nWithdrawl Options")
    print("$10")
    print("$20")
    print("$40")
    print("$60")
    print("$80")
    print("$100\n")

def displayBalance(balance):
    print("\nYour balance is now $" + str(balance) + "\n")

def displaySignOutMessage():
    print("Have a nice day, we are signing you out...\n")

def doesUserWantToLeave():
    
    yesOrNo = input("Would you like to go back to the main menu? (yes/no) ")
    
    if yesOrNo == "yes":
        return False

    return True

correctPin = "0343"
currentBalance = 100.0

print("\nWelcome to Humber Bank ATM")

while True:

    for i in range(0, 4):

        enteredPin = input("Please enter your 4-digit PIN: ")

        isPinCorrect = checkEnteredPin(correctPin, enteredPin)

        if not isPinCorrect:
            print("Incorrect PIN\n")
        else:
            print("Authentication successful\n")
            break

    if not isPinCorrect:
        quit("No more tries left, system shutting down...\n")

    while True:

        displayMainMenu()

        option = int(input("Please enter your option: "))

        if option == 1:
            
            displayBalance(currentBalance)

            if doesUserWantToLeave():
                displaySignOutMessage()
                break
            else:
                continue

        elif option == 2:

            displayWithdrawlMenu()
            withdrawlAmount = int(input("How much would you like to withdrawl? (1 for custom amount) "))

            if (withdrawlAmount == 1):

                customAmount = float(input("Please enter custom amount: "))

                currentBalance = withdrawl(currentBalance, customAmount)
                displayBalance(currentBalance)

            elif didUserEnteredValidWithdrawlOption(withdrawlAmount):

                currentBalance = withdrawl(currentBalance, withdrawlAmount)
                displayBalance(currentBalance)

            else:

                print("Invalid withdrawl option, please retry later.")
                continue

            if doesUserWantToLeave():
                displaySignOutMessage()
                break
            else:
                continue

        elif option == 3:

            depositAmount = float(input("How much would you like to deposit? "))

            currentBalance += depositAmount

            displayBalance(currentBalance)

            if doesUserWantToLeave():
                displaySignOutMessage()
                break
            else:
                continue

        elif option == 4:

            print("Returning your card, please wait...")

            displaySignOutMessage()
            break

