scores = list()
x = 1
while x <= 20: 
    score = int(input("Enter score: "))
    if score > 10 or score < 0:
        print("Score is out of range.")
    else:
        scores.append(score)
        x += 1

sorted_scores = sorted(scores)
print("Original list:")
print(scores)
for i in range(11):
    print(f"{i:>2} ", end="")
    for j in sorted_scores:
        if j == i:
            print("*", end="")
    print()
