num = int(input())
result = 0
while num > 0 or result >= 10:
    if num == 0:
        num = result
        result = 0
    result += num % 10
    num //= 10
print(result)