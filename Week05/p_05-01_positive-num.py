x = int(input())

if x > 0:
    while True:
        if x <= 0:
            break
        else:
            a = x % 10
            x //= 10
            print(a)
else:
    print("ERROR")