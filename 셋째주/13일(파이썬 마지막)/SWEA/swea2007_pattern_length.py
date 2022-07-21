T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = input()
    for i in range(10):
        if i == 0:
            continue
        if a[:i] == a[i:i * 2]:
            print(f'#{test_case} {i}') 
            break
   #슬라이싱 개념을 제대로 이해했다면 금방풀수있었던 문제다....
