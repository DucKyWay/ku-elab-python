# very new logic ahhhhhhhhh
ans, guess = input(), input()
correct, have = 0, 0
ans_use = [False for _ in range(len(ans))]
guess_use = [False for _ in range(len(guess))]

for i in range(len(ans)):
    if ans[i] == guess[i]:
        correct += 1
        ans_use[i] = True
        guess_use[i] = True

for i in range(len(guess)):
    if not guess_use[i]:
        for j in range(len(ans)):
            if not ans_use[j] and guess[i] == ans[j]:
                have += 1
                ans_use[j] = True
                break

print(f"{correct}-{have}")