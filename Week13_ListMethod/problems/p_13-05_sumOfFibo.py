def fibo(n):
    if n == 1 or n == 0: 
        return 1
    else:        
        return fibo(n-1) + fibo(n-2)

n, type = int(input()), input().lower()
result = 0
if n < 0:
    print("ERROR")
else:
    if type == 'e':
        for i in range(0, n+1, 2):
            result += fibo(i)
        print(result)
    elif type == 'o':
        if n == 0:
            print("ERROR")
        else:
            for i in range(1, n+1, 2):
                result += fibo(i)
            print(result)
    else: 
        print("ERROR")