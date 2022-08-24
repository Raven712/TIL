# n x n행렬 a. 내용물은 i x j로 이뤄짐. 이 수를 일차원배열 b에 넣으면 b 크기 n x n 임. 오름차순 했을때 b[k] 구하기. 인덱스가 1부터 시작함
import sys
sys.stdin = open('Kth.txt', 'r')
input = sys.stdin.readline

n = int(input())

A = [[0] * (n) for i in range(n)]
# print(A)
B = []

for i in range(n):
    for j in range(n):
        A[i][j] = (i + 1) * (j + 1)
        B.append(A[i][j])
        
# print(A)
B.sort()
print(B)

k = int(input())

# print(B[k])
# 일단 이건 절대아닌거같음. --> 메모리초과

start = 1
end = n ** 2

while start <= end:
    mid = (start + end) // 2
    for i in B:

# 발상자체가 어려운 문제임. 아주 나중에 풀어야할것같음
