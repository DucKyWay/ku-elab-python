food = input('Enter your buffet choice: ')
if food == "Japanese":
    day = input("Is today Wednesday (yes/no)? ")
    if day == "yes":
        print(f"Your payment is {1000*0.85:.2f} Baht.")
    else:
        print(f"Your payment is {1000:.2f} Baht.")
        
elif food == "Korean":
    day = input("Is today Wednesday (yes/no)? ")
    if day == "yes":
        print(f"Your payment is {1500*0.85:.2f} Baht.")
    else:
        print(f"Your payment is {1500:.2f} Baht.")

else:
    print(f"Sorry, there is no {food} buffet.")