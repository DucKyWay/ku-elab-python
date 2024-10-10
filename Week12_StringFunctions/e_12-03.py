line, result = 0, ""
while True:
    txt = input()
    if txt == "": break
    else:
        line += 1
        if line%2 == 0: result += min(txt)
        elif line%2 != 0: result += max(txt)
print(result)