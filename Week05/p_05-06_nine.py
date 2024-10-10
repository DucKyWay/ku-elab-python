num = int(input())
sum_digit = 0
while num > 0:
    sum_digit += num % 10
    num = num // 10
    # print(num, sum_digit)
if sum_digit % 9 == 0:
    print("Yes", sum_digit)
else:
    print("No", sum_digit % 9)