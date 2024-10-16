def count_char(word):
    word = word.lower()
    cha = {}
    for i in word:
        if i.isalpha(): 
            if i not in cha:
                cha[i] = 1
            else:
                cha[i] += 1
    return cha

print(count_char('Hello, There'))