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

def ps_ex(do, full, stand_pass):
    return (sum(do) / full) * 100

exercise = input().split(" ") # จำนวนข้อของแต่ละชุด
exercise = [int(_) for _ in exercise]
sum_ex = sum(exercise)

standard = input().split(" ") # ร้อยละเข้าเรียน ร้อยละแบบฝึกหัด
standard = [float(_) for _ in standard]

nisit = int(input())
ns_on_class, ns_passes = individual_int(nisit), individual_int(nisit)
sum_class = len(ns_on_class[0])
c = 0
for i in range(nisit):
    if ps_ex(ns_on_class[i], sum_class, standard[0]) < standard[0] and ps_ex(ns_passes[i], sum_ex, standard[1]) < standard[1]:
        c += 1
print(c)
for i in range(nisit):
    if ps_ex(ns_on_class[i], sum_class, standard[0]) >= standard[0] or ps_ex(ns_passes[i], sum_ex, standard[1]) >= standard[1]:
        print(f"{i+1} {ps_ex(ns_on_class[i], sum_class, standard[0]):.2f} {ps_ex(ns_passes[i], sum_ex, standard[1]):.2f}")
    else: print(f"({i+1}) {ps_ex(ns_on_class[i], sum_class, standard[0]):.2f} {ps_ex(ns_passes[i], sum_ex, standard[1]):.2f}")