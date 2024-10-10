import math
def find_sd(l):
    xi = 0
    for i in l:
        xi += (i - sum(l)/len(l))**2
    return math.sqrt(xi/(len(l)-1))

scores = list()
new_scores = list()
while True: 
    score = float(input("Enter score: "))
    if score == -1:
        break
    elif score > 100 or score < -1:
        print("Score is out of range.")
    else:
        scores.append(score)

if scores != []:
    print(f"Maximum score is {max(scores):.2f}.")
    print(f"Minimum score is {min(scores):.2f}.")
    print(f"Average score is {sum(scores)/len(scores):.2f}.")
    print(f"Standard deviation is {find_sd(scores):.2f}.")