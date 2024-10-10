frame, count = 1, 1
score, down = 0, 0

while count <= 10:
    if frame == 1:
        print(f"Frame # {count}")
        down = int(input("  Number of pins down: "))
        score += down
        if down == 10:
            count += 1
            continue
        frame += 1
    elif frame == 2:
        print(f"Frame # {count}")
        down = int(input(f"  Number of pins down (0-{10-down}): "))
        score += down
        down += down

        frame = 1
        count += 1
print(f"Total score is {score}")
