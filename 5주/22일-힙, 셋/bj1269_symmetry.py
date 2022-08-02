#A,B 공집합ㄴ  대칭차집합 원소개수차이 출력하기

A, B = map(int, input().split())
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

# A - B
# for i in range(A):
#     if set_A in set_B:
#         set_A.pop()            #시간복잡도가 높아보임..? <<< XX!! 세트의 추가, 제거는 시간복잡도가 상수다 <<<< 리스트처럼 특정 값을 지울수가 없는듯..
# print(set_A)

A_B_dic = {}
B_A_dic = {}
# A - B
for i in set_A:
    if i not in set_B:
        A_B_dic[i] = 1          A_B_dic = { 1 : 1 , 2 : 1}

#B - A
for i in set_B:
    if i not in set_A:
        B_A_dic[i] = 1

sum_A = len(A_B_dic.keys())
sum_B = len(B_A_dic.keys())
print(sum_A + sum_B)