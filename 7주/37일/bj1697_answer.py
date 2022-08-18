# 이 문제는 bfs 미로찾기처럼, 정점에서 같은거리에 있는 다음정점들을 모두 +1 해주는식으로 푸는 문제다.
# 단순히 time을 상수로 두면 역시 안된다. 미로찾기 bfs도 cnt를 상수로 두고 했다가 틀렸는데, bfs는 상수로 두면 특정정점에서 똑같은거리의 정점을 방문하는데도 방문할떄마다 +1 이 돼서 문제가 생긴다
# time이라는게 결국 생각해보면 visited와 같다. 
#이걸 꼭 생각하면서 풀자....
from collections import deque

n, k = map(int, input().split())
time = [0] * 100000 
queue = deque()
def bfs(n):
    global queue
    queue.append(n)
    global time
    
    while queue:
        x = queue.popleft()
        # queue.append(x - 1, x + 1, x * 2) # 이게 아니다. for문을 생각하자. 제발....
        if x == k:
            print(time[x])
            break
        for i in (x-1, x+1, x*2):
            if not time[i] and 0 <= i <= 100000:
                time[i] = time[x] + 1
                queue.append(i)
bfs(n)

print(queue)