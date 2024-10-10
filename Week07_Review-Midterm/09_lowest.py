n = int(input())
a, b, c = 1, 1, n
if n > 0:
    for _ in range(int(n/2)):
        a = _ + 1
        b = n / a
        if a * b == n and b - int(b) == 0:
            # print(a, b)
            if c > a + b or c >= n:
                c = a + b
            else:
                c = c
    print(int(c))