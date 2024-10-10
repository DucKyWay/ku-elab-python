def accum_sum(l):
    new_list.append(l)
    return sum(new_list)

ls = []
new_list = []
total = 0
while True:
    num = int(input("Enter a number (0 to end): "))
    if 1 <= num <= 999:
        ls.append(num)
    elif num == 0:
        break
    else:
        print("Number is out of range.")

print("Original list:")
print(ls)
print("Accumulative Sum:")
for i in ls:
    print(accum_sum(i))