def add_char(fileNameI, sign):
    out = ""
    if fileNameI in sign: out += '_'
    else: out += fileNameI
    return out

fileName, sign = input(), """\\/*:|"<>. """
type, out = fileName.rfind("."), ""
lenName, i = len(fileName), 0
while i < lenName:
    if type != -1:
        if i < type and i < 15:
            out += add_char(fileName[i], sign)
        elif i == type:
            out += '.'
        elif i > type and i < type+4:
            out += add_char(fileName[i], sign)
    else:
        if i < 15:
            out += add_char(fileName[i], sign)
    i += 1

print(out)