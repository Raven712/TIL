import sys
sys.stdin = open('cow.txt', 'r')

#첫줄 관찰횟수 N, 그뒤론 소의 번호와 위치로 이뤄짐 (0은 왼쪽 1은 오른쪽이란뜻)  ----> 소의 위치가 몇번바뀌었는지 세서 출력하기


N = int(input())
cnt = 0  # 이동횟수
dic_ = {}

for i in range(N):
    n, p = map(int, input().split()) #number place
    if n not in dic_:
        dic_[n] = p
    else:
        if dic_[n] != p:
            cnt += 1
            dic_[n] = p

print(cnt)




#     list_.append([n,p])
#     list_n.append(n)
# # n, p 를 묶어서 리스트에 등록하고, 이미 n이 리스트에 있는데 p가 바뀌면 cnt 를 늘리자.

# for i in range(N):
#     if list_n[i] in list_[i]: