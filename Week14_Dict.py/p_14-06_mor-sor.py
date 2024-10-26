def count_on_class(on_class):
    dt = {}
    for i in range(len(on_class)):
        dt[i] = sum(j for j in on_class[i]) 
    return dt

exercise = input().split(" ") # จำนวนข้อของแต่ละชุด
exercise = [int(_) for _ in exercise]

standard = input().split(" ")
standard = [float(_) for _ in standard]

nisit = int(input())
ns_on_class = [0 for i in range(nisit)]
for i in range(nisit):
    ns_on_class[i] = input().split(" ")
    ns_on_class[i] = [int(_) for _ in ns_on_class[i]] 

ns_passes = [0 for i in range(nisit)]
for i in range(nisit): 
    ns_passes[i] = input().split(" ")
    ns_passes[i] = [int(_) for _ in ns_passes[i]] 


print(exercise)
print(standard)
print("== การเข้าห้องเรียนของแต่ละคน ==")
print(count_on_class(ns_on_class))
print("== จำนวนข้อที่ทำผ่านของแต่ละ ex ==")
for i in ns_passes: print(i)