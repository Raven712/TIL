T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    total = 0
    k = []
    if n == m:         # n, m이 A와 B의 인덱스 개수인데, 까먹고 range(len(A)) 하면서 시간 끌었음.. // 두 리스트의 요소 개수가 같으면 아래와 같이 계산
        for i in range(n):    
            total += A[i] * B[i]      # 크기비교가 필요없으니 그냥 같이곱해서 넣으면 된다...
        print(f'#{test_case} {total}')
    if n > m:
        for i in range(n):
            for j in range(m):
                if 

## 이것도 행렬이라 보류