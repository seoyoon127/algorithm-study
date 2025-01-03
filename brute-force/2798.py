from itertools import combinations
inputs = list(map(int, input().split()))
N, M = inputs[0], inputs[1]
card = list(map(int, input().split()))
answer = 0
for combo in combinations(card, 3):
    sum3 = sum(i for i in combo)
    if sum3 <= M:
        answer=max(answer,sum3)
        if answer == M:
            break
print(answer)