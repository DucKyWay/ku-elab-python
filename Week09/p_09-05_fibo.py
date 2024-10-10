def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        i = 1
        a, b = 1, 1
        while i <= n-2:
            c = a + b
            a = b
            b = c    
            i += 1
        return c

n = int(input("Enter n: "))
print("fibo({}) = {}".format(n, fibo(n)))