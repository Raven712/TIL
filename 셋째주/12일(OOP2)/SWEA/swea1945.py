# 1945번, 2^a * 3^b * 5^c * 7^d * 11^e 인 수 N을 소인수분해 해서, abcde를 구하는 문제.
T = int(input())
for test_case in range(1, T + 1): # T번 테스트하라고 있는 문제양식
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
# 문제조건이 저렇게 주어졌으니 일단 abcde를 대충 정수 기본값 0으로 정의해줬다

    while N % 2 == 0:
        a += 1
        N /= 2
    while N % 3 == 0:
        b += 1
        N /= 3
    while N % 5 == 0:
        c += 1
        N /= 5
    while N % 7 == 0:
        d += 1
        N /= 7
    while N % 11 == 0:
        e += 1
        N /= 11             # 그냥 흔한 소인수분해, while은 조건이 만족되지않으면 알아서 반복이 풀리니 나머지가 0이 안되는 상황이 되면 반복이 깨짐
    print(f'#{test_case} {a} {b} {c} {d} {e}') #f 스트링으로 답안작성..
    