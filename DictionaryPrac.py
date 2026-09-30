from SorianoW11LA2 import search

students = {
    "Shem": 70,
    "Ras": 75,
    "Matthew": 90,
    "Digs": 94,
}
print("Student Grades")
print("==============================")
print("Shem: ", students["Shem"])
print("Ras: ", students["Ras"])
#
students["Tana"] = 98
#
students["Ras"] = 84
students["Shem"] = 79
name1 = input("Enter Student Name: ")
grade1 = int(input("Enter Grade: "))
students[name1] = grade1
print(students)
print("\nUpdated Student Grades")
print("==============================")
for name, grade in students.items():
    print(name, ":", grade)

search = input("\nEnter Student Name to search: ")
if search in students:
    print(search, "has a grade of ", students[search])
else:
    print("Student not found")
highest = max(students, key=students.get)
print(highest)
