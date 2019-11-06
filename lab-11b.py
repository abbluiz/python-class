# 2

list = []

list.append(int(input("Enter first number: ")))
print("\n")

list.append(int(input("Enter second number: ")))
print("\n")

list.append(int(input("Enter third number: ")))
print("\n")

print("The maximum numebr is: " + str(max(list)))
print("\n")

print("The minimum number is: " + str(min(list)))
print("\n")

print("The number of numbers entered is: " + str(len(list)))
print("\n")

print("The number 7 occurs " + str(list.count(7)) + " times")
print("\n")

list.reverse()
print("The numbers of the list reversed are: " + str(list))
print("\n")