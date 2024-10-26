para = {}

print("Enter variables and values:")
while True:
    txt = input()
    if txt == '-1': break
    [eq, val] = txt.split('=')
    eq, val = eq.strip(), val.strip()
    para[eq] = val

ls = []
print("Enter your program:")
while True:
    txt = input()
    if txt == '-1': break
    for eq in para:
        txt = txt.replace("{"+eq+"}", para[eq])
    ls.append(txt)

print("Result:")
print("\n".join(ls))