def check_list(l):
    check_in, check_de, check_same = 0, 0, 0
    for i in range(len(l)):
        if i == len(l)-1:
            break
        else:
            if l[i] < l[i+1]:
                check_in += 1 
            elif l[i] == l[i+1]:
                check_same += 1
            else:
                check_de += 1
    # print(check_de, check_same, check_in, len(l)-1)
    if check_same == len(l)-1: # เท่ากัน
        return "The list is in non-increasing and non-decreasing order."
    elif check_in + check_same == len(l)-1: # เพิ่ม
        return "The list is in non-decreasing order."
    elif check_de + check_same == len(l)-1: # ลด
        return "The list is in non-increasing order."
    else: # ไม่มี
        return "The list is in random order."
    
def main():
    ls = []
    while True:
        n = int(input("Enter a number (-1 to end): ")) 
        if n == -1:
            break
        elif 0 <= n <= 100:
            ls.append(n)
        else:
            print("Number is out of range.")
    print("-----")
    print(f"Original list:\n{ls}")
    if ls == []:    print("The list is empty.")
    else:           print(check_list(ls))
main()