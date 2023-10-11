a = input()

# n = abs(len(a) / 2)

# text = []
# if n % 2 != 1: # 짝수일떄
#     a[0 : (n - 1)]

# 슬라이싱 문제임..

if a == a[::-1]:
    print(1)
else:
    print(0)


