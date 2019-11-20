def addStudent(students, studentName, studentGrade):
    if studentName not in students:
        students[studentName] = studentGrade
        printLine()
        print("Student has been successfully added.")
    else:
        printLine()
        print("Student with name " + studentName + " already exists.")

def deleteStudent(students, studentName):
    if studentName in students:
        students.pop(studentName)
        printLine()
        print("Student has been successfully deleted.")
    else:
        printLine()
        print("Student with name " + studentName + " has not been found.")

def searchStudent(students, studentName):

    if studentName in students:
        printLine()
        print("Student with name " + studentName + " has been found. Its grade is " + str(students[studentName]) + ".")
    else:
        printLine()
        print("Student with name " + studentName + " has not been found.")

def updateStudent(students, studentName, studentMidterm, studentFinal):

    if studentName in students:
        students[studentName] = calculateGrade(studentMidterm, studentFinal)
        printLine()
        print("Student with name " + studentName + " has been updated.")
    else:
        printLine()
        print("Student with name " + studentName + " has not been found.")

def displayAllStudents(students):

    if len(students) > 0:
        printLine()
        print("List of all the students: ")
        print("----------------------------")
        for student in students:
            print("Student with name " + student + " and grade " + str(students[student]))
    else:
        printLine()
        print("There are no saved students.")

def displayExtremeGrades(students):

    if len(students) > 0:
        topGradeStudent = max(students, key=students.get)
        lowestGradeStudent = min(students, key=students.get)
        
        printLine()
        print("Top Grade: " + str(students[topGradeStudent]) + " (" + topGradeStudent + ") / Lowest Grade: " + str(students[lowestGradeStudent]) + " (" + lowestGradeStudent + ")")
    else:
        printLine()
        print("There are no saved students.")

def calculateGrade(midtermGrade, finalGrade):
    return ((midtermGrade * 0.4) + (finalGrade * 0.6))    

def printMenu():
    print("********* MAIN MENU *********")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Find Student")
    print("4. Update Student")
    print("5. View All Students")
    print("6. Display Top Grade and Lowest Grade")
    print("7. Exit")

def printLine():
    print("\n")

students = {}

while True:

    printLine()
    printMenu()
    printLine()

    option = int(input("Enter your option number: "))
    printLine()

    if (option == 1):
        
        studentName = input("Enter the name of the new student: ")
        studentMidterm = float(input("Enter the midterm grade of the new student: "))
        studentFinal = float(input("Enter the final grade of the new student: "))

        addStudent(students, studentName, calculateGrade(studentMidterm, studentFinal))

    elif (option == 2):

        studentName = input("Enter the name of the student you want to delete: ")
        deleteStudent(students, studentName)

    elif (option == 3):

        studentName = input("Enter the name of the student you are looking for: ")

        searchStudent(students, studentName)

    elif (option == 4):

        studentName = input("Enter the name of the student you want to update: ")

        midtermGrade = float(input("Enter the new midterm grade of the student you want to update: "))
        finalGrade = float(input("Enter the new final grade of the student you want to update: "))

        updateStudent(students, studentName, midtermGrade, finalGrade)

    elif (option == 5):

        displayAllStudents(students)

    elif (option == 6):

        displayExtremeGrades(students)

    elif (option == 7):

        printLine()
        print("Goodbye.")
        break

    else:

        printLine()
        print("Invalid option.")