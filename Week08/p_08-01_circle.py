import math
def circle(r):
    return math.pi * r * r
def circumference(r):
    return 2 * math.pi * r
def sphere(r):
    return 4/3 * math.pi * math.pow(r, 3)

r = float(input("Enter a radius: "))

print('Area of a circle with radius {:.2f} is {:.2f}.'.format(r, circle(r)))
print('Circumference of a circle with radius {:.2f} is {:.2f}.'.format(r, circumference(r)))
print('Volume of sphere with radius {:.2f} is {:.2f}.'.format(r, sphere(r)))