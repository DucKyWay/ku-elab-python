def read_hour():
    return int(input("Enter hour: "))
def read_minute():
    return int(input("Enter minute: "))
def read_second():
    return int(input("Enter second: "))
def to_seconds(h, m, s):
    return (h*3600) + (m*60) + s

def time_elapsed(start, finish):
    sum_sec = finish_time - start_time
    re_hr = sum_sec // 3600
    sum_sec %= 3600
    re_m = sum_sec // 60
    sum_sec %= 60
    return f"{re_hr} hours {re_m} minutes {sum_sec} seconds."

''' ============== fix code ============== '''
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))