submit = [_ for _ in input()]
have_point = [_ for _ in input()]
re_point = []
for i in have_point:
    if i not in re_point:
        re_point.append(i)
submit.pop(0)
submit.pop(-1)

score = 0
for i in range(len(submit)):
    for j in re_point:
        if submit[i] == j:
            score += 1
print(score)
if submit == []:
    print(f"{0:.2f}")
else:
    print(f"{score/len(submit)*100:.2f}")