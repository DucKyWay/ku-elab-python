num = int(input())
recent, can = 0, 0
while num >= 0:
    if num > recent:
        can += 1
        recent = num
    num = int(input())
print(can)