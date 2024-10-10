# 1
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
i = 0

total = 0
while i <= 9:
    total += primes[i]
    i += 1
print(total)

# 2
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 0
while i <= 11:
    print(f"{months[i]} {days_in_month[i]}")
    i += 1