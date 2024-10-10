'''
    -- JA MOR SOR BECAUSE KOR NEE LAE --
'''

all_ex = int(input())
percent = float(input()) * 0.01
n = int(input()) # Nisit
article = []
for i in range(n):
    article.append(int(input()))

criterion = all_ex * percent
can_sob = [0 for i in range(n)]
for i in range(n):
    if article[i] >= criterion:
        can_sob[i] = 1
        # print(f"{can_sob} {article[i]} {criterion}")

c = 0
for i in can_sob:
    if i == 0:
        c += 1
print(c)

for i in range(n):
    if can_sob[i] == 1:
        print(f"{i+1} {article[i]/all_ex * 100:.2f}")
    elif can_sob[i] == 0:
        print(f"({i+1}) {article[i]/all_ex * 100:.2f}")