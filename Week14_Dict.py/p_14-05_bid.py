history = {}
order = 0
while True:
    bid = input()
    if bid == 'end': break
    elif bid == '':  continue
    name, price = bid.split(" ")
    price = float(price)
    
    if name not in history:
        history[name] = {"price": 0, "time": 0, "order": 0}

    if price > history[name]["price"]:
        history[name]["price"] = price
        history[name]["order"] = order 
    history[name]["time"] += 1
    order += 1

history = dict(sorted(history.items()))
# kong bid at the price of 300.0 baht in 2 times.
for k, v in history.items():
    if v['time'] > 1:
        print(f"{k} bid at the price of {v['price']} baht in {v['time']} times.")
    else: print(f"{k} bid at the price of {v['price']} baht in {v['time']} time.")
    # print(k, v)

if history != {}:
    winner = max(history, key=lambda k: (history[k]['price'], -history[k]['order']))
    print(f"The winner is {winner}.")