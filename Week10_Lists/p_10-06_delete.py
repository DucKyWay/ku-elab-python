def remove_duplicates(t):
    not_dup = []
    for i in t:
        if i not in not_dup:
            not_dup.append(i)
    return not_dup

remove_duplicates([1, 2, 3, 2, 1, 2, 3, 4])
# [1, 2, 3, 4]
remove_duplicates(['a', 'b', 'c', 'e', 'f'])
# ['a', 'b', 'c', 'e', 'f']
remove_duplicates([2, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3])
# [2, 1, 3]