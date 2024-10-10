import math
numbers = []
cur_max = -math.inf
while True:
    num = int(input())
    if num == -1:
        break
    if num >= cur_max:
        numbers.append(num)
        cur_max = num
print(numbers) 