weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight/(height*height)

if bmi >= 30:
    print(f"BMI is {bmi:.1f}")
    print(f"Obesity")
elif bmi >= 25:
    print(f"BMI is {bmi:.1f}")
    print(f"Overweight")
elif bmi >= 18.5:
    print(f"BMI is {bmi:.1f}")
    print(f"Normal weight")
else:
    print(f"BMI is {bmi:.1f}")
    print(f"Underweight")