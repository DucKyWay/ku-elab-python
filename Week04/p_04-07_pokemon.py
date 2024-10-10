pokemon_level = int(input("Enter level pokemon: "))
pokeball_level = input("Enter level pokeball: ").lower()
distance = int(input("Enter distance: "))
s = 0

if pokemon_level >= 0 and pokemon_level <= 40:
    if pokeball_level == 'h':
        pokeball_level = 0.01
    elif pokeball_level == 'm':
        pokeball_level = 0.03
    elif pokeball_level == 'l':
        pokeball_level = 0.05

elif pokemon_level >= 41 and pokemon_level <= 60:
    if pokeball_level == 'h':
        pokeball_level = 0.01
    elif pokeball_level == 'm':
        pokeball_level = 0.05
    elif pokeball_level == 'l':
        pokeball_level = 0.03
        
elif pokemon_level >= 61 and pokemon_level <= 100:
    if pokeball_level == 'h':
        pokeball_level = 0.01
    elif pokeball_level == 'm':
        pokeball_level = 0.08
    elif pokeball_level == 'l':
        pokeball_level = 0.1


s = 100 - (pokemon_level * distance * pokeball_level)
if s < 0 :
    print("0.00 percent.")
elif s > 100:
    print("100.00 percent.")
else:
    print(f"{s:.2f} percent.") 