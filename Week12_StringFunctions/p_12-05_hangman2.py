txt = [_ for _ in input()]
game, fail = ["-" for _ in range(len(txt))], 5

while True:
    guess = input()
    if fail > 0 and guess != '0':
        if guess in txt:
            for i in range(len(txt)):
                if guess == txt[i]:
                    game[i] = guess
        else: fail -= 1
    else: break

for i in game: print(i, end="")