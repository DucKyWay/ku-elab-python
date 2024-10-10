num = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))
result = 0
if num >= 0:
    if 0 <= digit <= 9:
        num = str(num)
        for _ in num:
            if _ == str(digit):
                result += 1
        if result != 1:
            print(f"Digit {digit} occurs {result} times.")
        else:
            print(f"Digit {digit} occurs {result} time.")
    else:
        print("Invalid digit.")
else:
    print("Invalid number.")
    if not (0 <= digit <= 9):
        print("Invalid digit.")