# 3

import random

def printLine():
    print("\n")

def displayHint(randomNumber, guessedNumber):
    if guessedNumber > randomNumber:
        print("Your number is too high. Try again.")
    elif guessedNumber < randomNumber:
        print("Your number is too low. Try again.")

while True:

    printLine()
    randomNumber = random.randint(1, 10)
    print("New game started! Enter exit anytime if you want to stop playing.")
    printLine()

    while True:

        guessedNumber = input("Guess the number: ")
        if guessedNumber == "exit":
            randomNumber = "exit"
            break

        if int(guessedNumber) == randomNumber:
            printLine()
            print("Congratulations! You guessed it.")
            break
        else:
            printLine()
            displayHint(randomNumber, int(guessedNumber))
    
    if randomNumber == "exit":
        break
