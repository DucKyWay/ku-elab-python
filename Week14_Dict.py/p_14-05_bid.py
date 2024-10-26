history = {}
time = {}
while True:
    bid = input()
    if bid == 'end': break
    [bid, price] = bid.split(" ")
    history[bid] = float(price)
    if bid not in time:
        time[bid] = 1
    else: time[bid] += 1
print(f"{history} {time}")