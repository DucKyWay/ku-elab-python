txt = list(input())
new_txt = ['' for _ in range(len(txt))]
        
for i in range(len(txt)):
    if len(txt) % 2 == 0:
        if i < len(txt) // 2:
            new_txt[i*2-len(txt)] = txt[i]
        else:
            new_txt[(len(txt)-1)-(2*i)] = txt[i]
    else:
        if i <= len(txt) // 2:
            new_txt[i*2-len(txt)] = txt[i]
        else:
            new_txt[(len(txt)-1)-(2*i)] = txt[i]

for i in new_txt: print(i, end="")