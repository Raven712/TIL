T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
d = []
s = set()
for i in range(1, T+1):
    if T % i == 0:
        d.append(i)
s = set(d)
d2 = sorted(list(s))
for i in d2:
    print(i, end = ' ')