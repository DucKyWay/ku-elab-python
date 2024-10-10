txt, en, space = input(), [], '-_=.$'
ltxt, i = len(txt), 0
if ltxt != 0:
    while i < ltxt:
        if en != []:
            if txt[i] in space:
                if i != ltxt-1:
                    if txt[i+1] not in space:
                        i += 1
                        en.append(txt[i].upper())
            else:
                en.append(txt[i].lower())
        else:
            if txt[i] not in space:
                en.append(txt[i].lower())
        i += 1

    if en[-1] in space: en.pop()
    for i in en:
        print(i, end='')
else:
    print()