txt = input()
c = ''
for i in txt:
    if i not in "AEIOUaeiou":
        c += i
print(c)