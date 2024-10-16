def cloth_size(width_list):
    width = {
        'S': 0,
        'M': 0,
        'L': 0,
    }
    for i in width_list:
        if i <= 36: width['S'] += 1
        elif 36 < i <= 44: width['M'] += 1
        elif i > 44: width['L'] += 1
    return width

print(cloth_size([50, 44, 40, 48]))

