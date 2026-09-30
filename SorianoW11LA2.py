#Names and programs
#Shem Jude Alexis S. Soriano


SorianoStudents =  [("Jonah Perez", "BSCS", 1),
             ("Alex Santos", "BSMT", 2 ),
             ("Micah Mendoza", "BSCS", 2),
             ("Allen Torres", "BSMT", 1),
             ("Kinnith Digs", "BSCS", 3),
             ("Rassy Josh", "BSCS", 4),
             ("Mateo Unso", "BSMT", 3),
             ("Dean Lenard", "BSCS", 4),]

search = input("Search for Program: ")
count = 0

print("Student Information")
for SorianoStudents in SorianoStudents:

    if SorianoStudents[1] == search:
        print("Name: ", SorianoStudents[0])
        print("Program: ", SorianoStudents[1])
        print("Year Level: ", SorianoStudents[2])
        print()

        if SorianoStudents[2] in [3, 4]:
          count +=1

print("Number of", search, "Students in 3rd and 4th year:", count)