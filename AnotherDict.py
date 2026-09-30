students = {
    "Ana": [90,85,82],
    "Kirk": [72,73,78],
    "Liza": [69,71,83],
}
highest = 0
namehighest = ""
tally = 0
name75 = []
for name, grade in students.items():
   average = sum(grade) / len(grade)
   print(name, *grade, "Average:", round(average, 2))
   if average > highest:
       highest = average
       namehighest = name
   for g in grade:
        if g < 75:
            tally = tally + 1
            if name not in name75:
                name75.append(name)

print()
print("Highest average is", round(highest, 2))
print(f"Congratulations,{namehighest} is the highest grade!!")
print(f"There are {tally} grades are below 75, Owned by {', '.join(name75)}!")
print()