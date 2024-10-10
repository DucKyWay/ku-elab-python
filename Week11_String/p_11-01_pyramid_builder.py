layer = int(input())
for i in range(layer):
    print(f"|{' '*(layer-i-2//2)}{'*'*(i+1)}{'*'*(i)}{' '*(layer-i-2//2)}|")