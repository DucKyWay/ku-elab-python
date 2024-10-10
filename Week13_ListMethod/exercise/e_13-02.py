''' 1 '''

def count_factors_3_7(ls):
    count = 0
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            count += 1
    return count

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_factors_3_7(ls))


''' 2 '''

def filter_factors_3_7(ls):
    factor, not_factor = [], []
    for i in ls:
        if i <= 0: pass
        elif i % 3 == 0 or i % 7 == 0:
            factor.append(i)
        else: not_factor.append(i)
    return [factor, not_factor]

print(filter_factors_3_7([_ for _ in range(10)]))