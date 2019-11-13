# 1, 2

def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    
    if (y == 0.0):
        raise ZeroDivisionError("Division by zero is impossible.")
    else:
        return x / y

def getNumberInput (message):
    try:
        return float(input(message))
    except ValueError:
        print("ERROR: That is not a valid number. Exiting script...")
        exit()

def quitCalc():
    print("Goodbye! Thanks for using this script.")
    exit()

option=""

while option != "quit":

    print("\nPython Calculator")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("quit) Quit calculator\n")
    option = input("Enter you option: ")

    if option != "quit":
        x = getNumberInput("\nEnter first number: ")
        y = getNumberInput("Enter second number: ")
    else:
        quitCalc()

    if option == "1":
        print(str(x) + " + " + str(y) + " = " + str(add(x, y)))
    
    if option == "2":
        print(str(x) + " - " + str(y) + " = " + str(subtract(x, y)))

    if option == "3":
        print(str(x) + " * " + str(y) + " = " + str(multiply(x, y)))

    if option == "4":
        print(str(x) + " / " + str(y) + " = " + str(divide(x, y)))