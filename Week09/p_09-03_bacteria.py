def nb_year(p0, percent, aug, p):
    percent = percent/100
    now_p, day = p0, 0
    while True:
        if now_p >= p:
            break
        now_p = int(now_p) + int(now_p)*percent + aug
        day += 1
          
    return day

# print(nb_year(1000, 2, 30, 1150))
# print(nb_year(1500000, 0.25, 1000, 2000000))