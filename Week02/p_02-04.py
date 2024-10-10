print("First fraction:")
a = int(input(">>Enter a numerator a: "))
b = int(input(">>Enter a denominator b: "))
print("Second fraction:")
c = int(input(">>Enter a numerator c: "))
d = int(input(">>Enter a denominator d: "))

q = b * d
p = (a * d) + (c * b)
print("Summation of the two fractions is", p, "/", q)