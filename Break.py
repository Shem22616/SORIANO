while True:
    word = input("Enter a word: ")
    letter = input("Enter a character to search for: ")

    found = False

    for character in word:
        if character.lower() == letter.lower():
            found = True
            break

    if found:
        print("CHARACTER FOUND!")
    else:
        print("CHARACTER NOT FOUND!")

    again = input("TRY AGAIN? (y/n): ")
    if again.upper() != "Y":
        break


