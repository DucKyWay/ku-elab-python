txt = input()
c = 0
for i in txt:
    if i in "AEIOUaeiou":
        c += 1
print(c)