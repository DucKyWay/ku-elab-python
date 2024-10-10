hours, minutes = int(input("Enter number of hours: ")), int(input("Enter number of minutes: "))
buyAmt = int(input("Enter shopping amount: "))

price = 0

if hours >= 0 and hours <= 20 and minutes >= 0 and minutes <= 59:
    if minutes > 0:
        hours += 1

    if hours <= 20:
        if buyAmt >= 3001:
            free_hr = 99999999999999999999999999999999999
        elif buyAmt >= 300:
            free_hr = 4
        else:
            free_hr = 2

        if hours > free_hr and free_hr == 2:
            hours -= free_hr
            if hours == 1:
                price += 20
            elif hours == 2:
                price += 40
            else:
                price = 40 + ((hours-2) * 50)
            result = f"Total amount due is {price} Baht, thank you."
            
        elif hours > free_hr and free_hr == 4:
            hours -= free_hr
            price = hours * 50
            result = f"Total amount due is {price} Baht, thank you."

        else:
            result = "No charge, thank you."
    else:
        result = "Invalid time."
else:
    result = "Invalid time."

print(result)