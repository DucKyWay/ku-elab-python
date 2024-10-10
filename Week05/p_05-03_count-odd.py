num = int(input("Enter number: "))
count = 0
while num >= 0:
    if num % 2 != 0:
        count += 1
    num = int(input("Enter number: "))
print(f"Received {count} odd numbers")