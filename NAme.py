
while True:
    name = input ("Enter your name?")

    print("Hello ,", name)

    again = input ("Do you want to enter again? (Y/N): ")

    if again.upper() != "Y":
        print("Goodbye")
        break