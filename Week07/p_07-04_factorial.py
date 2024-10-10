def fac(num):
    result = ""
    i = num
    result = f"{num}! ="
    val = 1
    while i >= 1:
        if i == num:
            result += f" {i}"
        else:
            result += f" x {i}"
        val *= i
        i -= 1
    if num == 0:
        result += f" 1 = {val}"
    else:
        result += f" = {val}"
        
    return result

def main():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Invalid input, program terminates.")
    else:
        i = 0
        while i <= num:
            print(fac(i))
            i += 1
main()