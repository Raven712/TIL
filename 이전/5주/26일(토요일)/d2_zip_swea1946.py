#문서 너비 10. 여러줄

# T = int(input())
# for i in range(1, T+1):
#     N = int(input())
#     print(f'#{i}')
#     count = 0
#     list_ = []
#     list_2 = [] # 남는단어 옮겨놓는용
#     for j in range(N):
#         Ci, Ki = input().split()
#         Ai = Ci * int(Ki)
        # list_.append(Ai)
        

        # if len(list_) < 10 and count < 10:            
        #     print(Ai, end='')
        #     count += len(list_)
        #     list_ = []
        # elif len(list_) >= 10 or count >= 10:
        #     for i in range(10, 20):
        #         list2_.append(Ai[i])
        #         while count <= 10:
        #             print(list_[i-10])
        #             count += 1
                


T = int(input())
for i in range(1, T+1):
    N = int(input())
    print(f'#{i}')
    count = 0
    list_ = []
    for j in range(N):
        Ci, Ki = input().split()
        Ai = Ci * int(Ki)
        count += Ki  
        if count < 10:
            print(Ai, end = '')
            for i in range(Ki):
                list_.append(Ai[i])
        
        elif count == 10:
            print()
            list_ = []
        elif count > 10:
            for i in range(Ki):
                list_.append(Ai[i])
            for i in range(10):
