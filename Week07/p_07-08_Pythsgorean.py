def main():
    num = int(input())
    i = 1
    case = 0
    while i <= num:
        j = i
        while j <= num:
            #print(i, j)
            if i**2 + j**2 == num**2:
                case += 1
                #print("case:", case)
            j += 1
        i += 1 
    print(case)
main()