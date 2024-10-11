import math

ls = []
sum = -math.inf
while True:
    num = int(input())
    if num == 0:    break
    else:           ls.append(num)

for i in range(len(ls)):
    for j in range(len(ls)):
        if i != j:
            if ls[i] + ls[j] > sum:
                print(ls[i], ls[j], ls[i] + ls[j])
                sum = ls[i] + ls[j]
print(sum)

