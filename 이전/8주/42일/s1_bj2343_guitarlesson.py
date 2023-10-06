# n개의 강의. 강의 순서가 바뀌면 안됨. i, j번 강의를 녹화하려면 사이의 강의들도 다 블루레이에 넣어야함
#개수를 최대한 줄이려고함. m개의 블루레이에 녹화. 녹화가능 길이를 최소로 줄이려고함. 
import sys
sys.stdin = open('guitar.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split()) # n은 강의수 m은 블루레이 개수. 좌표문제와 비슷해보임

lec = list(map(int, input().split()))

start = 1 # 길이의 최소니까 ?
end = lec[-1] - lec[0] # 제일 큰 길이차이라서? // 길이차이묻는문제가아님

while start <= end:
    mid = (start + end) // 2

    for i in lec:
