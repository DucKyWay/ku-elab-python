def factor_count(n):
    div, count = 1, 0
    while div <= n:
        if n % div == 0:
            count += 1
        div += 1
    return count

''' Fix code '''

n = int(input("Enter n: "))
c = factor_count(n)
print(c)