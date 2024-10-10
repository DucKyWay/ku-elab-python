a, b = 0, 0
count, result, sum, new_target =  0, "", 0, 0
while result != "W" or result != "L":
    a, b = int(input()), int(input())
    if 1 <= a <= 6 and 1 <= b <= 6:
        count += 1
        if count > 1:
            if a + b == new_target:
                result = "W"
                sum = a + b
                break
            elif a + b == 7:
                result = "L"
                sum = a + b
                break
            else:
                continue
        else:
            if a + b == 7 or a + b == 11:
                result = "W"
                sum = a + b
                break
            elif a + b == 2 or a + b == 3 or a + b == 12:
                result = "L"
                sum = a + b
                break
            else:
                new_target = a + b
    else:
        print("ERROR")
print(f"{count} {sum} {result}")