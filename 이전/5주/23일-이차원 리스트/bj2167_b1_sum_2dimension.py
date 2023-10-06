# 2차원 배열 주어짐, i,j ~ x,y 까지 저장된수 합 구하기
# N x M 행렬
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
temp = 0
list_ = []

for i in range(N):
    temp = list(map(int, input().split()))         # temp 길이가 M
    list_.append(temp)

K = int(input())
sum = 0

for _ in range(K):
    i, j, x, y = map(int, input().split())      #여기서 list_[i-1][j-1] 부터 list_[x-1][y-1] 까지 더해야됨..

    for p in range(i-1, x):
        for q in range(j-1, y):
            sum += list_[p][q]
    print(sum)
    sum = 0
