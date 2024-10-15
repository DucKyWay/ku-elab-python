txt = input().split(' ')
for i in txt:
    if i in ['for', 'and', 'with', 'of']:
        print(i, end=" ")
    else: print(i.capitalize(), end=" ")