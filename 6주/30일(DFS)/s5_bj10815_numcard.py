#카드 N개있고 M개의 정수들이 주어졌을때 이 수가 적힌카드를 들고있는가 아닌가 ..
import sys
sys.stdin = open('num.txt', 'r')

N= int(input())
card = set(map(int, input().split()))   #세트가 빠른데, 문제조건에 중복카드가 입력되지않는다고함 !

M = int(input())
num = list(map(int, input().split())) #마찬가지 .. 인줄 알았으나 출력조건에 순서가있어서 리스트사용

cnt = 0

for i in range(M):
    if num[i] in card:
        print(1, end = ' ')

    else:
        print(0, end = ' ')
