# 나무 m미터 필요. 절단기 높이 h. 그냥 떡썰기문제와 같음
import sys
sys.stdin = open('tree.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split()) #나무 수와 필요한 나무길이

tree = list(map(int, input().split())) #나무높이가 주어짐


start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    height = 0
    for i in tree:
        if i > mid:
            height += i - mid
    if height >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)