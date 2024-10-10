damage, hp = int(input()), input().split(' ')
hp = [int(i) for i in hp]

c = 0
for i in range(len(hp)):
    while True:
        if hp[i] > 0:
            hp[i] -= damage
            c += 1
            if hp[i] <= 0:
                hp[i] = c
                break
        else: 
            c = 0
            break
print(hp[-1])
for i in hp:
    print(i, end=" ")