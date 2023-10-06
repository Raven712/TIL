# N = int(input())
# for i in range(1, N + 1):
#     for j in str(N):
#         if j == int(str(N)[i]) and int(str(N)[i + 1]) + d == int(str(N)(i)) < 이하 뻘짓

N = int(input())
count = 0
if N < 100:
    count = N
else:
    count = 99
    for i in range(100, N + 1):
        if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
            count += 1
print(count)
# 이 문제는 1~99까지 모두 한수이고, 100부터는 자릿수마다 등차가 같아야 한수임을 알아야 풀수있는 문제였다.