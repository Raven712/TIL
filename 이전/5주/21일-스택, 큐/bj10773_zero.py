K = int(input())         #0~ 100만, 0 이면 최근에 쓴수를 지우고, 아니면 적어나감. 0이 두번적히면 두번째전의 수를 지움. 리스트를 쓰자
list_ = []      
for test_case in range(K):
    test_case = int(input())
    if test_case != 0:                  ## 처음엔 인풋을 어떻게넣을지 생각하지말고, 테스트케이스를 불러와서 문제를 먼저보자.
        list_.append(test_case)
    else:
        list_.pop()

print(sum(list_))

    

