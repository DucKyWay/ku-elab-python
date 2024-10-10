num = int(input("Enter a number: "))

if 0 < num <= 26:
    i = num
    while i >= 1:
        
        j = 0
        while j < i:
            ch = ord('A') + j
            print(chr(ch), end="")
            j += 1
            
        print()
        i -= 1
else:
    print("Invalid input, program terminates.")