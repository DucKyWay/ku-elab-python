x, n = int(input()), int(input())
if 1 <= x <= 7 and 1 <= n <= 31:
    if (n-x) % 7 == 0:
        print("Sunday")
    elif (n-x) % 7 == 1:
        print("Monday")
    elif (n-x) % 7 == 2:
        print("Tuesday")
    elif (n-x) % 7 == 3:
        print("Wednesday")
    elif (n-x) % 7 == 4:
        print("Thursday")
    elif (n-x) % 7 == 5:
        print("Friday")
    elif (n-x) % 7 == 6:
        print("Saturday")
    else:   
        if x == 1:
            print("Sunday")
        elif x == 2:
            print("Monday")
        elif x == 3:
            print("Tuesday")
        elif x == 4:
            print("Wednesday")
        elif x == 5:
            print("Thursday")
        elif x == 6:
            print("Friday")
        elif x == 7:
            print("Saturday")
else:
    print("ERROR")