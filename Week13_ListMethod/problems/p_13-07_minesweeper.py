def show(table):
    for i in table:
        for j in i: 
            print(j, end="")
        print()    
        
def increase(table, r, c):
    if table[r][c] != '*':
        table[r][c] += 1
    return table

def add_bomp(table, row, column):
    table[row][column] = "*"
    return table

def add_count(table):
    for r in range(len(table)):
        for c in range(len(table[r])):
            if table[r][c] == '*':
                if r == 0 and c == 0: # ซ้ายบน
                    increase(table, r, c+1)
                    increase(table, r+1, c)
                    increase(table, r+1, c+1)
                elif r == 0 and c == len(table[r])-1: # ขวาบน
                    increase(table, r, c-1)
                    increase(table, r+1, c)
                    increase(table, r+1, c-1)
                elif r == len(table) - 1 and c == 0: # ซ้ายล่าง
                    increase(table, r-1, c)
                    increase(table, r-1, c+1)
                    increase(table, r, c+1)
                elif r == len(table) - 1 and c == len(table[r]) - 1: # ขวาล่าง
                    increase(table, r-1, c)
                    increase(table, r-1, c-1)
                    increase(table, r, c-1)
                elif r == 0: # บน
                    increase(table, r, c-1)
                    increase(table, r, c+1)
                    increase(table, r+1, c-1)
                    increase(table, r+1, c)
                    increase(table, r+1, c+1)
                elif r == len(table) - 1: # ล่าง
                    increase(table, r-1, c-1)
                    increase(table, r-1, c)
                    increase(table, r-1, c+1)
                    increase(table, r, c-1)
                    increase(table, r, c+1)
                elif c == 0: # ซ้าย
                    increase(table, r-1, c)
                    increase(table, r-1, c+1)
                    increase(table, r, c+1)
                    increase(table, r+1, c)
                    increase(table, r+1, c+1)
                elif c == len(table[r]) - 1: # ขวา
                    increase(table, r-1, c-1)
                    increase(table, r-1, c)
                    increase(table, r, c-1)
                    increase(table, r+1, c-1)
                    increase(table, r+1, c)
                else: # ใน
                    increase(table, r-1, c-1)
                    increase(table, r-1, c)
                    increase(table, r-1, c+1)
                    increase(table, r, c-1)
                    increase(table, r, c+1)
                    increase(table, r+1, c-1)
                    increase(table, r+1, c)
                    increase(table, r+1, c+1)
    return table

# size
size = input().split("x")
table = []
for i in range(int(size[0])):
    table.append([0 for j in range(int(size[1]))])

# amount bomp
amount = int(input())
for _ in range(amount):
    pos = input().split(",")
    table = add_bomp(table, int(pos[0]), int(pos[1]))

table = add_count(table)

# show
show(table)
