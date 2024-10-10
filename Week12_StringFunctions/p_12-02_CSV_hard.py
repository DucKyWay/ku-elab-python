def split(txt, case):
    ls, split = [], ""
    for i in txt:
        if i != case: 
            split += i
        else:
            ls.append(split)
            split = ""
    ls.append(split)
    return ls
            
def lstrip(txt):
    if txt[:txt.find(" ")+1] != " ":
        return txt
    return lstrip(txt[txt.find(" ")+1:])

def rstrip(txt):
    if txt[txt.rfind(" "):] != " ":
        return txt
    return rstrip(txt[:txt.rfind(" ")])

txt = split(input(), ',')
for i in range(len(txt)): txt[i] = lstrip(rstrip(txt[i]))
for i in range(len(txt)): 
    print(f'"{txt[i]}"', end="")
    if i != len(txt)-1:
        print(f',', end="")