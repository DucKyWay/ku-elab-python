txt = input()
count, new_txt = 0, ''
for i in range(len(txt)):
    if txt[i] not in new_txt:
        # sth
print(new_txt)