def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

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
        x = float(input("\nEnter first number: "))
        y = float(input("Enter second number: "))
    else:
        break

    if option == "1":
        print(str(x) + " + " + str(y) + " = " + str(add(x, y)))
    
    if option == "2":
        print(str(x) + " - " + str(y) + " = " + str(add(x, -y)))

    if option == "3":
        print(str(x) + " * " + str(y) + " = " + str(multiply(x, y)))

    if option == "4":
        if (y == 0):
            print(str(x) + " / " + str(y) + " = " + "error")
        else:
            print(str(x) + " / " + str(y) + " = " + str(multiply(x, 1/y)))