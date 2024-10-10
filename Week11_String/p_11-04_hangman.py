word = input()
c = 0
word_guess = []
while True:
    guess = input()
    if guess == '0':
        break
    else:
        word_guess.append(guess)
        
for i in word:
    if i in word_guess:
        c += 1

print(f"{c}/{len(word)}")