patients = {"Ras" :(105,135,300),
           "Shem" : (110, 140, 340)}
for pn,bs in patients.items():
    if (pn == "Ras"):
        print("Ras")
        print("Blood sugar summary:")
        for value in bs:

            if value<120:
                print(value, "Not Normal")
            else:
                print(value, "Normal")

        highest = max(bs)
        print(highest,pn)
        lowest = min(bs)
        print(lowest,pn)
