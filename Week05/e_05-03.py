count = 0
sum_x = 0
max_x = 0
min_x = 999999999999999999
avg_x = 0
x = input()
while x != "":
    x = float(x)
    sum_x += x
    if x >= max_x:
        max_x = x
    if x <= min_x:
        min_x = x
    count += 1
    x = input()

avg_x = sum_x / count
print(f"{max_x:.2f} {min_x:.2f}")
print(f"{sum_x:.2f} {avg_x:.2f}")