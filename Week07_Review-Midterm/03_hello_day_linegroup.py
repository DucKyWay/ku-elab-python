day_in, hours, minutes = int(input()), int(input()), int(input())

def get_times(hours, minutes):
    if 0 <= hours <= 24 and 0 <= minutes < 60:
        if hours == 4 and minutes == 0:
            return "night"
        elif (4 <= hours < 12) or (hours == 12 and minutes == 0):
            return "morning"
        elif (12 <= hours < 18) or (hours == 18 and minutes == 0):
            return "afternoon"
        elif (18 <= hours < 22) or (hours == 22 and minutes == 0):
            return "evening"
        else:
            return "night"

def get_day(day_in):
    if day_in == 1:
        return "sunday"
    elif day_in == 2:
        return "monday"
    elif day_in == 3:
        return "tuesday"
    elif day_in == 4:
        return "wednesday"
    elif day_in == 5:
        return "thursday"
    elif day_in == 6:
        return "friday"
    elif day_in == 7:
        return "saturday"

print(f"good-{get_times(hours, minutes)}-{get_day(day_in)}.png")