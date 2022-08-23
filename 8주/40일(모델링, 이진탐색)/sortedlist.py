# N개 원소를 포함한 수열이 오름차순 정렬되어있음. x가 등장하는 횟수 구하기. ---> {1, 1, 2, 2, 2, 2, 3} 일때, x = 2라면, 2인 원소가 4개니까 4 출력하기.
# 선형탐색하면 시간초과가 나므로 사용금지
import sys
sys.stdin = open('sort.txt','r')

from bisect import bisect_left, bisect_right

n, x = map(int, input().split()) # n은 수열의 길이, x는 찾아야되는 수

list_ = list(map(int, input().split()))

print(bisect_right(list_, x) - bisect_left(list_, x)) # ---> 그냥 이렇게 하면 right = left일때 ( x라는 원소가 없을 때 ) 되나.. ? 답은 이 상황에선 -1을 출력하도록 했음.


