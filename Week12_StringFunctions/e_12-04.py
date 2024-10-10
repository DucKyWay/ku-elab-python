txt, up, low = input(), 0, 0
for i in txt:
    if i.islower(): low += 1
    elif i.upper(): up += 1
print(low)
print(up)



txt, result = input(), ''
for i in txt:
    if i.islower(): result += i.upper()
    elif i.isupper(): result += i.lower()
print(result)