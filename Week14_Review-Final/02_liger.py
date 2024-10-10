fat, mot = input(), input()
new = ''
c = 0
for i in fat:
    if i not in 'aeiou':
        new += i
    else:
        c += 1
        if c == 2:
            break
        else:
            new += i
c = 0
for i in mot:
    if c >= 1:
        new += i
    else:
        if i in 'aeiou':
            c += 1
print(new)