def show_high(hand):
    if 'K' in hand:
        return 'K'
    elif 'Q' in hand:
        return 'Q'
    elif 'J' in hand:
        return 'J'
    else:
        hand = [1 if i == 'A' else i for i in hand]
        hand = [int(i) for i in hand]
        return max(hand)

hand = input().split(' ')
hand_op = []
for i in range(len(hand)):
    if hand[i] == 'A': hand_op.append(1)
    elif hand[i] in 'JQK': hand_op.append(10)
    else: hand_op.append(int(hand[i]))
score = 0
for i in range(len(hand_op)):
    if score > 16:
        break
    else:
        score += hand_op[i]
print(show_high(hand))
if score <= 21: print(score)
else: print('busted')