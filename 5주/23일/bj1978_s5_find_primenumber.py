# N개의 수중 소수가 몇개인지 출력하는것.
#정수의 성질을 이용해볼까???? (소수점 떨어져나감) ㄴㄴ 그럴것도없고 // 쓰면될듯

N = int(input())

numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    if i != 1:
        for j in range(2, i + 1):
            if j == i:
                count += 1
                break
            if i // j == i / j:
                break
            

print(count)