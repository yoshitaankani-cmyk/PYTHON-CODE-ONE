
attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
required = float(input("Enter required attendance percentage: "))

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details")

elif required < 0 or required > 100:
    print("Invalid required percentage")

else:
    percentage = (attended / conducted) * 100

    print("Current attendance:", percentage, "%")

    if percentage >= required:
        print("You are eligible")
        print("No extra classes required")

    else:
        extra = 0

        while ((attended + extra) / (conducted + extra)) * 100 < required:
            extra = extra + 1

        print("You are not eligible")
        print("Minimum extra classes required:", extra)

        print("Attendance after extra classes:",
              ((attended + extra) / (conducted + extra)) * 100, "%")

