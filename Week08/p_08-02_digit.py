def digit(num):
    return num%10
def tens(num):
    return num%100 // 10
def hundreds(num):
    return num%1000 // 100
def thousands(num):
    return num%10000 // 1000

def sum_digits(num):
    return digit(num) + tens(num) + hundreds(num) + thousands(num)

n   = int(input('Enter a number (0 to 9999): '))
print(f'Digit place is {digit(n)}.')
print(f'Tens place is {tens(n)}.')
print(f'Hundreds place is {hundreds(n)}.')
print(f'Thousands place is {thousands(n)}.')
print(f'Sum of all digits is {sum_digits(n)}.')
