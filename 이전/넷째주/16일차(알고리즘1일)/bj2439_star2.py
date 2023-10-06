N = int(input())
blank = (' ') 
for i in range(1, N + 1):
    if i == N:
        print('*' * i)
    else:
        blank = blank * (N - i) # 띄어쓰기 개수+ 별표의 개수의 합이 N이 되게끔 해서 열맞춤을 한다
        i = '*' * i
        print(blank + i)
        blank = (' ')   # 이걸 해주지 않으면 블랭크는 계속 위의 상태에서 추가가 되는형식이라 초기화시켜줘야함