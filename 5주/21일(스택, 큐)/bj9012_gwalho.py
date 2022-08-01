                                            # )( << 이것도 단순히 갯수로는 맞음..
T = int(input())

for case in range(T):
    gwalho = list(input())
    count_left = 0
    count_right = 0

    for i in gwalho:
#         if len(gwalho) == 1:
#             if gwalho[0] == ')':
#                 print('NO')
#                 break
#         if gwalho[-1] == ')':
#             count_right += 1
#         else:
#             count_left += 1
#         gwalho.pop()                                                      )( <<< 
#         if len(gwalho) == 0:
#             if count_left == count_right:
#                 print('YES')
#             else:
#                 print('NO')

        if i == '(':
            count_left += 1
        elif i == ')':
            count_right += 1
        if count_right > count_left:                ) <<<<<<<< ()()()()
            print('NO')     
            break                       ## 처음부터 확인을 하면서 그냥 ()) << 이 형태가 한번이라도 나오는순간 끝내는게 핵심이었음.....
    if count_right == count_left:       ( << ) ()( )()()
        print('YES')
    elif count_right < count_left:  ( <<<  ( )()( << 
        print('NO')