# 정수 n개가 주어짐. 이 정수는 A에 등록, m개 정수가 주어짐. 이 정수들이 A에 있는지 확인하기. 들어있으면 1, 없으면 0 출력
import sys
# sys.stdin = open('find.txt', 'r')

input = sys.stdin.readline

n = int(input()) # 10만 이하
A = set(map(int, input().split()))      # 여긴 들어있는지만 확인하면되니까 굳이 리스트 사용할 필요 없을것같음...


m = int(input())
list_m = list(map(int, input().split()))

# 이진 탐색을 하기엔 주어지는 수가 정렬되어있지않음.. for를 써야하나?

for i in list_m:
    if i in A:
        print(1)
    else:
        print(0)