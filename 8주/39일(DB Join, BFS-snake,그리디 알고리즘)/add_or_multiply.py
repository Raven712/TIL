# 문자열 S, 숫자로만 이뤄진게 입력됨. 왼쪽부터 오른쪽까지 하나씩 곱하거나 더하기를 해서 제일 큰수가 나오는 프로그램을 만듬.

S = input()

ans = 0
for i in S:
    if int(i) == 0:
        continue
    elif int(i) == 1 or ans == 0:
        ans += int(i)
    else:
        ans = ans * int(i)

print(ans)