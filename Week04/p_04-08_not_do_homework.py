import math

minutes = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
raining = input("Is it raining (y/n)? ").lower()

day = minutes/1440
if day - int(day) >= 0.5:
    day = math.ceil(day)
else:
    day = math.floor(day)
print(f">>> {day} days before due.")

if day < 2:
    print(">>> I will do the assignment.")
elif day > 5:
    print(">>> I will not do the assignment.")
else:
    if temp > 40 or (temp > 25 and raining == 'y'):
        print(">>> I will not do the assignment.")
    else:
        print(">>> I will do the assignment.")