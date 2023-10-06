# N일동안 사용할 금액. M번만 통장에서 빼냄. K원 인출. 생활가능하면 생활, 부족시 나머지를 넣고 다시 K원 인출. M번 인출을 맞추려고함. 
# 파라메트릭 서치 문제는 start와 end가 무엇인지 알아내는게 중요하다

import sys
sys.stdin = open('allowance.txt', 'r')

n, m = map(int, input().split())

all_list = []
for i in range(n):
    allowance = int(input())
    all_list.append(allowance)

start = min(all_list)
end = max(all_list)     # 

cnt = 0
while start <= end:
    mid = (start + end) // 2
    
    for i in range(n):
        if mid < all_list[i]:   # 써야할 돈이 가진 돈보다 많은상황이니까 초기화?
            # start = mid + 1     # 이게 아닌거같다.. ?
            # cnt += 1'
            

        else:
            end = mid - 1