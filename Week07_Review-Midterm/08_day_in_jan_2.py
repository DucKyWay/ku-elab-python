x, n = input(), int(input())
check = 0
if 1 <= n <= 31:
    if x == "Sunday":
        start_day = 0
    elif x == "Monday":
        start_day = 1
    elif x == "Tuesday":
        start_day = 2
    elif x == "Wednesday":
        start_day = 3
    elif x == "Thursday":
        start_day = 4
    elif x == "Friday":
        start_day = 5
    elif x == "Saturday":
        start_day = 6
    else:
        result = "ERROR"
        check = 1
        
    if check != 1:
        result = (start_day + n-1) % 7 #genius math
        if result == 0:
            result = "Sunday"
        elif result == 1:
            result = "Monday"
        elif result == 2:
            result = "Tuesday"
        elif result == 3:
            result = "Wednesday"
        elif result == 4:
            result = "Thursday"
        elif result == 5:
            result = "Friday"
        elif result == 6:
            result = "Saturday"
    else:
        result = "ERROR"
else:
    result = "ERROR"
print(result)
