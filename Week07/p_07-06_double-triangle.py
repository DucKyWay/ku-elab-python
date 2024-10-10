def star(amount, line):
    if line % 2 == 0:
        print(' *'*amount, end='')
    else:
        print('* '*amount, end='')
    print()

def main():
    height = int(input("Enter height: "))
    width = int(input("Enter width: "))
    if width <= 0 or height <= 0:
        print(f"Invalid input, program terminates.")
    else:
        i = 1
        while i <= height:
            star(width, i)
            i += 1
main()