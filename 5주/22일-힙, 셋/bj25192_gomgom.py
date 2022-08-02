#ENTER : 뉴비등장, 그외는 모두 닉네임 . ENTER와 ENTER사이에 동일닉이 두번 입력되면 두번이상은 카운트하지않음!!


N = int(input()) #채팅기록 수
list_chat = []
set_chat = set()
count_gom = 0
count_enter = 0
for i in range(N):
    chat = input()
    if chat == 'ENTER':
        count_gom += len(set_chat)
        set_chat = set()
        count_enter += 1
    else:
        set_chat.add(chat)
    if i == N - 1:
        count_gom += len(set_chat)   

print(count_gom)

