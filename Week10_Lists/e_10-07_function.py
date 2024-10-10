# 1
scores = [60, 70, 85, 66, 70, 0, 15, 9]
number_of_scores = len(scores)
print(number_of_scores)


days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( 'There are', len(days), 'days in a week.' )


print(len([]))

# 2
scores = [60, 70, 85, 66, 70, 0, 15, 9]
total = sum(scores)
print(total)

# 3
scores = [60, 70, 85, 66, 70, 0, 15, 9]
max_score = max(scores)
print(max_score)


days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( max(days) )

# 4
scores = [60, 70, 85, 66, 70, 0, 15, 9]
min_score = min(scores)
print(min_score)


days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( min(days) )


# ex
import math
data = []
max_num = -math.inf
while True:
    txt = input()
    if txt == '':
        break
    else:
        data.append(txt)

for i in data:
    if len(i) >= max_num:
        max_num = len(i)
        max_str = i
print(max_str)