age, income = int(input("Enter your age: ")), int(input("Enter your net income: "))
if age >= 15 and age <= 60:
    if income >= 80000:
        print("Invalid income.")
    elif income >= 30000 and income <= 79999:
        print(f"Your negative income tax is {(80000-income)*0.12:.2f} Baht.")
    elif income >= 1 and income <= 29999:
        print(f"Your negative income tax is {income*0.2:.2f} Baht.")
    else:
        print("Invalid income.")
else:
    print("Invalid age.")