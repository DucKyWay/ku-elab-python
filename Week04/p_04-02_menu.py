menu_list = ["---<< Main Menu >>---", "    <B>urger Meal", "    <C>hicken Meal", "    <P>asta Meal"]
burger_list = ["---<< Burger Sub Menu >>---", "    <R>egular Burger", "    <C>heese Burger", "    <D>ouble Cheese Burger"]
chicken_list = ["---<< Chicken Sub Menu >>---", "    <F>ried Chicken", "    <G>rilled Chicken", "    <C>hef's Chicken"]
pasta_list = ["---<< Pasta Sub Menu >>---", "    <S>paghetti de Italiano", "    <L>asagna Supreme", "    <M>acaroni Special"]

print("\n".join(menu_list))
enter_menu = input("Enter your choice: ")

def show_sub_menu(enter_menu):
    
    if enter_menu == 'b' or enter_menu == "B": # Burger
        print("\n".join(burger_list))
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
        print("\n".join(chicken_list))
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
        print("\n".join(pasta_list))
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

    return price

print(f"{show_sub_menu(enter_menu)}")
