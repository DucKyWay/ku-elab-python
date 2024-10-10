print("Upper left corner coordinate: ")
x = int(input("  << x axis: "))
y = int(input("  << y axis: "))
x2 = x + int(input("  << Eastern: "))
y2 = y - int(input("  << Southern: "))
print("Enter a coordinate: ")
point_x = int(input("  << x axis: "))
point_y = int(input("  << y axis: "))

if x <= point_x <= x2 and y2 <= point_y <= y:
    print(f">>> ({point_x:.2f}, {point_y:.2f}) is inside the rectangle.")
else:
    print(f">>> ({point_x:.2f}, {point_y:.2f}) is not inside the rectangle.") 