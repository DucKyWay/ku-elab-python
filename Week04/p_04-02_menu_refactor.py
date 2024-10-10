print(f"---<< Main Menu >>---\n    <B>urger Meal\n    <C>hicken Meal\n    <P>asta Meal")
enter_menu = input("Enter your choice: ")
    
if enter_menu == 'b' or enter_menu == "B": # Burger
    print(f"---<< Burger Sub Menu >>---\n    <R>egular Burger\n    <C>heese Burger\n    <D>ouble Cheese Burger")
    enter_sub_menu = input("Enter your choice: ")

    if enter_sub_menu == 'r' or enter_sub_menu == 'R':
        price = f"Your Regular Burger is {60} Baht."
    elif enter_sub_menu == 'c' or enter_sub_menu == 'C':
        price = f"Your Cheese Burger is {75} Baht."
    elif enter_sub_menu == 'd' or enter_sub_menu == 'D':
        price = f"Your Double Cheese Burger is {90} Baht."
    else:
        price = f"Invalid sub menu choice."

elif enter_menu == 'c' or enter_menu == 'C': # Chick
    print(f"---<< Chicken Sub Menu >>---\n    <F>ried Chicken\n    <G>rilled Chicken\n    <C>hef's Chicken")
    enter_sub_menu = input("Enter your choice: ")

    if enter_sub_menu == 'f' or enter_sub_menu == 'F':
        price = f"Your Fried Chicken is {120} Baht."
    elif enter_sub_menu == 'g' or enter_sub_menu == 'G':
        price = f"Your Grilled Chicken is {150} Baht."
    elif enter_sub_menu == 'c' or enter_sub_menu == 'C':
        price = f"Your Chef's Chicken is {180} Baht."
    else:
        price = f"Invalid sub menu choice."

elif enter_menu == 'p' or enter_menu == 'P': #Pastaaaaa
    print(f"---<< Pasta Sub Menu >>---\n    <S>paghetti de Italiano\n    <L>asagna Supreme\n    <M>acaroni Special")
    enter_sub_menu = input("Enter your choice: ")
    
    if enter_sub_menu == 's' or enter_sub_menu == 'S':
        price = f"Your Spaghetti de Italiano is {90} Baht."
    elif enter_sub_menu == 'l' or enter_sub_menu == 'L':
        price = f"Your Lasagna Supreme is {120} Baht."
    elif enter_sub_menu == 'm' or enter_sub_menu == 'M':
        price = f"Your Macaroni Special is {100} Baht."
    else:
        price = f"Invalid sub menu choice."
else:
    price = f"Invalid main menu choice."

print(f"{price}")
