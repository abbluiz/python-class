# 1

def inputStudentName():
    return input("Enter your name: ")

def inputStudentMidtermGrade():
    return float(input("Enter your midterm grade: "))

def inputStudentFinalGrade():
    return float(input("Enter your final grade: "))

def inputStudentAssignmentGrade():
    return float(input("Enter your assignment grade: "))

def calculateTotalGrade(midtermGrade, finalGrade, assignmentGrade):
    return midtermGrade + finalGrade + assignmentGrade

def exitCheck(keyword):
    if (keyword == "exit"):
        exit()
    elif(keyword == "stop"):
        return True
    else:
        return False

def printLine():
    print("\n")

def printHeader():
    print("Enter exit anytime to quit the program or enter stop to show all users with a total grade of 50+")

def printResults(studentName, studentGrade):
    print("Student Name: " + studentName + " / Total Grade: " + str(studentGrade))

students = []

while True:
    
    student = []

    printLine()
    printHeader()
    printLine()

    student.append(inputStudentName())
    if (exitCheck(student[0])): break
    
    student.append(inputStudentMidtermGrade())
    if (exitCheck(student[1])): break
    
    student.append(inputStudentFinalGrade())
    if (exitCheck(student[2])): break
    
    student.append(inputStudentAssignmentGrade())
    if (exitCheck(student[3])): break

    students.append(student)
    print("Student added.")

if len(students) != 0:
    successfulStudents = list(filter(lambda s: (calculateTotalGrade(float(s[1]), float(s[2]), float(s[3])) >= 50.0), students))

    if len(successfulStudents) != 0:
        for s in successfulStudents:
            printResults(s[0], calculateTotalGrade(float(s[1]), float(s[2]), float(s[3])))
            printLine()
    else:
        print("There are no successful students.")
else:
    print("You did not provide any students.")