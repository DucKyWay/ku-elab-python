import math

x = float(input("Enter x : "))
if x < 0:
    result = math.ceil( math.sqrt(math.pow(x, 2) + 1) )
elif x == 0:
    result = math.ceil( x )
elif x > 0 and x <= 99:
    result = math.ceil( 3*x**2 - math.pow(1-x, 2) )
elif x > 99:
    result = math.ceil( 2*x**3 - x/(math.sqrt(x+1)) )
    
print(f"f({x:.2f}) = {result}")