ls = []
left, right, chk = '', '', 0
while True:
    txt = input().strip()
    if txt == '-1': break
    else:
        find = txt.find('=')
        for i in txt:
            if i == '=': 
                chk = 1
            if chk == 0: left += i
            else: right += i
        left, right = left.strip(), right[1:].strip()
        txt = left + ' = ' + right
        left, right, chk = '', '', 0
        ls.append(txt)

max_space = max(i.find("=") for i in ls)
for i in ls:
    for j in i:
        if j == '=':
            chk = 1
        if chk == 0:
            left += j
        else:
            right += j
    remain = max_space-len(left)
    print(f"""{" "*remain}{left}{right}""")
    chk, left, right = 0, '', ''