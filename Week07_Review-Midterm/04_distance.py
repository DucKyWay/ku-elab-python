import math
a_x, a_y, b_x, b_y = 1, 1, 1, 1
while a_x != 0 and a_y != 0 and b_x != 0 and b_y != 0:
    print("<<Point a>>")
    a_x, a_y = int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))
    print("<<Point b>>")
    b_x, b_y = int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))
    if a_x != 0 and a_y != 0 and b_x != 0 and b_y != 0:
        print(f"Distance between ({a_x}, {a_y}) and ({b_x}, {b_y}):")

        euclidean = math.sqrt(math.pow((a_x - b_x), 2) + math.pow((a_y - b_y), 2))
        print(f"Euclidean distance is {euclidean:.2f}.")

        horizontal, vertical = abs(a_x - b_x), abs(a_y - b_y)
        print(f"Horizontal distance is {horizontal}.\nVertical distance is {vertical}.")

        if horizontal == 0 and vertical == 0:
            news = "nowhere"
            
        elif a_x - b_x > 0: #left
            if a_y - b_y > 0: #down
                news = "south-west"
            elif a_y - b_y == 0:
                news = "west"
            elif a_y - b_y < 0: #up
                news = "north-west"
            
        elif a_x - b_x < 0:  #right
            if a_y - b_y > 0: #down
                news = "south-east"
            elif a_y - b_y == 0:
                news = "east"
            elif a_y - b_y < 0: #up
                news = "north-east"
            
        elif a_x - b_x == 0:  
            if a_y - b_y > 0: #down
                news = "south"
            elif a_y - b_y < 0: #up
                news = "north"
        print(f"We are going {news}.")
print("Goodbye")