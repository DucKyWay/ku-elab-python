inc = float(input())
ex = float(input())

print("1234567890" * 3)

total_income = f"Total Income{inc:+9.2f} bahts"
expense = f"Expense{ex:+14.2f} bahts"
profit = f"Profit{' ':>7s}{inc+ex:08.2f} bahts"
print(f"{total_income}\n{expense}\n{profit}")