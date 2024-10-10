txt, result = input(), ""
for i in txt:
    if i in 'aeiouAEIOU': result += i.upper()
    elif i not in 'aeiouAEIOU': result += i.lower()
print(result)