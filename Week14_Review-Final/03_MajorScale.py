scale, find = input().split(','), int(input())

i, j = 0, 0
while i < find:
    if j == 7:
        j = 0
    j += 1
    i += 1
print(scale[j-1])