year = int(input("Enter year: "))
if year >=  1:
    if year % 4 == 0:
        if year % 100 != 0:
            print(year, "is a leap year.")
        elif year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is not a leap year.")
else:
    print("Invalid year.")