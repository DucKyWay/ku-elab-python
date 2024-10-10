i = 1
result = ""
while i <= 5:
    key = int(input())

    if 0 <= key < 60:
        a = 1
    else:
        a = 0
    
    if key%2 == 0:
        b = 2
    else:
        b = 0

    if 100 <= key**2 <= 9999:
        c = 4
    else:
        c = 0

    result += str(a + b + c)
    i += 1
print(result)