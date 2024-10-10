import math
def sqrt_n_times(x, n):
    result = x
    i = 1
    while i <= n: 
        result = math.sqrt(result)
        i += 1
    return result

x = float(input())
n = int(input())
print( sqrt_n_times(x, n) )