target = 72
guess = int(input("Enter your guess (0 - 100): "))

if guess == target:
    print("Congratulations, your guess is correct.")
elif guess > 100 or guess < 0:
    print("Sorry, out of range, try again later.")
else:
    print("Sorry, your guess is wrong, try again later.")