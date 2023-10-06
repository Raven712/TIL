#팔린책 제목 . 제일많이팔린책 적기. 제목이 입력. 베스트셀러 출력.

N = int(input())
book2 = []
count = {}
for i in range(1, N + 1):
    book = input()
    book2.append(book)          ## 이부분을 그냥 if book not in count: count[book] = 1 이런식으로 할수도 있음. else엔 +1 추가하고
    count[book] = 0

for i in book2:
    count[i] = count[i] + 1

val = count.values()
max_v = max(val)

count_max = 0
count_max_L = []
for i in count:
    if count[i] == max_v:
        count_max += 1
        count_max_L.append(i)

count_max_L = sorted(count_max_L)


print(count_max_L[0])