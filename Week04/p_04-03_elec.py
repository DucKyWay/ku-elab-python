tv = int(input("How many TVs? "))
dvd = int(input("How many DVD players? "))
aud = int(input("How many Audio Systems? "))
price = (tv*6000) + (dvd*1500) + (aud*3000)
print(f"Total price is {price:.2f} baht.")
if price >= 24000:
    sale = price*0.8
    print(f"You've got a discount of {price-sale:.2f} baht.")
    print(f"Your payment is {sale:.2f} baht. Thank you!")
else:
    print(f"Your payment is {price:.2f} baht. Thank you!")