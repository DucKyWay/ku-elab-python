def individual_int(nisit):
    ls = [0 for _ in range(nisit)]
    for i in range(nisit):
        ls[i] = input().split(" ")
        ls[i] = [int(_) for _ in ls[i]] 
    return ls

def count_on_class(on_class):
    dt = {}
    for i in range(len(on_class)):
        dt[i+1] = sum(j for j in on_class[i]) 
    return dt

def can_sob():
    return 0

exercise = input().split(" ") # จำนวนข้อของแต่ละชุด
exercise = [int(_) for _ in exercise]
sum_ex = 0
for c in exercise: sum_ex += c

standard = input().split(" ") # ร้อยละเข้าเรียน ร้อยละแบบฝึกหัด
standard = [float(_) for _ in standard]

nisit = int(input())
ns_on_class = individual_int(nisit)
ns_passes = individual_int(nisit)

print(exercise, sum_ex)
print(standard)
print("== การเข้าห้องเรียนของแต่ละคน ==")
print(count_on_class(ns_on_class))
print("== จำนวนข้อที่ทำผ่านของแต่ละ ex ==")
for i in ns_passes: print(i)

# print จำนวนของนิสิตที่หมดสิทธิ์สอบปฏิบัติการปลายภาค
# print (nitsit_id) ร้อยละการเขีาเรียน ร้อยละค.สำเร็จแบบฝึก