a, b, c = int(input()), int(input()), int(input())
if c*c == a*a + b*b:
    print(True)
else:
    if b*b == a*a + c*c:
        print(True)
    else:
        if a*a == b*b + c*c:
            print(True)
        else:
            print(False)