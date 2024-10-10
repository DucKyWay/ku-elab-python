txt, count = input(), int(input())
new_txt = ''
if count > 0:
    count %= len(txt)-1
    for i in range(len(txt)-count, len(txt)):
        new_txt += txt[i]
    for i in range(len(txt)-count):
        new_txt += txt[i]
elif count < 0:
    count = count % len(txt)
    print(count)
    for i in range(abs(count), len(txt)):
        new_txt += txt[i]
    for i in range(abs(count)):
        new_txt += txt[i]
else: new_txt = txt

print(new_txt)