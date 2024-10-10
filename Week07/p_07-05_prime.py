def check_prime(num):
    i = 2
    check = 0
    while i <= (num/2): 
        if (num % i) == 0:
            check = 1
            break
        else:
            i += 1
    if check == 1:
        print(num, "is not a prime number.")
    else:
        print(num, "is a prime number.")

def main():
    number = int(input("Enter a number: "))
    while True:
        if number == 0:
            print("End of program, goodbye.")
            break
        elif number <= 1:
            print("Invalid input, try again.")
            number = int(input("Enter a number: "))
        else:
            check_prime(number)          
            number = int(input("Enter a number: "))
main()