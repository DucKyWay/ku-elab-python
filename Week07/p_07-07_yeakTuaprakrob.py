def factorize(n):
    div = 2
    while n > 1:
        if n % div == 0:
            print(div)
            n //= div
        else:
            div += 1

number = int(input("Enter positive integer: "))
if number <= 0:
    print("Invalid number.")
else:
    factorize(number)
