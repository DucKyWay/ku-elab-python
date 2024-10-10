player = int(input())
hand, score = [], [0 for _ in range(player)]
for _ in range(player):
    hand.append(input().split(" "))
for i in range(player):
    for j in range(len(hand[i])):
        if hand[i][j] == 'J' or hand[i][j] == 'Q' or hand[i][j] == 'K': 
            hand[i][j] = 10
        elif hand[i][j] == 'A':
            hand[i][j] = 1
        else: 
            hand[i][j] = int(hand[i][j])
            
for i in range(player):    
    for j in hand[i]:
        score[i] += j
        if score[i] > 16:
            break
    if score[i] > 21:
        print("busted")
    else:
        print(score[i])
