num, result = input(), 0
for i in str(num):
    if int(i)%2 != 0:
        result += int(i)
if result > 0:
    print(result)
else:
    print(-1)