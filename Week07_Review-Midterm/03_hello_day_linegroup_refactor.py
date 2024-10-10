day_in, hours, minutes = int(input()), int(input()), int(input())

if 0 <= hours <= 24 and 0 <= minutes < 60:
    if hours == 4 and minutes == 0:
        times = "night"
    elif (4 <= hours < 12) or (hours == 12 and minutes == 0):
        times = "morning"
    elif (12 <= hours < 18) or (hours == 18 and minutes == 0):
        times = "afternoon"
    elif (18 <= hours < 22) or (hours == 22 and minutes == 0):
        times = "evening"
    else:
        times = "night"

if day_in == 1:
    days = "sunday"
elif day_in == 2:
    days = "monday"
elif day_in == 3:
    days = "tuesday"
elif day_in == 4:
    days = "wednesday"
elif day_in == 5:
    days = "thursday"
elif day_in == 6:
    days = "friday"
elif day_in == 7:
    days = "saturday"

print(f"good-{times}-{days}.png")