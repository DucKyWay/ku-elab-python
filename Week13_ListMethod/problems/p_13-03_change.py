def count(bank, remain):
    return remain//bank

type = int(input())
bank = [int(input()) for _ in range(type)]
bank.sort(reverse=True)
amount = int(input())

for i in range(type):
    print(f"{bank[i]}: {count(bank[i], amount)}")
    amount -= bank[i]*count(bank[i], amount)
