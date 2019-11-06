# 1

availableCourses = ["Python Crash Course", "Java Application Development", "English 101"]

userCourse = input("What course are you looking for? ")

if userCourse in availableCourses:
    print("It is available!")
else:
    print("Sorry, it is not available!")