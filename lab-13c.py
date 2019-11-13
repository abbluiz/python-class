# 4

def exitCheck(keyword):
    if (keyword == "exit"):
        exit()
    elif(keyword == "stop"):
        return True
    else:
        return False

drinks = []

while True:

    file = open("drinks.txt", "w+")

    print("Choose a drink\n")

    print("What is the size: small, medium or large?")
    