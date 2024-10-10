def filter_sort_factors_3_7(ls):
    ls_1, ls_2 = [], []
    for i in ls:
        if i <= 0:  pass
        elif i % 3 == 0 or i % 7 == 0:
            ls_1.append(i)
        elif i % 3 != 0 and i % 7 != 0:
            ls_2.append(i)
    ls_1.sort()
    ls_2.sort(reverse=True)
    return [ls_1, ls_2]

ls = [i for i in range(-10, 11)]
print(filter_sort_factors_3_7(ls))
