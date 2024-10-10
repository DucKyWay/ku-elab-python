line = int(input("Enter height: "))
i = 0

while i < line:
    s_1 = "  "* (line-i-1)

    if i == 0:
        result = "  "* (line-i-1) + "1"
    else:
        s_2 = " "*(4*i-1)
        result = s_1 + "1" + s_2 + "1"
    print(result)
    i += 1