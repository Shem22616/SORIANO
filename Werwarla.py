from random import choice

nohour=float(input("Enter hours: "))
choice = int(input("1] Janitor 2] Clerk:"))
positions=""
salary=0
if choice==1:
    positions="Janitor"
    salary=10000

elif choice==2:
    positions="Clerk"
    salary=20000

else:
    print("invalid")

halfmonth=salary/2
rateperhour=halfmonth/88
absenceded=0
if nohour>=88:
    extrahours=nohour-88
    otrate=rateperhour*1.25
    overtimepay=otrate*extrahours
    netsalary = halfmonth+overtimepay
    print("overtimepay:" , overtimepay)

elif nohour<88:
    absences=88-nohour
    absenceded = rateperhour*1.10*absences
    netsalary=halfmonth-absences
    print("absence deduction:  , {absenceded:,.2f}")

else:
    print("invalid")
print(f"Net salary: {netsalary:,.2f}")
print("Position: ", positions)
