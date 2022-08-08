import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    count = 0
    for j in range(N, M + 1):
        for x in range(len(str(j))): # 100만이하라서 자릿수가 7자리 이하 라서 7을 썼더니 str(j)[x] 에서 인덱스오류가 나버림. (j가 한자리수 이래버리면 str(j)는 3번째 4번째..7번째 요소가없어서)
            if str(j)[x] == '0':
                count += 1
    print(count)