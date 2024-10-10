import random
target = random.randint(0, 101)
count = 1
guess = int(input("Enter your guess: "))

while guess != target:
    if guess > target and guess <= 100:
        print("Sorry, your guess is too high.")
    elif guess < target and guess >= 0:
        print("Sorry, your guess is too low.")
    else:
        print("Sorry, your guess is out of range.")
    count += 1
    guess = int(input("Enter your guess: "))
print("Congratulations, your guess is correct.")
print(f"Total number of guesses is {count}.")