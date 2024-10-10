def check_day(day, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= day <= 31:  return 0
        else:               return 1
    elif month in [4, 6, 9, 11]:
        if 1 <= day <= 30:  return 0
        else:               return 1
    elif month == 2: 
        if 1 <= day <= 28:  return 0
        else:               return 1
    else:
        if 1 <= day <= 31:  return 0
        else:               return 1

def set_day(start, finish):
    if start[1] > finish[1]:
        start[1], finish[1] = finish[1], start[1]
        start[0], finish[0] = finish[0], start[0]
    elif start[1] == finish[1] and start[0] > finish[0]: # same month flip day
        start[0], finish[0] = finish[0], start[0]
    return start, finish

def generate_sundays(sunday, month_length):
    sundays = [[] for _ in range(12)]

    for month in range(12):
        sun_month = []
        while sunday <= month_length[month]:
            sun_month.append(sunday)
            sunday += 7
        sundays[month] = sun_month
        sunday -= month_length[month]
    
    return sundays

def check_day_is_sun(day, month, sun_list):
    if day in sun_list[month-1]:    return 1
    else:                           return 0
    
def main():
    start, finish = input().split("-"), input().split("-")
    sun = int(input())
    start = [int(start[i]) for i in range(len(start))]
    finish = [int(finish[i]) for i in range(len(finish))]
    start, finish = set_day(start, finish)

    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sun_list = generate_sundays(sun, month_length)

    if 1 < start[1] > 12 or 1 < finish[1] > 12:
        print("Wrong Month")
        check_day_start = check_day(start[0], start[1])
        check_day_finish = check_day(finish[0], finish[1])
        if check_day_start == 1 or check_day_finish == 1 or 1 >= sun >= 7: 
            print("Wrong Day")
        return ""
    else: 
        check_day_start = check_day(start[0], start[1])
        check_day_finish = check_day(finish[0], finish[1])
        if check_day_start == 1 or check_day_finish == 1 or 1 >= sun >= 7: 
            print("Wrong Day")
            return ""

    count_sun = 0
    if check_day_start == 0 and check_day_finish == 0:
        if start[1] != finish[1]:
            for i in range(start[1], finish[1]+1):      # start to finish
                if i == start[1]:
                    for j in range(start[0], month_length[i-1]+1): # start month : start to finish
                        # print(j, i, check_day_is_sun(j, i, sun_list) end="  ")
                        count_sun += check_day_is_sun(j, i, sun_list)
                elif i == finish[1]:
                    for j in range(1, finish[0]+1):         # last month : 1 to finish
                        # print(j, i, check_day_is_sun(j, i, sun_list),  end="  ")
                        count_sun += check_day_is_sun(j, i, sun_list)
                else:
                    for j in range(1, month_length[i-1]+1):        # normal : 1 to last
                        # print(j, i, check_day_is_sun(j, i, sun_list),  end="  ")
                        count_sun += check_day_is_sun(j, i, sun_list)
                # print()
        else:
            for i in range(start[0], finish[0]+1):      # 1 month : loop in month only
                # print(i, start[1], end="  ")
                count_sun += check_day_is_sun(i, start[1], sun_list)
    print(count_sun)
main()