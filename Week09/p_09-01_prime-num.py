def check_prime(n):
    i = 2
    check = 0
    while i <= (n/2): 
        if (n % i) == 0:
            check = 1
            break
        else:
            i += 1
    if check == 1:
        return False
    else:
        return True

''' Fix code '''

n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")