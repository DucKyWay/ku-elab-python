day = int(input())
month = int(input())
skip = int(input())

new_month = month + skip
if new_month > 12 or new_month <= 0:
    new_month %= 12
    if new_month == 0:
        new_month = 12

if new_month == 1 or new_month == 3 or new_month == 5 or new_month == 7 or new_month == 8 or new_month == 10 or new_month == 12:
    last_day = 31
elif new_month == 4 or new_month == 6 or new_month == 9 or new_month == 11:
    last_day = 30
elif new_month == 2:
    last_day = 28

if day > last_day:
    day = last_day
print(day, new_month)