N, M = map(int, input().split()) # N은 카드갯수 M은 목적점수 (초과불가)

card = list(map(int,input().split()))   # 길이 N

sum_ = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):           #정확히는 range(1, N - 1)이 아니고, i + 1로해야된다 !!
        for x in range(j + 1, N): 
            if card[i] + card[j] + card[x] <= M and card[i] + card[j]  + card[x] > sum_:
                sum_ = card[i] + card[j] + card[x]

print(sum_)