students = {}
number = int(input("Enter number of students: "))
for i in range(number):
    print("\nStudent" , 1+1)
    name = input("Enter name of student: ")
    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))
    students[name] = (grade1, grade2, grade3)

print("\n=======STUDENT RECORD=======")
highest = 0
namehighest = ""
tally = 0
