def check(is_float, num, dec):
    if is_float != -1: # float
        if len(dec) > 2:
            return "ERROR"
        
    rev_num = num[::-1]
    count = 0
    if num.find(",") != -1:
        for i in rev_num: 
            count += 1
            if count == 4:
                if i == ',':
                    count = 0
                else:
                    return "ERROR"
            if i not in '0123456789,': return "ERROR"
    else: 
        for i in num:
            if i not in '0123456789,': return "ERROR"
    
    sp_num = num.split(",")
    num = ""
    for _ in sp_num: 
        num += _
    if is_float != -1: 
        return f"{int(num)+1}.{dec}"
    else: return f"{int(num)+1}"

num = input()
isFloat = num.rfind(".")
if isFloat != -1: # isFloat
    num, dec = num[:isFloat], num[isFloat+1::]
    chk = check(isFloat, num, dec)
else:
    chk = check(isFloat, num, 0)
print(chk)