target, guess = int(input("Enter a target (4-digit integer): ")), int(input("Enter your guess (4-digit integer): "))

correct_positions, correct_digits = 0, 0
temp_target, temp_guess = target, guess

i = 1
while i <= 4: #position
    if temp_target % 10 == temp_guess % 10: correct_positions += 1
    temp_target //= 10
    temp_guess //= 10 
    i += 1 #each digit

temp_target = target
i = 1
while i <= 4: #digit
    digit_target = temp_target % 10
    temp_target //= 10
    
    temp_guess = guess
    j = 1
    while j <= 4:
        if digit_target == temp_guess % 10:
            correct_digits += 1
            break
        temp_guess //= 10
        j += 1
    i += 1

position_s, digit_s = "position", "digit"
correct_digits -= correct_positions
if correct_positions == 4:
    print("Congratulations, you just mastered my mind!!")
else:
    if correct_positions == 0: 
        correct_positions = "No"
        position_s += "s"
    elif correct_positions == 1: correct_positions = "One"
    elif correct_positions == 2: 
        correct_positions = "Two"
        position_s += "s"
    elif correct_positions == 3: 
        correct_positions = "Three"
        position_s += "s"
        
    if correct_digits == 0: 
        correct_digits = "no"
        digit_s += "s"
    elif correct_digits == 1: correct_digits = "one"
    elif correct_digits == 2: 
        correct_digits = "two"
        digit_s += "s"
    elif correct_digits == 3: 
        correct_digits = "three"
        digit_s += "s"
    elif correct_digits == 4: 
        correct_digits = "four"
        digit_s += "s"
    
    print(f"{correct_positions} {position_s} correct, {correct_digits} {digit_s} correct")