num = list(input().lstrip('0'))
if not num: num = ['0']
num = [num[i] for i in range(len(num)-1, -1, -1)]
txt = ['' for _ in range(len(num))]

digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten = ["", ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"], "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hun = "-hundred"

if len(num) <= 3:
    for i in range(len(num)):
        if num[i].isdigit():
            if i == 0:
                txt[0] = digit[int(num[i])]
            if i == 1:
                if txt[0] == "zero":
                    txt[0] = "" 
                    if num[1] != '1':
                        txt[1] = ten[int(num[i])]
                    else: txt[1] = ten[1][int(num[i-1])]
                elif num[1] == '1':
                    txt[0] = ""
                    txt[1] = ten[1][int(num[i-1])]
                else: 
                    if num[0] != "0":
                        txt[1] = ten[int(num[i])] + '-'
                    else: txt[1] = ten[int(num[i])]
            if i == 2:
                if num[1] == "0":
                    txt[2] = digit[int(num[i])] + hun
                else: txt[2] = digit[int(num[i])] + hun + '-'
        else:
            txt = "ERROR"
            break
else: txt = "ERROR"

if txt != "ERROR":
    txt.reverse()
    for i in txt: print(i, end="")
else: print(txt)