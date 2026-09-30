patients = {"Ras" :(105,135,300),
           "Shem" : (110, 140, 340),}

normal = 120
for key, value in patients.items():
    print(key)
    for v in value:
        if v>normal:
         print(v,"diabetic")
        else:
            print(v,"normal")
