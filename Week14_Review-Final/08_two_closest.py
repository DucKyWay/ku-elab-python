amount, data = int(input()), []
closet, dis = [], []
for i in range(amount): 
    data.append(int(input()))
data.sort()
for i in range(amount):
    if i != amount-1:   
        dis.append(data[i+1] - data[i])
for i in range(len(dis)):
    if dis[i] == min(dis):
        print(f"{data[i]} {data[i+1]}")