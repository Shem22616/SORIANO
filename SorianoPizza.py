print("========================")
print("Pizza Flavor ")
print("========================")
print("White Pizza")
print("Cheese Pizza")
print("Hawaiian Pizza")
print("========================")
print("Sizes (Small/Medium/Large)")
print("================")

Sorianoflavor = input("Enter a Pizza Flavor: ").lower()
Sorianosize = input("Enter size (Small/Medium/Large): ").lower()
Sorianoprice = 0

print("=======Receipt Price=======")

match Sorianoflavor:
    case "hawaiian":
        if Sorianosize == "small":
            Sorianoprice = 499
        elif Sorianosize == "medium":
            Sorianoprice = 750
        elif Sorianosize == "large":
            Sorianoprice = 1200
        else:
            print("Invalid size")
            print("Please Try Again!")

    case "cheese":
        if Sorianosize == "small":
            Sorianoprice = 399
        elif Sorianosize == "medium":
            Sorianoprice = 600
        elif Sorianosize == "large":
            Sorianoprice = 999
        else:
            print("Invalid size")
            print("Please Try Again!")

    case "white":
        if Sorianosize == "small":
            Sorianoprice = 599
        elif Sorianosize == "medium":
            Sorianoprice = 800
        elif Sorianosize == "large":
            Sorianoprice = 1400
        else:
            print("Invalid size")
            print("Please Try Again!")

    case _:
        print("Invalid Pizza Flavor")

if Sorianoprice > 0:
    print(f"{Sorianoflavor.capitalize()} Pizza")
    print(f"Price: {Sorianoprice}")
    print("Thank you for Purchasing")
    print("======================")