# 45분 빠른 알람시계 만들기

H, M = map(int, input().split())
# H =0~23, M = 0~59

# 44분까지는 H - 1하고 45부턴 유지
# H가 음수가 되면 23으로 바꾼다

if M < 45:
    if H - 1 < 0:
        H = 23
    else:
        H = H - 1
    M = 15 + M
else:
    M = M - 45

print(H, end = ' ')
print(M, end = '')