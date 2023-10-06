
import sys
sys.stdin = open('num2.txt', 'r')
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n = int(input())
card_n = list(map(int, input().split()))    # 상근이 카드

m = int(input())
card_m = list(map(int, input().split()))    # 주어지는 정수카드

# 상근이가 들고있는 카드리스트를 참고하여 정수가 주어질떄 그 정수가 카드리스트에 몇개 들어있는지 출력하는 문제임.
# 수의 크기가 중요한게 아니니까 이진탐색을 해도 된다? xx 수의 크기가 의미가 있어보임...

# sort 후 이진탐색 하는게 그냥 탐색하는것보다 빠르다!! (탐색의 횟수가 1이 아니라면!!)

card_n.sort()

# 이 문제는 bisect를 쓰면 쉽게풀릴것같음..

for i in card_m:
    print(bisect_right(card_n, i) - bisect_left(card_n, i), end =' ')
