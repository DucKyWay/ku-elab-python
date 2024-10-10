# i lucus dek narok
encode, decode = [_ for _ in input()], []
count = len(encode)-1
i = 0
while i <= count:
    if i != count and i != count-1:
        if encode[i] in 'aeiou' and encode[i+1] == 'p' and encode[i+2] == encode[i]:
            decode.append(encode[i])
            i += 2
        else:
            decode.append(encode[i])
        i += 1
    else:
        decode.append(encode[i])
for i in decode:
    print(i, end="")