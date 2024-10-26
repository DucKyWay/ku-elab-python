exercise = input().split(" ") # จำนวนข้อของแต่ละชุด
exercise = [int(_) for _ in exercise]

standard = input().split(" ")
standard = [float(_) for _ in standard]

nisit = int(input())
ns_on_class = [0 for i in range(nisit)]
ns_passes = [0 for i in range(nisit)]

for i in range(nisit):
    ns_on_class[i] = input().split(" ")
for i in range(nisit):
    ns_passes[i] = input().split(" ")

print(exercise)
print(standard)
print("== การเข้าห้องเรียนของแต่ละคน ==")
for i in ns_on_class: print(i)
print("== จำนวนข้อที่ทำผ่านของแต่ละ ex ==")
for i in ns_passes: print(i)