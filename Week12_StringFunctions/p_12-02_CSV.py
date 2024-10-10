txt = input().split(",")
for i in range(len(txt)): txt[i] = txt[i].strip()

for i in range(len(txt)):
    if i == len(txt)-1:
        print(f'"{txt[i]}"')
    else: print(f'"{txt[i]}",', end="")