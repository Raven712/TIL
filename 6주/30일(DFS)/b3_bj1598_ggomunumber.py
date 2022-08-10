
#행렬로 만들려고 했으나 그게 훨씬 복잡해지는 문제같다


a, b = map(int, input().split())

if a % 4 != 0:
    ac = divmod(a, 4)[0] + 1         #divmod() ==> 나눗셈의 몫과 나머지를 튜플형식으로 반환함. -> divmod(33,4) == (8,1)
    ar = divmod(a, 4)[1]

    # bc = divmod(b, 4)[0] + 1
    # br = divmod(b, 4)[1]

else:
    ac = divmod(a-1, 4)[0] + 1
    ar = divmod(a-1, 4)[1] + 1

    # bc = divmod(b-1, 4)[0] + 1
    # br = divmod(b-1, 4)[1] + 1

if b % 4 != 0:
    bc = divmod(b, 4)[0] + 1
    br = divmod(b, 4)[1]

else:
    bc = divmod(b-1, 4)[0] + 1
    br = divmod(b-1, 4)[1] + 1

ans = abs(ac - bc) + abs(ar - br)   #거리이므로 절대값을 씌워줌

print(ans)