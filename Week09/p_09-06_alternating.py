def alt(n):
    i = 1
    res = 0
    while i <= n:
        if i%2==0:
            res -= i
        else:
            res += i
        i += 1
    return res

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n, alt(n)))