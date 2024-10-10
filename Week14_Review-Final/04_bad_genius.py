orignal, secret, txt = input(), input(), input()
s = ''
result = ''

for i in orignal:
    if i.isspace(): pass
    elif i not in s:    
        s += i

for i in txt:
    if i in secret:
        position = secret.index(i)
        result += s[position]
    else: result += i

print(result)