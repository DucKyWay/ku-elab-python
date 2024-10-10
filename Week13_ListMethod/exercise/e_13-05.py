''' 1 '''
ls = input().split('.')
print(ls)

''' 2 '''
ls = input().split('.')
ls = [int(i) for i in ls]
print(ls)

''' 3 '''
pos_1, pos_2 = input().split(','), input().split(',')
print(f"{float(pos_1[0]) + float(pos_2[0])},{float(pos_1[1]) + float(pos_2[1])}")