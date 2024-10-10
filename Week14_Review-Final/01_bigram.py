txt = input()
ls = []
for i in range(len(txt)):
    if i != len(txt)-1:
        ls.append(txt[i].lower()+txt[i+1].lower())
ls.sort()
new_ls = []
for i in range(len(ls)):
    if ls[i] not in new_ls:
        new_ls.append(ls[i])
for i in new_ls:
    print(i)