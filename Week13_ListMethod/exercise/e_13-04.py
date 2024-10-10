ls = []
while True:
    txt = input()
    if txt == '': break
    else: ls.append(float(txt))
print(ls.count(min(ls)))