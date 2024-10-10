def extract_string(text: str):
    ls = []
    tmp = ''
    is_digit = text[0:1].isdigit() # What About 1

    for i in range(len(text)):
        if tmp == '':  # start
            tmp += text[i]
        elif text[i].isdigit() == is_digit: # start by digit
            tmp += text[i]
        else:
            if tmp.isdigit():   ls.append(int(tmp))
            else:               ls.append(tmp)
            is_digit = text[i].isdigit()
            tmp = text[i]
    if tmp: 
        if tmp.isdigit(): ls.append(int(tmp))
        else: ls.append(tmp)

    return ls

print( extract_string("G2X3t4") )
print( extract_string("AB12XY23") )
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )