# fac 1 = 1 / fac2 = 1*2 fac 3= 1*2*3

N = int(input())
factorial = 1
for i in range(1, N + 1):
    if N == 0:
        factorial = 1
        break
    else:
        factorial = factorial * i

print(factorial)
