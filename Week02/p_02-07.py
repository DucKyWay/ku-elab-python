import math
x, y, z = float(input("Enter x: ")), float(input("Enter y: ")), float(input("Enter z: "))
print(f"a1 = {math.pow(x, y) + z:.2f}")
print(f"a2 = {math.cos(2*math.pi) + math.log(x, math.e):.2f}")
print(f"a3 = {math.fabs(x) + math.fabs(y):.2f}")
print(f"a4 = {math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)):.2f}")
print(f"a5 = {(math.sin(x))**2 + (math.cos(x))**2:.2f}")
print(f"a6 = {math.pow(x+y, 1/5):.2f}")
print(f"a7 = {math.pow(math.e, x*math.log(y, math.e)):.2f}")