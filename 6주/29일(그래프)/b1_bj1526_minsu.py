#금민수 = 4,7로만 이뤄진수
import sys
input = sys.stdin.readline

N = int(input())

minsu = 0
list_minsu = []
not_minsu = {0, 1, 2, 3, 5, 6, 8, 9}
for i in range(4, N + 1):
    cnt = 0         # i의 자릿수에 대해서, 그 자릿수가 4 혹은 7일때 1 증가시키는 변수
    for j in str(i):
        if int(j) not in not_minsu: # N이하의 수 i에 대해서, i의 자릿수 하나하나를 분석한것이 모두 4,7로만 이뤄져있다면 (01235689가 아니라면)
            cnt += 1
    if cnt == len(str(i)):
        list_minsu.append(i) # list_minsu에 N이하의 모든 금민수들이 추가됨

print(max(list_minsu))  #그중에서 최대값 출력