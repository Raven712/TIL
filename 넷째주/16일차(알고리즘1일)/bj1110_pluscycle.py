N = int(input())
ans = 0
count = 0
add = 0
if N < 10:
    N = N * 10           # N이 10이하면 10을 곱함
    add = int(str(N)[1])
    ans = int(str(N)[0]) + int(str(N)[1])
    count += 1     # 기본규칙은 십의자리수 숫자를 떼온것과 일의자리수 수를 떼온것을 더하고,

else:
    ans = N
    add = int(str(N)[1])
    ans = int(str(N)[0]) + int(str(N)[1])
    ans = add * 10 + ans
    count += 1

while ans != N:
    if N < 10:
        N = N * 10          
        add = int(str(ans)[1])
        ans = int(str(ans)[0]) + int(str(ans)[1])
        count += 1     

    else:
        if ans < 10:
            add = int(str(ans)[0])
        else:
            add = int(str(ans)[1])
        
        if ans < 10:
            ans = int(str(ans)[0]) + int(str(ans)[0])
        else:
            ans = int(str(ans)[0]) + int(str(ans)[1])
        if ans < 10:
            ans = add * 10 + int(str(ans)[0])
        else:
            ans = add * 10 + int(str(ans)[1])
        count += 1

print(count) #그 카운트의 값을 구한다.


# 삽질하다가 망함