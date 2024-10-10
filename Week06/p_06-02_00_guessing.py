target, count = 72, 1
guess = int(input("Enter your guess: "))
while guess != target:
    if guess > 72 and guess <= 100:
        print("Sorry, your guess is too high.")
    elif guess < 72 and guess >= 0:
        print("Sorry, your guess is too low.")
    else:
        print("Sorry, your guess is out of range.")
    count += 1
    guess = int(input("Enter your guess: "))
print("Congratulations, your guess is correct.")
print(f"Total number of guesses is {count}.")