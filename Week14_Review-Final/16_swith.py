#abcde	baced
#abcdef	cbafed

txt = [_ for _ in input()]
for i in range(len(txt)):
    if i >= (len(txt)-1)//2:
        print(i, txt[i])
    else:
        print(i, txt[i])