distance = int(input())
full = int(input())

kaew_re_distance = (full * 15) * 0.5
kwan_re_distance = (full * 15) * 0.9

kaew = (distance // kaew_re_distance) + 1
kwan = (distance // kwan_re_distance) + 1

print(int(kaew))
print(int(kwan))