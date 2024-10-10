temp = float(input())
unit = input()

if unit == "f" or unit == "F":
    temp = (9/5)*temp+32
    print(temp)
elif unit == "k" or unit == "K":
    temp = temp + 273.15
    print(temp)
else:
    print("ERROR")