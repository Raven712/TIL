# 그냥 촌수 계산하기.
import sys
sys.stdin = open('chonsu.txt', 'r')

n = int(input()) #전체 사람수 
a, b = map(int, input().split())  # a, b간의 촌수 격차를 출력해야하는 문제.

m = int(input()) #부모자식 관계 개수

graph = [[] * m for i in range(n + 1)]      # 0번부터 계산하니까 인덱스개수를 추가해줌. 0번은 버림.

# dic_fam = {}
for i in range(m):
    x, y = map(int, input().split())            #인접 리스트 만들기
    graph[x].append(y)
    graph[y].append(x)
    # if x not in dic_fam:
    #     dic_fam[x] = [y]                  # 딕셔너리 필요없음. 오히려 이걸로 하면 꼬였음.
    # else:
    #     dic_fam[x].add[y]
visited = [False] * (n + 1)

# 조건1. 한 연결리스트안에 a,b가 같이 존재해야함
# 조건2. dfs를 할떄 친척을 돌때는 cnt가 오르면 안됨. 부모자식간일떄만 올라야함 ....

cnt = 0
def dfs(start):
    stack = [(start, 0)]      #스택에 촌수 (0) 도 넣어줌 ! (맨처음은 자기자신이라 0)
    visited[start] = True
    global cnt 
    while stack:
        cur, count = stack.pop()        #count 도 넣어줌. 스택이 튜플이라서 (촌수)
        if cur == b:         #dfs(a) 를 해서, b를 만나면 브레이크 하게만드는것. 
            answer = count
            break
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append((adj, count + 1))    #
    return answer



print(dfs(a))