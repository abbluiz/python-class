# 4

import time

def calculatePrice(prices, quantity, size, type):
    
    sizeIndex = 0
    typeIndex = 0

    if (size == "small"):
        sizeIndex = 0
    elif (size == "medium"):
        sizeIndex = 1
    elif (size == "large"):
        sizeIndex = 2

    if (type == "decaf"):
        typeIndex = 0
    elif (type == "latte"):
        typeIndex = 1
    elif (type == "black"):
        typeIndex = 2

    return prices[sizeIndex][typeIndex] * quantity

file = open("drinks.txt", "a+")

print("Drink Ordering System\n")

prices = [[1.00, 1.80, 0.80], [1.25, 2.00, 1.10], [1.50, 2.25, 1.30]]

while True:

    name = input("\nWhat is your name? (stop to exit script) ")
    
    if (name == "stop"):
        break

    print("\n")

    totalPrice = 0.00
    orderCount = 1

    localtime = time.asctime(time.localtime(time.time()))

    file.write("Customer Name: " + name + "\n")
    file.write("Order Date: " + localtime + "\n")
    file.write("-------------------------\n\n")

    while True:

        print("Item Number " + str(orderCount) + " (enter stop to stop ordering)\n")
        
        cupSize = input("Cup Size: small, medium, or large? ")

        if (cupSize == "stop"):
            if (orderCount == 1):
                file.write("Order canceled.")
            break

        coffeeType = input("Coffee Type: decaf, latte, or black? ")

        if (coffeeType == "stop"):
            if (orderCount == 1):
                file.write("Order canceled.")
            break 

        quantity = input("Quantity? ")

        if (quantity == "stop"):
            if (orderCount == 1):
                file.write("Order canceled.")
            break 

        print("\n")

        itemPrice = calculatePrice(prices, int(quantity), cupSize, coffeeType)

        file.write("Item Number " + str(orderCount) + "\n")
        file.write(cupSize + ", " + coffeeType + " coffee ($" + str(itemPrice) + ")\n\n")

        totalPrice += itemPrice
        orderCount += 1

    file.write("Total Price: $" + str(totalPrice) + "\n\n")

file.close()