f,s = int(input("Enter the first number: ")), int(input("Enter the second number: "))
f_l, s_l = f, s
gcd, lcm = 0, 0
gcd = f_l % s_l
while gcd > 0:
  f_l = s_l
  s_l = gcd
  gcd = f_l % s_l

lcm = (f*s)/s_l

print(f"  >> gcd({f}, {s}) ={s_l:7}")
print(f"  >> lcm({f}, {s}) ={lcm:7n}")
