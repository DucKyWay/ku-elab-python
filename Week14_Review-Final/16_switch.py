txt = [_ for _ in input()]
len_in = len(txt)-1
for i in range(len(txt)):
    if i == (len_in/2) and (len_in%2 == 0):
        print(txt[i], end="")
    elif i > (len_in//2) and (True):
        print(txt[(len_in//2)-i], end="")
    elif i <= (len_in//2) and (len(txt) % 2 == 0):
        print(txt[(len_in//2)-i], end="")
    elif i <= (len_in//2) and (len(txt) % 2 != 0):
        print(txt[(len_in//2)-i-1], end="")