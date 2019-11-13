# 3

def inputStudentName():
    return input("Enter your name: ")

def inputStudentMidtermGrade():
    return float(input("Enter your midterm grade: "))

def inputStudentFinalGrade():
    return float(input("Enter your final grade: "))

def inputStudentAssignmentGrade():
    return float(input("Enter your assignment grade: "))

def calculateTotalGrade(midtermGrade, finalGrade, assignmentGrade):
    assert (midtermGrade >= 0.0)
    assert (finalGrade >= 0.0)
    assert (assignmentGrade >= 0.0)
    return ( (midtermGrade * 0.3) + (finalGrade * 0.5) + (assignmentGrade * 0.2) )

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
    print("Enter exit anytime to quit the program or enter stop to show all students")

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
    for s in students:
        printResults(s[0], calculateTotalGrade(float(s[1]), float(s[2]), float(s[3])))
        printLine()
else:
    print("There are no students.")
    