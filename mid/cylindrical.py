import math
x1, x2 = float(input()), float(input())
y1, y2 = float(input()), float(input())
r = float(input())

h = math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(f"{math.pi * r**2 * h:.2f}")