an1 = int(input())
an2 = int(input())
an3 = int(input())
a, b, c = 0, 0, 0 
i = 1
if an1 >= 0 and an2 >= 0 and an3 >= 0:
    while i <= an3:

        b = an1 - i
        c = an2 - i
        a = i

        if a + b == an1 and a + c == an2 and b + c == an3:
            print(a, b, c)
            break
        else:
            i += 1

    if a + b != an1 or a + c != an2 or b + c != an3:
        print(-1)
else:
    print(-1)