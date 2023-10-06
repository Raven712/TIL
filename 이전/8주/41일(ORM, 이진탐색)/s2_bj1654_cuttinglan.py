import sys
sys.stdin = open('cut.txt', 'r')
input = sys.stdin.readline

k, n = map(int, input().split()) #가진거 필요한거
lan = []            # 랜 길이는 자연수

for i in range(k):
    lan.append(int(input()))

lan.sort()

start = 1
end = max(lan)
#왜 이문제는 이분탐색인가 . 

while start <= end:
    mid = (start + end) // 2
    line = 0
    for i in lan:
        line += i // mid
    if line >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)


