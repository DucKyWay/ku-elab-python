def display(n):
    result = ''
    j = 0
    while j < n:
        ch = ord('A') + j
        result += chr(ch)
        j += 1
    return result
    
def main():
    num = int(input("Enter a number: "))
    
    if 0 < num <= 26:
        i = 1
        while i < num:
            res = display(i)
            print(res)
            i += 1
        while i >= 1:
            res = display(i)
            print(res)
            i-=1
            
    else:
        print("Invalid input, program terminates.")
main()