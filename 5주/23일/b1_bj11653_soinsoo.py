#그냥 소인수분해하기

N = int(input())

# for i in range(N):
#     for j in range(2, i + 1)
#         if N == 1:
#             break
#         if N // i == N / i:
#             print(i)
#             N = N / i
div = 2
while N != 1:
    if N // div == N / div:                     #의외의외 while생각하기 어려웠음
        print(div)
        N = N / div
    else:
        div += 1