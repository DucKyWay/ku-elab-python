import math

hr = int(input("Enter number of hours: "))
m = int(input("Enter number of minutes: "))

m_total = (hr*60)+m
total = 0

if hr >= 0 and m >= 0 and m_total >= 0 and m < 60:
    if m_total <= 15:
        total = 0
    elif m_total > 15: 
        total = total + 10
    
    if m_total >= 120:
        m_total = m_total - 120
        hr2 = math.ceil(m_total/60) * 10
        total = total + hr2
    
    if total != 0:
        print(f"Total amount due is {total} Bahts.")
    elif total == 0:
        print("No charge, thanks.")
else:
    print("Input Error!")