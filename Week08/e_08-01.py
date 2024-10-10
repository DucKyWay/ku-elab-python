'''Exercise 1, 2, 3'''
# def fn1(x, y):
#     g = x // (10 ** (y - 1)) % 10
#     return g

# print(fn1(12345, 3)) # 3
# print(fn1(fn1(12345, 10), 4)) # 0
# print(fn1(12345, 5)) * 5

'''Exercise 4 
ชื่อฟังก์ชัน: f1
Parameter: รับข้อมูล a เป็นจำนวนเต็ม และรับ b เป็นเลขโดด
Process: ใช้ while loop นับว่ามีเลขโดดใน a ที่มีค่ามากกว่าหรือเท่ากับ b กี่ตัว
Return: จำนวนที่นับได้
'''
def f1(n, chk):
    count = 0
    while True:
        v_n = n % 10
        n //= 10
        if v_n >= chk:
            count += 1
        if n <= 0:
            break
    return count

a, b = int(input()), int(input())
print(f1(a, b))

'''Exersise 5
รับจำนวนเต็มบวก 2 จำนวน บรรทัดละจำนวน โดยจำนวนแรกเป็นเลขโดด 
แล้วแสดงผลลัพธ์ว่ามีเลขโดดในจำนวนที่สองที่มีค่ามากกว่าหรือเท่ากับเลขโดดจำนวนแรกที่รับเข้ามากี่ตัว 
โดยเรียกใช้ฟังก์ชัน f1 จากข้อ 4.
'''
a, b = int(input()), int(input())
print(f1(b, a))