import math
def find_mode(l):
    for i in range(11):
        for j in l:
            if j == i:
                mode_score[i] += 1
    mode = max(mode_score)
    return [i for i in range(11) if mode_score[i] == mode]

scores = list()
mode_score = [0 for _ in range(11)]
i = 0
while i < 20: 
    score = int(input("Enter score: "))
    if score > 10 or score < 0:
        print("Score is out of range.")
    else:
        scores.append(score)
        i += 1

print(f"-----")
print(f"Original list:\n{scores}")
print(f"Mode of scores:")
res = find_mode(scores)
for i in res: print(i)