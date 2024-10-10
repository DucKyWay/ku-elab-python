num, result, count = input(), 0, 0
for i in str(num):
    if int(i)%2 == 0:
        if count > 0:
            result *= int(i)
        else:
            result = int(i)
        count += 1
if count > 0:
    print(result)
else:
    print(-1)