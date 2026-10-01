SorianoSalary = { "E104": {
        "EmpName": "Shem Soriano",
        "DayRate": [8, 9, 8.5, 10, 8]
    },
    "E601": {
        "EmpName": "Jude Alexis",
        "DayRate": [9, 10, 8, 8, 9]
}}

SorianoEmplInfo = ""
SorianoOT = 0
SorianoWeeklyBasic = 9000

employee_id = input("Enter employee ID: ")


if employee_id not in SorianoSalary:
    print("not yours")
else:
    employee = SorianoSalary[employee_id]
    SorianoEmplInfo = employee["EmpName"]
    duty_hours = employee["DayRate"]

    rate_per_hour = SorianoWeeklyBasic / 40

    total_weekly_hours = sum(duty_hours)

    SorianoOT = 0

    for hours in duty_hours:
        if hours > 8:
            excess_hours = hours - 8
            SorianoOT += excess_hours * 1.5 * rate_per_hour


    gross_pay = (40 * rate_per_hour) + SorianoOT

    # Display results
    print("\nEmployee Name:", SorianoEmplInfo)
    print("Duty Hours:", duty_hours)
    print("Total Weekly Hours:", total_weekly_hours)
    print("Rate per Hour:", rate_per_hour)
    print("Overtime Pay:", SorianoOT)
    print("Gross Pay:", gross_pay)


